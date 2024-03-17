from __future__ import annotations

from enum import Enum
from typing import NamedTuple

__all__ = [ 'PixelFormat', 'MetaFormat' ]

def str_to_fourcc(s: str):
    return \
        ord(s[0]) << 0 | \
        ord(s[1]) << 8 | \
        ord(s[2]) << 16 | \
        ord(s[3]) << 24


class PixelColorEncoding(Enum):
    RGB = 0
    YUV = 1
    RAW = 2
    UNDEFINED = 3


class PixelFormatPlaneInfo(NamedTuple):
    bytespergroup: int
    verticalsubsampling: int


class PixelFormatInfo:
    def __init__(self,
                 drm_fourcc: None | str, v4l2_fourcc: str,
                 bitsperpixel: int, colorencoding: PixelColorEncoding, packed: bool,
                 pixelspergroup: int, planes) -> None:
        self.drm_fourcc = str_to_fourcc(drm_fourcc) if drm_fourcc else None
        self.v4l2_fourcc = str_to_fourcc(v4l2_fourcc)
        self.bitsperpixel = bitsperpixel
        self.color = colorencoding
        self.packed = packed
        self.pixelspergroup = pixelspergroup
        self.planes = [PixelFormatPlaneInfo(*p) for p in planes]

    def stride(self, width: int, plane: int = 0, align: int = 1):
        if plane >= len(self.planes):
            raise RuntimeError()

        # ceil(width / pixelsPerGroup) * bytesPerGroup
        stride = (width + self.pixelspergroup - 1) // self.pixelspergroup * self.planes[plane].bytespergroup

        # ceil(stride / align) * align
        return (stride + align - 1) // align * align

    def planesize(self, width, height, plane, align: int = 1):
        stride = self.stride(width, plane, align)
        if stride == 0:
            return 0

        #return self.planeSize(height, plane, stride)

        vertsubsample = self.planes[plane].verticalsubsampling

        # stride * ceil(height / verticalSubSampling)
        return stride * ((height + vertsubsample - 1) // vertsubsample)


#    def planesize(self, height, plane, stride):
#        vertSubSample = self.planes[plane].verticalSubSampling
#        if vertSubSample == 0:
#            return 0
#
#        # stride * ceil(height / verticalSubSampling)
#        return stride * ((height + vertSubSample - 1) // vertSubSample)

    def framesize(self, width, height, align: int = 1):
        return sum([self.planesize(width, height, i, align) for i in range(len(self.planes))])


class PixelFormat(Enum):

    # RGB

    RGB565 = PixelFormatInfo(
        'RG16', 'RGBP',
        16,
        PixelColorEncoding.RGB,
        False,
        1,
        ( ( 2, 1 ), ),
    )

    RGB888 = PixelFormatInfo(
        'RG24', 'BGR3',
        24,
        PixelColorEncoding.RGB,
        False,
        1,
        ( ( 3, 1 ), ),
    )
    BGR888 = PixelFormatInfo(
        'BG24', 'RGB3',
        24,
        PixelColorEncoding.RGB,
        False,
        1,
        ( ( 3, 1 ), ),
    )

    # YUV

    NV12 = PixelFormatInfo(
        'NV12', 'NM12',
        12,
        PixelColorEncoding.YUV,
        False,
        2,
        ( ( 2, 1 ), ( 2, 2 ), ),
    )

    YUYV = PixelFormatInfo(
        'YUYV', 'YUYV',
        16,
        PixelColorEncoding.YUV,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    UYVY = PixelFormatInfo(
        'UYVY', 'UYVY',
        16,
        PixelColorEncoding.YUV,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    # RAW

    SBGGR8 = PixelFormatInfo(
        None, 'BA81',
        8,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 2, 1 ), ),
    )

    SGBRG8 = PixelFormatInfo(
        None, 'GBRG',
        8,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 2, 1 ), ),
    )

    SGRBG8 = PixelFormatInfo(
        None, 'GRBG',
        8,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 2, 1 ), ),
    )

    SRGGB8 = PixelFormatInfo(
        None, 'RGGB',
        8,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 2, 1 ), ),
    )


    SRGGB10 = PixelFormatInfo(
        None, 'RG10',
        10,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    SBGGR10 = PixelFormatInfo(
        None, 'BG10',
        10,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    SRGGB10P = PixelFormatInfo(
        None, 'pRAA',
        10,
        PixelColorEncoding.RAW,
        True,
        4,
        ( ( 5, 1 ), ),
    )

    SRGGB12 = PixelFormatInfo(
        None, 'RG12',
        12,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    SRGGB16 = PixelFormatInfo(
        None, 'RG16',
        16,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 4, 1 ), ),
    )


class MetaFormatInfo:
    def __init__(self, v4l2_fourcc: str, pixelspergroup: int, bytespergroup: int) -> None:
        self.v4l2_fourcc = str_to_fourcc(v4l2_fourcc)
        self.pixelspergroup = pixelspergroup
        self.bytespergroup = bytespergroup

    def stride(self, width: int, align: int = 1):
        # ceil(width / pixelsPerGroup) * bytesPerGroup
        stride = (width + self.pixelspergroup - 1) // self.pixelspergroup * self.bytespergroup

        # ceil(stride / align) * align
        return (stride + align - 1) // align * align


class MetaFormat(Enum):
    GENERIC_8 = MetaFormatInfo('MET8', 2, 2)
    GENERIC_CSI2_10 = MetaFormatInfo('MC1A', 4, 5)
    GENERIC_CSI2_12 = MetaFormatInfo('MC1C', 2, 3)

    RPI_FE_CFG = MetaFormatInfo('RPFC', 1, 1)
    RPI_FE_STATS = MetaFormatInfo('RPFS', 1, 1)

    # XXX deprecated rpi format
    SENSOR_DATA = MetaFormatInfo('SENS', 1, 1)
