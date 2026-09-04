from __future__ import annotations

import ctypes
import errno
import fcntl
from dataclasses import dataclass
from enum import Enum, IntFlag

import v4l2.uapi

from .device import V4L2Device
from .helpers import (
    ColorSpace,
    Field,
    Quantization,
    Rect,
    SelectionTarget,
    XferFunc,
    YCbCrEncoding,
    enum_or_int,
    enum_value,
)
from .mbusformats import BusFormat

__all__ = ['Route', 'RouteFlag', 'SubDevice', 'SubdevFormat', 'Which']


class Which(Enum):
    TRY = v4l2.uapi.V4L2_SUBDEV_FORMAT_TRY
    ACTIVE = v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE


@dataclass
class SubdevFormat:
    width: int
    height: int
    code: BusFormat | int
    field: Field | int = Field.NONE
    colorspace: ColorSpace | int | None = None
    ycbcr_enc: YCbCrEncoding | int | None = None
    quantization: Quantization | int | None = None
    xfer_func: XferFunc | int | None = None
    flags: int = 0

    @classmethod
    def from_v4l2_mbus_framefmt(cls, f: v4l2.uapi.v4l2_mbus_framefmt):
        return cls(
            f.width,
            f.height,
            enum_or_int(BusFormat, f.code),
            enum_or_int(Field, f.field),
            enum_or_int(ColorSpace, f.colorspace),
            enum_or_int(YCbCrEncoding, f.ycbcr_enc),
            enum_or_int(Quantization, f.quantization),
            enum_or_int(XferFunc, f.xfer_func),
            f.flags,
        )

    def to_v4l2_mbus_framefmt(self, f: v4l2.uapi.v4l2_mbus_framefmt):
        """Fill in f. Fields that are None keep the value they have in f."""
        f.width = self.width
        f.height = self.height
        f.code = enum_value(self.code)
        f.field = enum_value(self.field)
        if self.colorspace is not None:
            f.colorspace = enum_value(self.colorspace)
        if self.ycbcr_enc is not None:
            f.ycbcr_enc = enum_value(self.ycbcr_enc)
        if self.quantization is not None:
            f.quantization = enum_value(self.quantization)
        if self.xfer_func is not None:
            f.xfer_func = enum_value(self.xfer_func)
        f.flags = self.flags


class RouteFlag(IntFlag):
    ACTIVE = v4l2.uapi.V4L2_SUBDEV_ROUTE_FL_ACTIVE
    IMMUTABLE = v4l2.uapi.V4L2_SUBDEV_ROUTE_FL_IMMUTABLE


_NO_ROUTE_FLAGS = RouteFlag(0)


@dataclass
class Route:
    sink_pad: int = 0
    sink_stream: int = 0
    source_pad: int = 0
    source_stream: int = 0
    flags: RouteFlag = _NO_ROUTE_FLAGS

    @property
    def is_active(self):
        return bool(self.flags & RouteFlag.ACTIVE)

    @property
    def is_immutable(self):
        return bool(self.flags & RouteFlag.IMMUTABLE)

    def __repr__(self) -> str:
        return f'Route({self.sink_pad}/{self.sink_stream}->{self.source_pad}/{self.source_stream} ({self.flags:#x}))'

    @classmethod
    def from_v4l2_subdev_route(cls, route: v4l2.uapi.v4l2_subdev_route):
        return cls(
            route.sink_pad,
            route.sink_stream,
            route.source_pad,
            route.source_stream,
            RouteFlag(route.flags),
        )

    def to_v4l2_subdev_route(self):
        return v4l2.uapi.v4l2_subdev_route(
            sink_pad=self.sink_pad,
            sink_stream=self.sink_stream,
            source_pad=self.source_pad,
            source_stream=self.source_stream,
            flags=int(self.flags),
        )


