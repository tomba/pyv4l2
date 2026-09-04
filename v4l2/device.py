from __future__ import annotations

import fcntl
import os
import weakref

import v4l2.uapi


class Device:
    """Base for objects owning a device node fd.

    The fd is closed with close(), when leaving a with block, or when the
    object is garbage collected."""

    def __init__(self, dev_path: str) -> None:
        self.dev_path = dev_path
        self.fd = os.open(dev_path, os.O_RDWR | os.O_NONBLOCK)
        self._finalizer = weakref.finalize(self, os.close, self.fd)

    def close(self):
        if self._finalizer.alive:
            self._finalizer()
            self.fd = -1

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


class V4L2Device(Device):
    """A video or subdev node."""

    def get_control(self, ctrl_id: int) -> int:
        ctrl = v4l2.uapi.v4l2_control()
        ctrl.id = ctrl_id
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_G_CTRL, ctrl, True)
        return ctrl.value

    def set_control(self, ctrl_id: int, value: int) -> int:
        """Set a control. Returns the value the driver applied."""
        ctrl = v4l2.uapi.v4l2_control()
        ctrl.id = ctrl_id
        ctrl.value = value
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_S_CTRL, ctrl, True)
        return ctrl.value
