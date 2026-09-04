from __future__ import annotations

import ctypes
import errno
import fcntl
import fnmatch
import glob
import os
from dataclasses import dataclass

import v4l2.uapi

from .device import V4L2Device
from .helpers import enum_or_int

__all__ = ['Streamer', 'VideoBuffer', 'VideoDevice', 'VideoFormat']


@dataclass
class VideoFormat:
    format: v4l2.PixelFormat | v4l2.MetaFormat | str
    width: int | None = None
    height: int | None = None
    sizeimage: int | None = None
    num_planes: int | None = None
    field: v4l2.Field | int | None = None
    colorspace: v4l2.ColorSpace | int | None = None
    ycbcr_enc: v4l2.YCbCrEncoding | int | None = None
    quantization: v4l2.Quantization | int | None = None
    xfer_func: v4l2.XferFunc | int | None = None


class VideoDevice(V4L2Device):
    def __init__(self, dev_path: str) -> None:
        super().__init__(dev_path)

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

    def get_format(self, buf_type: v4l2.BufType) -> VideoFormat:
        fmt = v4l2.uapi.v4l2_format()
        fmt.type = buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, fmt, True)

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
            return VideoFormat(
                format=find_format(m.dataformat),
                width=m.width,
                height=m.height,
                sizeimage=m.buffersize,
            )

        if buf_type in [v4l2.BufType.VIDEO_CAPTURE_MPLANE, v4l2.BufType.VIDEO_OUTPUT_MPLANE]:
            p = fmt.fmt.pix_mp
            sizeimage = sum(p.plane_fmt[i].sizeimage for i in range(p.num_planes))
            num_planes = p.num_planes
        else:
            p = fmt.fmt.pix
            sizeimage = p.sizeimage
            num_planes = 1

        return VideoFormat(
            format=find_format(p.pixelformat),
            width=p.width,
            height=p.height,
            sizeimage=sizeimage,
            num_planes=num_planes,
            field=enum_or_int(v4l2.Field, p.field),
            colorspace=enum_or_int(v4l2.ColorSpace, p.colorspace),
            ycbcr_enc=enum_or_int(v4l2.YCbCrEncoding, p.ycbcr_enc),
            quantization=enum_or_int(v4l2.Quantization, p.quantization),
            xfer_func=enum_or_int(v4l2.XferFunc, p.xfer_func),
        )

    def get_capture_streamer(
        self, mem_type: v4l2.MemType, width: int, height: int, format: v4l2.PixelFormat
    ):
        if not self.has_capture:
            raise NotImplementedError()

        if self.has_mplane_capture:
            buf_type = v4l2.BufType.VIDEO_CAPTURE_MPLANE
        else:
            buf_type = v4l2.BufType.VIDEO_CAPTURE

        return Streamer(self, mem_type, buf_type, (width, height), format)

    def get_meta_capture_streamer(
        self, mem_type: v4l2.MemType, size: int | tuple[int, int], format: v4l2.MetaFormat
    ):
        if self.has_meta_capture:
            return Streamer(self, mem_type, v4l2.BufType.META_CAPTURE, size, format)

        if self.has_meta_output:
            assert isinstance(size, int)

            return Streamer(self, mem_type, v4l2.BufType.META_OUTPUT, size, format)

        raise NotImplementedError()


