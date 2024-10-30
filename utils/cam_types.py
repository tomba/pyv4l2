from __future__ import annotations

from collections import deque
from typing import TypedDict

from kms import DumbFramebuffer, Plane
from v4l2 import PixelFormat, MetaFormat

from v4l2.videodev import CaptureStreamer, VideoBuffer, VideoDevice


pix_or_meta_fmt = PixelFormat | MetaFormat


Stream = TypedDict(
    'Stream',
    {
        'id': int,
        'num_bufs': int,
        'display': bool,
        'embedded': bool,
        'fmt': tuple[int, int, pix_or_meta_fmt] | tuple[int, pix_or_meta_fmt],
        'w': int,
        'h': int,
        'size': int,
        'format': pix_or_meta_fmt,
        'entity': str,
        'dev_path': str,
        'dev': VideoDevice,
        'device': tuple[str, str],
        'cap': CaptureStreamer,
        'fbs': list[DumbFramebuffer],
        'kms-buf-w': int,
        'kms-buf-h': int,
        'kms-format': PixelFormat,
        'kms-src-w': int,
        'kms-src-h': int,
        'kms-src-x': int,
        'kms-src-y': int,
        'kms-dst-w': int,
        'kms-dst-h': int,
        'kms-dst-x': int,
        'kms-dst-y': int,
        'kms_old_fb': DumbFramebuffer | None,
        'kms_fb': DumbFramebuffer,
        'kms_fb_queue': deque,
        'plane': Plane,
        'total_num_frames': int,
        'last_framenum': int,
        'last_timestamp': float,
        'tx_buf': VideoBuffer | None,
    },
)
