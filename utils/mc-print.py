#!/usr/bin/python3

import v4l2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--device", default="/dev/media0", help="media device")
parser.add_argument("pattern", nargs="?", help="Entity pattern to show")
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

        print("  Pad{} ({}) ".format(pad.index, "Source" if pad.is_source else "Sink"))

        for link in links:
            remote_pad = link.source_pad if link.sink_pad == pad else link.sink_pad
            print("    {} '{}':{}".format("->" if pad.is_source else "<-", remote_pad.entity.name, remote_pad.index))

        streams = set([r.source_stream for r in routes if r.source_pad == pad.index] + [r.sink_stream for r in routes if r.sink_pad == pad.index])

        if len(streams) == 0:
            streams = [ 0 ]

        streams = sorted(streams)

        for s in streams:
            fmt = None
            err = ""

            if subdev:
                try:
                    fmt = subdev.get_format(pad.index, s)
                except Exception as e:
                    fmt = None
                    err = e
            elif videodev:
                try:
                    fmt = videodev.get_format()
                except Exception as e:
                    fmt = None
                    err = e

            if err:
                print("    Stream{} <{}>".format(s, err))
            else:
                print("    Stream{} {}".format(s, fmt))

            if subdev:
                sel = subdev.get_selection(v4l2.V4L2_SEL_TGT_CROP_BOUNDS, pad.index)
                print("    crop.bounds", sel.r)

                sel = subdev.get_selection(v4l2.V4L2_SEL_TGT_CROP, pad.index)
                print("    crop", sel.r)

    if subdev:
        routes = [r for r in subdev.get_routes() if r.is_active]
        if len(routes) > 0:
            print("  Routing:")
            for r in routes:
                print("    {}/{} -> {}/{}".format(r.sink_pad, r.sink_stream, r.source_pad, r.source_stream))

    print()
