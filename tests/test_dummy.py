#!/usr/bin/python3

import unittest
import iob

class TestDummy(unittest.TestCase):
    def test_dummy(self):
        print("KALAAA")
        self.assertEqual(iob.PixelFormats.RGB888.name, 'RGB888')


if __name__ == '__main__':
    unittest.main()
