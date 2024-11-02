from __future__ import annotations

from enum import Enum
import v4l2.uapi

__all__ = [ 'BufType', 'MemType' ]

def filepath_for_major_minor(major: int, minor: int):
    with open(f'/sys/dev/char/{major}:{minor}/uevent', encoding='ascii') as f:
        for l in f.readlines():
            if not l.startswith('DEVNAME='):
                continue
            path = l[len('DEVNAME='):].strip()
            return '/dev/' + path

    raise RuntimeError(f'No device-node found for ({major},{minor})')

class BufType(Enum):
    VIDEO_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_CAPTURE
    VIDEO_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_OUTPUT
    VIDEO_OVERLAY = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_OVERLAY
    VBI_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_VBI_CAPTURE
    VBI_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_VBI_OUTPUT
    SLICED_VBI_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_SLICED_VBI_CAPTURE
    SLICED_VBI_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_SLICED_VBI_OUTPUT
    VIDEO_OUTPUT_OVERLAY = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY
    VIDEO_CAPTURE_MPLANE = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE
    VIDEO_OUTPUT_MPLANE = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE
    SDR_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_SDR_CAPTURE
    SDR_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_SDR_OUTPUT
    META_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_META_CAPTURE
    META_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_META_OUTPUT
    PRIVATE = v4l2.uapi.V4L2_BUF_TYPE_PRIVATE

class MemType(Enum):
    MMAP = v4l2.uapi.V4L2_MEMORY_MMAP
    USERPTR = v4l2.uapi.V4L2_MEMORY_USERPTR
    OVERLAY = v4l2.uapi.V4L2_MEMORY_OVERLAY
    DMABUF = v4l2.uapi.V4L2_MEMORY_DMABUF
