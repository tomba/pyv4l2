import importlib
import kms
import mmap
import os
import socket
import sys
import typing
import v4l2
import v4l2.uapi

# Disable all possible links
def disable_all_links(md: v4l2.MediaDevice):
    for ent in md.entities:
        for l in ent.pad_links:
            if l.is_immutable:
                continue
            #print((l.sink, l.sink_pad), (l.source, l.source_pad))
            l.enabled = False
            md.link_setup(l.source, l.sink, 0)
            #ent.setup_link(l)


# Enable link between (src_ent, src_pad) -> (sink_ent, sink_pad)
def link(md: v4l2.MediaDevice, source, sink):
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

    if link == None:
        raise Exception('Failed to find link between', source, sink)

    #if link.is_enabled:
    #    return

    #print('CONF')

    if link.is_immutable:
        return

    link.enabled = True
    #src_ent.setup_link(link)

    md.link_setup(link.source, link.sink, v4l2.uapi.MEDIA_LNK_FL_ENABLED)

def embedded_fourcc_to_bytes_per_pixel(fmt):
    if fmt == v4l2.MetaFormat.GENERIC_CSI2_12:
        return 12
    elif fmt == v4l2.MetaFormat.GENERIC_CSI2_10:
        return 10
    elif fmt == v4l2.MetaFormat.GENERIC_8:
        return 8
    elif fmt == v4l2.MetaFormat.SENSOR_DATA:
        return 8
    elif fmt == v4l2.MetaFormat.RPI_FE_CFG:
        return 8
    else:
        raise NotImplementedError(f'Unsupported fmt {fmt.name}')

class NetTX:
    import struct

    # ctx-idx, width, height, bytesperline, format, num-planes, plane1, plane2, plane3, plane4
    struct_fmt = struct.Struct('<IIII16pI4I')

    def __init__(self) -> None:
        HOST, PORT = '192.168.88.20', 43242

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

    def tx(self, stream, vbuf, is_drm):
        cap = stream['cap']

        if is_drm:
            fb = next((fb for fb in stream['fbs'] if fb.fd(0) == vbuf.fd), None)
            assert(fb != None)
            plane_sizes = [fb.size(0), 0, 0, 0]
        else:
            plane_sizes = [vbuf.buffer_size, 0, 0, 0]

        fmt = stream['fourcc']
        fmt = fmt.name

        if stream.get('embedded', False):
            # XXX we dont' really have 'lines' with embedded data
            bytesperline = stream['w']
            bpp = embedded_fourcc_to_bytes_per_pixel(stream['fourcc'])
            bytesperline = bytesperline * bpp // 8
        else:
            bytesperline = stream['cap'].bytesperline

        hdr = NetTX.struct_fmt.pack(stream['id'],
                              stream['w'], stream['h'],
                              bytesperline,
                              bytes(fmt, 'ascii'),
                              1, *plane_sizes)

        self.sock.sendall(hdr)

        if is_drm:
            with mmap.mmap(fb.fd(0), fb.size(0), mmap.MAP_SHARED, mmap.PROT_READ) as b:
                self.sock.sendall(b)
        else:
            with mmap.mmap(cap.fd, vbuf.buffer_size, mmap.MAP_SHARED, mmap.PROT_READ,
                           offset=vbuf.offset) as b:
                self.sock.sendall(b)

#
# Config file functions
#

def merge_configs(configs):
    d = { 'subdevs': [], 'devices': [], 'links': [] }

    for config in configs:
        # links can be appended directly
        # xxx there may be (harmless) duplicates
        d['links'] += config['links']

        # devices can be appended directly
        d['devices'] += config['devices']

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

def read_config(config_name):
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
def setup_links(md, config):
    for l in config.get('links', []):
        source_ent, source_pad = l['src']
        sink_ent, sink_pad = l['dst']

        try:
            source_ent = md.find_entity(source_ent)
            if source_ent == None:
                print('Failed to find entity', l['src'])
                exit(-1)

            sink_ent = md.find_entity(sink_ent)
            if sink_ent == None:
                print('Failed to find entity', l['dst'])
                exit(-1)

            link(md, (source_ent, source_pad), (sink_ent, sink_pad))
        except Exception as e:
            print('Failed to link {} -> {}'.format((source_ent, source_pad), (sink_ent, sink_pad)))
            raise e

# Configure entities
def configure_subdevs(md, config):
    subdevices = {}

    for e in config.get('subdevs', []):
        ent = md.find_entity(e['entity'])
        assert ent
        subdev = v4l2.SubDevice(ent)
        assert subdev, 'no subdev for entity %s' % ent

        subdevices[ent.name] = subdev

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
                try:
                    subdev.set_routes(routes)
                except Exception as e:
                    print('Failed to set routes for {}'.format(ent))
                    raise e

        # Configure streams
        for p in e.get('pads', []):
            if type(p['pad']) == tuple:
                pad, stream = p['pad']
            else:
                pad = p['pad']
                stream = 0

            w, h, fmt = p['fmt']
            try:
                subdev.set_format(pad, stream, w, h, fmt)
            except Exception as e:
                print('Failed to set format for {}'.format(ent))
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
        fb = typing.cast(kms.DumbFramebuffer, fb_or_vbuf)

        with mmap.mmap(fb.fd(0), fb.size(0), mmap.MAP_SHARED, mmap.PROT_READ) as b:
            with open(filename, 'wb') as f:
                f.write(b)
    else:
        vbuf = typing.cast(v4l2.VideoBuffer, fb_or_vbuf)

        with mmap.mmap(cap.fd, vbuf.buffer_size, mmap.MAP_SHARED, mmap.PROT_READ,
                       offset=vbuf.offset) as b:
            with open(filename, 'wb') as f:
                f.write(b)
