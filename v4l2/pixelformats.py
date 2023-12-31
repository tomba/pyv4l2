from __future__ import annotations

from enum import Enum, IntEnum
from typing import NamedTuple
import v4l2.uapi

__all__ = [ 'PixelFormat', 'MetaFormat' ]

# str.join('\n', [f'    {e[13:]} = v4l2.uapi.{e}' for e in v4l2.uapi.__dir__() if e.startswith("V4L2_PIX_FMT_")])

class PixelFormat(IntEnum):
    RGB332 = v4l2.uapi.V4L2_PIX_FMT_RGB332
    RGB444 = v4l2.uapi.V4L2_PIX_FMT_RGB444
    ARGB444 = v4l2.uapi.V4L2_PIX_FMT_ARGB444
    XRGB444 = v4l2.uapi.V4L2_PIX_FMT_XRGB444
    RGBA444 = v4l2.uapi.V4L2_PIX_FMT_RGBA444
    RGBX444 = v4l2.uapi.V4L2_PIX_FMT_RGBX444
    ABGR444 = v4l2.uapi.V4L2_PIX_FMT_ABGR444
    XBGR444 = v4l2.uapi.V4L2_PIX_FMT_XBGR444
    BGRA444 = v4l2.uapi.V4L2_PIX_FMT_BGRA444
    BGRX444 = v4l2.uapi.V4L2_PIX_FMT_BGRX444
    RGB555 = v4l2.uapi.V4L2_PIX_FMT_RGB555
    ARGB555 = v4l2.uapi.V4L2_PIX_FMT_ARGB555
    XRGB555 = v4l2.uapi.V4L2_PIX_FMT_XRGB555
    RGBA555 = v4l2.uapi.V4L2_PIX_FMT_RGBA555
    RGBX555 = v4l2.uapi.V4L2_PIX_FMT_RGBX555
    ABGR555 = v4l2.uapi.V4L2_PIX_FMT_ABGR555
    XBGR555 = v4l2.uapi.V4L2_PIX_FMT_XBGR555
    BGRA555 = v4l2.uapi.V4L2_PIX_FMT_BGRA555
    BGRX555 = v4l2.uapi.V4L2_PIX_FMT_BGRX555
    RGB565 = v4l2.uapi.V4L2_PIX_FMT_RGB565
    RGB555X = v4l2.uapi.V4L2_PIX_FMT_RGB555X
    ARGB555X = v4l2.uapi.V4L2_PIX_FMT_ARGB555X
    XRGB555X = v4l2.uapi.V4L2_PIX_FMT_XRGB555X
    RGB565X = v4l2.uapi.V4L2_PIX_FMT_RGB565X
    BGR666 = v4l2.uapi.V4L2_PIX_FMT_BGR666
    BGR24 = v4l2.uapi.V4L2_PIX_FMT_BGR24
    RGB24 = v4l2.uapi.V4L2_PIX_FMT_RGB24
    BGR32 = v4l2.uapi.V4L2_PIX_FMT_BGR32
    ABGR32 = v4l2.uapi.V4L2_PIX_FMT_ABGR32
    XBGR32 = v4l2.uapi.V4L2_PIX_FMT_XBGR32
    BGRA32 = v4l2.uapi.V4L2_PIX_FMT_BGRA32
    BGRX32 = v4l2.uapi.V4L2_PIX_FMT_BGRX32
    RGB32 = v4l2.uapi.V4L2_PIX_FMT_RGB32
    RGBA32 = v4l2.uapi.V4L2_PIX_FMT_RGBA32
    RGBX32 = v4l2.uapi.V4L2_PIX_FMT_RGBX32
    ARGB32 = v4l2.uapi.V4L2_PIX_FMT_ARGB32
    XRGB32 = v4l2.uapi.V4L2_PIX_FMT_XRGB32
    RGBX1010102 = v4l2.uapi.V4L2_PIX_FMT_RGBX1010102
    RGBA1010102 = v4l2.uapi.V4L2_PIX_FMT_RGBA1010102
    ARGB2101010 = v4l2.uapi.V4L2_PIX_FMT_ARGB2101010
    BGR48_12 = v4l2.uapi.V4L2_PIX_FMT_BGR48_12
    ABGR64_12 = v4l2.uapi.V4L2_PIX_FMT_ABGR64_12
    GREY = v4l2.uapi.V4L2_PIX_FMT_GREY
    Y4 = v4l2.uapi.V4L2_PIX_FMT_Y4
    Y6 = v4l2.uapi.V4L2_PIX_FMT_Y6
    Y10 = v4l2.uapi.V4L2_PIX_FMT_Y10
    Y12 = v4l2.uapi.V4L2_PIX_FMT_Y12
    Y012 = v4l2.uapi.V4L2_PIX_FMT_Y012
    Y14 = v4l2.uapi.V4L2_PIX_FMT_Y14
    Y16 = v4l2.uapi.V4L2_PIX_FMT_Y16
    Y16_BE = v4l2.uapi.V4L2_PIX_FMT_Y16_BE
    Y10BPACK = v4l2.uapi.V4L2_PIX_FMT_Y10BPACK
    Y10P = v4l2.uapi.V4L2_PIX_FMT_Y10P
    IPU3_Y10 = v4l2.uapi.V4L2_PIX_FMT_IPU3_Y10
    PAL8 = v4l2.uapi.V4L2_PIX_FMT_PAL8
    UV8 = v4l2.uapi.V4L2_PIX_FMT_UV8
    YUYV = v4l2.uapi.V4L2_PIX_FMT_YUYV
    YYUV = v4l2.uapi.V4L2_PIX_FMT_YYUV
    YVYU = v4l2.uapi.V4L2_PIX_FMT_YVYU
    UYVY = v4l2.uapi.V4L2_PIX_FMT_UYVY
    VYUY = v4l2.uapi.V4L2_PIX_FMT_VYUY
    Y41P = v4l2.uapi.V4L2_PIX_FMT_Y41P
    YUV444 = v4l2.uapi.V4L2_PIX_FMT_YUV444
    YUV555 = v4l2.uapi.V4L2_PIX_FMT_YUV555
    YUV565 = v4l2.uapi.V4L2_PIX_FMT_YUV565
    YUV24 = v4l2.uapi.V4L2_PIX_FMT_YUV24
    YUV32 = v4l2.uapi.V4L2_PIX_FMT_YUV32
    AYUV32 = v4l2.uapi.V4L2_PIX_FMT_AYUV32
    XYUV32 = v4l2.uapi.V4L2_PIX_FMT_XYUV32
    VUYA32 = v4l2.uapi.V4L2_PIX_FMT_VUYA32
    VUYX32 = v4l2.uapi.V4L2_PIX_FMT_VUYX32
    YUVA32 = v4l2.uapi.V4L2_PIX_FMT_YUVA32
    YUVX32 = v4l2.uapi.V4L2_PIX_FMT_YUVX32
    M420 = v4l2.uapi.V4L2_PIX_FMT_M420
    YUV48_12 = v4l2.uapi.V4L2_PIX_FMT_YUV48_12
    Y210 = v4l2.uapi.V4L2_PIX_FMT_Y210
    Y212 = v4l2.uapi.V4L2_PIX_FMT_Y212
    Y216 = v4l2.uapi.V4L2_PIX_FMT_Y216
    NV12 = v4l2.uapi.V4L2_PIX_FMT_NV12
    NV21 = v4l2.uapi.V4L2_PIX_FMT_NV21
    NV16 = v4l2.uapi.V4L2_PIX_FMT_NV16
    NV61 = v4l2.uapi.V4L2_PIX_FMT_NV61
    NV24 = v4l2.uapi.V4L2_PIX_FMT_NV24
    NV42 = v4l2.uapi.V4L2_PIX_FMT_NV42
    P010 = v4l2.uapi.V4L2_PIX_FMT_P010
    P012 = v4l2.uapi.V4L2_PIX_FMT_P012
    NV12M = v4l2.uapi.V4L2_PIX_FMT_NV12M
    NV21M = v4l2.uapi.V4L2_PIX_FMT_NV21M
    NV16M = v4l2.uapi.V4L2_PIX_FMT_NV16M
    NV61M = v4l2.uapi.V4L2_PIX_FMT_NV61M
    P012M = v4l2.uapi.V4L2_PIX_FMT_P012M
    YUV410 = v4l2.uapi.V4L2_PIX_FMT_YUV410
    YVU410 = v4l2.uapi.V4L2_PIX_FMT_YVU410
    YUV411P = v4l2.uapi.V4L2_PIX_FMT_YUV411P
    YUV420 = v4l2.uapi.V4L2_PIX_FMT_YUV420
    YVU420 = v4l2.uapi.V4L2_PIX_FMT_YVU420
    YUV422P = v4l2.uapi.V4L2_PIX_FMT_YUV422P
    YUV420M = v4l2.uapi.V4L2_PIX_FMT_YUV420M
    YVU420M = v4l2.uapi.V4L2_PIX_FMT_YVU420M
    YUV422M = v4l2.uapi.V4L2_PIX_FMT_YUV422M
    YVU422M = v4l2.uapi.V4L2_PIX_FMT_YVU422M
    YUV444M = v4l2.uapi.V4L2_PIX_FMT_YUV444M
    YVU444M = v4l2.uapi.V4L2_PIX_FMT_YVU444M
    NV12_4L4 = v4l2.uapi.V4L2_PIX_FMT_NV12_4L4
    NV12_16L16 = v4l2.uapi.V4L2_PIX_FMT_NV12_16L16
    NV12_32L32 = v4l2.uapi.V4L2_PIX_FMT_NV12_32L32
    NV15_4L4 = v4l2.uapi.V4L2_PIX_FMT_NV15_4L4
    P010_4L4 = v4l2.uapi.V4L2_PIX_FMT_P010_4L4
    NV12_8L128 = v4l2.uapi.V4L2_PIX_FMT_NV12_8L128
    NV12_10BE_8L128 = v4l2.uapi.V4L2_PIX_FMT_NV12_10BE_8L128
    NV12MT = v4l2.uapi.V4L2_PIX_FMT_NV12MT
    NV12MT_16X16 = v4l2.uapi.V4L2_PIX_FMT_NV12MT_16X16
    NV12M_8L128 = v4l2.uapi.V4L2_PIX_FMT_NV12M_8L128
    NV12M_10BE_8L128 = v4l2.uapi.V4L2_PIX_FMT_NV12M_10BE_8L128
    SBGGR8 = v4l2.uapi.V4L2_PIX_FMT_SBGGR8
    SGBRG8 = v4l2.uapi.V4L2_PIX_FMT_SGBRG8
    SGRBG8 = v4l2.uapi.V4L2_PIX_FMT_SGRBG8
    SRGGB8 = v4l2.uapi.V4L2_PIX_FMT_SRGGB8
    SBGGR10 = v4l2.uapi.V4L2_PIX_FMT_SBGGR10
    SGBRG10 = v4l2.uapi.V4L2_PIX_FMT_SGBRG10
    SGRBG10 = v4l2.uapi.V4L2_PIX_FMT_SGRBG10
    SRGGB10 = v4l2.uapi.V4L2_PIX_FMT_SRGGB10
    SBGGR10P = v4l2.uapi.V4L2_PIX_FMT_SBGGR10P
    SGBRG10P = v4l2.uapi.V4L2_PIX_FMT_SGBRG10P
    SGRBG10P = v4l2.uapi.V4L2_PIX_FMT_SGRBG10P
    SRGGB10P = v4l2.uapi.V4L2_PIX_FMT_SRGGB10P
    SBGGR10ALAW8 = v4l2.uapi.V4L2_PIX_FMT_SBGGR10ALAW8
    SGBRG10ALAW8 = v4l2.uapi.V4L2_PIX_FMT_SGBRG10ALAW8
    SGRBG10ALAW8 = v4l2.uapi.V4L2_PIX_FMT_SGRBG10ALAW8
    SRGGB10ALAW8 = v4l2.uapi.V4L2_PIX_FMT_SRGGB10ALAW8
    SBGGR10DPCM8 = v4l2.uapi.V4L2_PIX_FMT_SBGGR10DPCM8
    SGBRG10DPCM8 = v4l2.uapi.V4L2_PIX_FMT_SGBRG10DPCM8
    SGRBG10DPCM8 = v4l2.uapi.V4L2_PIX_FMT_SGRBG10DPCM8
    SRGGB10DPCM8 = v4l2.uapi.V4L2_PIX_FMT_SRGGB10DPCM8
    SBGGR12 = v4l2.uapi.V4L2_PIX_FMT_SBGGR12
    SGBRG12 = v4l2.uapi.V4L2_PIX_FMT_SGBRG12
    SGRBG12 = v4l2.uapi.V4L2_PIX_FMT_SGRBG12
    SRGGB12 = v4l2.uapi.V4L2_PIX_FMT_SRGGB12
    SBGGR12P = v4l2.uapi.V4L2_PIX_FMT_SBGGR12P
    SGBRG12P = v4l2.uapi.V4L2_PIX_FMT_SGBRG12P
    SGRBG12P = v4l2.uapi.V4L2_PIX_FMT_SGRBG12P
    SRGGB12P = v4l2.uapi.V4L2_PIX_FMT_SRGGB12P
    SBGGR14 = v4l2.uapi.V4L2_PIX_FMT_SBGGR14
    SGBRG14 = v4l2.uapi.V4L2_PIX_FMT_SGBRG14
    SGRBG14 = v4l2.uapi.V4L2_PIX_FMT_SGRBG14
    SRGGB14 = v4l2.uapi.V4L2_PIX_FMT_SRGGB14
    SBGGR14P = v4l2.uapi.V4L2_PIX_FMT_SBGGR14P
    SGBRG14P = v4l2.uapi.V4L2_PIX_FMT_SGBRG14P
    SGRBG14P = v4l2.uapi.V4L2_PIX_FMT_SGRBG14P
    SRGGB14P = v4l2.uapi.V4L2_PIX_FMT_SRGGB14P
    SBGGR16 = v4l2.uapi.V4L2_PIX_FMT_SBGGR16
    SGBRG16 = v4l2.uapi.V4L2_PIX_FMT_SGBRG16
    SGRBG16 = v4l2.uapi.V4L2_PIX_FMT_SGRBG16
    SRGGB16 = v4l2.uapi.V4L2_PIX_FMT_SRGGB16
    HSV24 = v4l2.uapi.V4L2_PIX_FMT_HSV24
    HSV32 = v4l2.uapi.V4L2_PIX_FMT_HSV32
    MJPEG = v4l2.uapi.V4L2_PIX_FMT_MJPEG
    JPEG = v4l2.uapi.V4L2_PIX_FMT_JPEG
    DV = v4l2.uapi.V4L2_PIX_FMT_DV
    MPEG = v4l2.uapi.V4L2_PIX_FMT_MPEG
    H264 = v4l2.uapi.V4L2_PIX_FMT_H264
    H264_NO_SC = v4l2.uapi.V4L2_PIX_FMT_H264_NO_SC
    H264_MVC = v4l2.uapi.V4L2_PIX_FMT_H264_MVC
    H263 = v4l2.uapi.V4L2_PIX_FMT_H263
    MPEG1 = v4l2.uapi.V4L2_PIX_FMT_MPEG1
    MPEG2 = v4l2.uapi.V4L2_PIX_FMT_MPEG2
    MPEG2_SLICE = v4l2.uapi.V4L2_PIX_FMT_MPEG2_SLICE
    MPEG4 = v4l2.uapi.V4L2_PIX_FMT_MPEG4
    XVID = v4l2.uapi.V4L2_PIX_FMT_XVID
    VC1_ANNEX_G = v4l2.uapi.V4L2_PIX_FMT_VC1_ANNEX_G
    VC1_ANNEX_L = v4l2.uapi.V4L2_PIX_FMT_VC1_ANNEX_L
    VP8 = v4l2.uapi.V4L2_PIX_FMT_VP8
    VP8_FRAME = v4l2.uapi.V4L2_PIX_FMT_VP8_FRAME
    VP9 = v4l2.uapi.V4L2_PIX_FMT_VP9
    VP9_FRAME = v4l2.uapi.V4L2_PIX_FMT_VP9_FRAME
    HEVC = v4l2.uapi.V4L2_PIX_FMT_HEVC
    FWHT = v4l2.uapi.V4L2_PIX_FMT_FWHT
    FWHT_STATELESS = v4l2.uapi.V4L2_PIX_FMT_FWHT_STATELESS
    H264_SLICE = v4l2.uapi.V4L2_PIX_FMT_H264_SLICE
    HEVC_SLICE = v4l2.uapi.V4L2_PIX_FMT_HEVC_SLICE
    AV1_FRAME = v4l2.uapi.V4L2_PIX_FMT_AV1_FRAME
    SPK = v4l2.uapi.V4L2_PIX_FMT_SPK
    RV30 = v4l2.uapi.V4L2_PIX_FMT_RV30
    RV40 = v4l2.uapi.V4L2_PIX_FMT_RV40
    CPIA1 = v4l2.uapi.V4L2_PIX_FMT_CPIA1
    WNVA = v4l2.uapi.V4L2_PIX_FMT_WNVA
    SN9C10X = v4l2.uapi.V4L2_PIX_FMT_SN9C10X
    SN9C20X_I420 = v4l2.uapi.V4L2_PIX_FMT_SN9C20X_I420
    PWC1 = v4l2.uapi.V4L2_PIX_FMT_PWC1
    PWC2 = v4l2.uapi.V4L2_PIX_FMT_PWC2
    ET61X251 = v4l2.uapi.V4L2_PIX_FMT_ET61X251
    SPCA501 = v4l2.uapi.V4L2_PIX_FMT_SPCA501
    SPCA505 = v4l2.uapi.V4L2_PIX_FMT_SPCA505
    SPCA508 = v4l2.uapi.V4L2_PIX_FMT_SPCA508
    SPCA561 = v4l2.uapi.V4L2_PIX_FMT_SPCA561
    PAC207 = v4l2.uapi.V4L2_PIX_FMT_PAC207
    MR97310A = v4l2.uapi.V4L2_PIX_FMT_MR97310A
    JL2005BCD = v4l2.uapi.V4L2_PIX_FMT_JL2005BCD
    SN9C2028 = v4l2.uapi.V4L2_PIX_FMT_SN9C2028
    SQ905C = v4l2.uapi.V4L2_PIX_FMT_SQ905C
    PJPG = v4l2.uapi.V4L2_PIX_FMT_PJPG
    OV511 = v4l2.uapi.V4L2_PIX_FMT_OV511
    OV518 = v4l2.uapi.V4L2_PIX_FMT_OV518
    STV0680 = v4l2.uapi.V4L2_PIX_FMT_STV0680
    TM6000 = v4l2.uapi.V4L2_PIX_FMT_TM6000
    CIT_YYVYUY = v4l2.uapi.V4L2_PIX_FMT_CIT_YYVYUY
    KONICA420 = v4l2.uapi.V4L2_PIX_FMT_KONICA420
    JPGL = v4l2.uapi.V4L2_PIX_FMT_JPGL
    SE401 = v4l2.uapi.V4L2_PIX_FMT_SE401
    S5C_UYVY_JPG = v4l2.uapi.V4L2_PIX_FMT_S5C_UYVY_JPG
    Y8I = v4l2.uapi.V4L2_PIX_FMT_Y8I
    Y12I = v4l2.uapi.V4L2_PIX_FMT_Y12I
    Z16 = v4l2.uapi.V4L2_PIX_FMT_Z16
    MT21C = v4l2.uapi.V4L2_PIX_FMT_MT21C
    MM21 = v4l2.uapi.V4L2_PIX_FMT_MM21
    MT2110T = v4l2.uapi.V4L2_PIX_FMT_MT2110T
    MT2110R = v4l2.uapi.V4L2_PIX_FMT_MT2110R
    INZI = v4l2.uapi.V4L2_PIX_FMT_INZI
    CNF4 = v4l2.uapi.V4L2_PIX_FMT_CNF4
    HI240 = v4l2.uapi.V4L2_PIX_FMT_HI240
    QC08C = v4l2.uapi.V4L2_PIX_FMT_QC08C
    QC10C = v4l2.uapi.V4L2_PIX_FMT_QC10C
    AJPG = v4l2.uapi.V4L2_PIX_FMT_AJPG
    HEXTILE = v4l2.uapi.V4L2_PIX_FMT_HEXTILE
    IPU3_SBGGR10 = v4l2.uapi.V4L2_PIX_FMT_IPU3_SBGGR10
    IPU3_SGBRG10 = v4l2.uapi.V4L2_PIX_FMT_IPU3_SGBRG10
    IPU3_SGRBG10 = v4l2.uapi.V4L2_PIX_FMT_IPU3_SGRBG10
    IPU3_SRGGB10 = v4l2.uapi.V4L2_PIX_FMT_IPU3_SRGGB10
    PRIV_MAGIC = v4l2.uapi.V4L2_PIX_FMT_PRIV_MAGIC
    FLAG_PREMUL_ALPHA = v4l2.uapi.V4L2_PIX_FMT_FLAG_PREMUL_ALPHA
    FLAG_SET_CSC = v4l2.uapi.V4L2_PIX_FMT_FLAG_SET_CSC
    HM12 = v4l2.uapi.V4L2_PIX_FMT_HM12
    SUNXI_TILED_NV12 = v4l2.uapi.V4L2_PIX_FMT_SUNXI_TILED_NV12

