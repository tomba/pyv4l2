from enum import IntEnum

from .v4l2 import *

def fourcc_to_str(fourcc: int):
    return ''.join((
        chr((fourcc >> 0) & 0xff),
        chr((fourcc >> 8) & 0xff),
        chr((fourcc >> 16) & 0xff),
        chr((fourcc >> 24) & 0xff)
    ))

def str_to_fourcc(s: str):
    return \
        ord(s[0]) << 0 | \
        ord(s[1]) << 8 | \
        ord(s[2]) << 16 | \
        ord(s[3]) << 24

def __v4l2_subdev_format_to_str(self: v4l2_subdev_format):
    return f'v4l2_subdev_format({self.format.width}x{self.format.height}-0x{self.format.code:x})'

v4l2_subdev_format.__repr__ = __v4l2_subdev_format_to_str

def __v4l2_format_to_str(self: v4l2_format):
    return f'v4l2_format({self.fmt.pix.width}x{self.fmt.pix.height}-{fourcc_to_str(self.fmt.pix.pixelformat)})'

v4l2_format.__repr__ = __v4l2_format_to_str


def v4l2_subdev_route_to_str(self: v4l2_subdev_route):
    return f'v4l2_subdev_route({self.sink_pad}/{self.sink_stream}->{self.source_pad}/{self.source_stream})'

v4l2_subdev_route.__repr__ = v4l2_subdev_route_to_str


def v4l2_rect_to_str(self: v4l2_rect):
    return f'v4l2_rect(({self.left},{self.top})/{self.width}x{self.height})'

v4l2_rect.__repr__ = v4l2_rect_to_str

V4L2_SEL_TGT_CROP = 0x0000
V4L2_SEL_TGT_CROP_DEFAULT = 0x0001
V4L2_SEL_TGT_CROP_BOUNDS = 0x0002
V4L2_SEL_TGT_NATIVE_SIZE = 0x0003
V4L2_SEL_TGT_COMPOSE = 0x0100
V4L2_SEL_TGT_COMPOSE_DEFAULT = 0x0101
V4L2_SEL_TGT_COMPOSE_BOUNDS = 0x0102
V4L2_SEL_TGT_COMPOSE_PADDED = 0x0103

class v4l2_sel_tgt(IntEnum):
    CROP = V4L2_SEL_TGT_CROP
    CROP_DEFAULT = V4L2_SEL_TGT_CROP_DEFAULT
    CROP_BOUNDS = V4L2_SEL_TGT_CROP_BOUNDS
    NATIVE_SIZE = V4L2_SEL_TGT_NATIVE_SIZE
    COMPOSE = V4L2_SEL_TGT_COMPOSE
    COMPOSE_DEFAULT = V4L2_SEL_TGT_COMPOSE_DEFAULT
    COMPOSE_BOUNDS = V4L2_SEL_TGT_COMPOSE_BOUNDS
    COMPOSE_PADDED = V4L2_SEL_TGT_COMPOSE_PADDED
