#!/usr/bin/python3

import v4l2
from typing import cast

md = v4l2.MediaDevice('/dev/media0')

for e in md.entities:
    print(f'- entity {e.id}: {e.name} ({len(e.pads)} pad(s), {len(e.pad_links)} link(s))')
    print(f'\t\tfunction:{e.function} flags:{e.flags}')

    if e.interface:
        print("\t\tdevice node name", e.interface.dev_path)

        if e.interface.is_video:
            vdev = v4l2.VideoDevice(e)

            try:
                f = vdev.get_format()
            except:
                pass
            else:
                print(f'\t\tfmt: {f.fmt.pix.width}x{f.fmt.pix.height}')
        elif e.interface.is_subdev:
            subdev = v4l2.SubDevice(e)

            try:
                f = subdev.get_format(v4l2.V4L2_SUBDEV_FORMAT_ACTIVE, 0, stream=0)
            except:
                pass
            finally:
                print(f'\t\tfmt: {f}')

    for p in e.pads:
        print("\tpad{}: {}{}".format(p.index, "Source" if p.is_source else "", "Sink" if p.is_sink else ""))

        for l in p.links:
            if p.is_source:
                other = l.sink
            else:
                other = l.source

            other = cast(v4l2.MediaPad, other)

            print(f'\t\t"{other.entity.name}":{other.index} [flags:{l.flags}]')
