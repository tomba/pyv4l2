from __future__ import annotations

import ctypes
import errno
import fcntl
import fnmatch
import glob
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass

import v4l2.uapi

__all__ = ['VideoBuffer', 'VideoDevice', 'VideoFormatInfo']


def _enum_or_int(enum_cls, value):
    # Keep the raw value if the driver returns something we don't know
    try:
        return enum_cls(value)
    except ValueError:
        return value


@dataclass
class VideoFormatInfo:
    format: v4l2.PixelFormat | v4l2.MetaFormat | str
    width: int | None = None
    height: int | None = None
    sizeimage: int | None = None
    field: v4l2.Field | int | None = None
    colorspace: v4l2.ColorSpace | int | None = None
    ycbcr_enc: v4l2.YCbCrEncoding | int | None = None
    quantization: v4l2.Quantization | int | None = None
    xfer_func: v4l2.XferFunc | int | None = None


class VideoDevice:
    def __init__(self, dev_path: str) -> None:
        self.dev_path = dev_path
        self.fd = os.open(dev_path, os.O_RDWR | os.O_NONBLOCK)
        assert self.fd != -1

        cap = v4l2.uapi.v4l2_capability()
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QUERYCAP, cap, True)

        caps = cap.device_caps

        self.has_mplane_m2m = bool(caps & v4l2.uapi.V4L2_CAP_VIDEO_M2M_MPLANE)
        self.has_m2m = self.has_mplane_m2m or bool(caps & v4l2.uapi.V4L2_CAP_VIDEO_M2M)

        self.has_mplane_capture = self.has_mplane_m2m or bool(
            caps & v4l2.uapi.V4L2_CAP_VIDEO_CAPTURE_MPLANE
        )
        self.has_capture = (
            self.has_mplane_capture or self.has_m2m or bool(caps & v4l2.uapi.V4L2_CAP_VIDEO_CAPTURE)
        )

        self.has_mplane_output = self.has_mplane_m2m or bool(
            caps & v4l2.uapi.V4L2_CAP_VIDEO_OUTPUT_MPLANE
        )
        self.has_output = (
            self.has_mplane_output or self.has_m2m or bool(caps & v4l2.uapi.V4L2_CAP_VIDEO_OUTPUT)
        )

        self.has_meta_capture = bool(caps & v4l2.uapi.V4L2_CAP_META_CAPTURE)
        self.has_meta_output = bool(caps & v4l2.uapi.V4L2_CAP_META_OUTPUT)

    def __del__(self):
        os.close(self.fd)

    @staticmethod
    def find_video_device(key: str, value: str) -> str:
        for path in glob.glob('/dev/video*'):
            try:
                fd = os.open(path, os.O_RDWR | os.O_NONBLOCK)
            except OSError:
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

    def get_formats(self, buf_type: v4l2.BufType, mbus_code: v4l2.BusFormat | None = None):
        fmt = v4l2.uapi.v4l2_fmtdesc()
        fmt.type = buf_type.value
        fmt.mbus_code = mbus_code if mbus_code else 0
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

            try:
                if buf_type in [v4l2.BufType.META_CAPTURE, v4l2.BufType.META_OUTPUT]:
                    f = v4l2.MetaFormats.find_v4l2_fourcc(fmt.pixelformat)
                else:
                    f = v4l2.PixelFormats.find_v4l2_fourcc(fmt.pixelformat)
                fmts.append(f)
            except StopIteration:
                pass

            fmt.index += 1

        return fmts

    # Get formats that the pyv4l2 does not support, as a list of fourcc strings
    def get_unsupported_formats(self, buf_type: v4l2.BufType) -> list[str]:
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

            try:
                if buf_type in [v4l2.BufType.META_CAPTURE, v4l2.BufType.META_OUTPUT]:
                    v4l2.MetaFormats.find_v4l2_fourcc(fmt.pixelformat)
                else:
                    v4l2.PixelFormats.find_v4l2_fourcc(fmt.pixelformat)
            except StopIteration:
                fmts.append(v4l2.fourcc_to_str(fmt.pixelformat))

            fmt.index += 1

        return fmts

    def get_format(self, buf_type: v4l2.BufType):
        fmt = v4l2.uapi.v4l2_format()
        fmt.type = buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, fmt, True)
        return fmt

    def get_format_info(self, buf_type: v4l2.BufType) -> VideoFormatInfo:
        fmt = self.get_format(buf_type)

        def find_format(fourcc):
            # Fall back to the fourcc string for formats pyv4l2 doesn't know
            try:
                if buf_type in [v4l2.BufType.META_CAPTURE, v4l2.BufType.META_OUTPUT]:
                    return v4l2.MetaFormats.find_v4l2_fourcc(fourcc)
                return v4l2.PixelFormats.find_v4l2_fourcc(fourcc)
            except StopIteration:
                return v4l2.fourcc_to_str(fourcc)

        if buf_type in [v4l2.BufType.META_CAPTURE, v4l2.BufType.META_OUTPUT]:
            m = fmt.fmt.meta
            return VideoFormatInfo(
                format=find_format(m.dataformat),
                width=m.width,
                height=m.height,
                sizeimage=m.buffersize,
            )

        if buf_type in [v4l2.BufType.VIDEO_CAPTURE_MPLANE, v4l2.BufType.VIDEO_OUTPUT_MPLANE]:
            p = fmt.fmt.pix_mp
            sizeimage = sum(p.plane_fmt[i].sizeimage for i in range(p.num_planes))
        else:
            p = fmt.fmt.pix
            sizeimage = p.sizeimage

        return VideoFormatInfo(
            format=find_format(p.pixelformat),
            width=p.width,
            height=p.height,
            sizeimage=sizeimage,
            field=_enum_or_int(v4l2.Field, p.field),
            colorspace=_enum_or_int(v4l2.ColorSpace, p.colorspace),
            ycbcr_enc=_enum_or_int(v4l2.YCbCrEncoding, p.ycbcr_enc),
            quantization=_enum_or_int(v4l2.Quantization, p.quantization),
            xfer_func=_enum_or_int(v4l2.XferFunc, p.xfer_func),
        )

    def get_capture_streamer(
        self, mem_type: v4l2.MemType, width: int, height: int, format: v4l2.PixelFormat
    ):
        if not self.has_capture:
            raise NotImplementedError()

        if self.has_mplane_capture:
            return MPlaneCaptureStreamer(
                self, mem_type, v4l2.BufType.VIDEO_CAPTURE_MPLANE, width, height, format
            )

        return SPlaneCaptureStreamer(
            self, mem_type, v4l2.BufType.VIDEO_CAPTURE, width, height, format
        )

    def get_meta_capture_streamer(
        self, mem_type: v4l2.MemType, size: int | tuple[int, int], format: v4l2.MetaFormat
    ):
        if self.has_meta_capture:
            return MetaCaptureStreamer(self, mem_type, v4l2.BufType.META_CAPTURE, size, format)

        if self.has_meta_output:
            assert isinstance(size, int)

            return MetaOutputStreamer(self, mem_type, v4l2.BufType.META_OUTPUT, size, format)

        raise NotImplementedError()


