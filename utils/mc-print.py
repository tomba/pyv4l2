#!/usr/bin/env python3

import argparse
import errno
import textwrap
import sys

import v4l2
import v4l2.uapi

def print_selection(subdev, pad, stream, target):
    name = target.name.lower()

    try:
        r = subdev.get_selection(target.value, pad.index, stream)
        print(f'      {name}:({r.left},{r.top})/{r.width}✕{r.height}')
    except OSError as e:
        if e.errno not in (errno.ENOTTY, errno.EINVAL):
            print(f'      {name}:({e})')


def print_selections(subdev, pad, stream):
    print_selection(subdev, pad, stream, v4l2.uapi.v4l2_sel_tgt.NATIVE_SIZE)
    print_selection(subdev, pad, stream, v4l2.uapi.v4l2_sel_tgt.CROP_BOUNDS)
    print_selection(subdev, pad, stream, v4l2.uapi.v4l2_sel_tgt.CROP_DEFAULT)
    print_selection(subdev, pad, stream, v4l2.uapi.v4l2_sel_tgt.CROP)
    print_selection(subdev, pad, stream, v4l2.uapi.v4l2_sel_tgt.COMPOSE_BOUNDS)
    print_selection(subdev, pad, stream, v4l2.uapi.v4l2_sel_tgt.COMPOSE_DEFAULT)
    print_selection(subdev, pad, stream, v4l2.uapi.v4l2_sel_tgt.COMPOSE)
    print_selection(subdev, pad, stream, v4l2.uapi.v4l2_sel_tgt.COMPOSE_PADDED)


def print_routes(subdev):
    routes = subdev.get_routes()
    if not routes:
        return

    print('  Routing:')
    for r in routes:
        print('    {}/{} -> {}/{} [{}]'.format(r.sink_pad, r.sink_stream,
                                               r.source_pad, r.source_stream,
                                               v4l2.RouteFlag(r.flags).name))


def print_videodev_pad(videodev, print_supported):
    def print_videodef_fmts(videodev, buftype, title,):
        fmts = videodev.get_formats(buftype)
        fmts = [f"{f.name} ('{v4l2.fourcc_to_str(f.v4l2_fourcc)}')" for f in fmts]

        unsupported_fmts = videodev.get_unsupported_formats(buftype)
        unsupported_fmts = [f"'{f}'" for f in unsupported_fmts]

        fmts += unsupported_fmts

        if not fmts:
            return

        fmts = ' '.join(fmts)
        fmts = (f'{title}: {fmts}')
        fmts = textwrap.fill(fmts, width=100, initial_indent=' ' * 4,
                             subsequent_indent=' ' * (4 + len(title) + 2))
        print(fmts)

    if videodev.has_capture:
        try:
            fmt = videodev.get_format(v4l2.BufType.VIDEO_CAPTURE)
            f = fmt.fmt.pix
            fmt = f'{f.width}x{f.height}/{v4l2.fourcc_to_str(f.pixelformat)}'
            print(f'    vcap: {fmt}')
        except OSError as e:
            if e.errno != errno.ENOTTY:
                print(f'    <{e}>')

        if print_supported:
            print_videodef_fmts(videodev, v4l2.BufType.VIDEO_CAPTURE, 'vcap')

    if videodev.has_mplane_capture:
        try:
            fmt = videodev.get_format(v4l2.BufType.VIDEO_CAPTURE_MPLANE)
            f = fmt.fmt.pix_mp
            fmt = f'{f.width}x{f.height}/{v4l2.fourcc_to_str(f.pixelformat)} numplanes:{f.num_planes}'
            print(f'    vcapm: {fmt}')
        except OSError as e:
            if e.errno != errno.ENOTTY:
                print(f'    <{e}>')

        if print_supported:
            print_videodef_fmts(videodev, v4l2.BufType.VIDEO_CAPTURE_MPLANE, 'vcapm')

    if videodev.has_meta_capture:
        try:
            fmt = videodev.get_format(v4l2.BufType.META_CAPTURE)
            f = fmt.fmt.meta
            fmt = f'{f.buffersize}/{v4l2.fourcc_to_str(f.dataformat)}'
            print(f'    mcap: {fmt}')
        except OSError as e:
            if e.errno != errno.ENOTTY:
                print(f'    <{e}>')

        if print_supported:
            print_videodef_fmts(videodev, v4l2.BufType.META_CAPTURE, 'mcap')

    if videodev.has_meta_output:
        try:
            fmt = videodev.get_format(v4l2.BufType.META_OUTPUT)
            f = fmt.fmt.meta
            fmt = f'{f.buffersize}/{v4l2.fourcc_to_str(f.dataformat)}'
            print(f'    mout: {fmt}')
        except OSError as e:
            if e.errno != errno.ENOTTY:
                print(f'    <{e}>')

        if print_supported:
            print_videodef_fmts(videodev, v4l2.BufType.META_OUTPUT, 'mout')


