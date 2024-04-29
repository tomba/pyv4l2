from __future__ import annotations

import ctypes
import errno
import fcntl
import fnmatch
import glob
import os

import v4l2.uapi
import v4l2.pixelformats

__all__ = [ 'VideoDevice', 'VideoBuffer' ]

class VideoDevice:
    def __init__(self, dev_path: str) -> None:
        self.fd = os.open(dev_path, os.O_RDWR | os.O_NONBLOCK)
        assert(self.fd != -1)

        cap = v4l2.uapi.v4l2_capability()
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QUERYCAP, cap, True)

        if cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_CAPTURE_MPLANE:
            self.has_capture = True
            self.has_mplane_capture = True
        elif cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_CAPTURE:
            self.has_capture = True
            self.has_mplane_capture = False
        else:
            self.has_capture = False
            self.has_mplane_capture = False

        if cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_OUTPUT_MPLANE:
            self.has_output = True
            self.has_mplane_output = True
        elif cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_OUTPUT:
            self.has_output = True
            self.has_mplane_output = False
        else:
            self.has_output = False
            self.has_mplane_output = False

        if cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_M2M_MPLANE:
            self.has_m2m = True
            self.has_capture = True
            self.has_output = True
            self.has_mplane_m2m = True
            self.has_mplane_capture = True
            self.has_mplane_output = True
        elif cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_M2M:
            self.has_m2m = True
            self.has_capture = True
            self.has_output = True
            self.has_mplane_m2m = False
            self.has_mplane_capture = False
            self.has_mplane_output = False

        if cap.device_caps & v4l2.uapi.V4L2_CAP_META_CAPTURE:
            self.has_meta_capture = True
        else:
            self.has_meta_capture = False

        if cap.device_caps & v4l2.uapi.V4L2_CAP_META_OUTPUT:
            self.has_meta_output = True
        else:
            self.has_meta_output = False

    def __del__(self):
        os.close(self.fd)

    @staticmethod
    def find_video_device(key: str, value: str) -> str:
        for path in glob.glob('/dev/video*'):
            try:
                fd = os.open(path, os.O_RDWR | os.O_NONBLOCK)
            except:
                continue

            try:
                cap = v4l2.uapi.v4l2_capability()
                fcntl.ioctl(fd, v4l2.uapi.VIDIOC_QUERYCAP, cap, True)

                device_val = getattr(cap, key)
                device_val = ctypes.string_at(ctypes.addressof(device_val))
                device_val = device_val.decode()

                if fnmatch.fnmatch(device_val, value):
                    return path
            finally:
                os.close(fd)

        raise FileNotFoundError(f'No video device "{key}" = "{value}" found')

    def get_formats(self, buf_type: v4l2.BufType):
        fmt = v4l2.uapi.v4l2_fmtdesc()
        fmt.type = buf_type.value
        fmt.index = 0

        fmts = []

        while True:
            try:
                fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_ENUM_FMT, fmt, True)
            except OSError as e:
                if e.errno == errno.EINVAL:
                    break
                if e.errno == errno.ENOTTY:
                    return []
                raise

            if buf_type in [v4l2.BufType.META_CAPTURE, v4l2.BufType.META_OUTPUT]:
                f = v4l2.MetaFormats.find_v4l2_fourcc_unsupported(fmt.pixelformat)
            else:
                f = v4l2.PixelFormats.find_v4l2_fourcc_unsupported(fmt.pixelformat)

            fmts.append(f)

            fmt.index += 1

        return fmts

    def get_format(self, buf_type: v4l2.BufType):
        fmt = v4l2.uapi.v4l2_format()
        fmt.type = buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, fmt, True)
        return fmt

    def get_capture_streamer(self, mem_type: v4l2.MemType,
                             width: int, height: int, format: v4l2.PixelFormat):
        if not self.has_capture:
            raise NotImplementedError()

        if self.has_mplane_capture:
            return MPlaneCaptureStreamer(self, mem_type, v4l2.BufType.VIDEO_CAPTURE_MPLANE,
                                         width, height, format)
        else:
            return SPlaneCaptureStreamer(self, mem_type, v4l2.BufType.VIDEO_CAPTURE,
                                   width, height, format)

    def get_meta_capture_streamer(self, mem_type: v4l2.MemType,
                                  size: int, format: v4l2.MetaFormat):
        if self.has_meta_capture:
            return MetaCaptureStreamer(self, mem_type, v4l2.BufType.META_CAPTURE,
                                       size, format)

        if self.has_meta_output:
            return MetaOutputStreamer(self, mem_type, v4l2.BufType.META_OUTPUT,
                                       size, format)

        raise NotImplementedError()


