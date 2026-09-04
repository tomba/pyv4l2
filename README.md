[![Lint Status](https://github.com/tomba/pyv4l2/actions/workflows/ci.yml/badge.svg)](https://github.com/tomba/pyv4l2/actions/workflows/ci.yml)

# Pure-Python Linux kernel Video4Linux2 (V4L2) bindings

## v4l2.uapi

v4l2.uapi namespace contains the kernel user-space API (uAPI).

The uAPI is generated with (slighly customized) ctypesgen, with the gen.py script. Also, the `v4l2/uapi/__init__.py` contains some minor additions to the uAPI.

## v4l2

v4l2 namespace contains wrappers to the uAPI to simplify the use of the uAPI. The target is that the user of the v4l2 namespace does not need to use any types from the v4l2.uapi namespace.

### State

The wrappers cache only what the kernel keeps stable, or what only this process changes through its own fd. Everything else is read from the kernel on every access:

- The media graph structure (entities, interfaces, pads, links) and the device capabilities are read when the device is opened. `MediaDevice.refresh()` re-reads the graph; objects from the old graph are not updated.
- Link flags, formats, selections, routes, frame intervals and controls are never cached. `get_*()` methods do an ioctl, and `set_*()` methods return what the driver applied.
- A `Streamer` keeps track of what it has done: the format it set, the buffers it allocated, which of them are queued to the driver, and whether streaming is on.

Devices close their fd with `close()`, when used as a context manager, or when garbage collected.

## utils

utils directory contains miscallaneous more-or-less under-work utilities:

- mc-print.py: Print the media graph from a media device
- mc-dot.py: Generate a graphviz dot file from the media graph
- cam.py: A video capture utility. It uses media graph configs from cam-configs, and optionally shows the frames with kms or sends the frames over network
- cam-rx.py: A Qt utility that receives frames from cam.py over network, and shows the frames with Qt

## License

This project is covered by the [LGPL-3.0](LICENSE.md) license.

## Install

`pip install git+https://github.com/tomba/pyv4l2.git`
