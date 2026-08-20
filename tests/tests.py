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

    def test_card(self):
        mdev = self._get_mdev()

        fd = mdev.fd

        mdev = None
        gc.collect()
        with self.assertRaises(OSError):
            fcntl.fcntl(fd, fcntl.F_GETFD)


if __name__ == '__main__':
    unittest.main()
