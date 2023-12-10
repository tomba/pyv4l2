import ctypes
import fcntl
import os
import v4l2
import v4l2.uapi

class VideoDevice:
    def __init__(self, entity: v4l2.MediaEntity) -> None:
        self.entity = entity
        assert(entity.interface.is_video)
        self.fd = os.open(entity.interface.dev_path, os.O_RDWR | os.O_NONBLOCK)
        assert(self.fd != -1)

        cap = v4l2.uapi.v4l2_capability()
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QUERYCAP, cap, True)

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
        fmt = v4l2.uapi.v4l2_format()
        fmt.type = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_CAPTURE
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, fmt, True)
        return fmt

    def get_capture_streamer(self, mem_type):
        assert(self.has_capture)

        if self.has_mplane_capture:
            return MPlaneCaptureStreamer(self, mem_type, v4l2.uapi.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE)
        else:
            return CaptureStreamer(self, mem_type, v4l2.uapi.V4L2_BUF_TYPE_VIDEO_CAPTURE)

class CaptureStreamer:
    _fourcc_bitspp_map = {
        v4l2.uapi.V4L2_PIX_FMT_UYVY: 16,
        v4l2.uapi.V4L2_PIX_FMT_YUYV: 16,
        v4l2.uapi.V4L2_PIX_FMT_SRGGB12: 16,
    }

    def __init__(self, vdev: VideoDevice, mem_type, buf_type) -> None:
        self.vdev = vdev
        self.mem_type = mem_type
        self.buf_type = buf_type
        self.fbs = []

    def set_port(self, port):
        pass

    def set_format(self, fourcc, width, height):
        global __fourcc_bitspp_map

        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        if fourcc not in CaptureStreamer._fourcc_bitspp_map:
            print("Missing support for fourcc", v4l2.uapi.fourcc_to_str(fourcc))
        assert(fourcc in CaptureStreamer._fourcc_bitspp_map)

        bitspp = CaptureStreamer._fourcc_bitspp_map[fourcc]

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

    def set_queue_size(self, queue_size):
        self.fbs = [ False ] * queue_size

        v4lreqbuf = v4l2.uapi.v4l2_requestbuffers()
        v4lreqbuf.type = self.buf_type
        v4lreqbuf.memory = self.mem_type
        v4lreqbuf.count = queue_size
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_REQBUFS, v4lreqbuf, True)
        assert(v4lreqbuf.count == queue_size)

    def queue(self, vbuf):
        idx = -1
        for _idx in range(len(self.fbs)):
            if self.fbs[_idx] == False:
                idx = _idx
                break

        assert(idx != -1)

        vbuf.index = idx

        self.fbs[idx] = True

        buf = v4l2.uapi.v4l2_buffer()
        buf.type = self.buf_type
        buf.memory = vbuf.mem_type
        buf.index = vbuf.index
        if vbuf.mem_type == v4l2.uapi.V4L2_MEMORY_DMABUF:
            buf.m.fd = vbuf.fd

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QBUF, buf, True)

    def dequeue(self):
        fb = VideoBuffer(self.mem_type)

        buf = v4l2.uapi.v4l2_buffer()
        buf.type = self.buf_type
        buf.memory = self.mem_type

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, buf, True)

        fb.index = buf.index
        fb.buffer_size = buf.length

        if self.mem_type == v4l2.uapi.V4L2_MEMORY_DMABUF:
            fb.fd = buf.m.fd
        else:
            fb.offset = buf.m.offset

        idx = buf.index

        self.fbs[idx] = False

        return fb

    def stream_on(self):
        buf_type = ctypes.c_uint32(self.buf_type)
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_STREAMON, buf_type, True)

    def stream_off(self):
        buf_type = ctypes.c_uint32(self.buf_type)
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_STREAMOFF, buf_type, True)

    @property
    def fd(self):
        return self.vdev.fd


class MPlaneCaptureStreamer(CaptureStreamer):
    def __init__(self, vdev: VideoDevice, mem_type, buf_type) -> None:
        super().__init__(vdev, mem_type, buf_type)
        self.bytesperline = 0

    def set_format(self, fourcc, width, height):
        global __fourcc_bitspp_map

        v4lfmt = v4l2.uapi.v4l2_format()

        v4lfmt.type = self.buf_type
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_FMT, v4lfmt, True)

        if fourcc not in CaptureStreamer._fourcc_bitspp_map:
            print("Missing support for fourcc", v4l2.uapi.fourcc_to_str(fourcc))
        assert(fourcc in CaptureStreamer._fourcc_bitspp_map)

        bitspp = CaptureStreamer._fourcc_bitspp_map[fourcc]

        num_planes = 1 # XXX

        mp = v4lfmt.fmt.pix_mp

        mp.pixelformat = fourcc;
        mp.width = width;
        mp.height = height;

        mp.num_planes = num_planes;

        for i in range(num_planes):
            p = mp.plane_fmt[i]

            p.bytesperline = width * bitspp // 8;
            p.sizeimage = p.bytesperline * height # XXX / pfpi.ysub;
            p.field = v4l2.uapi.V4L2_FIELD_NONE

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_FMT, v4lfmt, True)

        # XXX AAARGH
        self.bytesperline = v4lfmt.fmt.pix_mp.plane_fmt[0].bytesperline

    def queue(self, vbuf):
        idx = -1
        for _idx in range(len(self.fbs)):
            if self.fbs[_idx] == False:
                idx = _idx
                break

        assert(idx != -1)

        vbuf.index = idx

        self.fbs[idx] = True

        buf = v4l2.uapi.v4l2_buffer()
        buf.type = self.buf_type
        buf.memory = vbuf.mem_type
        buf.index = vbuf.index

        num_planes = 1

        planes = (v4l2.uapi.v4l2_plane * num_planes)()
        buf.m.planes = planes

        #bitspp = CaptureStreamer._fourcc_bitspp_map[vbuf.fourcc]

        if vbuf.mem_type == v4l2.uapi.V4L2_MEMORY_DMABUF:
            planes[0].m.fd = vbuf.fd

        planes[0].bytesused = vbuf.payload_size # vbuf.width * vbuf.height * bitspp // 8

        buf.length = num_planes

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_QBUF, buf, True)

    def dequeue(self):
        vfb = VideoBuffer(self.mem_type)

        buf = v4l2.uapi.v4l2_buffer()
        buf.type = self.buf_type
        buf.memory = self.mem_type

        num_planes = 1

        planes = (v4l2.uapi.v4l2_plane * num_planes)()
        buf.m.planes = planes
        buf.length = num_planes

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_DQBUF, buf, True)

        vfb.index = buf.index
        vfb.buffer_size = buf.m.planes[0].length

        if self.mem_type == v4l2.uapi.V4L2_MEMORY_DMABUF:
            vfb.fd = buf.m.planes[0].m.fd
        else:
            vfb.offset = buf.m.planes[0].m.mem_offset

        idx = buf.index

        self.fbs[idx] = False

        return vfb


class MetaCaptureStreamer:
    pass

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
    buf = VideoBuffer(v4l2.uapi.V4L2_MEMORY_MMAP)
    buf.width = w
    buf.height = h
    buf.fourcc = fourcc
    buf.payload_size = payload_size
    return buf

def create_dmabuffer(fd, w, h, fourcc, payload_size):
    buf = VideoBuffer(v4l2.uapi.V4L2_MEMORY_DMABUF)
    buf.fd = fd
    buf.width = w
    buf.height = h
    buf.fourcc = fourcc
    buf.payload_size = payload_size
    return buf
