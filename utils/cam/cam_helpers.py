from __future__ import annotations

import importlib
import mmap
import os
import sys
import typing
from typing import TYPE_CHECKING

from cam_types import Stream

import v4l2
import v4l2.uapi

if TYPE_CHECKING:
    import kms

    from .cam import Subcontext


# Disable all possible links
def disable_all_links(md: v4l2.MediaDevice):
    for ent in md.entities:
        for l in ent.pad_links:
            if l.is_immutable:
                continue
            # print(l)
            l.disable()


# Enable link between (src_ent, src_pad) -> (sink_ent, sink_pad)
def enable_link(source, sink):
    src_ent = source[0]
    sink_ent = sink[0]

    source_pad = src_ent.pads[source[1]]

    # links = src_ent.get_links(source[1])
    links = source_pad.links

    link = None

    for l in links:
        if l.sink_pad.entity == sink_ent and l.sink_pad.index == sink[1]:
            link = l
            break

    if link is None:
        raise RuntimeError('Failed to find link between', source, sink)

    # if link.is_enabled:
    #    return

    # print('CONF')

    if link.is_immutable:
        return

    link.enabled = True
    # src_ent.setup_link(link)

    link.enable()


#
# Config file functions
#


def gen_subdev(entity, fmt=None, routing=None, controls=None, pads=None):
    """Generate a subdev config dict entry.

    Args:
        routing: A single route ((src_pad, src_stream), (dst_pad, dst_stream))
                 or a list of routes. Each route is a (src, dst) tuple.
        pads: A dict {(pad, stream): fmt, ...} or a list of pad dicts
              for cases needing extra fields (ival, crop, etc.).
        controls: A dict {ctrl_id: value, ...} or a list of (id, value) tuples.

    If routing and fmt are given but pads is not, auto-generate pad entries
    by setting fmt on each (pad, stream) pair mentioned in the routing.
    """
    d = {'entity': entity}

    # Normalize routing: single route tuple → list of routes
    routes = None
    if routing:
        if isinstance(routing[0][0], tuple):
            routes = routing
        else:
            routes = [routing]
        d['routing'] = [{'src': r[0], 'dst': r[1]} for r in routes]

    # Normalize pads: dict → list of pad dicts
    if pads:
        if isinstance(pads, dict):
            d['pads'] = [{'pad': k, 'fmt': v} for k, v in pads.items()]
        else:
            d['pads'] = pads
    elif routes and fmt:
        d['pads'] = []
        for r in routes:
            d['pads'].append({'pad': r[0], 'fmt': fmt})
            d['pads'].append({'pad': r[1], 'fmt': fmt})
    elif fmt:
        # Store format for propagation to pick up later
        d['fmt'] = fmt

    # Normalize controls: dict → list of tuples
    if controls:
        if isinstance(controls, dict):
            d['controls'] = list(controls.items())
        else:
            d['controls'] = controls

    return d


def infer_links(md, config):
    """Derive links from the ordered subdevs + devices lists.

    For each consecutive pair of entities in the subdevs list, and between
    the last subdev and each device, find the media graph link connecting
    them and add it to config['links'].
    """
    entities = [sd['entity'] for sd in config['subdevs']]
    entities += [dev['entity'] for dev in config['devices']]

    links = []
    for i in range(len(entities) - 1):
        src_name = entities[i]
        dst_name = entities[i + 1]

        src_ent = md.find_entity(src_name) if isinstance(src_name, str) else src_name
        dst_ent = md.find_entity(dst_name) if isinstance(dst_name, str) else dst_name
        assert src_ent, f'Entity not found: {src_name}'
        assert dst_ent, f'Entity not found: {dst_name}'

        # Find a link from src to dst by checking all source pads of src
        found = False
        for pad in src_ent.pads:
            if not pad.is_source:
                continue
            for link in pad.links:
                if link.sink_pad.entity == dst_ent:
                    links.append(
                        {
                            'src': (src_name, pad.index),
                            'dst': (dst_name, link.sink_pad.index),
                        }
                    )
                    found = True
                    break
            if found:
                break

        if not found:
            raise RuntimeError(f'No link found between {src_name} and {dst_name}')

    config['links'] = links


def propagate_formats(config):
    """Fill missing pad formats in subdev entries by propagation.

    Walk subdevs in order. When a subdev has a 'fmt' key or explicit pads
    with fmt, that becomes the current format. For subdevs with routing but
    no pads (pass-throughs), generate pads using the current format.
    """
    current_fmt = None

    for sd in config['subdevs']:
        if 'fmt' in sd:
            current_fmt = sd.pop('fmt')

        if 'pads' in sd:
            # Extract format from existing pads for propagation
            for p in sd['pads']:
                if 'fmt' in p:
                    current_fmt = p['fmt']
        elif 'routing' in sd and current_fmt:
            sd['pads'] = []
            for r in sd['routing']:
                sd['pads'].append({'pad': r['src'], 'fmt': current_fmt})
                sd['pads'].append({'pad': r['dst'], 'fmt': current_fmt})


