#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-3-Clause
# Copyright (C) 2023, Tomi Valkeinen <tomi.valkeinen@ideasonboard.com>

from cam_rx_helpers import data_to_pix
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
import PyQt5.QtNetwork
import struct
import sys
import traceback

PORT = 43242
receivers = []

struct_fmt = struct.Struct('<IIII16pI4I')

# Loading MJPEG to a QPixmap produces corrupt JPEG data warnings. Ignore these.
def qt_message_handler(msg_type, msg_log_context, msg_string):
    if msg_string.startswith("Corrupt JPEG data"):
        return

    # For some reason qInstallMessageHandler returns None, so we won't
    # call the old handler
    if old_msg_handler is not None:
        old_msg_handler(msg_type, msg_log_context, msg_string)
    else:
        print(msg_string)


old_msg_handler = QtCore.qInstallMessageHandler(qt_message_handler)


def meta_to_pix(fmt, w, h, bytesperline, data):
    prev = None
    nskip = 0
    cnt = 0
    for i in data:
        if cnt == bytesperline:
            if nskip > 0:
                print("... ({} skipped) ".format(nskip), end='')

            cnt = 0
            prev = None
            nskip = 0
            print("LE")

        cnt += 1

        if i == prev:
            nskip += 1
            continue

        if nskip > 0:
            print("... ({} skipped) ".format(nskip), end='')

        print('{:02x} '.format(i), end='')

        prev = i
        nskip = 0

    if nskip > 0:
        print("... ({} skipped) ".format(nskip), end='')

    if cnt == bytesperline:
        print("LE")
    else:
        print()


class Receiver(QtWidgets.QWidget):
    def __init__(self, socket: PyQt5.QtNetwork.QTcpSocket):
        super().__init__()

        self.name = '{}:{}'.format(socket.peerAddress().toString(), socket.peerPort())

        print('[{}] Accepted new connection'.format(self.name))

        self.socket = socket

        self.socket.readyRead.connect(self.on_ready_read)
        self.socket.disconnected.connect(self.on_disconnected)
        self.socket.error.connect(self.on_error)

        self.header_buffer = bytearray()
        self.data_buffer = bytearray()
        self.data_size = 0

        self.state = 0

        self.resize(1000, 600)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        self.gridLayout = QtWidgets.QGridLayout()
        self.setLayout(self.gridLayout)

        self.labels = {}

        self.show()
        print("done")

    def on_ready_read(self):
        qApp = QtWidgets.QApplication.instance()

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
                        qApp.exit(-1)
                        return

    def on_header(self):
        self.header_tuple = struct_fmt.unpack_from(self.header_buffer)
        idx, w, h, bytesperline, fmtstr, num_planes, p0, p1, p2, p3 = self.header_tuple
        self.data_size = p0 + p1 + p2 + p3
        self.header_buffer = bytearray()

        self.state = 1

    def on_buffers(self):
        idx, w, h, bytesperline, fmtstr, num_planes, p0, p1, p2, p3 = self.header_tuple
        fmt = fmtstr.decode('ascii')

        print('[{}] cam{} {}x{}-{}, buflen {}, bpl {}'.format(self.name, idx, w, h, fmt, len(self.data_buffer), bytesperline))

        if idx not in self.labels:
            label = QtWidgets.QLabel()
            label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            self.labels[idx] = label
            self.gridLayout.addWidget(label, self.gridLayout.count() // 2, self.gridLayout.count() % 2)

        label = self.labels[idx]

        if fmt in [ "GENERIC_8", "GENERIC_CSI2_10", "GENERIC_CSI2_12", "SENSOR_DATA" ]:
            meta_to_pix(fmt, w, h, bytesperline, self.data_buffer)
        else:
            pix = data_to_pix(fmt, w, h, bytesperline, self.data_buffer)

            # pylint: disable=no-member
            pix = pix.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio,
                             Qt.TransformationMode.FastTransformation)

            label.setPixmap(pix)

        self.data_buffer = bytearray()

        self.state = 0

    def on_disconnected(self):
        print('[{}] Disconnected'.format(self.name))
        self.close()
        receivers.remove(self)

    def on_error(self):
        print('[{}] Error: {}'.format(self.name, self.socket.errorString()))


def new_connection(tcpServer):
    clientConnection: PyQt5.QtNetwork.QTcpSocket = tcpServer.nextPendingConnection()
    w = Receiver(clientConnection)
    receivers.append(w)


def readkey():
    qApp = QtWidgets.QApplication.instance()
    sys.stdin.readline()
    qApp.quit()


if __name__ == '__main__':
    qApp = QtWidgets.QApplication(sys.argv)
    qApp.setQuitOnLastWindowClosed(False)

    keynotif = QtCore.QSocketNotifier(sys.stdin.fileno(), QtCore.QSocketNotifier.Read)
    keynotif.activated.connect(readkey)

    tcpServer = PyQt5.QtNetwork.QTcpServer(qApp)
    tcpServer.listen(PyQt5.QtNetwork.QHostAddress('0.0.0.0'), PORT)
    tcpServer.newConnection.connect(lambda: new_connection(tcpServer))

    sys.exit(qApp.exec_())
