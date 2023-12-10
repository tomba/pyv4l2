#!/usr/bin/python3

import fcntl
import gc
import unittest
import v4l2


class TestCardMethods(unittest.TestCase):
    def test_card(self):
        mdev = v4l2.MediaDevice('/dev/media0')
        fd = mdev.fd

        mdev = None
        gc.collect()
        with self.assertRaises(Exception):
            fcntl.fcntl(fd, fcntl.F_GETFD)


if __name__ == '__main__':
    unittest.main()
