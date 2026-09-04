#!/usr/bin/env python3

import fcntl
import gc
import unittest

import v4l2


class TestCardMethods(unittest.TestCase):
    def _get_mdev(self):
        try:
            mdev = v4l2.MediaDevice('/dev/media0')
        except FileNotFoundError as e:
            self.skipTest(e)

        return mdev

    def _assert_closed(self, fd):
        with self.assertRaises(OSError):
            fcntl.fcntl(fd, fcntl.F_GETFD)

    def test_card(self):
        mdev = self._get_mdev()

        fd = mdev.fd

        mdev = None
        gc.collect()
        self._assert_closed(fd)

    def test_close(self):
        mdev = self._get_mdev()
        fd = mdev.fd

        mdev.close()
        self._assert_closed(fd)
        self.assertEqual(mdev.fd, -1)

        # A second close is a no-op
        mdev.close()

    def test_with(self):
        with self._get_mdev() as mdev:
            fd = mdev.fd

        self._assert_closed(fd)

    def test_subdev_and_videodev_close(self):
        mdev = self._get_mdev()

        for iface in mdev.interfaces:
            if iface.is_subdev:
                dev = v4l2.SubDevice(iface.dev_path)
            elif iface.is_video:
                dev = v4l2.VideoDevice(iface.dev_path)
            else:
                continue

            fd = dev.fd
            dev.close()
            self._assert_closed(fd)


if __name__ == '__main__':
    unittest.main()
