from __future__ import annotations

import ctypes
import fcntl
import os
import v4l2.uapi
import v4l2.pixelformats

class VideoDevice:
    def __init__(self, entity: v4l2.MediaEntity) -> None:
        self.entity = entity
        assert(entity.interface.is_video)
        self.fd = os.open(entity.interface.dev_path, os.O_RDWR | os.O_NONBLOCK)
        assert(self.fd != -1)

        cap = v4l2.uapi.v4l2_capability()
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QUERYCAP, cap, True)

        self.has_capture = False
        self.has_mplane_capture = False

        if cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_CAPTURE_MPLANE:
            self.has_capture = True
            self.has_mplane_capture = True
        elif cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_CAPTURE:
            self.has_capture = True
            self.has_mplane_capture = False

        if cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_OUTPUT_MPLANE:
            self.has_output = True
            self.has_mplane_output = True
        elif cap.device_caps & v4l2.uapi.V4L2_CAP_VIDEO_OUTPUT:
            self.has_output = True
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

    def __del__(self):
        os.close(self.fd)

    def get_format(self):
        if not self.has_capture:
            raise NotImplementedError()

        fmt = v4l2.uapi.v4l2_format()

        if self.has_mplane_capture:
            fmt.type = v4l2.BufType.VIDEO_CAPTURE_MPLANE
        elif self.has_capture:
            fmt.type = v4l2.BufType.VIDEO_CAPTURE
        else:
            raise NotImplementedError()

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, fmt, True)
        return fmt

    def get_capture_streamer(self, mem_type: v4l2.MemType,
                             width: int, height: int, fourcc: v4l2.PixelFormat):
        if not self.has_capture:
            raise NotImplementedError()

        if self.has_mplane_capture:
            return MPlaneCaptureStreamer(self, mem_type, v4l2.BufType.VIDEO_CAPTURE_MPLANE,
                                         width, height, fourcc)
        else:
            return SPlaneCaptureStreamer(self, mem_type, v4l2.BufType.VIDEO_CAPTURE,
                                   width, height, fourcc)

    def get_meta_capture_streamer(self, mem_type: v4l2.MemType,
                                  size: int, fourcc: v4l2.MetaFormat):
        assert(self.has_meta_capture)
        return MetaCaptureStreamer(self, mem_type, v4l2.BufType.META_CAPTURE,
                                   size, fourcc)

class CaptureStreamer():
    def __init__(self, vdev: VideoDevice, mem_type: v4l2.MemType, buf_type: v4l2.BufType) -> None:
        self.vdev = vdev
        self.mem_type = mem_type
        self.buf_type = buf_type
        self.fbs = []

    def set_queue_size(self, queue_size):
        self.fbs = [ False ] * queue_size

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
                 width: int, height: int, fourcc: v4l2.PixelFormat) -> None:
        super().__init__(vdev, mem_type, buf_type)

        self.width = width
        self.height = height
        self.fourcc = fourcc


class SPlaneCaptureStreamer(VideoCaptureStreamer):
    def __init__(self, vdev: VideoDevice, mem_type: v4l2.MemType, buf_type: v4l2.BufType,
                 width: int, height: int, fourcc: v4l2.PixelFormat) -> None:
        super().__init__(vdev, mem_type, buf_type, width, height, fourcc)

        pfi = v4l2.pixelformats.get_pixel_format_info(fourcc)
        assert(len(pfi.planes) == 1)
        bitspp = pfi.planes[0].bitspp # XXX quick hack
        self.bytesperline = width * bitspp // 8

        self.set_format(self.fourcc, self.width, self.height)

    def set_format(self, fourcc, width, height):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        pfi = v4l2.pixelformats.get_pixel_format_info(fourcc)
        bitspp = pfi.planes[0].bitspp # XXX quick hack

        v4lfmt.fmt.pix.pixelformat = fourcc
        v4lfmt.fmt.pix.width = width
        v4lfmt.fmt.pix.height = height
        v4lfmt.fmt.pix.bytesperline = width * bitspp // 8
        v4lfmt.fmt.pix.field = v4l2.uapi.V4L2_FIELD_NONE

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

        assert(v4lfmt.fmt.pix.pixelformat == fourcc)
        assert(v4lfmt.fmt.pix.width == width)
        assert(v4lfmt.fmt.pix.height == height)
        #assert(v4lfmt.fmt.pix.bytesperline >= width * pfi.planes[0].bitspp / 8)

    def queue(self, vbuf):
        idx = -1
        for _idx in range(len(self.fbs)):
            if self.fbs[_idx] == False:
                idx = _idx
                break

        assert(idx != -1)

        vbuf.index = idx

        self.fbs[idx] = True

        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = vbuf.mem_type.value
        v4l2buf.index = vbuf.index
        if vbuf.mem_type == v4l2.MemType.DMABUF:
            v4l2buf.m.fd = vbuf.fd

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QBUF, v4l2buf, True)

    def dequeue(self):
        fb = VideoBuffer(self.mem_type)

        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = self.mem_type.value

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, v4l2buf, True)

        fb.index = v4l2buf.index
        fb.buffer_size = v4l2buf.length

        if self.mem_type == v4l2.MemType.DMABUF:
            fb.fd = v4l2buf.m.fd
        else:
            fb.offset = v4l2buf.m.offset

        idx = v4l2buf.index

        self.fbs[idx] = False

        return fb


