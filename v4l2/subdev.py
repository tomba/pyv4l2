from __future__ import annotations

import ctypes
import errno
import fcntl
from dataclasses import dataclass
from enum import IntFlag

import v4l2.uapi

from .device import V4L2Device
from .helpers import Rect, SelectionTarget

__all__ = ['Route', 'RouteFlag', 'SubDevice']


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

    def get_formats(self, pad, stream=0, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        val = v4l2.uapi.v4l2_subdev_mbus_code_enum()
        val.pad = pad
        val.stream = stream
        val.which = which
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

    def get_unsupported_formats(self, pad, stream=0, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        val = v4l2.uapi.v4l2_subdev_mbus_code_enum()
        val.pad = pad
        val.stream = stream
        val.which = which
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

    def get_framesizes(self, pad, code, stream=0, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        val = v4l2.uapi.v4l2_subdev_frame_size_enum()
        val.pad = pad
        val.code = code
        val.stream = stream
        val.which = which
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

    def get_format(self, pad, stream=0, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        fmt = v4l2.uapi.v4l2_subdev_format()
        fmt.pad = pad
        fmt.stream = stream
        fmt.which = which
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_FMT, fmt, True)
        return fmt

    def set_format(self, pad, stream, w, h, code, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        try:
            fmt = self.get_format(pad, stream, which)
        except OSError:
            print(
                f'Failed to get format from {self}:{pad}/{stream}, trying set_format with blank v4l2_subdev_format'
            )
            fmt = v4l2.uapi.v4l2_subdev_format()

        fmt.pad = pad
        fmt.stream = stream
        fmt.which = which
        fmt.format.width = w
        fmt.format.height = h
        fmt.format.code = code
        fmt.format.field = v4l2.uapi.V4L2_FIELD_NONE
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_FMT, fmt, True)

    def get_routes(self, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE) -> list[Route]:
        routing = v4l2.uapi.v4l2_subdev_routing()
        routing.which = which

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

    def set_routes(
        self, routes: list[Route], which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE
    ) -> list[Route]:
        kroutes = (v4l2.uapi.v4l2_subdev_route * len(routes))()
        for i, route in enumerate(routes):
            kroutes[i] = route.to_v4l2_subdev_route()

        routing = v4l2.uapi.v4l2_subdev_routing()
        routing.which = which
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
        which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE,
    ) -> Rect:
        sel = v4l2.uapi.v4l2_subdev_selection()
        sel.pad = pad
        sel.stream = stream
        sel.which = which
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
        which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE,
    ) -> Rect:
        """Set a selection rectangle. Returns the rectangle the driver applied."""
        sel = v4l2.uapi.v4l2_subdev_selection()
        sel.pad = pad
        sel.stream = stream
        sel.which = which
        sel.target = target.value
        sel.flags = 0
        sel.r = rect.to_v4l2_rect()

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_SELECTION, sel, True)

        return Rect.from_v4l2_rect(sel.r)

    def get_frame_interval(self, pad, stream=0, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        v4l2_ival = v4l2.uapi.v4l2_subdev_frame_interval()
        v4l2_ival.pad = pad
        v4l2_ival.stream = stream
        v4l2_ival.which = which

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_FRAME_INTERVAL, v4l2_ival, True)

        return (v4l2_ival.interval.numerator, v4l2_ival.interval.denominator)

    def set_frame_interval(
        self, pad, stream, interval: tuple[int, int], which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE
    ):
        v4l2_ival = v4l2.uapi.v4l2_subdev_frame_interval()
        v4l2_ival.pad = pad
        v4l2_ival.stream = stream
        v4l2_ival.which = which
        v4l2_ival.interval.numerator = interval[0]
        v4l2_ival.interval.denominator = interval[1]

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_FRAME_INTERVAL, v4l2_ival, True)

        return (v4l2_ival.interval.numerator, v4l2_ival.interval.denominator)