class Streamer:
    """Buffer queue of a VideoDevice for one buffer type.

    The streamer keeps what it has done through the fd: the format it set,
    the buffers it allocated, which of them are queued to the driver, and
    whether streaming is on. Only plane 0 of multi-planar buffers is
    handled."""

    def __init__(
        self,
        vdev: VideoDevice,
        mem_type: v4l2.MemType,
        buf_type: v4l2.BufType,
        size: int | tuple[int, int],
        format: v4l2.PixelFormat | v4l2.MetaFormat,
    ) -> None:
        self.vdev = vdev
        self.mem_type = mem_type
        self.buf_type = buf_type
        self.size = size
        self.format = format
        self.vbuffers: list[VideoBuffer] = []
        self.streaming = False

        self.is_mplane = buf_type in (
            v4l2.BufType.VIDEO_CAPTURE_MPLANE,
            v4l2.BufType.VIDEO_OUTPUT_MPLANE,
        )
        self.is_meta = buf_type in (v4l2.BufType.META_CAPTURE, v4l2.BufType.META_OUTPUT)
        self.is_output = buf_type in (
            v4l2.BufType.VIDEO_OUTPUT,
            v4l2.BufType.VIDEO_OUTPUT_MPLANE,
            v4l2.BufType.META_OUTPUT,
        )

        if isinstance(size, int):
            self.width, self.height = size, 1
        else:
            self.width, self.height = size

        assert format.v4l2_fourcc

        if isinstance(format, v4l2.MetaFormat):
            self.__strides = [format.stride(self.width)]
            self.__buffersizes = [format.buffersize(self.width, self.height)]
            self.framesize = self.__buffersizes[0]
        else:
            assert not isinstance(size, int)
            num_planes = len(format.planes)
            self.__strides = [format.stride(self.width, i) for i in range(num_planes)]
            self.__buffersizes = [
                format.planesize(self.__strides[i], self.height, i) for i in range(num_planes)
            ]
            self.framesize = format.framesize(self.width, self.height)

        self.__set_format()

    @property
    def fd(self):
        return self.vdev.fd

    @property
    def strides(self) -> list[int]:
        return list(self.__strides)

    @property
    def buffersizes(self) -> list[int]:
        return list(self.__buffersizes)

    @property
    def queued_buffers(self) -> list[VideoBuffer]:
        return [b for b in self.vbuffers if b.queued]

    @property
    def unqueued_buffers(self) -> list[VideoBuffer]:
        return [b for b in self.vbuffers if not b.queued]

    def __set_format(self):
        v4lfmt = v4l2.uapi.v4l2_format()
        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        fourcc = self.format.v4l2_fourcc

        if self.is_meta:
            meta = v4lfmt.fmt.meta
            meta.dataformat = fourcc
            if isinstance(self.size, int):
                meta.buffersize = self.__buffersizes[0]
            else:
                meta.width = self.width
                meta.height = self.height

            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

            assert meta.buffersize == self.__buffersizes[0], (
                f'{meta.buffersize} != {self.__buffersizes[0]}'
            )
        elif self.is_mplane:
            mp = v4lfmt.fmt.pix_mp
            mp.pixelformat = fourcc
            mp.width = self.width
            mp.height = self.height
            mp.field = v4l2.uapi.V4L2_FIELD_NONE
            mp.num_planes = len(self.__strides)

            for i in range(mp.num_planes):
                mp.plane_fmt[i].bytesperline = self.__strides[i]
                mp.plane_fmt[i].sizeimage = self.__buffersizes[i]

            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

            assert mp.pixelformat == fourcc, f'{mp.pixelformat} != {fourcc}'
            assert mp.width == self.width
            assert mp.height == self.height

            for i in range(mp.num_planes):
                p = mp.plane_fmt[i]
                assert p.bytesperline == self.__strides[i], (
                    f'{p.bytesperline} != {self.__strides[i]}'
                )
                assert p.sizeimage == self.__buffersizes[i], (
                    f'{p.sizeimage} != {self.__buffersizes[i]}'
                )
        else:
            pix = v4lfmt.fmt.pix
            pix.pixelformat = fourcc
            pix.width = self.width
            pix.height = self.height
            pix.bytesperline = self.__strides[0]
            pix.field = v4l2.uapi.V4L2_FIELD_NONE

            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

            assert pix.pixelformat == fourcc, f'{pix.pixelformat} != {fourcc}'
            assert pix.width == self.width
            assert pix.height == self.height
            assert pix.bytesperline == self.__strides[0], (
                f'{pix.bytesperline} != {self.__strides[0]}'
            )

    def __request_buffers(self, count: int) -> int:
        """VIDIOC_REQBUFS. Returns the number of buffers the driver allocated."""
        reqbuf = v4l2.uapi.v4l2_requestbuffers()
        reqbuf.type = self.buf_type.value
        reqbuf.memory = self.mem_type.value
        reqbuf.count = count
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_REQBUFS, reqbuf, True)
        return reqbuf.count

    def __new_v4l2_buffer(self, vbuf: VideoBuffer | None = None):
        """Create a v4l2_buffer, and the planes array for multi-planar types.

        Returns the buffer and the plane 0 substructure that holds the memory
        fields."""
        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = self.mem_type.value

        if vbuf:
            v4l2buf.index = vbuf.index

        if self.is_mplane:
            num_planes = len(self.__strides)
            planes = (v4l2.uapi.v4l2_plane * num_planes)()
            v4l2buf.m.planes = planes
            v4l2buf.length = num_planes
            # Keep the planes array alive with the buffer
            v4l2buf._planes = planes  # type: ignore
            return v4l2buf, planes[0]

        return v4l2buf, v4l2buf

    def __query_buffer(self, vbuf: VideoBuffer):
        v4l2buf, mem = self.__new_v4l2_buffer(vbuf)

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QUERYBUF, v4l2buf, True)

        vbuf.length = mem.length
        if self.mem_type == v4l2.MemType.MMAP:
            vbuf.offset = mem.m.mem_offset if self.is_mplane else mem.m.offset

    def reserve_buffers(self, num_bufs: int):
        """Allocate MMAP buffers. The driver may allocate more than asked."""
        assert self.mem_type == v4l2.MemType.MMAP

        count = self.__request_buffers(num_bufs)

        self.vbuffers = [VideoBuffer(v4l2.MemType.MMAP, i) for i in range(count)]

        for vbuf in self.vbuffers:
            self.__query_buffer(vbuf)

    def reserve_buffers_dmabuf(self, dmabuf_fds: list[int]):
        assert self.mem_type == v4l2.MemType.DMABUF

        count = self.__request_buffers(len(dmabuf_fds))
        if count < len(dmabuf_fds):
            raise RuntimeError(f'Driver allocated {count} of {len(dmabuf_fds)} buffers')

        self.vbuffers = []

        for i, fd in enumerate(dmabuf_fds):
            vbuf = VideoBuffer(v4l2.MemType.DMABUF, i)
            vbuf.fd = fd
            self.vbuffers.append(vbuf)

    def export_dmabuf_fds(self):
        for vbuf in self.vbuffers:
            assert vbuf.mem_type == v4l2.MemType.MMAP

            expbuf = v4l2.uapi.v4l2_exportbuffer()
            expbuf.type = self.buf_type.value
            expbuf.index = vbuf.index
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_EXPBUF, expbuf, True)
            vbuf.fd = expbuf.fd

    def queue(self, vbuf: VideoBuffer):
        assert vbuf in self.vbuffers
        assert not vbuf.queued

        v4l2buf, mem = self.__new_v4l2_buffer(vbuf)

        if self.mem_type == v4l2.MemType.DMABUF:
            mem.m.fd = vbuf.fd

        if self.is_output:
            mem.bytesused = self.__buffersizes[0]

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QBUF, v4l2buf, True)

        vbuf.queued = True

    def dequeue(self) -> VideoBuffer:
        v4l2buf, mem = self.__new_v4l2_buffer()

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, v4l2buf, True)

        # The buffer may be larger than the used size, e.g. if a DRM dumb
        # buffer was allocated and the driver aligned it to a bigger size.
        assert mem.length >= self.__buffersizes[0], f'{mem.length} < {self.__buffersizes[0]}'

        vbuf = self.vbuffers[v4l2buf.index]

        if self.mem_type == v4l2.MemType.DMABUF:
            assert vbuf.fd == mem.m.fd
        else:
            vbuf.offset = mem.m.mem_offset if self.is_mplane else mem.m.offset

        vbuf.length = mem.length
        vbuf.bytesused = mem.bytesused
        vbuf.sequence = v4l2buf.sequence
        vbuf.timestamp = v4l2buf.timestamp.tv_sec + v4l2buf.timestamp.tv_usec / 1e6
        vbuf.queued = False

        return vbuf

    def stream_on(self):
        buf_type = ctypes.c_uint32(self.buf_type.value)
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_STREAMON, buf_type, True)
        self.streaming = True

    def stream_off(self):
        buf_type = ctypes.c_uint32(self.buf_type.value)
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_STREAMOFF, buf_type, True)
        self.streaming = False

        # STREAMOFF returns all buffers to the application
        for vbuf in self.vbuffers:
            vbuf.queued = False


class VideoBuffer:
    __slots__ = [
        'bytesused',
        'fd',
        'index',
        'length',
        'mem_type',
        'offset',
        'queued',
        'sequence',
        'timestamp',
    ]

    def __init__(self, mem_type: v4l2.MemType, index: int) -> None:
        self.index = index
        self.mem_type = mem_type
        # dmabuf fd
        self.fd = -1
        # mmap offset of plane 0
        self.offset = 0
        # size of plane 0 in the driver
        self.length = 0
        # queued to the driver
        self.queued = False
        # from the last dequeue
        self.bytesused = 0
        self.sequence = 0
        self.timestamp = 0.0

    def __repr__(self) -> str:
        return f'VideoBuffer({self.index}, {self.mem_type.name}, queued={self.queued})'
