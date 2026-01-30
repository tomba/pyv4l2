from __future__ import annotations

import mmap
import queue
import socket
import struct
import threading

from v4l2 import MetaFormat

from cam_types import Stream, Context, Consumer

class NetConsumer(Consumer):
    # ctx-idx, width, height, strides[4], format[16], num-planes, plane[4]
    struct_fmt = struct.Struct('<III4I16pI4I')

    def __init__(self, host: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.net_tx_queue = queue.Queue()
        self.net_done_queue = queue.Queue()
        self.net_thread = None
        self.current_buf = { }

    def setup_stream(self, ctx: Context, stream: Stream) -> bool:
        self.current_buf[stream.id] = None
        return False

    def setup_streams_done(self, ctx: Context):
        self.net_thread = threading.Thread(target=self.net_main)
        self.net_thread.start()

    def handle_frame(self, ctx: Context, stream: Stream, vbuf):
        assert ctx.tx

        if ctx.tx != ['all'] and str(stream.id) not in ctx.tx:
            return

        if self.current_buf[stream.id]:
            # Already sending a frame
            cap = stream.cap
            cap.queue(vbuf)
            return

        self.current_buf[stream.id] = vbuf
        self.net_tx_queue.put((stream, vbuf, ctx.buf_type == 'drm'))

    def cleanup(self, ctx: Context):
        self.net_tx_queue.put(None)
        if self.net_thread:
            self.net_thread.join()

    def net_main(self):
        while True:
            data = self.net_tx_queue.get()
            if not data:
                break
            stream, vbuf, is_drm = data
            self.tx(stream, vbuf, is_drm)
            self.net_done_queue.put((stream, vbuf))

    def handle_tick(self, ctx: Context):
        while not self.net_done_queue.empty():
            stream, vbuf = self.net_done_queue.get()
            self.current_buf[stream.id] = None

            cap = stream.cap
            cap.queue(vbuf)

    def tx(self, stream: Stream, vbuf, is_drm):
        cap = stream.cap

        plane_sizes = cap.buffersizes
        strides = cap.strides

        # Extend lists to 4 elements
        plane_sizes.extend(0 for _ in range(4 - len(plane_sizes)))
        strides.extend(0 for _ in range(4 - len(strides)))

        fmt = stream.format

        if isinstance(fmt, MetaFormat):
            num_planes = 1
        else:
            num_planes = len(fmt.planes)

        hdr = NetConsumer.struct_fmt.pack(
            stream.id,
            stream.w,
            stream.h,
            *strides,
            bytes(fmt.name, 'ascii'),
            num_planes,
            *plane_sizes,
        )

        self.sock.sendall(hdr)

        if is_drm:
            fb = next((fb for fb in stream.fbs if fb.fd(0) == vbuf.fd), None)
            assert fb is not None

            with mmap.mmap(fb.fd(0), fb.size(0), mmap.MAP_SHARED, mmap.PROT_READ) as b:
                self.sock.sendall(b)
        else:
            with mmap.mmap(
                cap.fd,
                cap.framesize,
                mmap.MAP_SHARED,
                mmap.PROT_READ,
                offset=vbuf.offset,
            ) as b:
                self.sock.sendall(b)