class CaptureStreamer(ABC):
    def __init__(self, vdev: VideoDevice, mem_type: v4l2.MemType, buf_type: v4l2.BufType) -> None:
        self.vdev = vdev
        self.mem_type = mem_type
        self.buf_type = buf_type
        self.vbuffers: list[VideoBuffer] = []

    def set_queue_size(self, queue_size) -> int:
        """Request buffers. Returns the number of buffers the driver allocated."""
        v4lreqbuf = v4l2.uapi.v4l2_requestbuffers()
        v4lreqbuf.type = self.buf_type.value
        v4lreqbuf.memory = self.mem_type.value
        v4lreqbuf.count = queue_size
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_REQBUFS, v4lreqbuf, True)
        return v4lreqbuf.count

    def _set_dmabuf_queue_size(self, dmabuf_fds: list[int]):
        count = self.set_queue_size(len(dmabuf_fds))
        if count < len(dmabuf_fds):
            raise RuntimeError(f'Driver allocated {count} of {len(dmabuf_fds)} buffers')

    def stream_on(self):
        buf_type = ctypes.c_uint32(self.buf_type.value)
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_STREAMON, buf_type, True)

    def stream_off(self):
        buf_type = ctypes.c_uint32(self.buf_type.value)
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_STREAMOFF, buf_type, True)

    @abstractmethod
    def reserve_buffers(self, num_bufs: int): ...

    @abstractmethod
    def reserve_buffers_dmabuf(self, dmabuf_fds: list[int]): ...

    def export_dmabuf_fds(self):
        for vbuf in self.vbuffers:
            assert vbuf.mem_type == v4l2.MemType.MMAP

            expbuf = v4l2.uapi.v4l2_exportbuffer()
            expbuf.type = self.buf_type.value
            expbuf.index = vbuf.index
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_EXPBUF, expbuf, True)
            vbuf.fd = expbuf.fd

    @abstractmethod
    def queue(self, vbuf: VideoBuffer): ...

    @abstractmethod
    def dequeue(self) -> VideoBuffer: ...

    @property
    @abstractmethod
    def buffersizes(self) -> list[int]: ...

    @property
    @abstractmethod
    def strides(self) -> list[int]: ...

    @property
    @abstractmethod
    def framesize(self) -> int: ...

    @property
    @abstractmethod
    def format(self) -> v4l2.PixelFormat | v4l2.MetaFormat: ...

    @property
    def fd(self):
        return self.vdev.fd


