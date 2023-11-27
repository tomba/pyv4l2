from .v4l2_kernel import *
from .media import *
from .subdev import *

def __v4l2_subdev_format_to_str(self: v4l2_subdev_format):
    return f'v4l2_subdev_format({self.format.width}x{self.format.height}-0x{self.format.code:x})'

v4l2_subdev_format.__repr__ = __v4l2_subdev_format_to_str


def filepath_for_major_minor(major, minor):
    import os
    import glob

    for fname in glob.glob('/dev/video*'):
        dev = os.stat(fname).st_rdev
        dev_major = os.major(dev)
        dev_minor = os.minor(dev)

        if major == dev_major and minor == dev_minor:
            return fname

    for fname in glob.glob('/dev/v4l-subdev*'):
        dev = os.stat(fname).st_rdev
        dev_major = os.major(dev)
        dev_minor = os.minor(dev)

        if major == dev_major and minor == dev_minor:
            return fname

    raise Exception("No device-node found for ({},{})".format(major, minor))