class CaptureStreamer():
    def __init__(self, vdev: VideoDevice, mem_type: v4l2.MemType, buf_type: v4l2.BufType) -> None:
        self.vdev = vdev
        self.mem_type = mem_type
        self.buf_type = buf_type
        self.buffers: list[VideoBuffer] = []

    def set_queue_size(self, queue_size):
        v4lreqbuf = v4l2.uapi.v4l2_requestbuffers()
        v4lreqbuf.type = self.buf_type.value
        v4lreqbuf.memory = self.mem_type.value
        v4lreqbuf.count = queue_size
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_REQBUFS, v4lreqbuf, True)
        assert(v4lreqbuf.count == queue_size)

    def stream_on(self):
        buf_type = ctypes.c_uint32(self.buf_type.value)
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_STREAMON, buf_type, True)

    def stream_off(self):
        buf_type = ctypes.c_uint32(self.buf_type.value)
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_STREAMOFF, buf_type, True)

    @property
    def fd(self):
        return self.vdev.fd


class VideoCaptureStreamer(CaptureStreamer):
    def __init__(self, vdev: VideoDevice, mem_type: v4l2.MemType, buf_type: v4l2.BufType,
                 width: int, height: int, format: v4l2.PixelFormat) -> None:
        super().__init__(vdev, mem_type, buf_type)

        self.width = width
        self.height = height
        self.format = format

        assert(len(format.planes) == 1)

        #bitspp = format.planes[0].bitspp # XXX quick hack
        #self.bytesperline = width * bitspp // 8
        self.bytesperline = format.stride(width, plane=0)
        self.buffersize = format.framesize(width, height)

    def reserve_buffers(self, num_bufs):
        self.set_queue_size(num_bufs)

        self.buffers = []

        for i in range(num_bufs):
            buf = VideoBuffer(v4l2.MemType.MMAP)
            buf.index = i
            buf.width = self.width
            buf.height = self.height
            buf.fourcc = self.format.v4l2_fourcc
            buf.payload_size = self.height * self.bytesperline
            self.buffers.append(buf)

    def reserve_buffers_dmabuf(self, dmabuf_fds: list[int]):
        self.set_queue_size(len(dmabuf_fds))

        self.buffers = []

        for i,fd in enumerate(dmabuf_fds):
            buf = VideoBuffer(v4l2.MemType.DMABUF)
            buf.index = i
            buf.fd = fd
            buf.width = self.width
            buf.height = self.height
            buf.fourcc = self.format.v4l2_fourcc
            buf.payload_size = self.height * self.bytesperline
            self.buffers.append(buf)


class SPlaneCaptureStreamer(VideoCaptureStreamer):
    def __init__(self, vdev: VideoDevice, mem_type: v4l2.MemType, buf_type: v4l2.BufType,
                 width: int, height: int, format: v4l2.PixelFormat) -> None:
        super().__init__(vdev, mem_type, buf_type, width, height, format)

        self.set_format(self.format, self.width, self.height)

    def set_format(self, format: v4l2.PixelFormat, width, height):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        v4lfmt.fmt.pix.pixelformat = format.v4l2_fourcc
        v4lfmt.fmt.pix.width = width
        v4lfmt.fmt.pix.height = height
        v4lfmt.fmt.pix.bytesperline = format.stride(width, 0)
        v4lfmt.fmt.pix.field = v4l2.uapi.V4L2_FIELD_NONE

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

        assert v4lfmt.fmt.pix.pixelformat == format.v4l2_fourcc, f'{v4lfmt.fmt.pix.pixelformat} != {format.v4l2_fourcc}'
        assert(v4lfmt.fmt.pix.width == width)
        assert(v4lfmt.fmt.pix.height == height)
        #assert(v4lfmt.fmt.pix.bytesperline >= width * format.planes[0].bitspp / 8)

    def queue(self, vbuf: VideoBuffer):
        assert(vbuf in self.buffers)
        assert(vbuf.index != -1)

        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = vbuf.mem_type.value
        v4l2buf.index = vbuf.index
        if vbuf.mem_type == v4l2.MemType.DMABUF:
            v4l2buf.m.fd = vbuf.fd

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QBUF, v4l2buf, True)

    def dequeue(self) -> VideoBuffer:
        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = self.mem_type.value

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, v4l2buf, True)

        vbuf = self.buffers[v4l2buf.index]

        # XXX
        vbuf.buffer_size = v4l2buf.length

        if self.mem_type == v4l2.MemType.DMABUF:
            assert(vbuf.fd == v4l2buf.m.fd)
        else:
            vbuf.offset = v4l2buf.m.offset

        return vbuf


