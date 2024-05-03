from __future__ import annotations

from enum import Enum
from typing import NamedTuple

from v4l2.uapi import fourcc_to_str

__all__ = [ 'PixelFormat', 'PixelFormats', 'MetaFormat', 'MetaFormats' ]

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


class PixelFormat:
    def __init__(self, name: str,
                 drm_fourcc: None | str, v4l2_fourcc: str,
                 bitsperpixel: int, colorencoding: PixelColorEncoding, packed: bool,
                 pixelspergroup: int, planes) -> None:
        self.name = name
        self.drm_fourcc = str_to_fourcc(drm_fourcc) if drm_fourcc else None
        self.v4l2_fourcc = str_to_fourcc(v4l2_fourcc)
        self.bitsperpixel = bitsperpixel
        self.color = colorencoding
        self.packed = packed
        self.pixelspergroup = pixelspergroup
        self.planes = [PixelFormatPlaneInfo(*p) for p in planes]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'PixelFormat({self.name})'

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


class PixelFormats:
    @staticmethod
    def find_v4l2_fourcc(fourcc):
        return next(v for v in PixelFormats.__dict__.values() if isinstance(v, PixelFormat) and v.v4l2_fourcc == fourcc)

    @staticmethod
    def find_v4l2_fourcc_unsupported(fourcc):
        try:
            return PixelFormats.find_v4l2_fourcc(fourcc)
        except StopIteration:
            s = fourcc_to_str(fourcc)
            return PixelFormat(f'Unsupported<{s}>', None, s,
                               0, PixelColorEncoding.UNDEFINED, False,
                               0, [])

    @staticmethod
    def find_by_name(name):
        return next(v for v in PixelFormats.__dict__.values() if isinstance(v, PixelFormat) and v.name == name)

    # RGB

    RGB565 = PixelFormat('RGB565',
        'RG16', 'RGBP',
        16,
        PixelColorEncoding.RGB,
        False,
        1,
        ( ( 2, 1 ), ),
    )

    RGB888 = PixelFormat('RGB888',
        'RG24',     # DRM_FORMAT_RGB888
        'BGR3',     # V4L2_PIX_FMT_BGR24
        24,
        PixelColorEncoding.RGB,
        False,
        1,
        ( ( 3, 1 ), ),
    )
    BGR888 = PixelFormat('BGR888',
        'BG24',     # DRM_FORMAT_BGR888
        'RGB3',     # V4L2_PIX_FMT_RGB24
        24,
        PixelColorEncoding.RGB,
        False,
        1,
        ( ( 3, 1 ), ),
    )

    XRGB8888 = PixelFormat('XRGB8888',
        'XR24',     # DRM_FORMAT_XRGB8888
        'XR24',     # V4L2_PIX_FMT_XBGR32
        32,
        PixelColorEncoding.RGB,
        False,
        1,
        ( ( 4, 1 ), ),
    )
    XBGR8888 = PixelFormat('XBGR8888',
        'XB24',     # DRM_FORMAT_XBGR8888
        'XB24',     # V4L2_PIX_FMT_RGBX32
        32,
        PixelColorEncoding.RGB,
        False,
        1,
        ( ( 4, 1 ), ),
    )

    # YUV

    NV12 = PixelFormat('NV12',
        'NV12', 'NM12',
        12,
        PixelColorEncoding.YUV,
        False,
        2,
        ( ( 2, 1 ), ( 2, 2 ), ),
    )

    YUYV = PixelFormat('YUYV',
        'YUYV', 'YUYV',
        16,
        PixelColorEncoding.YUV,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    UYVY = PixelFormat('UYVY',
        'UYVY', 'UYVY',
        16,
        PixelColorEncoding.YUV,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    # YUV 4:4:4

    VUY888 = PixelFormat('VUY888',
        'VU24',     # DRM_FORMAT_VUY888
        'YUV3',     # V4L2_PIX_FMT_YUV24
        24,
        PixelColorEncoding.YUV,
        False,
        1,
        ( ( 3, 1 ), ),
    )

    XVUY8888 = PixelFormat('XVUY8888',
        'XVUY',     # DRM_FORMAT_XVUY8888
        'YUVX',     # V4L2_PIX_FMT_YUVX32
        32,
        PixelColorEncoding.YUV,
        False,
        1,
        ( ( 4, 1 ), ),
    )

    # Y8

    Y8 = PixelFormat('Y8',
        None, 'GREY',
        8,
        PixelColorEncoding.YUV,
        False,
        1,
        ( ( 1, 1 ), ),
    )

    # RAW

    SBGGR8 = PixelFormat('SBGGR8',
        None, 'BA81',
        8,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 2, 1 ), ),
    )

    SGBRG8 = PixelFormat('SGBRG8',
        None, 'GBRG',
        8,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 2, 1 ), ),
    )

    SGRBG8 = PixelFormat('SGRBG8',
        None, 'GRBG',
        8,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 2, 1 ), ),
    )

    SRGGB8 = PixelFormat('SRGGB8',
        None, 'RGGB',
        8,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 2, 1 ), ),
    )


    SRGGB10 = PixelFormat('SRGGB10',
        None, 'RG10',
        10,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    SBGGR10 = PixelFormat('SBGGR10',
        None, 'BG10',
        10,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    SRGGB10P = PixelFormat('SRGGB10P',
        None, 'pRAA',
        10,
        PixelColorEncoding.RAW,
        True,
        4,
        ( ( 5, 1 ), ),
    )

    SRGGB12 = PixelFormat('SRGGB12',
        None, 'RG12',
        12,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 4, 1 ), ),
    )

    SRGGB16 = PixelFormat('SRGGB16',
        None, 'RG16',
        16,
        PixelColorEncoding.RAW,
        False,
        2,
        ( ( 4, 1 ), ),
    )


class MetaFormat:
    def __init__(self, name: str, v4l2_fourcc: str, pixelspergroup: int, bytespergroup: int) -> None:
        self.name = name
        self.v4l2_fourcc = str_to_fourcc(v4l2_fourcc)
        self.pixelspergroup = pixelspergroup
        self.bytespergroup = bytespergroup

    def stride(self, width: int, align: int = 1):
        # ceil(width / pixelsPerGroup) * bytesPerGroup
        stride = (width + self.pixelspergroup - 1) // self.pixelspergroup * self.bytespergroup

        # ceil(stride / align) * align
        return (stride + align - 1) // align * align


class MetaFormats:
    @staticmethod
    def find_v4l2_fourcc(fourcc):
        return next(v for v in MetaFormats.__dict__.values() if isinstance(v, MetaFormat) and v.v4l2_fourcc == fourcc)

    @staticmethod
    def find_v4l2_fourcc_unsupported(fourcc):
        try:
            return MetaFormats.find_v4l2_fourcc(fourcc)
        except StopIteration:
            s = fourcc_to_str(fourcc)
            return MetaFormat(f'Unsupported<{s}>', s, 0, 0)

    GENERIC_8 = MetaFormat('GENERIC_8', 'MET8', 2, 2)
    GENERIC_CSI2_10 = MetaFormat('GENERIC_CSI2_10', 'MC1A', 4, 5)
    GENERIC_CSI2_12 = MetaFormat('GENERIC_CSI2_12', 'MC1C', 2, 3)

    RPI_FE_CFG = MetaFormat('RPI_FE_CFG', 'RPFC', 1, 1)
    RPI_FE_STATS = MetaFormat('RPI_FE_STATS', 'RPFS', 1, 1)

    # XXX deprecated rpi format
    SENSOR_DATA = MetaFormat('SENSOR_DATA', 'SENS', 1, 1)
