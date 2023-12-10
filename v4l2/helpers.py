from __future__ import annotations

import os
import glob

def filepath_for_major_minor(major, minor):
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