class MPlaneCaptureStreamer(VideoCaptureStreamer):
    def __init__(self, vdev: VideoDevice, mem_type, buf_type,
                 width: int, height: int, fourcc: v4l2.PixelFormat) -> None:
        super().__init__(vdev, mem_type, buf_type, width, height, fourcc)

        pfi = v4l2.pixelformats.get_pixel_format_info(fourcc)
        assert(len(pfi.planes) == 1) # XXX
        bitspp = pfi.planes[0].bitspp # XXX quick hack

        self.bytesperline = width * bitspp // 8

        self.set_format(self.fourcc, self.width, self.height)

    def set_format(self, fourcc, width, height):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        pfi = v4l2.pixelformats.get_pixel_format_info(fourcc)
        bitspp = pfi.planes[0].bitspp # XXX quick hack

        num_planes = 1 # XXX

        mp = v4lfmt.fmt.pix_mp

        mp.pixelformat = fourcc;
        mp.width = width;
        mp.height = height;

        mp.num_planes = num_planes;

        for i in range(num_planes):
            p = mp.plane_fmt[i]

            p.bytesperline = width * bitspp // 8
            p.sizeimage = p.bytesperline * height # XXX / pfpi.ysub;
            p.field = v4l2.uapi.V4L2_FIELD_NONE

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

    def queue(self, vbuf):
        idx = -1
        for _idx in range(len(self.fbs)):
            if self.fbs[_idx] == False:
                idx = _idx
                break

        assert(idx != -1)

        vbuf.index = idx

        self.fbs[idx] = True

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

    def dequeue(self):
        vfb = VideoBuffer(self.mem_type)

        v4l2buf = v4l2.uapi.v4l2_buffer()
        v4l2buf.type = self.buf_type.value
        v4l2buf.memory = self.mem_type.value

        num_planes = 1

        planes = (v4l2.uapi.v4l2_plane * num_planes)()
        v4l2buf.m.planes = planes
        v4l2buf.length = num_planes

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, v4l2buf, True)

        vfb.index = v4l2buf.index
        vfb.buffer_size = v4l2buf.m.planes[0].length

        if self.mem_type == v4l2.MemType.DMABUF:
            vfb.fd = v4l2buf.m.planes[0].m.fd
        else:
            vfb.offset = v4l2buf.m.planes[0].m.mem_offset

        idx = v4l2buf.index

        self.fbs[idx] = False

        return vfb


class MetaCaptureStreamer(CaptureStreamer):
    def __init__(self, vdev: VideoDevice, mem_type: v4l2.MemType, buf_type: v4l2.BufType,
                 size: int, fourcc: v4l2.MetaFormat) -> None:
        super().__init__(vdev, mem_type, buf_type)

        self.size = size
        self.fourcc = fourcc

        self.set_format(fourcc, size)

    def set_format(self, fourcc, size):
        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type.value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        pfi = v4l2.pixelformats.get_pixel_format_info(fourcc)
        #bitspp = pfi.planes[0].bitspp # XXX quick hack

        v4lfmt.fmt.meta.dataformat = fourcc
        v4lfmt.fmt.meta.buffersize = size

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)


class VideoBuffer:
    def __init__(self, mem_type) -> None:
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

def create_mmapbuffer(w, h, fourcc, payload_size):
    buf = VideoBuffer(v4l2.MemType.MMAP)
    buf.width = w
    buf.height = h
    buf.fourcc = fourcc
    buf.payload_size = payload_size
    return buf

def create_dmabuffer(fd, w, h, fourcc, payload_size):
    buf = VideoBuffer(v4l2.MemType.DMABUF)
    buf.fd = fd
    buf.width = w
    buf.height = h
    buf.fourcc = fourcc
    buf.payload_size = payload_size
    return buf
