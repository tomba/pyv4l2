#!/usr/bin/python3

import unittest
import v4l2

class TestInstall(unittest.TestCase):
    def test_install(self):
        # Just do something with v4l2 to see it has imported ok
        self.assertEqual(v4l2.PixelFormats.XRGB8888.drm_fourcc, 0x34325258)

if __name__ == '__main__':
    unittest.main()