def print_streams(subdev, pad, streams, print_supported):
    for s in streams:
        try:
            fmt = subdev.get_format(pad.index, s)
            f = fmt.format

            try:
                bfmt = v4l2.BusFormat(f.code).name
            except ValueError:
                bfmt = f'0x{f.code:x}'

            print(f'    Stream{s} {f.width}✕{f.height}/{bfmt} field:{f.field} colorspace:{f.colorspace} quantization:{f.quantization} xfer:{f.xfer_func} flags:{f.flags}')
        except OSError as e:
            if e.errno != errno.ENOTTY:
                print(f'    Stream{s} <{e}>')

        try:
            ival = subdev.get_frame_interval(pad.index, s)
            if ival[0] == 0:
                ival = (1, 0)
            print(f'            Interval {ival[0]}/{ival[1]} = {ival[1] / ival[0]} fps')
        except OSError as e:
            if e.errno != errno.ENOTTY:
                print(f'            Interval {e}')

        print_selections(subdev, pad, s)

        if print_supported:
            codes = subdev.get_formats(pad.index, s)
            codes = [c.name for c in codes]

            unsupported_codes = subdev.get_unsupported_formats(pad.index, s)
            unsupported_codes = [f'{f:#x}' for f in unsupported_codes]

            codes += unsupported_codes

            if codes:
                codes = 'codes: ' + str.join(' ', codes)

                codes = textwrap.fill(codes, width=100, initial_indent=' ' * 6,
                                     subsequent_indent=' ' * (7 + 6))
                print(codes)


def print_pads(ent, subdev, videodev, only_graph: bool, print_supported):
    if subdev:
        routes = [r for r in subdev.get_routes() if r.is_active]
    else:
        routes = None

    for pad in ent.pads:
        links = list([l for l in pad.links if l.is_enabled])

        # Don't show external pads that have no enabled links
        #if len(links) == 0 and not pad.is_internal:
        #    continue

        link_dir = '->' if pad.is_source else '<-'

        # If there's only one link, use compact formatting
        if len(links) == 1:
            link = links[0]
            remote_pad = link.source_pad if link.sink_pad == pad else link.sink_pad
            link_fmt = f"{link_dir} '{remote_pad.entity.name}':{remote_pad.index} [{v4l2.MediaLinkFlag(link.flags).name}]"
            print(f'  Pad{pad.index} [{pad.flags.name}] {link_fmt}')
        else:
            print(f'  Pad{pad.index} [{pad.flags.name}]')

            for link in links:
                remote_pad = link.source_pad if link.sink_pad == pad else link.sink_pad
                print(f"      {link_dir} '{remote_pad.entity.name}':{remote_pad.index} [{v4l2.MediaLinkFlag(link.flags).name}]")

        if routes:
            streams = set([r.source_stream for r in routes if r.source_pad == pad.index] + [r.sink_stream for r in routes if r.sink_pad == pad.index])
        else:
            streams = [ 0 ]

        streams = sorted(streams)

        if not only_graph and videodev:
            print_videodev_pad(videodev, print_supported)

        if not only_graph and subdev:
            print_streams(subdev, pad, streams, print_supported)


def print_entity(ent, only_graph: bool, print_supported):
    print(f"Entity {ent.id}: '{ent.name}', Function: {ent.function.name}", end='')
    if ent.interface:
        print(f', Interface: {ent.interface.intf_type.name}', end='')
        if ent.interface.dev_path:
            print(f', Path: {ent.interface.dev_path}')
        else:
            print()
    else:
        print()

    if ent.interface and ent.interface.is_subdev:
        subdev = v4l2.SubDevice(ent.interface.dev_path)
    else:
        subdev = None

    if ent.interface and ent.interface.is_video:
        videodev = v4l2.VideoDevice(ent.interface.dev_path)
    else:
        videodev = None

    print_pads(ent, subdev, videodev, only_graph, print_supported)

    if not only_graph and subdev:
        print_routes(subdev)

    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device', default='/dev/media0', help='Media device')
    parser.add_argument('-g', '--graph', action='store_true', help='Print only the graph, no streams or routing')
    parser.add_argument('-s', '--supported', action='store_true', help='Print also supported formats')
    parser.add_argument('-a', '--all', action='store_true', help='Print all entitites, not just linked ones')
    parser.add_argument('pattern', nargs='?', help='Entity pattern to show')
    args = parser.parse_args()

    md = v4l2.MediaDevice(args.device)

    if args.pattern:
        if args.all:
            print('Entity pattern and --all cannot be used at the same time')
            return -1

        pat = args.pattern.lower()

        entities = [ent for ent in md.entities if pat in ent.name.lower() or pat in (ent.interface.dev_path if ent.interface else '')]
        print_queue = entities
        recurse = False
    else:
        entities = list(md.entities)

        # start with source-only subdevs (sensors)
        print_queue = sorted([ent for ent in entities if not any(p.is_sink and not p.is_internal for p in ent.pads)], key=lambda e: e.name)

        recurse = True

    def flatten(t):
        return [item for sublist in t for item in sublist]

    print(f'Driver: {md.driver}, Model: {md.model}, Bus info: {md.bus_info}')
    print()

    printed = set()

    while len(print_queue) > 0:
        ent = print_queue.pop(0)

        if ent in printed:
            continue

        printed.add(ent)

        if recurse:
            if args.all:
                links = flatten([ p.links for p in ent.pads ])

                print_queue += [ l.sink_pad.entity for l in links ]
                print_queue += [ l.source_pad.entity for l in links ]
            else:
                links = flatten([ p.links for p in ent.pads if p.is_source ])
                links = [l for l in links if l.is_enabled]

                print_queue += [ l.sink_pad.entity for l in links ]

        print_entity(ent, only_graph=args.graph, print_supported=args.supported)

    return 0

if __name__ == '__main__':
    sys.exit(main())