# XXX Manually added
class MetaFormat(IntEnum):
    GENERIC_8 = v4l2.uapi.v4l2_fourcc('M', 'E', 'T', '8')
    GENERIC_CSI2_10 = v4l2.uapi.v4l2_fourcc('M', 'C', '1', 'A')
    GENERIC_CSI2_12 = v4l2.uapi.v4l2_fourcc('M', 'C', '1', 'C')
    # XXX deprecated rpi format
    SENSOR_DATA = v4l2.uapi.v4l2_fourcc('S', 'E', 'N', 'S')

class PixelFormatPlaneInfo(NamedTuple):
    bitspp: int
    xsub: int
    ysub: int

class PixelFormatInfo:
    fourcc: int
    name: str
    colortype: int
    planes: list[PixelFormatPlaneInfo]

    def __init__(self, data) -> None:
        self.fourcc = data[0]
        self.name = data[0].name
        self.colortype = data[1]
        self.planes = [PixelFormatPlaneInfo(*t) for t in data[2]]

    def __repr__(self) -> str:
        return f'PixelFormatInfo({self.fourcc:#8x}, {self.name}, {self.colortype}, {self.planes})'

class PixelColorType(Enum):
    RGB = 0
    YUV = 1
    RAW = 2
    UNDEFINED = 3

