r"""Wrapper for pisp_statistics.h

Generated with:
/home/tomba/work/ctypesgen/run.py --no-embed-preamble --no-macro-try-except --no-source-comments -D__volatile__= -D__signed__= -U__SIZEOF_INT128__ -I/home/tomba/work/libpisp/src/libpisp -o pisp/pisp.py /home/tomba/work/libpisp/src/libpisp/frontend/pisp_statistics.h /home/tomba/work/libpisp/src/libpisp/frontend/pisp_fe_config.h

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

from .ctypes_preamble import *
from .ctypes_preamble import _variadic_function

# End preamble

# No libraries

# No modules

__uint8_t = c_ubyte

__uint16_t = c_ushort

__uint32_t = c_uint

__uint64_t = c_ulong

uint8_t = __uint8_t

uint16_t = __uint16_t

uint32_t = __uint32_t

uint64_t = __uint64_t


class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'Y_sum',
    'counted',
    'pad',
]
struct_anon_2._fields_ = [
    ('Y_sum', uint64_t),
    ('counted', uint32_t),
    ('pad', uint32_t),
]

pisp_agc_statistics_zone = struct_anon_2


class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'row_sums',
    'histogram',
    'floating',
]
struct_anon_3._fields_ = [
    ('row_sums', uint32_t * int(512)),
    ('histogram', uint32_t * int(1024)),
    ('floating', pisp_agc_statistics_zone * int(4)),
]

pisp_agc_statistics = struct_anon_3


class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'R_sum',
    'G_sum',
    'B_sum',
    'counted',
]
struct_anon_4._fields_ = [
    ('R_sum', uint32_t),
    ('G_sum', uint32_t),
    ('B_sum', uint32_t),
    ('counted', uint32_t),
]

pisp_awb_statistics_zone = struct_anon_4


class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'zones',
    'floating',
]
struct_anon_5._fields_ = [
    ('zones', pisp_awb_statistics_zone * int((32 * 32))),
    ('floating', pisp_awb_statistics_zone * int(4)),
]

pisp_awb_statistics = struct_anon_5


class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'foms',
    'floating',
]
struct_anon_6._fields_ = [
    ('foms', uint64_t * int((8 * 8))),
    ('floating', uint64_t * int(4)),
]

pisp_cdaf_statistics = struct_anon_6


class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'awb',
    'agc',
    'cdaf',
]
struct_anon_7._fields_ = [
    ('awb', pisp_awb_statistics),
    ('agc', pisp_agc_statistics),
    ('cdaf', pisp_cdaf_statistics),
]

pisp_statistics = struct_anon_7


class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'width',
    'height',
    'format',
    'stride',
    'stride2',
]
struct_anon_26._fields_ = [
    ('width', uint16_t),
    ('height', uint16_t),
    ('format', uint32_t),
    ('stride', c_int32),
    ('stride2', c_int32),
]

pisp_image_format_config = struct_anon_26


class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'black_level_r',
    'black_level_gr',
    'black_level_gb',
    'black_level_b',
    'output_black_level',
    'pad',
]
struct_anon_30._fields_ = [
    ('black_level_r', uint16_t),
    ('black_level_gr', uint16_t),
    ('black_level_gb', uint16_t),
    ('black_level_b', uint16_t),
    ('output_black_level', uint16_t),
    ('pad', uint8_t * int(2)),
]

pisp_bla_config = struct_anon_30


class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'offset',
    'pad',
    'mode',
]
struct_anon_32._fields_ = [
    ('offset', uint16_t),
    ('pad', uint8_t),
    ('mode', uint8_t),
]

pisp_compress_config = struct_anon_32


class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'offset',
    'pad',
    'mode',
]
struct_anon_33._fields_ = [
    ('offset', uint16_t),
    ('pad', uint8_t),
    ('mode', uint8_t),
]

pisp_decompress_config = struct_anon_33

enum_anon_36 = c_int

PISP_FE_ENABLE_INPUT = 0x000001

PISP_FE_ENABLE_DECOMPRESS = 0x000002

PISP_FE_ENABLE_DECOMPAND = 0x000004

PISP_FE_ENABLE_BLA = 0x000008

PISP_FE_ENABLE_DPC = 0x000010

PISP_FE_ENABLE_STATS_CROP = 0x000020

PISP_FE_ENABLE_DECIMATE = 0x000040

PISP_FE_ENABLE_BLC = 0x000080

PISP_FE_ENABLE_CDAF_STATS = 0x000100

PISP_FE_ENABLE_AWB_STATS = 0x000200

PISP_FE_ENABLE_RGBY = 0x000400

PISP_FE_ENABLE_LSC = 0x000800

PISP_FE_ENABLE_AGC_STATS = 0x001000

PISP_FE_ENABLE_CROP0 = 0x010000

PISP_FE_ENABLE_DOWNSCALE0 = 0x020000

PISP_FE_ENABLE_COMPRESS0 = 0x040000

PISP_FE_ENABLE_OUTPUT0 = 0x080000

PISP_FE_ENABLE_CROP1 = 0x100000

PISP_FE_ENABLE_DOWNSCALE1 = 0x200000

PISP_FE_ENABLE_COMPRESS1 = 0x400000

PISP_FE_ENABLE_OUTPUT1 = 0x800000

pisp_fe_enable = enum_anon_36

enum_anon_37 = c_int

PISP_FE_DIRTY_GLOBAL = 0x0001

PISP_FE_DIRTY_FLOATING = 0x0002

PISP_FE_DIRTY_OUTPUT_AXI = 0x0004

pisp_fe_dirty = enum_anon_37


class struct_anon_38(Structure):
    pass

struct_anon_38.__slots__ = [
    'enables',
    'bayer_order',
    'pad',
]
struct_anon_38._fields_ = [
    ('enables', uint32_t),
    ('bayer_order', uint8_t),
    ('pad', uint8_t * int(3)),
]

pisp_fe_global_config = struct_anon_38


class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'maxlen_flags',
    'cache_prot',
    'qos',
]
struct_anon_39._fields_ = [
    ('maxlen_flags', uint8_t),
    ('cache_prot', uint8_t),
    ('qos', uint16_t),
]

pisp_fe_input_axi_config = struct_anon_39


class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'maxlen_flags',
    'cache_prot',
    'qos',
    'thresh',
    'throttle',
]
struct_anon_40._fields_ = [
    ('maxlen_flags', uint8_t),
    ('cache_prot', uint8_t),
    ('qos', uint16_t),
    ('thresh', uint16_t),
    ('throttle', uint16_t),
]

pisp_fe_output_axi_config = struct_anon_40


class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'streaming',
    'pad',
    'format',
    'axi',
    'holdoff',
    'pad2',
]
struct_anon_41._fields_ = [
    ('streaming', uint8_t),
    ('pad', uint8_t * int(3)),
    ('format', pisp_image_format_config),
    ('axi', pisp_fe_input_axi_config),
    ('holdoff', uint8_t),
    ('pad2', uint8_t * int(3)),
]

pisp_fe_input_config = struct_anon_41


class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    'format',
    'ilines',
    'pad',
]
struct_anon_42._fields_ = [
    ('format', pisp_image_format_config),
    ('ilines', uint16_t),
    ('pad', uint8_t * int(2)),
]

pisp_fe_output_config = struct_anon_42


class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'addr_lo',
    'addr_hi',
    'frame_id',
    'pad',
]
struct_anon_43._fields_ = [
    ('addr_lo', uint32_t),
    ('addr_hi', uint32_t),
    ('frame_id', uint16_t),
    ('pad', uint16_t),
]

pisp_fe_input_buffer_config = struct_anon_43


class struct_anon_44(Structure):
    pass

struct_anon_44.__slots__ = [
    'lut',
    'pad',
]
struct_anon_44._fields_ = [
    ('lut', uint16_t * int(65)),
    ('pad', uint16_t),
]

pisp_fe_decompand_config = struct_anon_44


class struct_anon_45(Structure):
    pass

struct_anon_45.__slots__ = [
    'coeff_level',
    'coeff_range',
    'coeff_range2',
    'flags',
]
struct_anon_45._fields_ = [
    ('coeff_level', uint8_t),
    ('coeff_range', uint8_t),
    ('coeff_range2', uint8_t),
    ('flags', uint8_t),
]

pisp_fe_dpc_config = struct_anon_45


class struct_anon_46(Structure):
    pass

struct_anon_46.__slots__ = [
    'shift',
    'pad0',
    'scale',
    'centre_x',
    'centre_y',
    'lut',
]
struct_anon_46._fields_ = [
    ('shift', uint8_t),
    ('pad0', uint8_t),
    ('scale', uint16_t),
    ('centre_x', uint16_t),
    ('centre_y', uint16_t),
    ('lut', uint16_t * int(16)),
]

pisp_fe_lsc_config = struct_anon_46


class struct_anon_47(Structure):
    pass

struct_anon_47.__slots__ = [
    'gain_r',
    'gain_g',
    'gain_b',
    'maxflag',
    'pad',
]
struct_anon_47._fields_ = [
    ('gain_r', uint16_t),
    ('gain_g', uint16_t),
    ('gain_b', uint16_t),
    ('maxflag', uint8_t),
    ('pad', uint8_t),
]

pisp_fe_rgby_config = struct_anon_47


class struct_anon_48(Structure):
    pass

struct_anon_48.__slots__ = [
    'offset_x',
    'offset_y',
    'size_x',
    'size_y',
    'weights',
    'row_offset_x',
    'row_offset_y',
    'row_size_x',
    'row_size_y',
    'row_shift',
    'float_shift',
    'pad1',
]
struct_anon_48._fields_ = [
    ('offset_x', uint16_t),
    ('offset_y', uint16_t),
    ('size_x', uint16_t),
    ('size_y', uint16_t),
    ('weights', uint8_t * int(((16 * 16) / 2))),
    ('row_offset_x', uint16_t),
    ('row_offset_y', uint16_t),
    ('row_size_x', uint16_t),
    ('row_size_y', uint16_t),
    ('row_shift', uint8_t),
    ('float_shift', uint8_t),
    ('pad1', uint8_t * int(2)),
]

pisp_fe_agc_stats_config = struct_anon_48


class struct_anon_49(Structure):
    pass

struct_anon_49.__slots__ = [
    'offset_x',
    'offset_y',
    'size_x',
    'size_y',
    'shift',
    'pad',
    'r_lo',
    'r_hi',
    'g_lo',
    'g_hi',
    'b_lo',
    'b_hi',
]
struct_anon_49._fields_ = [
    ('offset_x', uint16_t),
    ('offset_y', uint16_t),
    ('size_x', uint16_t),
    ('size_y', uint16_t),
    ('shift', uint8_t),
    ('pad', uint8_t * int(3)),
    ('r_lo', uint16_t),
    ('r_hi', uint16_t),
    ('g_lo', uint16_t),
    ('g_hi', uint16_t),
    ('b_lo', uint16_t),
    ('b_hi', uint16_t),
]

pisp_fe_awb_stats_config = struct_anon_49


class struct_anon_50(Structure):
    pass

struct_anon_50.__slots__ = [
    'offset_x',
    'offset_y',
    'size_x',
    'size_y',
]
struct_anon_50._fields_ = [
    ('offset_x', uint16_t),
    ('offset_y', uint16_t),
    ('size_x', uint16_t),
    ('size_y', uint16_t),
]

pisp_fe_floating_stats_region = struct_anon_50


class struct_anon_51(Structure):
    pass

struct_anon_51.__slots__ = [
    'regions',
]
struct_anon_51._fields_ = [
    ('regions', pisp_fe_floating_stats_region * int(4)),
]

pisp_fe_floating_stats_config = struct_anon_51


class struct_anon_52(Structure):
    pass

struct_anon_52.__slots__ = [
    'noise_constant',
    'noise_slope',
    'offset_x',
    'offset_y',
    'size_x',
    'size_y',
    'skip_x',
    'skip_y',
    'mode',
]
struct_anon_52._fields_ = [
    ('noise_constant', uint16_t),
    ('noise_slope', uint16_t),
    ('offset_x', uint16_t),
    ('offset_y', uint16_t),
    ('size_x', uint16_t),
    ('size_y', uint16_t),
    ('skip_x', uint16_t),
    ('skip_y', uint16_t),
    ('mode', uint32_t),
]

pisp_fe_cdaf_stats_config = struct_anon_52


class struct_anon_53(Structure):
    pass

struct_anon_53.__slots__ = [
    'addr_lo',
    'addr_hi',
]
struct_anon_53._fields_ = [
    ('addr_lo', uint32_t),
    ('addr_hi', uint32_t),
]

pisp_fe_stats_buffer_config = struct_anon_53


class struct_anon_54(Structure):
    pass

struct_anon_54.__slots__ = [
    'offset_x',
    'offset_y',
    'width',
    'height',
]
struct_anon_54._fields_ = [
    ('offset_x', uint16_t),
    ('offset_y', uint16_t),
    ('width', uint16_t),
    ('height', uint16_t),
]

pisp_fe_crop_config = struct_anon_54

enum_anon_55 = c_int

DOWNSCALE_BAYER = 1

DOWNSCALE_BIN = 2

pisp_fe_downscale_flags = enum_anon_55


class struct_anon_56(Structure):
    pass

struct_anon_56.__slots__ = [
    'xin',
    'xout',
    'yin',
    'yout',
    'flags',
    'pad',
    'output_width',
    'output_height',
]
struct_anon_56._fields_ = [
    ('xin', uint8_t),
    ('xout', uint8_t),
    ('yin', uint8_t),
    ('yout', uint8_t),
    ('flags', uint8_t),
    ('pad', uint8_t * int(3)),
    ('output_width', uint16_t),
    ('output_height', uint16_t),
]

pisp_fe_downscale_config = struct_anon_56


class struct_anon_57(Structure):
    pass

struct_anon_57.__slots__ = [
    'addr_lo',
    'addr_hi',
]
struct_anon_57._fields_ = [
    ('addr_lo', uint32_t),
    ('addr_hi', uint32_t),
]

pisp_fe_output_buffer_config = struct_anon_57


class struct_anon_58(Structure):
    pass

struct_anon_58.__slots__ = [
    'crop',
    'downscale',
    'compress',
    'output',
    'pad',
]
struct_anon_58._fields_ = [
    ('crop', pisp_fe_crop_config),
    ('downscale', pisp_fe_downscale_config),
    ('compress', pisp_compress_config),
    ('output', pisp_fe_output_config),
    ('pad', uint32_t),
]

pisp_fe_output_branch_config = struct_anon_58


class struct_anon_59(Structure):
    pass

struct_anon_59.__slots__ = [
    'stats_buffer',
    'output_buffer',
    'input_buffer',
    'global',
    'input',
    'decompress',
    'decompand',
    'bla',
    'dpc',
    'stats_crop',
    'spare1',
    'blc',
    'rgby',
    'lsc',
    'agc_stats',
    'awb_stats',
    'cdaf_stats',
    'floating_stats',
    'output_axi',
    'ch',
    'dirty_flags',
    'dirty_flags_extra',
]
struct_anon_59._fields_ = [
    ('stats_buffer', pisp_fe_stats_buffer_config),
    ('output_buffer', pisp_fe_output_buffer_config * int(2)),
    ('input_buffer', pisp_fe_input_buffer_config),
    ('global', pisp_fe_global_config),
    ('input', pisp_fe_input_config),
    ('decompress', pisp_decompress_config),
    ('decompand', pisp_fe_decompand_config),
    ('bla', pisp_bla_config),
    ('dpc', pisp_fe_dpc_config),
    ('stats_crop', pisp_fe_crop_config),
    ('spare1', uint32_t),
    ('blc', pisp_bla_config),
    ('rgby', pisp_fe_rgby_config),
    ('lsc', pisp_fe_lsc_config),
    ('agc_stats', pisp_fe_agc_stats_config),
    ('awb_stats', pisp_fe_awb_stats_config),
    ('cdaf_stats', pisp_fe_cdaf_stats_config),
    ('floating_stats', pisp_fe_floating_stats_config),
    ('output_axi', pisp_fe_output_axi_config),
    ('ch', pisp_fe_output_branch_config * int(2)),
    ('dirty_flags', uint32_t),
    ('dirty_flags_extra', uint32_t),
]

pisp_fe_config = struct_anon_59


PISP_FLOATING_STATS_NUM_ZONES = 4


PISP_AGC_STATS_NUM_BINS = 1024


PISP_AGC_STATS_SIZE = 16


PISP_AGC_STATS_NUM_ZONES = (PISP_AGC_STATS_SIZE * PISP_AGC_STATS_SIZE)


PISP_AGC_STATS_NUM_ROW_SUMS = 512


PISP_AWB_STATS_SIZE = 32


PISP_AWB_STATS_NUM_ZONES = (PISP_AWB_STATS_SIZE * PISP_AWB_STATS_SIZE)


PISP_CDAF_STATS_SIZE = 8


PISP_CDAF_STATS_NUM_FOMS = (PISP_CDAF_STATS_SIZE * PISP_CDAF_STATS_SIZE)


PISP_FE_NUM_OUTPUTS = 2


def PISP_FE_ENABLE_CROP(i):
    return (PISP_FE_ENABLE_CROP0 << (4 * i))


def PISP_FE_ENABLE_DOWNSCALE(i):
    return (PISP_FE_ENABLE_DOWNSCALE0 << (4 * i))


def PISP_FE_ENABLE_COMPRESS(i):
    return (PISP_FE_ENABLE_COMPRESS0 << (4 * i))


def PISP_FE_ENABLE_OUTPUT(i):
    return (PISP_FE_ENABLE_OUTPUT0 << (4 * i))


PISP_FE_DECOMPAND_LUT_SIZE = 65


PISP_FE_DPC_FLAG_FOLDBACK = 1


PISP_FE_DPC_FLAG_VFLAG = 2


PISP_FE_LSC_LUT_SIZE = 16


PISP_FE_CDAF_NUM_WEIGHTS = 8

# No inserted files

# No prefix-stripping