class MPlaneCaptureStreamer(VideoCaptureStreamer):
    def __init__(self, vdev: VideoDevice, mem_type, buf_type,
                 width: int, height: int, format: v4l2.PixelFormat) -> None:
        super().__init__(vdev, mem_type, buf_type, width, height, format)

        self.set_format(self.format, self.width, self.height)

    def set_format(self, format: v4l2.PixelFormat, width, height):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        num_planes = 1 # XXX

        mp = v4lfmt.fmt.pix_mp

        mp.pixelformat = format.v4l2_fourcc
        mp.width = width
        mp.height = height

        mp.num_planes = num_planes

        for i in range(num_planes):
            p = mp.plane_fmt[i]

            p.bytesperline = format.stride(width, i)
            p.sizeimage = format.planesize(width, height, i)
            p.field = v4l2.uapi.V4L2_FIELD_NONE

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

    def queue(self, vbuf: VideoBuffer):
        assert(vbuf in self.buffers)
        assert(vbuf.index != -1)

        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = vbuf.mem_type.value
        v4l2buf.index = vbuf.index

        num_planes = 1

        planes = (v4l2.uapi.v4l2_plane * num_planes)()
        v4l2buf.m.planes = planes

        #bitspp = CaptureStreamer._fourcc_bitspp_map[vbuf.fourcc]

        if vbuf.mem_type == v4l2.MemType.DMABUF:
            planes[0].m.fd = vbuf.fd

        planes[0].bytesused = vbuf.payload_size # vbuf.width * vbuf.height * bitspp // 8

        v4l2buf.length = num_planes

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QBUF, v4l2buf, True)

    def dequeue(self) -> VideoBuffer:
        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = self.mem_type.value

        num_planes = 1

        planes = (v4l2.uapi.v4l2_plane * num_planes)()
        v4l2buf.m.planes = planes
        v4l2buf.length = num_planes

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, v4l2buf, True)

        vbuf = self.buffers[v4l2buf.index]

        vbuf.buffer_size = v4l2buf.m.planes[0].length

        if self.mem_type == v4l2.MemType.DMABUF:
            assert(vbuf.fd == v4l2buf.m.planes[0].m.fd)
        else:
            vbuf.offset = v4l2buf.m.planes[0].m.mem_offset

        return vbuf


class MetaCaptureStreamer(CaptureStreamer):
    def __init__(self, vdev: VideoDevice, mem_type: v4l2.MemType, buf_type: v4l2.BufType,
                 size: int | tuple, format: v4l2.MetaFormat) -> None:
        super().__init__(vdev, mem_type, buf_type)

        self.size = size
        self.format = format

        self.set_format(format, size)

    def set_format(self, format: v4l2.MetaFormat, size: int | tuple):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        v4lfmt.fmt.meta.dataformat = format.v4l2_fourcc

        if isinstance(size, int):
            v4lfmt.fmt.meta.buffersize = size
            self.bytesperline = size
        else:
            v4lfmt.fmt.meta.width = size[0]
            v4lfmt.fmt.meta.height = size[1]
            self.bytesperline = format.stride(size[0])

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

        self.buffersize = v4lfmt.fmt.meta.buffersize

    def reserve_buffers(self, num_bufs):
        self.set_queue_size(num_bufs)

        self.buffers = []

        for i in range(num_bufs):
            buf = VideoBuffer(v4l2.MemType.MMAP)
            buf.index = i
            buf.fourcc = self.format.v4l2_fourcc
            buf.payload_size = self.buffersize
            self.buffers.append(buf)

    def reserve_buffers_dmabuf(self, dmabuf_fds: list[int]):
        self.set_queue_size(len(dmabuf_fds))

        self.buffers = []

        for i,fd in enumerate(dmabuf_fds):
            buf = VideoBuffer(v4l2.MemType.DMABUF)
            buf.index = i
            buf.fd = fd
            buf.fourcc = self.format.v4l2_fourcc
            buf.payload_size = self.buffersize
            self.buffers.append(buf)

    def queue(self, vbuf: VideoBuffer):
        assert(vbuf in self.buffers)
        assert(vbuf.index != -1)

        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = vbuf.mem_type.value
        v4l2buf.index = vbuf.index
        if vbuf.mem_type == v4l2.MemType.DMABUF:
            v4l2buf.m.fd = vbuf.fd

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QBUF, v4l2buf, True)

    def dequeue(self) -> VideoBuffer:
        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = self.mem_type.value

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, v4l2buf, True)

        vbuf = self.buffers[v4l2buf.index]

        # XXX
        vbuf.buffer_size = v4l2buf.length

        if self.mem_type == v4l2.MemType.DMABUF:
            assert(vbuf.fd == v4l2buf.m.fd)
        else:
            vbuf.offset = v4l2buf.m.offset

        return vbuf


