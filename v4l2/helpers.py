from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import v4l2.uapi

__all__ = [
    'BufType',
    'ColorSpace',
    'Field',
    'HSVEncoding',
    'MemType',
    'Quantization',
    'Rect',
    'SelectionTarget',
    'XferFunc',
    'YCbCrEncoding',
]


def filepath_for_major_minor(major: int, minor: int):
    with open(f'/sys/dev/char/{major}:{minor}/uevent', encoding='ascii') as f:
        for l in f:
            if not l.startswith('DEVNAME='):
                continue
            path = l[len('DEVNAME=') :].strip()
            return '/dev/' + path

    raise RuntimeError(f'No device-node found for ({major},{minor})')


class BufType(Enum):
    VIDEO_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_CAPTURE
    VIDEO_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_OUTPUT
    VIDEO_OVERLAY = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_OVERLAY
    VBI_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_VBI_CAPTURE
    VBI_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_VBI_OUTPUT
    SLICED_VBI_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_SLICED_VBI_CAPTURE
    SLICED_VBI_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_SLICED_VBI_OUTPUT
    VIDEO_OUTPUT_OVERLAY = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY
    VIDEO_CAPTURE_MPLANE = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE
    VIDEO_OUTPUT_MPLANE = v4l2.uapi.V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE
    SDR_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_SDR_CAPTURE
    SDR_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_SDR_OUTPUT
    META_CAPTURE = v4l2.uapi.V4L2_BUF_TYPE_META_CAPTURE
    META_OUTPUT = v4l2.uapi.V4L2_BUF_TYPE_META_OUTPUT
    PRIVATE = v4l2.uapi.V4L2_BUF_TYPE_PRIVATE


class MemType(Enum):
    MMAP = v4l2.uapi.V4L2_MEMORY_MMAP
    USERPTR = v4l2.uapi.V4L2_MEMORY_USERPTR
    OVERLAY = v4l2.uapi.V4L2_MEMORY_OVERLAY
    DMABUF = v4l2.uapi.V4L2_MEMORY_DMABUF


class ColorSpace(Enum):
    DEFAULT = v4l2.uapi.V4L2_COLORSPACE_DEFAULT
    SMPTE170M = v4l2.uapi.V4L2_COLORSPACE_SMPTE170M
    SMPTE240M = v4l2.uapi.V4L2_COLORSPACE_SMPTE240M
    REC709 = v4l2.uapi.V4L2_COLORSPACE_REC709
    BT878 = v4l2.uapi.V4L2_COLORSPACE_BT878
    SYSTEM_470_M = v4l2.uapi.V4L2_COLORSPACE_470_SYSTEM_M
    SYSTEM_470_BG = v4l2.uapi.V4L2_COLORSPACE_470_SYSTEM_BG
    JPEG = v4l2.uapi.V4L2_COLORSPACE_JPEG
    SRGB = v4l2.uapi.V4L2_COLORSPACE_SRGB
    OPRGB = v4l2.uapi.V4L2_COLORSPACE_OPRGB
    BT2020 = v4l2.uapi.V4L2_COLORSPACE_BT2020
    RAW = v4l2.uapi.V4L2_COLORSPACE_RAW
    DCI_P3 = v4l2.uapi.V4L2_COLORSPACE_DCI_P3


class YCbCrEncoding(Enum):
    DEFAULT = v4l2.uapi.V4L2_YCBCR_ENC_DEFAULT
    BT601 = v4l2.uapi.V4L2_YCBCR_ENC_601
    BT709 = v4l2.uapi.V4L2_YCBCR_ENC_709
    XV601 = v4l2.uapi.V4L2_YCBCR_ENC_XV601
    XV709 = v4l2.uapi.V4L2_YCBCR_ENC_XV709
    SYCC = v4l2.uapi.V4L2_YCBCR_ENC_SYCC
    BT2020 = v4l2.uapi.V4L2_YCBCR_ENC_BT2020
    BT2020_CONST_LUM = v4l2.uapi.V4L2_YCBCR_ENC_BT2020_CONST_LUM
    SMPTE240M = v4l2.uapi.V4L2_YCBCR_ENC_SMPTE240M


class HSVEncoding(Enum):
    HSV_180 = v4l2.uapi.V4L2_HSV_ENC_180
    HSV_256 = v4l2.uapi.V4L2_HSV_ENC_256


class Quantization(Enum):
    DEFAULT = v4l2.uapi.V4L2_QUANTIZATION_DEFAULT
    FULL_RANGE = v4l2.uapi.V4L2_QUANTIZATION_FULL_RANGE
    LIM_RANGE = v4l2.uapi.V4L2_QUANTIZATION_LIM_RANGE


class XferFunc(Enum):
    DEFAULT = v4l2.uapi.V4L2_XFER_FUNC_DEFAULT
    F709 = v4l2.uapi.V4L2_XFER_FUNC_709
    SRGB = v4l2.uapi.V4L2_XFER_FUNC_SRGB
    OPRGB = v4l2.uapi.V4L2_XFER_FUNC_OPRGB
    SMPTE240M = v4l2.uapi.V4L2_XFER_FUNC_SMPTE240M
    NONE = v4l2.uapi.V4L2_XFER_FUNC_NONE
    DCI_P3 = v4l2.uapi.V4L2_XFER_FUNC_DCI_P3
    SMPTE2084 = v4l2.uapi.V4L2_XFER_FUNC_SMPTE2084


class SelectionTarget(Enum):
    CROP = v4l2.uapi.V4L2_SEL_TGT_CROP
    CROP_DEFAULT = v4l2.uapi.V4L2_SEL_TGT_CROP_DEFAULT
    CROP_BOUNDS = v4l2.uapi.V4L2_SEL_TGT_CROP_BOUNDS
    NATIVE_SIZE = v4l2.uapi.V4L2_SEL_TGT_NATIVE_SIZE
    COMPOSE = v4l2.uapi.V4L2_SEL_TGT_COMPOSE
    COMPOSE_DEFAULT = v4l2.uapi.V4L2_SEL_TGT_COMPOSE_DEFAULT
    COMPOSE_BOUNDS = v4l2.uapi.V4L2_SEL_TGT_COMPOSE_BOUNDS
    COMPOSE_PADDED = v4l2.uapi.V4L2_SEL_TGT_COMPOSE_PADDED


@dataclass
class Rect:
    left: int = 0
    top: int = 0
    width: int = 0
    height: int = 0

    @classmethod
    def from_v4l2_rect(cls, r: v4l2.uapi.v4l2_rect):
        return cls(r.left, r.top, r.width, r.height)

    def to_v4l2_rect(self):
        return v4l2.uapi.v4l2_rect(self.left, self.top, self.width, self.height)


class Field(Enum):
    ANY = v4l2.uapi.V4L2_FIELD_ANY
    NONE = v4l2.uapi.V4L2_FIELD_NONE
    TOP = v4l2.uapi.V4L2_FIELD_TOP
    BOTTOM = v4l2.uapi.V4L2_FIELD_BOTTOM
    INTERLACED = v4l2.uapi.V4L2_FIELD_INTERLACED
    SEQ_TB = v4l2.uapi.V4L2_FIELD_SEQ_TB
    SEQ_BT = v4l2.uapi.V4L2_FIELD_SEQ_BT
    ALTERNATE = v4l2.uapi.V4L2_FIELD_ALTERNATE
    INTERLACED_TB = v4l2.uapi.V4L2_FIELD_INTERLACED_TB
    INTERLACED_BT = v4l2.uapi.V4L2_FIELD_INTERLACED_BT
