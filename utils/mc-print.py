#!/usr/bin/python3

import v4l2
import v4l2.uapi
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--device', default='/dev/media0', help='media device')
parser.add_argument('pattern', nargs='?', help='Entity pattern to show')
args = parser.parse_args()

md = v4l2.MediaDevice(args.device)

if args.pattern:
    pat = args.pattern.lower()

    entities = [ent for ent in md.entities if pat in ent.name.lower() or pat in (ent.interface.dev_path if ent.interface else '')]
    print_queue = entities
    recurse = False
else:
    entities = list(md.entities)

    # start with source-only subdevs (sensors)
    print_queue = sorted([ent for ent in entities if not any(p.is_sink and not p.is_internal for p in ent.pads)], key=lambda e: e.name)

    recurse = True

flatten = lambda t: [item for sublist in t for item in sublist]

printed = set()

while len(print_queue) > 0:
    ent = print_queue.pop(0)

    if ent in printed:
        continue

    printed.add(ent)

    links = flatten([ p.links for p in ent.pads if p.is_source ])

    if recurse:
        print_queue += [ l.sink.entity for l in links ]

    pads_with_links = any([p for p in ent.pads if any([l for l in p.links if l.is_enabled])])
    if not pads_with_links:
        continue

    subdev = None
    if ent.interface and ent.interface.is_subdev:
        subdev = v4l2.SubDevice(ent)

    videodev = None
    if ent.interface and ent.interface.is_video:
        videodev = v4l2.VideoDevice(ent)

    routes = []
    if subdev:
        routes = [r for r in subdev.get_routes() if r.is_active]

    print(ent.name, ent.interface.dev_path if ent.interface else '')

    for pad in ent.pads:
        links = list([l for l in pad.links if l.is_enabled])
        if len(links) == 0:
            continue

        print('  Pad{} ({}) '.format(pad.index, 'Source' if pad.is_source else 'Sink'))

        for link in links:
            remote_pad = link.source_pad if link.sink_pad == pad else link.sink_pad
            dir = '->' if pad.is_source else '<-'
            print(f'    {dir} \'{remote_pad.entity.name}\':{remote_pad.index} [{v4l2.MediaLinkFlag(link.flags).name}]')

        streams = set([r.source_stream for r in routes if r.source_pad == pad.index] + [r.sink_stream for r in routes if r.sink_pad == pad.index])

        if len(streams) == 0:
            streams = [ 0 ]

        streams = sorted(streams)

        for s in streams:
            fmt = None
            err = ''

            if subdev:
                try:
                    fmt = subdev.get_format(pad.index, s)
                    f = fmt.format
                    try:
                        bfmt = v4l2.BusFormat(f.code).name
                    except ValueError:
                        bfmt = f'0x{f.code:x}'

                    fmt = f'{f.width}✕{f.height}/{bfmt} field:{f.field} colorspace:{f.colorspace} quantization:{f.quantization} xfer:{f.xfer_func} flags:{f.flags}'
                except Exception as e:
                    fmt = None
                    err = e
            elif videodev:
                try:
                    fmt = videodev.get_format()

                    if fmt.type == v4l2.uapi.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE:
                        f = fmt.fmt.pix_mp
                        fmt = f'{f.width}x{f.height}-{v4l2.fourcc_to_str(f.pixelformat)} numplanes:{f.num_planes}'
                    elif fmt.type == v4l2.uapi.V4L2_BUF_TYPE_VIDEO_CAPTURE:
                        f = fmt.fmt.pix
                        fmt = f'{f.width}x{f.height}-{v4l2.fourcc_to_str(f.pixelformat)}'
                except Exception as e:
                    fmt = None
                    err = repr(e)

            if err:
                print('    Stream{} <{}>'.format(s, err))
            else:
                print('    Stream{} {}'.format(s, fmt))

            if subdev:
                r = subdev.get_selection(v4l2.uapi.V4L2_SEL_TGT_CROP_BOUNDS, pad.index)
                print(f'    crop.bounds:({r.left},{r.top})/{r.width}✕{r.height}')

                r = subdev.get_selection(v4l2.uapi.V4L2_SEL_TGT_CROP, pad.index)
                print(f'    crop:({r.left},{r.top})/{r.width}✕{r.height}')

    if subdev:
        routes = [r for r in subdev.get_routes() if r.is_active]
        if len(routes) > 0:
            print('  Routing:')
            for r in routes:
                print('    {}/{} -> {}/{}'.format(r.sink_pad, r.sink_stream, r.source_pad, r.source_stream))

    print()