class SubDevice(V4L2Device):
    def __init__(self, dev_path: str) -> None:
        super().__init__(dev_path)

        try:
            cap = v4l2.uapi.v4l2_subdev_client_capability()
            cap.capabilities = v4l2.uapi.V4L2_SUBDEV_CLIENT_CAP_STREAMS
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_CLIENT_CAP, cap, True)
            self.has_streams = (cap.capabilities & v4l2.uapi.V4L2_SUBDEV_CLIENT_CAP_STREAMS) != 0
        except OSError:
            self.has_streams = False

    def get_formats(self, pad, stream=0, which: Which = Which.ACTIVE):
        val = v4l2.uapi.v4l2_subdev_mbus_code_enum()
        val.pad = pad
        val.stream = stream
        val.which = which.value
        val.index = 0

        codes = []

        while True:
            try:
                fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_ENUM_MBUS_CODE, val, True)
            except OSError as e:
                if e.errno == errno.EINVAL:
                    break
                if e.errno == errno.ENOTTY:
                    return []
                raise

            try:
                code = v4l2.BusFormat(val.code)
                codes.append(code)
            except ValueError:
                pass

            val.index += 1

        return codes

    def get_unsupported_formats(self, pad, stream=0, which: Which = Which.ACTIVE):
        val = v4l2.uapi.v4l2_subdev_mbus_code_enum()
        val.pad = pad
        val.stream = stream
        val.which = which.value
        val.index = 0

        codes = []

        while True:
            try:
                fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_ENUM_MBUS_CODE, val, True)
            except OSError as e:
                if e.errno == errno.EINVAL:
                    break
                if e.errno == errno.ENOTTY:
                    return []
                raise

            try:
                v4l2.BusFormat(val.code)
            except ValueError:
                codes.append(val.code)

            val.index += 1

        return codes

    def get_framesizes(self, pad, code, stream=0, which: Which = Which.ACTIVE):
        val = v4l2.uapi.v4l2_subdev_frame_size_enum()
        val.pad = pad
        val.code = code
        val.stream = stream
        val.which = which.value
        val.index = 0

        frame_sizes = []

        while True:
            try:
                fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_ENUM_FRAME_SIZE, val, True)
            except OSError as e:
                if e.errno == errno.EINVAL:
                    break
                if e.errno == errno.ENOTTY:
                    return []
                raise

            frame_sizes.append((val.min_width, val.min_height))

            val.index += 1

        return frame_sizes

    def get_format(self, pad, stream=0, which: Which = Which.ACTIVE) -> SubdevFormat:
        fmt = v4l2.uapi.v4l2_subdev_format()
        fmt.pad = pad
        fmt.stream = stream
        fmt.which = which.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_FMT, fmt, True)
        return SubdevFormat.from_v4l2_mbus_framefmt(fmt.format)

    def set_format(
        self, pad, stream, format: SubdevFormat, which: Which = Which.ACTIVE
    ) -> SubdevFormat:
        """Set the format. Fields that are None keep their current values.

        Returns the format the driver applied."""
        fmt = v4l2.uapi.v4l2_subdev_format()
        fmt.pad = pad
        fmt.stream = stream
        fmt.which = which.value

        try:
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_FMT, fmt, True)
        except OSError:
            # Some drivers fail G_FMT on some pads. Start from a blank format.
            pass

        format.to_v4l2_mbus_framefmt(fmt.format)
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_FMT, fmt, True)

        return SubdevFormat.from_v4l2_mbus_framefmt(fmt.format)

    def get_routes(self, which: Which = Which.ACTIVE) -> list[Route]:
        routing = v4l2.uapi.v4l2_subdev_routing()
        routing.which = which.value

        try:
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_ROUTING, routing, True)
        except OSError as e:
            if e.errno == errno.ENOTTY:
                return []
            if e.errno != errno.ENOSPC:
                raise

        routes = (v4l2.uapi.v4l2_subdev_route * routing.num_routes)()
        routing.routes = ctypes.addressof(routes)
        routing.len_routes = routing.num_routes

        try:
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_ROUTING, routing, True)
        except OSError as e:
            if e.errno == errno.ENOTTY:
                routes = (v4l2.uapi.v4l2_subdev_route * 0)()
            else:
                raise

        routes = [Route.from_v4l2_subdev_route(r) for r in routes]

        return routes

    def set_routes(self, routes: list[Route], which: Which = Which.ACTIVE) -> list[Route]:
        kroutes = (v4l2.uapi.v4l2_subdev_route * len(routes))()
        for i, route in enumerate(routes):
            kroutes[i] = route.to_v4l2_subdev_route()

        routing = v4l2.uapi.v4l2_subdev_routing()
        routing.which = which.value
        routing.len_routes = len(routes)
        routing.num_routes = len(routes)
        routing.routes = ctypes.addressof(kroutes)

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_ROUTING, routing, True)

        # The driver may have added routes that did not fit in the array
        if routing.num_routes > len(routes):
            return self.get_routes(which)

        return [Route.from_v4l2_subdev_route(kroutes[i]) for i in range(routing.num_routes)]

    def get_selection(
        self,
        target: SelectionTarget,
        pad,
        stream=0,
        which: Which = Which.ACTIVE,
    ) -> Rect:
        sel = v4l2.uapi.v4l2_subdev_selection()
        sel.pad = pad
        sel.stream = stream
        sel.which = which.value
        sel.target = target.value
        sel.flags = 0

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_SELECTION, sel, True)

        return Rect.from_v4l2_rect(sel.r)

    def set_selection(
        self,
        target: SelectionTarget,
        rect: Rect,
        pad,
        stream=0,
        which: Which = Which.ACTIVE,
    ) -> Rect:
        """Set a selection rectangle. Returns the rectangle the driver applied."""
        sel = v4l2.uapi.v4l2_subdev_selection()
        sel.pad = pad
        sel.stream = stream
        sel.which = which.value
        sel.target = target.value
        sel.flags = 0
        sel.r = rect.to_v4l2_rect()

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_SELECTION, sel, True)

        return Rect.from_v4l2_rect(sel.r)

    def get_frame_interval(self, pad, stream=0, which: Which = Which.ACTIVE):
        v4l2_ival = v4l2.uapi.v4l2_subdev_frame_interval()
        v4l2_ival.pad = pad
        v4l2_ival.stream = stream
        v4l2_ival.which = which.value

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_FRAME_INTERVAL, v4l2_ival, True)

        return (v4l2_ival.interval.numerator, v4l2_ival.interval.denominator)

    def set_frame_interval(
        self, pad, stream, interval: tuple[int, int], which: Which = Which.ACTIVE
    ):
        v4l2_ival = v4l2.uapi.v4l2_subdev_frame_interval()
        v4l2_ival.pad = pad
        v4l2_ival.stream = stream
        v4l2_ival.which = which.value
        v4l2_ival.interval.numerator = interval[0]
        v4l2_ival.interval.denominator = interval[1]

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_FRAME_INTERVAL, v4l2_ival, True)

        return (v4l2_ival.interval.numerator, v4l2_ival.interval.denominator)