formats = (
    # YUV packed
    ( PixelFormat.UYVY,
                     PixelColorType.YUV,
                     ( ( 16, 2, 1 ), ),
                 ),
    ( PixelFormat.YUYV,
                     PixelColorType.YUV,
                     ( ( 16, 2, 1 ), ),
                 ),
    ( PixelFormat.YVYU,
                     PixelColorType.YUV,
                     ( ( 16, 2, 1 ), ),
                 ),
    ( PixelFormat.VYUY,
                     PixelColorType.YUV,
                     ( ( 16, 2, 1 ), ),
                 ),
    # YUV semi-planar
    ( PixelFormat.NV12,
                     PixelColorType.YUV,
                     ( ( 8, 1, 1 ),
                       ( 8, 2, 2 ), ),
                 ),
    ( PixelFormat.NV21,
                     PixelColorType.YUV,
                     ( ( 8, 1, 1 ),
                       ( 8, 2, 2 ), ),
                 ),
    ( PixelFormat.NV16,
                     PixelColorType.YUV,
                     ( ( 8, 1, 1 ),
                       ( 8, 2, 1 ), ),
                 ),
    ( PixelFormat.NV61,
                     PixelColorType.YUV,
                     ( ( 8, 1, 1 ),
                       ( 8, 2, 1 ), ),
                 ),
    # RGB16
    ( PixelFormat.RGB565,
                       PixelColorType.RGB,
                       ( ( 16, 1, 1 ), ),
                   ),
#    # RGB24
#    ( PixelFormat.RGB888,
#                       PixelColorType.RGB,
#                       ( ( 24, 1, 1 ), ),
#                   ),
#    # RGB32
#    ( PixelFormat.XRGB8888,
#                     PixelColorType.RGB,
#                     ( ( 32, 1, 1 ), ),
#                 ),
    ( PixelFormat.SBGGR8,
                       PixelColorType.RAW,
                       ( ( 8, 1, 1 ), ),
                   ),
    ( PixelFormat.SGBRG8,
                       PixelColorType.RAW,
                       ( ( 8, 1, 1 ), ),
                   ),
    ( PixelFormat.SGRBG8,
                       PixelColorType.RAW,
                       ( ( 8, 1, 1 ), ),
                   ),
    ( PixelFormat.SRGGB8,
                       PixelColorType.RAW,
                       ( ( 8, 1, 1 ), ),
                   ),
    ( PixelFormat.SRGGB10,
                    PixelColorType.RAW,
                    ( ( 16, 1, 1 ), ),
                ),
    ( PixelFormat.SRGGB10P,
                     PixelColorType.RAW,
                     ( ( 10, 1, 1 ), ),
                 ),
    ( PixelFormat.SBGGR12,
                    PixelColorType.RAW,
                    ( ( 16, 1, 1 ), ),
                ),
    ( PixelFormat.SRGGB12,
                    PixelColorType.RAW,
                    ( ( 16, 1, 1 ), ),
                ),
    ( PixelFormat.SRGGB16,
                    PixelColorType.RAW,
                    ( ( 16, 1, 1 ), ),
                ),
#    ( PixelFormat.Y8,
#                   PixelColorType.YUV,
#                   ( ( 8, 1, 1 ), ),
#               ),
    ( MetaFormat.GENERIC_8,
                       PixelColorType.UNDEFINED,
                       ( ( 8, 1, 1 ), ),
                   ),
    ( MetaFormat.GENERIC_CSI2_10,
                         PixelColorType.UNDEFINED,
                         ( ( 10, 1, 1 ), ),
                     ),
    ( MetaFormat.GENERIC_CSI2_12,
                         PixelColorType.UNDEFINED,
                         ( ( 12, 1, 1 ), ),
                     ),
    ( MetaFormat.SENSOR_DATA,
                        PixelColorType.UNDEFINED,
                        ( ( 8, 1, 1 ), ),
                    ),
)

def get_pixel_format_info(fourcc) -> PixelFormatInfo:
    for p in formats:
        if p[0] == fourcc:
            info = PixelFormatInfo(p)
            return info

    raise Exception("Pixel format not found")