def merge_configs(configs):
    d = {'media': None, 'subdevs': [], 'devices': [], 'links': []}

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
                    if 'routing' not in dst:
                        dst['routing'] = []
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

    cam_configs_path = os.path.dirname(os.path.abspath(__file__)) + '/cam-configs'
    sys.path.append(cam_configs_path)

    cam_config_module = importlib.import_module(config_file)
    try:
        config = cam_config_module.get_configs(config_names)
    except TypeError:
        # Try legacy style
        configurations, default_configurations = cam_config_module.get_configs()

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
def setup_links(sctx: Subcontext, config):
    md = sctx.md
    assert md is not None

    for l in config.get('links', []):
        source_ent, source_pad = l['src']
        sink_ent, sink_pad = l['dst']

        try:
            if not isinstance(source_ent, v4l2.MediaEntity):
                source_ent = md.find_entity(source_ent)
                if source_ent is None:
                    raise RuntimeError(f'Failed to find entity {l["src"]}')

            if not isinstance(sink_ent, v4l2.MediaEntity):
                sink_ent = md.find_entity(sink_ent)
                if sink_ent is None:
                    raise RuntimeError(f'Failed to find entity {l["dst"]}')

            if sctx.ctx.verbose:
                print(f'Link {source_ent.name} -> {sink_ent.name}')

            enable_link((source_ent, source_pad), (sink_ent, sink_pad))
        except Exception:
            print('Failed to link {} -> {}'.format((source_ent, source_pad), (sink_ent, sink_pad)))
            raise


# Configure entities
def configure_subdevs(sctx: Subcontext, config):
    ctx = sctx.ctx
    md = sctx.md
    assert md is not None

    subdevices = {}

    for e in config.get('subdevs', []):
        if isinstance(e['entity'], v4l2.MediaEntity):
            ent = e['entity']
        else:
            ent = md.find_entity(e['entity'])
        assert ent
        subdev = v4l2.SubDevice(ent.interface.dev_path)

        if ctx.verbose:
            print(f'Configuring {ent.name}')

        subdevices[ent.name] = subdev

        # Configure controls that need to be set before format
        if 'pre-controls' in e:
            for ctrl_id, ctrl_val in e['pre-controls']:
                subdev.set_control(ctrl_id, ctrl_val)

        # Configure routes
        if 'routing' in e:
            routes = []
            for r in e['routing']:
                sink_pad, sink_stream = r['src']
                source_pad, source_stream = r['dst']

                routes.append(
                    v4l2.Route(
                        sink_pad, sink_stream, source_pad, source_stream, v4l2.RouteFlag.ACTIVE
                    )
                )

            if len(routes) > 0:
                if ctx.verbose:
                    print(f'  Routes {routes}')

                try:
                    subdev.set_routes(routes)
                except Exception:
                    print('Failed to set routes for {}'.format(ent))
                    print('  Attempted routes:')
                    for route in routes:
                        print(
                            f'    sink_pad={route.sink_pad}, sink_stream={route.sink_stream}, source_pad={route.source_pad}, source_stream={route.source_stream}'
                        )
                    raise

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
            except Exception:
                print(f'Failed to set format for {ent}:{pad}/{stream}: {w}x{h}-{fmt}')
                raise

            if 'crop.bounds' in p:
                x, y, w, h = p['crop.bounds']
                subdev.set_selection(
                    v4l2.uapi.V4L2_SEL_TGT_CROP_BOUNDS, v4l2.uapi.v4l2_rect(x, y, w, h), pad, stream
                )

            if 'crop' in p:
                x, y, w, h = p['crop']
                subdev.set_selection(
                    v4l2.uapi.V4L2_SEL_TGT_CROP, v4l2.uapi.v4l2_rect(x, y, w, h), pad, stream
                )

            if 'ival' in p:
                assert len(p['ival']) == 2
                subdev.set_frame_interval(pad, stream, p['ival'])

        # Configure controls
        if 'controls' in e:
            for ctrl_id, ctrl_val in e['controls']:
                subdev.set_control(ctrl_id, ctrl_val)

    return subdevices


def save_fb_to_file(stream: Stream, is_drm, fb_or_vbuf):
    cap = stream.cap

    filename = 'frame-{}-{}-{}x{}-{}.data'.format(
        stream.id, stream.total_num_frames, stream.w, stream.h, stream.format.name
    )
    print('save to ' + filename)

    if is_drm:
        fb: kms.DumbFramebuffer = fb_or_vbuf

        with (
            mmap.mmap(fb.fd(0), fb.size(0), mmap.MAP_SHARED, mmap.PROT_READ) as b,
            open(filename, 'wb') as f,
        ):
            f.write(b)
    else:
        vbuf = typing.cast(v4l2.VideoBuffer, fb_or_vbuf)

        with (
            mmap.mmap(
                cap.fd, cap.framesize, mmap.MAP_SHARED, mmap.PROT_READ, offset=vbuf.offset
            ) as b,
            open(filename, 'wb') as f,
        ):
            f.write(b)