class VideoCaptureStreamer(CaptureStreamer):
    def __init__(
        self,
        vdev: VideoDevice,
        mem_type: v4l2.MemType,
        buf_type: v4l2.BufType,
        width: int,
        height: int,
        format: v4l2.PixelFormat,
    ) -> None:
        super().__init__(vdev, mem_type, buf_type)

        assert format.v4l2_fourcc

        self.width = width
        self.height = height

        self.__format = format
        self.__strides = [format.stride(width, i) for i in range(len(format.planes))]
        self.__buffersizes = [
            format.planesize(self.__strides[i], height, i) for i in range(len(format.planes))
        ]
        self.__framesize = format.framesize(width, height)

    @property
    def buffersizes(self):
        return list(self.__buffersizes)

    @property
    def framesize(self):
        return self.__framesize

    @property
    def strides(self):
        return list(self.__strides)

    @property
    def format(self) -> v4l2.PixelFormat:
        return self.__format

    def reserve_buffers(self, num_bufs):
        assert self.format.v4l2_fourcc

        count = self.set_queue_size(num_bufs)

        self.vbuffers = []

        for i in range(count):
            vbuf = VideoBuffer(v4l2.MemType.MMAP, i)
            self.vbuffers.append(vbuf)

    def reserve_buffers_dmabuf(self, dmabuf_fds: list[int]):
        assert self.format.v4l2_fourcc

        self._set_dmabuf_queue_size(dmabuf_fds)

        self.vbuffers = []

        for i, fd in enumerate(dmabuf_fds):
            vbuf = VideoBuffer(v4l2.MemType.DMABUF, i)
            vbuf.fd = fd
            self.vbuffers.append(vbuf)


class SPlaneCaptureStreamer(VideoCaptureStreamer):
    def __init__(
        self,
        vdev: VideoDevice,
        mem_type: v4l2.MemType,
        buf_type: v4l2.BufType,
        width: int,
        height: int,
        format: v4l2.PixelFormat,
    ) -> None:
        super().__init__(vdev, mem_type, buf_type, width, height, format)

        self.set_format()

    def set_format(self):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        pix = v4lfmt.fmt.pix

        pix.pixelformat = self.format.v4l2_fourcc
        pix.width = self.width
        pix.height = self.height
        pix.bytesperline = self.strides[0]
        pix.field = v4l2.uapi.V4L2_FIELD_NONE

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

        assert pix.pixelformat == self.format.v4l2_fourcc, (
            f'{pix.pixelformat} != {self.format.v4l2_fourcc}'
        )
        assert pix.width == self.width
        assert pix.height == self.height
        assert pix.bytesperline == self.strides[0], f'{pix.bytesperline} != {self.strides[0]}'

    def queue(self, vbuf: VideoBuffer):
        assert vbuf in self.vbuffers
        assert vbuf.index != -1

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

        # We don't test for match here, as sometimes the buffer might be larger
        # than the used size. E.g. if DRM dumbbuffer is allocated and the
        # driver aligns it to a bigger size.
        assert v4l2buf.length >= self.buffersizes[0], f'{v4l2buf.length} < {self.buffersizes[0]}'

        vbuf = self.vbuffers[v4l2buf.index]

        if self.mem_type == v4l2.MemType.DMABUF:
            assert vbuf.fd == v4l2buf.m.fd
        else:
            vbuf.offset = v4l2buf.m.offset

        return vbuf


