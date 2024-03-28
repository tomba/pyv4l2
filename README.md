[![Lint Status](https://github.com/tomba/pyv4l2/actions/workflows/pylint.yml/badge.svg)](https://github.com/tomba/pyv4l2/actions/workflows/pylint.yml)

# Pure-Python Linux kernel Video4Linux2 (V4L2) bindings

## v4l2.uapi

v4l2.uapi namespace contains the kernel user-space API (uAPI).

The uapi is generated with (slighly customized) ctypesgen, with the gen.sh script. Also, the v4l2/uapi/__init__.py contains some minor additions to the uapi.

## v4l2

v4l2 namespace contains wrappers to the uAPI to simplify the use of the uAPI. The target is that the user of the v4l2 namespace does not need to use any types from the v4l2.uapi namespace.

## utils

utils directory contains miscallaneous more-or-less under-work utilities:

- mc-print.py: Print the media graph from a media device
- mc-dot.py: Generate a graphviz dot file from the media graph
- cam.py: A video capture utility. It uses media graph configs from cam-configs, and optionally shows the frames with kms or sends the frames over network
- cam-rx.py: A Qt utility that receives frames from cam.py over network, and shows the frames with Qt

## License

This project is covered by the [LGPL-3.0](LICENSE.md) license.
