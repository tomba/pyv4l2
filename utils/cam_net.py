from __future__ import annotations

import mmap
import socket
import struct

from cam_types import Stream
from v4l2 import MetaFormat


class NetTX:
    # ctx-idx, width, height, strides[4], format[16], num-planes, plane[4]
    struct_fmt = struct.Struct('<III4I16pI4I')

    def __init__(self, host: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def tx(self, stream: Stream, vbuf, is_drm):
        cap = stream['cap']

        plane_sizes = cap.buffersizes
        strides = cap.strides

        # Extend lists to 4 elements
        plane_sizes.extend(0 for _ in range(4 - len(plane_sizes)))
        strides.extend(0 for _ in range(4 - len(strides)))

        fmt = stream['format']

        if isinstance(fmt, MetaFormat):
            num_planes = 1
        else:
            num_planes = len(fmt.planes)

        hdr = NetTX.struct_fmt.pack(
            stream['id'],
            stream['w'],
            stream['h'],
            *strides,
            bytes(fmt.name, 'ascii'),
            num_planes,
            *plane_sizes,
        )

        self.sock.sendall(hdr)

        if is_drm:
            fb = next((fb for fb in stream['fbs'] if fb.fd(0) == vbuf.fd), None)
            assert fb is not None

            with mmap.mmap(fb.fd(0), fb.size(0), mmap.MAP_SHARED, mmap.PROT_READ) as b:
                self.sock.sendall(b)
        else:
            # Need PROT_WRITE to be able to read fe-config buffers
            with mmap.mmap(
                cap.fd,
                cap.framesize,
                mmap.MAP_SHARED,
                mmap.PROT_READ | mmap.PROT_WRITE,
                offset=vbuf.offset,
            ) as b:
                self.sock.sendall(b)