class MPlaneCaptureStreamer(VideoCaptureStreamer):
    def __init__(
        self,
        vdev: VideoDevice,
        mem_type,
        buf_type,
        width: int,
        height: int,
        format: v4l2.PixelFormat,
    ) -> None:
        super().__init__(vdev, mem_type, buf_type, width, height, format)

        self.set_format()

    def set_format(self):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        num_planes = len(self.format.planes)

        mp = v4lfmt.fmt.pix_mp

        mp.pixelformat = self.format.v4l2_fourcc
        mp.width = self.width
        mp.height = self.height

        mp.num_planes = num_planes

        for i in range(num_planes):
            p = mp.plane_fmt[i]

            p.bytesperline = self.strides[i]
            p.sizeimage = self.buffersizes[i]
            p.field = v4l2.uapi.V4L2_FIELD_NONE

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

        assert mp.pixelformat == self.format.v4l2_fourcc, (
            f'{mp.pixelformat} != {self.format.v4l2_fourcc}'
        )
        assert mp.width == self.width
        assert mp.height == self.height

        for i in range(num_planes):
            p = mp.plane_fmt[i]

            assert p.bytesperline == self.strides[i]
            assert p.sizeimage == self.buffersizes[i]

    def queue(self, vbuf: VideoBuffer):
        assert vbuf in self.vbuffers
        assert vbuf.index != -1

        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = vbuf.mem_type.value
        v4l2buf.index = vbuf.index

        num_planes = len(self.format.planes)

        planes = (v4l2.uapi.v4l2_plane * num_planes)()
        v4l2buf.m.planes = planes

        # bitspp = CaptureStreamer._fourcc_bitspp_map[vbuf.fourcc]

        if vbuf.mem_type == v4l2.MemType.DMABUF:
            planes[0].m.fd = vbuf.fd

        # planes[0].bytesused = vbuf.payload_size # vbuf.width * vbuf.height * bitspp // 8
        planes[0].bytesused = self.buffersizes[0]  # XXX

        v4l2buf.length = num_planes

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QBUF, v4l2buf, True)

    def dequeue(self) -> VideoBuffer:
        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = self.mem_type.value

        num_planes = len(self.format.planes)

        planes = (v4l2.uapi.v4l2_plane * num_planes)()
        v4l2buf.m.planes = planes
        v4l2buf.length = num_planes

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, v4l2buf, True)

        assert v4l2buf.m.planes[0].length == self.buffersizes[0]

        # XXX CHECK planes[0]

        vbuf = self.vbuffers[v4l2buf.index]

        if self.mem_type == v4l2.MemType.DMABUF:
            assert vbuf.fd == v4l2buf.m.planes[0].m.fd
        else:
            vbuf.offset = v4l2buf.m.planes[0].m.mem_offset

        return vbuf


