#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-3-Clause
# Copyright (C) 2023-2026, Tomi Valkeinen <tomi.valkeinen@ideasonboard.com>

from __future__ import annotations

import argparse
import struct
import sys
import traceback

import numpy as np
from pixutils.formats import PixelFormats, MetaFormat, MetaFormats
from pixutils.qt import ImageViewerWidget
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
import PyQt6.QtNetwork

receivers = []

# ctx-idx, width, height, strides[4], format[16], num-planes, plane[4]
struct_fmt = struct.Struct('<III4I16pI4I')


# Loading MJPEG to a QPixmap produces corrupt JPEG data warnings. Ignore these.
def qt_message_handler(msg_type, msg_log_context, msg_string):
    if msg_string.startswith('Corrupt JPEG data'):
        return

    # For some reason qInstallMessageHandler returns None, so we won't
    # call the old handler
    if old_msg_handler is not None:
        old_msg_handler(msg_type, msg_log_context, msg_string)
    else:
        print(msg_string)


old_msg_handler = QtCore.qInstallMessageHandler(qt_message_handler)


NO_SKIP = False


def meta_to_pix(bytesperline, data):
    prev = None
    nskip = 0
    cnt = 0
    for i in data:
        if cnt == bytesperline:
            if nskip > 0:
                print('(* {}) '.format(nskip), end='')

            cnt = 0
            prev = None
            nskip = 0
            print('LE')

        cnt += 1

        if not NO_SKIP and i == prev:
            nskip += 1
            continue

        if nskip > 0:
            print('(* {}) '.format(nskip), end='')

        print('{:02x} '.format(i), end='')

        prev = i
        nskip = 0

    if nskip > 0:
        print('(* {}) '.format(nskip), end='')

    if cnt == bytesperline:
        print('LE')
    else:
        print()


class Receiver(QtWidgets.QWidget):
    def __init__(self, socket: PyQt6.QtNetwork.QTcpSocket):
        super().__init__()

        self.name = '{}:{}'.format(socket.peerAddress().toString(), socket.peerPort())

        print('[{}] Accepted new connection'.format(self.name))

        self.socket = socket

        self.socket.readyRead.connect(self.on_ready_read)
        self.socket.disconnected.connect(self.on_disconnected)
        self.socket.errorOccurred.connect(self.on_error)

        self.header_buffer = bytearray()
        self.header_tuple = ()
        self.data_buffer = bytearray()
        self.data_size = 0

        self.state = 0

        self.resize(1600, 900)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        self.viewer = ImageViewerWidget(options={})
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.viewer)
        self.setLayout(layout)

        self.ctx_idx_to_stream_num = {}
        self.next_stream_num = 0
        self.pixel_stream_count = 0

        self.show()
        print('done')

    def on_ready_read(self):
        while self.socket.bytesAvailable():
            if self.state == 0:
                data = self.socket.read(struct_fmt.size - len(self.header_buffer))
                self.header_buffer.extend(data)

                if len(self.header_buffer) == struct_fmt.size:
                    self.on_header()
            else:
                data = self.socket.read(self.data_size - len(self.data_buffer))
                self.data_buffer.extend(data)

                if len(self.data_buffer) == self.data_size:
                    try:
                        self.on_buffers()
                    except Exception:
                        print(traceback.format_exc())
                        qApp = QtWidgets.QApplication.instance()
                        assert qApp
                        qApp.exit(-1)
                        return

    def on_header(self):
        self.header_tuple = struct_fmt.unpack_from(self.header_buffer)
        *_, p0, p1, p2, p3 = self.header_tuple
        self.data_size = p0 + p1 + p2 + p3
        self.header_buffer = bytearray()

        self.state = 1

    def _register_pixel_stream(self, ctx_idx: int) -> int | None:
        """Register new pixel stream, return viewer stream number (0-3) or None if at limit."""
        # If already registered, return cached mapping
        if ctx_idx in self.ctx_idx_to_stream_num:
            return self.ctx_idx_to_stream_num[ctx_idx]

        # Check 4-stream limit
        if self.pixel_stream_count >= 4:
            print(
                f'[{self.name}] WARNING: Cannot display ctx-idx {ctx_idx}, '
                f'already showing 4 streams. Dropping frames.'
            )
            return None

        # Assign next available stream number
        stream_num = self.next_stream_num
        self.ctx_idx_to_stream_num[ctx_idx] = stream_num
        self.next_stream_num += 1
        self.pixel_stream_count += 1

        # Resize viewer grid (MUST call before set_frame)
        self.viewer.setNumStreams(self.pixel_stream_count)
        print(f'[{self.name}] Registered ctx-idx {ctx_idx} → stream {stream_num}')

        return stream_num

    def on_buffers(self):
        idx, w, h, s0, s1, s2, s3, fmtstr, num_planes, p0, p1, p2, p3 = self.header_tuple
        bytesperline = s0
        try:
            fmt = PixelFormats.find_by_name(fmtstr.decode('ascii'))
        except StopIteration:
            try:
                fmt = MetaFormats.find_by_name(fmtstr.decode('ascii'))
            except StopIteration as exc:
                raise RuntimeError(f'Format not found: {fmtstr}') from exc

        print(
            f'[{self.name}] cam{idx} {w}x{h}-{fmt}, buflen {len(self.data_buffer)}, bpl {bytesperline}'
        )

        if isinstance(fmt, MetaFormat):
            # MetaFormat: print to console (unchanged)
            meta_to_pix(bytesperline, self.data_buffer)
        else:
            # PixelFormat: display in viewer
            stream_num = self._register_pixel_stream(idx)

            if stream_num is not None:
                # Convert bytearray to numpy array (zero-copy view)
                buffer_np = np.frombuffer(self.data_buffer, dtype=np.uint8)

                # Update viewer
                self.viewer.set_frame(stream_num, w, h, fmt, buffer_np, bytesperline)

        self.data_buffer = bytearray()

        self.state = 0

    def on_disconnected(self):
        print('[{}] Disconnected'.format(self.name))
        self.close()
        receivers.remove(self)

    def on_error(self):
        print('[{}] Error: {}'.format(self.name, self.socket.errorString()))


def new_connection(tcpServer):
    clientConnection: PyQt6.QtNetwork.QTcpSocket = tcpServer.nextPendingConnection()
    w = Receiver(clientConnection)
    receivers.append(w)


def readkey():
    qApp = QtWidgets.QApplication.instance()
    assert qApp
    sys.stdin.readline()
    qApp.quit()


def main():
    parser = argparse.ArgumentParser(description='Camera RX server')
    parser.add_argument('-H', '--host', default='0.0.0.0')
    parser.add_argument('-P', '--port', default=43242, type=int)
    args = parser.parse_args()

    qApp = QtWidgets.QApplication(sys.argv)
    qApp.setQuitOnLastWindowClosed(False)

    keynotif = QtCore.QSocketNotifier(sys.stdin.fileno(), QtCore.QSocketNotifier.Type.Read)
    keynotif.activated.connect(readkey)

    tcpServer = PyQt6.QtNetwork.QTcpServer(qApp)
    tcpServer.listen(PyQt6.QtNetwork.QHostAddress(args.host), args.port)
    tcpServer.newConnection.connect(lambda: new_connection(tcpServer))
    print(f'Network receive on {args.host}:{args.port}')

    return qApp.exec()


if __name__ == '__main__':
    sys.exit(main())