class MetaOutputStreamer(CaptureStreamer):
    def __init__(self, vdev: VideoDevice, mem_type: v4l2.MemType, buf_type: v4l2.BufType,
                 size: int, format: v4l2.MetaFormat) -> None:
        super().__init__(vdev, mem_type, buf_type)

        self.size = size
        self.format = format

        self.set_format(format, size)

    def set_format(self, format: v4l2.MetaFormat, size):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        #bitspp = format.planes[0].bitspp # XXX quick hack

        v4lfmt.fmt.meta.dataformat = format.v4l2_fourcc
        v4lfmt.fmt.meta.buffersize = size

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

    def reserve_buffers(self, num_bufs):
        self.set_queue_size(num_bufs)

        self.buffers = []

        for i in range(num_bufs):
            buf = VideoBuffer(v4l2.MemType.MMAP)
            buf.index = i
            buf.fourcc = self.format.v4l2_fourcc
            buf.payload_size = self.size
            self.buffers.append(buf)

        for vbuf in self.buffers:
            v4l2buf = v4l2.uapi.v4l2_buffer()
            v4l2buf.type = self.buf_type.value
            v4l2buf.memory = vbuf.mem_type.value
            v4l2buf.index = vbuf.index

            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QUERYBUF, v4l2buf, True)

            vbuf.offset = v4l2buf.m.offset
            vbuf.buffer_size = v4l2buf.length

    def reserve_buffers_dmabuf(self, dmabuf_fds: list[int]):
        self.set_queue_size(len(dmabuf_fds))

        self.buffers = []

        for i,fd in enumerate(dmabuf_fds):
            buf = VideoBuffer(v4l2.MemType.DMABUF)
            buf.index = i
            buf.fd = fd
            buf.fourcc = self.format.v4l2_fourcc
            buf.payload_size = self.size
            buf.buffer_size = self.size
            self.buffers.append(buf)

    def queue(self, vbuf: VideoBuffer):
        assert(vbuf in self.buffers)
        assert(vbuf.index != -1)

        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = vbuf.mem_type.value
        v4l2buf.index = vbuf.index
        v4l2buf.bytesused = self.size
        if vbuf.mem_type == v4l2.MemType.DMABUF:
            v4l2buf.m.fd = vbuf.fd

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QBUF, v4l2buf, True)

    def dequeue(self) -> VideoBuffer:
        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = self.mem_type.value

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, v4l2buf, True)

        vbuf = self.buffers[v4l2buf.index]

        # XXX
        vbuf.buffer_size = v4l2buf.length

        if self.mem_type == v4l2.MemType.DMABUF:
            assert(vbuf.fd == v4l2buf.m.fd)
        else:
            vbuf.offset = v4l2buf.m.offset

        return vbuf





class VideoBuffer:
    def __init__(self, mem_type: v4l2.MemType) -> None:
        self.index = -1
        self.mem_type = mem_type
        # dmabuf fd
        self.fd = -1
        # mmap offset
        self.offset = 0
        self.width = 0
        self.height = 0
        self.fourcc = 0
        self.payload_size = 0

        # Size of the buffer (not the payload) in bytes
        self.buffer_size = 0