class MetaCaptureStreamer(CaptureStreamer):
    def __init__(
        self,
        vdev: VideoDevice,
        mem_type: v4l2.MemType,
        buf_type: v4l2.BufType,
        size: int | tuple,
        format: v4l2.MetaFormat,
    ) -> None:
        super().__init__(vdev, mem_type, buf_type)

        self.size = size
        self.__format = format

        if isinstance(size, int):
            w, h = (size, 1)
        else:
            w, h = size

        self.stride = format.stride(w)
        self.buffersize = format.buffersize(w, h)

        self.set_format()

    @property
    def strides(self):
        return [self.stride]

    @property
    def buffersizes(self):
        return [self.buffersize]

    @property
    def framesize(self):
        return self.buffersize

    @property
    def format(self) -> v4l2.MetaFormat:
        return self.__format

    def set_format(self):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        v4lfmt.fmt.meta.dataformat = self.format.v4l2_fourcc

        if isinstance(self.size, int):
            v4lfmt.fmt.meta.buffersize = self.buffersize
        else:
            v4lfmt.fmt.meta.width = self.size[0]
            v4lfmt.fmt.meta.height = self.size[1]

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

        assert v4lfmt.fmt.meta.buffersize == self.buffersize, (
            f'{v4lfmt.fmt.meta.buffersize} != {self.buffersize}'
        )

    def reserve_buffers(self, num_bufs):
        count = self.set_queue_size(num_bufs)

        self.vbuffers = []

        for i in range(count):
            vbuf = VideoBuffer(v4l2.MemType.MMAP, i)
            self.vbuffers.append(vbuf)

    def reserve_buffers_dmabuf(self, dmabuf_fds: list[int]):
        self._set_dmabuf_queue_size(dmabuf_fds)

        self.vbuffers = []

        for i, fd in enumerate(dmabuf_fds):
            vbuf = VideoBuffer(v4l2.MemType.DMABUF, i)
            vbuf.fd = fd
            self.vbuffers.append(vbuf)

    def queue(self, vbuf: VideoBuffer):
        assert vbuf in self.vbuffers
        assert vbuf.index != -1

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

        assert v4l2buf.length >= self.buffersize, f'{v4l2buf.length} < {self.buffersize}'

        vbuf = self.vbuffers[v4l2buf.index]

        if self.mem_type == v4l2.MemType.DMABUF:
            assert vbuf.fd == v4l2buf.m.fd
        else:
            vbuf.offset = v4l2buf.m.offset

        return vbuf


class MetaOutputStreamer(CaptureStreamer):
    def __init__(
        self,
        vdev: VideoDevice,
        mem_type: v4l2.MemType,
        buf_type: v4l2.BufType,
        size: int,
        format: v4l2.MetaFormat,
    ) -> None:
        super().__init__(vdev, mem_type, buf_type)

        self.size = size
        self.__format = format

        self.stride = format.stride(size)
        self.buffersize = self.stride

        self.set_format()

    @property
    def strides(self):
        return [self.stride]

    @property
    def buffersizes(self):
        return [self.buffersize]

    @property
    def framesize(self):
        return self.buffersize

    @property
    def format(self) -> v4l2.MetaFormat:
        return self.__format

    def set_format(self):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        # bitspp = format.planes[0].bitspp # XXX quick hack

        v4lfmt.fmt.meta.dataformat = self.format.v4l2_fourcc
        v4lfmt.fmt.meta.buffersize = self.size

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

    def reserve_buffers(self, num_bufs):
        count = self.set_queue_size(num_bufs)

        self.vbuffers = []

        for i in range(count):
            vbuf = VideoBuffer(v4l2.MemType.MMAP, i)
            self.vbuffers.append(vbuf)

        for vbuf in self.vbuffers:
            v4l2buf = v4l2.uapi.v4l2_buffer()
            v4l2buf.type = self.buf_type.value
            v4l2buf.memory = vbuf.mem_type.value
            v4l2buf.index = vbuf.index

            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QUERYBUF, v4l2buf, True)

            vbuf.offset = v4l2buf.m.offset

    def reserve_buffers_dmabuf(self, dmabuf_fds: list[int]):
        self._set_dmabuf_queue_size(dmabuf_fds)

        self.vbuffers = []

        for i, fd in enumerate(dmabuf_fds):
            vbuf = VideoBuffer(v4l2.MemType.DMABUF, i)
            vbuf.fd = fd
            self.vbuffers.append(vbuf)

    def queue(self, vbuf: VideoBuffer):
        assert vbuf in self.vbuffers
        assert vbuf.index != -1

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

        assert v4l2buf.length == self.buffersize

        vbuf = self.vbuffers[v4l2buf.index]

        if self.mem_type == v4l2.MemType.DMABUF:
            assert vbuf.fd == v4l2buf.m.fd
        else:
            vbuf.offset = v4l2buf.m.offset

        return vbuf


class VideoBuffer:
    __slots__ = ['fd', 'index', 'mem_type', 'offset']

    def __init__(self, mem_type: v4l2.MemType, index: int) -> None:
        self.index = index
        self.mem_type = mem_type
        # dmabuf fd
        self.fd = -1
        # mmap offset
        self.offset = 0
