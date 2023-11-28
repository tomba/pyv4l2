import ctypes
import errno
import fcntl
import v4l2

class Route:
    def __init__(self, route: v4l2.v4l2_subdev_route) -> None:
        self.v4l2_route = route
        self.sink_pad = route.sink_pad
        self.sink_stream = route.sink_stream
        self.source_pad = route.source_pad
        self.source_stream = route.source_stream
        self.flags = route.flags

    @property
    def is_active(self):
        return (self.flags & v4l2.V4L2_SUBDEV_ROUTE_FL_ACTIVE) != 0


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

    def get_routes(self, which=v4l2.V4L2_SUBDEV_FORMAT_ACTIVE):
        routing = v4l2.v4l2_subdev_routing()
        routing.which = which

        try:
            fcntl.ioctl(self.fd, v4l2.VIDIOC_SUBDEV_G_ROUTING, routing, True)
        except OSError as e:
            if e.errno == errno.ENOTTY:
                return(v4l2.v4l2_subdev_route * 0)()
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

        routes = [Route(r) for r in routes]

        return routes

    def set_routes(self, routes: list[v4l2.v4l2_subdev_route], which=v4l2.V4L2_SUBDEV_FORMAT_ACTIVE):
        routing = v4l2.v4l2_subdev_routing()
        routing.which = which

        _routes = (v4l2.v4l2_subdev_route * len(routes))()
        for i in range(len(routes)):
            _routes[i] = routes[i]

        routing.num_routes = len(routes)
        routing.routes = ctypes.addressof(_routes)

        fcntl.ioctl(self.fd, v4l2.VIDIOC_SUBDEV_S_ROUTING, routing, True)

        kroutes = [r for r in self.get_routes() if r.flags & v4l2.V4L2_SUBDEV_ROUTE_FL_ACTIVE]
        assert(len(kroutes) == len(routes))
