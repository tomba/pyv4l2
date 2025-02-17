from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from selectors import BaseSelector
from typing import TypedDict, Callable
import types

from kms import DumbFramebuffer, Plane

import v4l2
from v4l2 import PixelFormat, MetaFormat
from v4l2.videodev import CaptureStreamer, VideoBuffer, VideoDevice


pix_or_meta_fmt = PixelFormat | MetaFormat

class Updater(ABC):
    @abstractmethod
    def update(self):
        pass

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
        'size': int | tuple[int, int],
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

# Media device context
class Subcontext:
    md: v4l2.MediaDevice | None
    config: dict
    subdevices: dict[str, v4l2.SubDevice] | None
    streams: list[Stream]
    ctx: Context

# Application wide context
class Context:
    subcontexts: list[Subcontext]
    verbose: bool
    use_ipython: bool
    user_script: types.ModuleType | None
    buf_type: str
    use_display: bool
    kms_committed: bool
    print_config: bool
    config_only: bool
    delay: int
    save: bool
    tx: None | list[str]
    run_ipython: Callable
    exit: bool
    exit_num_frames: int

    net_host: str
    net_port: int

    updater: None | Updater

    consumer: None | Consumer


# Frame consumer interface
class Consumer(ABC):
    @abstractmethod
    def setup_stream(self, ctx: Context, stream: Stream):
        pass

    def setup_streams_done(self, ctx: Context):
        pass

    def cleanup(self, ctx: Context):
        pass

    @abstractmethod
    def handle_frame(self, ctx: Context, stream: Stream, vbuf):
        """Handle a frame from a stream."""
        pass

    def handle_tick(self, ctx: Context):
        """Called every time there's any event"""
        pass

    def register_selector(self, sel: BaseSelector):
        pass
