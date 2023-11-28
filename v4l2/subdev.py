import ctypes
import errno
import fcntl
import v4l2

class Route:
    sink_pad: int
    sink_stream: int
    source_pad: int
    source_stream: int
    flags: int

    def __init__(self) -> None:
        pass

    @property
    def is_active(self):
        return (self.flags & v4l2.V4L2_SUBDEV_ROUTE_FL_ACTIVE) != 0

    def __repr__(self) -> str:
        return f'Route({self.sink_pad}/{self.sink_stream}->{self.source_pad}/{self.source_stream} ({self.flags:#x}))'

    @classmethod
    def from_v4l2_subdev_route(cls, route: v4l2.v4l2_subdev_route):
        r = Route()
        r.sink_pad = route.sink_pad
        r.sink_stream = route.sink_stream
        r.source_pad = route.source_pad
        r.source_stream = route.source_stream
        r.flags = route.flags
        return r

    def to_v4l2_subdev_route(self):
        r = v4l2.v4l2_subdev_route(sink_pad=self.sink_pad,
                                   sink_stream=self.sink_stream,
                                   source_pad=self.source_pad,
                                   source_stream=self.source_stream,
                                   flags=self.flags)
        return r


class SubDevice:
    def __init__(self, entity: v4l2.MediaEntity) -> None:
        self.entity = entity
        assert(entity.interface.is_subdev)
        self.file = open(entity.interface.dev_path)
        self.fd = self.file.fileno()

        cap = v4l2.v4l2_subdev_client_capability()
        cap.capabilities = v4l2.V4L2_SUBDEV_CLIENT_CAP_STREAMS
        fcntl.ioctl(self.fd, v4l2.VIDIOC_SUBDEV_S_CLIENT_CAP, cap, True)
        self.has_streams = (cap.capabilities & v4l2.V4L2_SUBDEV_CLIENT_CAP_STREAMS) != 0;

    def get_format(self, pad, stream=0, which=v4l2.V4L2_SUBDEV_FORMAT_ACTIVE):
        fmt = v4l2.v4l2_subdev_format()
        fmt.pad = pad
        fmt.stream = stream
        fmt.which = which
        fcntl.ioctl(self.fd, v4l2.VIDIOC_SUBDEV_G_FMT, fmt, True)
        return fmt

    def set_format(self, pad, stream, w, h, code, which=v4l2.V4L2_SUBDEV_FORMAT_ACTIVE):
        fmt = self.get_format(pad, stream, which)

        #fmt = v4l2.v4l2_subdev_format()
        fmt.pad = pad
        fmt.stream = stream
        fmt.which = which
        fmt.format.width = w
        fmt.format.height = h
        fmt.format.code = code
        fmt.format.field = v4l2.V4L2_FIELD_NONE
        fcntl.ioctl(self.fd, v4l2.VIDIOC_SUBDEV_S_FMT, fmt, True)

    def get_routes(self, which=v4l2.V4L2_SUBDEV_FORMAT_ACTIVE) -> list[Route]:
        routing = v4l2.v4l2_subdev_routing()
        routing.which = which

        try:
            fcntl.ioctl(self.fd, v4l2.VIDIOC_SUBDEV_G_ROUTING, routing, True)
        except OSError as e:
            if e.errno == errno.ENOTTY:
                return []
            elif e.errno != errno.ENOSPC:
                raise

        routes = (v4l2.v4l2_subdev_route * routing.num_routes)()
        routing.routes = ctypes.addressof(routes)

        try:
            fcntl.ioctl(self.fd, v4l2.VIDIOC_SUBDEV_G_ROUTING, routing, True)
        except OSError as e:
            if e.errno == errno.ENOTTY:
                routes = (v4l2.v4l2_subdev_route * 0)()
            else:
                raise

        routes = [Route.from_v4l2_subdev_route(r) for r in routes]

        return routes

    def set_routes(self, routes: list[Route], which=v4l2.V4L2_SUBDEV_FORMAT_ACTIVE) -> list[Route]:
        # Allocate extra space for return routes
        kroutes = (v4l2.v4l2_subdev_route * 16)()
        for i in range(len(routes)):
            kroutes[i] = routes[i].to_v4l2_subdev_route()

        routing = v4l2.v4l2_subdev_routing()
        routing.which = which
        routing.len_routes = len(kroutes)
        routing.num_routes = len(routes)
        routing.routes = ctypes.addressof(kroutes)

        fcntl.ioctl(self.fd, v4l2.VIDIOC_SUBDEV_S_ROUTING, routing, True)

        routes = [Route.from_v4l2_subdev_route(kroutes[idx]) for idx in range(routing.num_routes)]

        return routes
