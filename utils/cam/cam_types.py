from __future__ import annotations

import types
from abc import ABC, abstractmethod
from collections.abc import Callable
from enum import Enum, auto
from selectors import BaseSelector

from kms import DumbFramebuffer

import v4l2
from v4l2 import MetaFormat, PixelFormat
from v4l2.videodev import Streamer, VideoDevice

pix_or_meta_fmt = PixelFormat | MetaFormat


class Updater(ABC):
    @abstractmethod
    def update(self):
        pass


class StreamState(Enum):
    RUNNING = auto()
    DRAINING = auto()  # Stopping, waiting for the consumer to return buffers
    STOPPED = auto()


class Stream:
    id: int  # Unique stream ID
    sctx: Subcontext
    state: StreamState
    num_bufs: int
    display: bool
    embedded: bool
    fmt: tuple[int, int, pix_or_meta_fmt] | tuple[int, pix_or_meta_fmt]
    w: int
    h: int
    size: int | tuple[int, int]
    format: pix_or_meta_fmt
    entity: str
    dev_path: str
    dev: VideoDevice
    device: tuple[str, str]
    cap: Streamer
    fbs: list[DumbFramebuffer]  # XXX used from cam_net...
    total_num_frames: int
    last_framenum: int
    last_timestamp: float

    # XXX Hack to get the format from the config to the kms consumer
    kms_format: PixelFormat


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
    use_tui: bool
    start_streams: bool
    user_script: types.ModuleType | None
    buf_type: str
    use_display: bool
    print_config: bool
    config_only: bool
    delay: int
    save: bool
    tx: None | list[str]
    run_tui: Callable
    exit: bool
    exit_num_frames: int

    net_host: str
    net_port: int

    updater: None | Updater

    consumer: None | Consumer


# Frame consumer interface
class Consumer(ABC):
    @abstractmethod
    def setup_stream(self, ctx: Context, stream: Stream) -> bool:
        """Returns if the first buffer of the stream was taken by the consumer"""
        return False

    def setup_streams_done(self, ctx: Context):
        pass

    def cleanup(self, ctx: Context):
        pass

    @abstractmethod
    def handle_frame(self, ctx: Context, stream: Stream, vbuf):
        """Handle a frame from a stream."""

    def handle_tick(self, ctx: Context):
        """Called every time there's any event"""

    def register_selector(self, sel: BaseSelector):
        pass

    def drain_done(self, ctx: Context, stream: Stream) -> bool:
        """Has the consumer returned all the buffers it can for a stopping stream"""
        return True

    def held_vbuffers(self, ctx: Context, stream: Stream) -> list:
        """Buffers the consumer keeps over a stream stop (e.g. the fb on screen).

        These must not be queued to the camera when restarting the stream."""
        return []
