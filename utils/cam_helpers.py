from __future__ import annotations
import importlib
import mmap
import os
import socket
import struct
import sys
import typing
from typing import TYPE_CHECKING

import v4l2
import v4l2.uapi

if TYPE_CHECKING:
    from .cam import Context
    import kms

# Disable all possible links
def disable_all_links(md: v4l2.MediaDevice):
    for ent in md.entities:
        for l in ent.pad_links:
            if l.is_immutable:
                continue
            #print(l)
            l.disable()


# Enable link between (src_ent, src_pad) -> (sink_ent, sink_pad)
def enable_link(source, sink):
    src_ent = source[0]
    sink_ent = sink[0]

    source_pad = src_ent.pads[source[1]]

    #links = src_ent.get_links(source[1])
    links = source_pad.links

    link = None

    for l in links:
        if l.sink_pad.entity == sink_ent and l.sink_pad.index == sink[1]:
            link = l
            break

    if link is None:
        raise RuntimeError('Failed to find link between', source, sink)

    #if link.is_enabled:
    #    return

    #print('CONF')

    if link.is_immutable:
        return

    link.enabled = True
    #src_ent.setup_link(link)

    link.enable()


class NetTX:
    # ctx-idx, width, height, strides[4], format[16], num-planes, plane[4]
    struct_fmt = struct.Struct('<III4I16pI4I')

    def __init__(self, host: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def tx(self, stream, vbuf, is_drm):
        cap = stream['cap']

        plane_sizes = cap.buffersizes
        strides = cap.strides

        # Extend lists to 4 elements
        plane_sizes.extend(0 for _ in range(4 - len(plane_sizes)))
        strides.extend(0 for _ in range(4 - len(strides)))

        fmt = stream['format']

        if isinstance(fmt, v4l2.MetaFormat):
            num_planes = 1
        else:
            num_planes = len(fmt.planes)

        hdr = NetTX.struct_fmt.pack(stream['id'],
                              stream['w'], stream['h'],
                              *strides,
                              bytes(fmt.name, 'ascii'),
                              num_planes,
                              *plane_sizes)

        self.sock.sendall(hdr)

        if is_drm:
            fb = next((fb for fb in stream['fbs'] if fb.fd(0) == vbuf.fd), None)
            assert fb is not None

            with mmap.mmap(fb.fd(0), fb.size(0), mmap.MAP_SHARED, mmap.PROT_READ) as b:
                self.sock.sendall(b)
        else:
            # Need PROT_WRITE to be able to read fe-config buffers
            with mmap.mmap(cap.fd, cap.framesize, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE,
                           offset=vbuf.offset) as b:
                self.sock.sendall(b)

#
# Config file functions
#

def merge_configs(configs):
    d = { 'media': None, 'subdevs': [], 'devices': [], 'links': [] }

    for config in configs:
        # XXX maybe restructure configs to have media as a "parent" config
        if not d['media']:
            d['media'] = config.get('media', None)

        # links can be appended directly
        # xxx there may be (harmless) duplicates
        d['links'] += config.get('links', [])

        # devices can be appended directly
        d['devices'] += config.get('devices', [])

        # subdevs need to be merged based on entity
        for subdev in config.get('subdevs', []):
            ent = subdev['entity']

            dst = next((s for s in d['subdevs'] if s['entity'] == ent), None)
            if dst:
                if 'pads' in subdev:
                    dst['pads'] += subdev['pads']
                if 'routing' in subdev:
                    dst['routing'] += subdev['routing']
            else:
                d['subdevs'].append(subdev)

    return d

def read_config(config_name, params):
    parts = config_name.split(':')

    if len(parts) > 2:
        sys.exit(-1)

    config_file = parts[0]

    if len(parts) == 2:
        config_names = parts[1].split(',')
    else:
        config_names = []

    config_names = [c for c in config_names if len(c) > 0]

    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/cam-configs')
    if params:
        configurations, default_configurations = importlib.import_module(config_file).get_configs(params)
    else:
        configurations, default_configurations = importlib.import_module(config_file).get_configs()

    if len(config_names) == 0:
        config_names = default_configurations

    for cfg in config_names:
        if cfg not in configurations:
            print('Cannot find config "{}"'.format(cfg))
            sys.exit(-1)

    config = merge_configs([configurations[x] for x in config_names])

    return config

#
# V4L2 configuration
#

# Setup links
def setup_links(ctx: Context, config):
    md = ctx.md

    for l in config.get('links', []):
        source_ent, source_pad = l['src']
        sink_ent, sink_pad = l['dst']

        try:
            source_ent = md.find_entity(source_ent)
            if source_ent is None:
                raise RuntimeError(f'Failed to find entity {l["src"]}')

            sink_ent = md.find_entity(sink_ent)
            if sink_ent is None:
                raise RuntimeError(f'Failed to find entity {l["dst"]}')

            if ctx.verbose:
                print(f'Link {source_ent.name} -> {sink_ent.name}')

            enable_link((source_ent, source_pad), (sink_ent, sink_pad))
        except Exception as e:
            print('Failed to link {} -> {}'.format((source_ent, source_pad), (sink_ent, sink_pad)))
            raise e

# Configure entities
def configure_subdevs(ctx: Context, config):
    md = ctx.md

    subdevices = {}

    for e in config.get('subdevs', []):
        ent = md.find_entity(e['entity'])
        assert ent
        subdev = v4l2.SubDevice(ent.interface.dev_path)
        assert subdev, f'no subdev for entity {ent}'

        if ctx.verbose:
            print(f'Configuring {ent.name}')

        subdevices[ent.name] = subdev

        if 'controls' in e:
            for ctrl_id, ctrl_val in e['controls']:
                subdev.set_control(ctrl_id, ctrl_val)

        # Configure routes
        if 'routing' in e:
            routes = []
            for r in e['routing']:
                sink_pad, sink_stream = r['src']
                source_pad, source_stream = r['dst']

                route = v4l2.Route()
                route.sink_pad = sink_pad
                route.sink_stream = sink_stream
                route.source_pad = source_pad
                route.source_stream = source_stream
                route.flags = v4l2.uapi.V4L2_SUBDEV_ROUTE_FL_ACTIVE

                routes.append(route)

            if len(routes) > 0:
                if ctx.verbose:
                    print(f'  Routes {routes}')

                try:
                    subdev.set_routes(routes)
                except Exception as e:
                    print('Failed to set routes for {}'.format(ent))
                    raise e

        # Configure streams
        for p in e.get('pads', []):
            if isinstance(p['pad'], tuple):
                pad, stream = p['pad']
            else:
                pad = p['pad']
                stream = 0

            w, h, fmt = p['fmt']
            try:
                subdev.set_format(pad, stream, w, h, fmt)
            except Exception as e:
                print(f'Failed to set format for {ent}:{pad}/{stream}: {w}x{h}-{fmt}')
                raise e

            if 'crop.bounds' in p:
                x, y, w, h = p['crop.bounds']
                subdev.set_selection(v4l2.uapi.V4L2_SEL_TGT_CROP_BOUNDS, v4l2.uapi.v4l2_rect(x, y, w, h), pad, stream)

            if 'crop' in p:
                x, y, w, h = p['crop']
                subdev.set_selection(v4l2.uapi.V4L2_SEL_TGT_CROP, v4l2.uapi.v4l2_rect(x, y, w, h), pad, stream)

            if 'ival' in p:
                assert(len(p['ival']) == 2)
                subdev.set_frame_interval(pad, stream, p['ival'])

    return subdevices

def save_fb_to_file(stream, is_drm, fb_or_vbuf):
    cap = stream['cap']

    filename = 'frame-{}-{}.data'.format(stream['id'], stream['total_num_frames'])
    print('save to ' + filename)

    if is_drm:
        fb: kms.DumbFramebuffer = fb_or_vbuf

        with mmap.mmap(fb.fd(0), fb.size(0), mmap.MAP_SHARED, mmap.PROT_READ) as b:
            with open(filename, 'wb') as f:
                f.write(b)
    else:
        vbuf = typing.cast(v4l2.VideoBuffer, fb_or_vbuf)

        with mmap.mmap(cap.fd, vbuf.buffer_size, mmap.MAP_SHARED, mmap.PROT_READ,
                       offset=vbuf.offset) as b:
            with open(filename, 'wb') as f:
                f.write(b)
