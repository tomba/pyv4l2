r"""Wrapper for videodev2.h

Generated with:
ctypesgen --no-embed-preamble --no-macro-try-except --no-source-comments -D__volatile__= -D__signed__= -U__SIZEOF_INT128__ -I/home/tomba/tmp/khdrs/include -ov4l2/uapi/v4l2.py /home/tomba/tmp/khdrs/include/linux/videodev2.h /home/tomba/tmp/khdrs/include/linux/media.h /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h /home/tomba/tmp/khdrs/include/linux/media-bus-format.h /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

from .ctypes_preamble import *
from .ctypes_preamble import _variadic_function

# End preamble

# No libraries

# No modules

__time_t = c_long

__suseconds_t = c_long

__syscall_slong_t = c_long


class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]


class struct_timespec(Structure):
    pass

struct_timespec.__slots__ = [
    'tv_sec',
    'tv_nsec',
]
struct_timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]

__s8 = c_char

__u8 = c_ubyte

__s16 = c_short

__u16 = c_ushort

__s32 = c_int

__u32 = c_uint

__s64 = c_longlong

__u64 = c_ulonglong

__le32 = __u32


class struct_v4l2_edid(Structure):
    pass

struct_v4l2_edid.__slots__ = [
    'pad',
    'start_block',
    'blocks',
    'reserved',
    'edid',
]
struct_v4l2_edid._fields_ = [
    ('pad', __u32),
    ('start_block', __u32),
    ('blocks', __u32),
    ('reserved', __u32 * int(5)),
    ('edid', POINTER(__u8)),
]

enum_v4l2_power_line_frequency = c_int

V4L2_CID_POWER_LINE_FREQUENCY_DISABLED = 0

V4L2_CID_POWER_LINE_FREQUENCY_50HZ = 1

V4L2_CID_POWER_LINE_FREQUENCY_60HZ = 2

V4L2_CID_POWER_LINE_FREQUENCY_AUTO = 3

enum_v4l2_colorfx = c_int

V4L2_COLORFX_NONE = 0

V4L2_COLORFX_BW = 1

V4L2_COLORFX_SEPIA = 2

V4L2_COLORFX_NEGATIVE = 3

V4L2_COLORFX_EMBOSS = 4

V4L2_COLORFX_SKETCH = 5

V4L2_COLORFX_SKY_BLUE = 6

V4L2_COLORFX_GRASS_GREEN = 7

V4L2_COLORFX_SKIN_WHITEN = 8

V4L2_COLORFX_VIVID = 9

V4L2_COLORFX_AQUA = 10

V4L2_COLORFX_ART_FREEZE = 11

V4L2_COLORFX_SILHOUETTE = 12

V4L2_COLORFX_SOLARIZATION = 13

V4L2_COLORFX_ANTIQUE = 14

V4L2_COLORFX_SET_CBCR = 15

V4L2_COLORFX_SET_RGB = 16

enum_v4l2_mpeg_stream_type = c_int

V4L2_MPEG_STREAM_TYPE_MPEG2_PS = 0

V4L2_MPEG_STREAM_TYPE_MPEG2_TS = 1

V4L2_MPEG_STREAM_TYPE_MPEG1_SS = 2

V4L2_MPEG_STREAM_TYPE_MPEG2_DVD = 3

V4L2_MPEG_STREAM_TYPE_MPEG1_VCD = 4

V4L2_MPEG_STREAM_TYPE_MPEG2_SVCD = 5

enum_v4l2_mpeg_stream_vbi_fmt = c_int

V4L2_MPEG_STREAM_VBI_FMT_NONE = 0

V4L2_MPEG_STREAM_VBI_FMT_IVTV = 1

enum_v4l2_mpeg_audio_sampling_freq = c_int

V4L2_MPEG_AUDIO_SAMPLING_FREQ_44100 = 0

V4L2_MPEG_AUDIO_SAMPLING_FREQ_48000 = 1

V4L2_MPEG_AUDIO_SAMPLING_FREQ_32000 = 2

enum_v4l2_mpeg_audio_encoding = c_int

V4L2_MPEG_AUDIO_ENCODING_LAYER_1 = 0

V4L2_MPEG_AUDIO_ENCODING_LAYER_2 = 1

V4L2_MPEG_AUDIO_ENCODING_LAYER_3 = 2

V4L2_MPEG_AUDIO_ENCODING_AAC = 3

V4L2_MPEG_AUDIO_ENCODING_AC3 = 4

enum_v4l2_mpeg_audio_l1_bitrate = c_int

V4L2_MPEG_AUDIO_L1_BITRATE_32K = 0

V4L2_MPEG_AUDIO_L1_BITRATE_64K = 1

V4L2_MPEG_AUDIO_L1_BITRATE_96K = 2

V4L2_MPEG_AUDIO_L1_BITRATE_128K = 3

V4L2_MPEG_AUDIO_L1_BITRATE_160K = 4

V4L2_MPEG_AUDIO_L1_BITRATE_192K = 5

V4L2_MPEG_AUDIO_L1_BITRATE_224K = 6

V4L2_MPEG_AUDIO_L1_BITRATE_256K = 7

V4L2_MPEG_AUDIO_L1_BITRATE_288K = 8

V4L2_MPEG_AUDIO_L1_BITRATE_320K = 9

V4L2_MPEG_AUDIO_L1_BITRATE_352K = 10

V4L2_MPEG_AUDIO_L1_BITRATE_384K = 11

V4L2_MPEG_AUDIO_L1_BITRATE_416K = 12

V4L2_MPEG_AUDIO_L1_BITRATE_448K = 13

enum_v4l2_mpeg_audio_l2_bitrate = c_int

V4L2_MPEG_AUDIO_L2_BITRATE_32K = 0

V4L2_MPEG_AUDIO_L2_BITRATE_48K = 1

V4L2_MPEG_AUDIO_L2_BITRATE_56K = 2

V4L2_MPEG_AUDIO_L2_BITRATE_64K = 3

V4L2_MPEG_AUDIO_L2_BITRATE_80K = 4

V4L2_MPEG_AUDIO_L2_BITRATE_96K = 5

V4L2_MPEG_AUDIO_L2_BITRATE_112K = 6

V4L2_MPEG_AUDIO_L2_BITRATE_128K = 7

V4L2_MPEG_AUDIO_L2_BITRATE_160K = 8

V4L2_MPEG_AUDIO_L2_BITRATE_192K = 9

V4L2_MPEG_AUDIO_L2_BITRATE_224K = 10

V4L2_MPEG_AUDIO_L2_BITRATE_256K = 11

V4L2_MPEG_AUDIO_L2_BITRATE_320K = 12

V4L2_MPEG_AUDIO_L2_BITRATE_384K = 13

enum_v4l2_mpeg_audio_l3_bitrate = c_int

V4L2_MPEG_AUDIO_L3_BITRATE_32K = 0

V4L2_MPEG_AUDIO_L3_BITRATE_40K = 1

V4L2_MPEG_AUDIO_L3_BITRATE_48K = 2

V4L2_MPEG_AUDIO_L3_BITRATE_56K = 3

V4L2_MPEG_AUDIO_L3_BITRATE_64K = 4

V4L2_MPEG_AUDIO_L3_BITRATE_80K = 5

V4L2_MPEG_AUDIO_L3_BITRATE_96K = 6

V4L2_MPEG_AUDIO_L3_BITRATE_112K = 7

V4L2_MPEG_AUDIO_L3_BITRATE_128K = 8

V4L2_MPEG_AUDIO_L3_BITRATE_160K = 9

V4L2_MPEG_AUDIO_L3_BITRATE_192K = 10

V4L2_MPEG_AUDIO_L3_BITRATE_224K = 11

V4L2_MPEG_AUDIO_L3_BITRATE_256K = 12

V4L2_MPEG_AUDIO_L3_BITRATE_320K = 13

enum_v4l2_mpeg_audio_mode = c_int

V4L2_MPEG_AUDIO_MODE_STEREO = 0

V4L2_MPEG_AUDIO_MODE_JOINT_STEREO = 1

V4L2_MPEG_AUDIO_MODE_DUAL = 2

V4L2_MPEG_AUDIO_MODE_MONO = 3

enum_v4l2_mpeg_audio_mode_extension = c_int

V4L2_MPEG_AUDIO_MODE_EXTENSION_BOUND_4 = 0

V4L2_MPEG_AUDIO_MODE_EXTENSION_BOUND_8 = 1

V4L2_MPEG_AUDIO_MODE_EXTENSION_BOUND_12 = 2

V4L2_MPEG_AUDIO_MODE_EXTENSION_BOUND_16 = 3

enum_v4l2_mpeg_audio_emphasis = c_int

V4L2_MPEG_AUDIO_EMPHASIS_NONE = 0

V4L2_MPEG_AUDIO_EMPHASIS_50_DIV_15_uS = 1

V4L2_MPEG_AUDIO_EMPHASIS_CCITT_J17 = 2

enum_v4l2_mpeg_audio_crc = c_int

V4L2_MPEG_AUDIO_CRC_NONE = 0

V4L2_MPEG_AUDIO_CRC_CRC16 = 1

enum_v4l2_mpeg_audio_ac3_bitrate = c_int

V4L2_MPEG_AUDIO_AC3_BITRATE_32K = 0

V4L2_MPEG_AUDIO_AC3_BITRATE_40K = 1

V4L2_MPEG_AUDIO_AC3_BITRATE_48K = 2

V4L2_MPEG_AUDIO_AC3_BITRATE_56K = 3

V4L2_MPEG_AUDIO_AC3_BITRATE_64K = 4

V4L2_MPEG_AUDIO_AC3_BITRATE_80K = 5

V4L2_MPEG_AUDIO_AC3_BITRATE_96K = 6

V4L2_MPEG_AUDIO_AC3_BITRATE_112K = 7

V4L2_MPEG_AUDIO_AC3_BITRATE_128K = 8

V4L2_MPEG_AUDIO_AC3_BITRATE_160K = 9

V4L2_MPEG_AUDIO_AC3_BITRATE_192K = 10

V4L2_MPEG_AUDIO_AC3_BITRATE_224K = 11

V4L2_MPEG_AUDIO_AC3_BITRATE_256K = 12

V4L2_MPEG_AUDIO_AC3_BITRATE_320K = 13

V4L2_MPEG_AUDIO_AC3_BITRATE_384K = 14

V4L2_MPEG_AUDIO_AC3_BITRATE_448K = 15

V4L2_MPEG_AUDIO_AC3_BITRATE_512K = 16

V4L2_MPEG_AUDIO_AC3_BITRATE_576K = 17

V4L2_MPEG_AUDIO_AC3_BITRATE_640K = 18

enum_v4l2_mpeg_audio_dec_playback = c_int

V4L2_MPEG_AUDIO_DEC_PLAYBACK_AUTO = 0

V4L2_MPEG_AUDIO_DEC_PLAYBACK_STEREO = 1

V4L2_MPEG_AUDIO_DEC_PLAYBACK_LEFT = 2

V4L2_MPEG_AUDIO_DEC_PLAYBACK_RIGHT = 3

V4L2_MPEG_AUDIO_DEC_PLAYBACK_MONO = 4

V4L2_MPEG_AUDIO_DEC_PLAYBACK_SWAPPED_STEREO = 5

enum_v4l2_mpeg_video_encoding = c_int

V4L2_MPEG_VIDEO_ENCODING_MPEG_1 = 0

V4L2_MPEG_VIDEO_ENCODING_MPEG_2 = 1

V4L2_MPEG_VIDEO_ENCODING_MPEG_4_AVC = 2

enum_v4l2_mpeg_video_aspect = c_int

V4L2_MPEG_VIDEO_ASPECT_1x1 = 0

V4L2_MPEG_VIDEO_ASPECT_4x3 = 1

V4L2_MPEG_VIDEO_ASPECT_16x9 = 2

V4L2_MPEG_VIDEO_ASPECT_221x100 = 3

enum_v4l2_mpeg_video_bitrate_mode = c_int

V4L2_MPEG_VIDEO_BITRATE_MODE_VBR = 0

V4L2_MPEG_VIDEO_BITRATE_MODE_CBR = 1

V4L2_MPEG_VIDEO_BITRATE_MODE_CQ = 2

enum_v4l2_mpeg_video_header_mode = c_int

V4L2_MPEG_VIDEO_HEADER_MODE_SEPARATE = 0

V4L2_MPEG_VIDEO_HEADER_MODE_JOINED_WITH_1ST_FRAME = 1

enum_v4l2_mpeg_video_multi_slice_mode = c_int

V4L2_MPEG_VIDEO_MULTI_SLICE_MODE_SINGLE = 0

V4L2_MPEG_VIDEO_MULTI_SLICE_MODE_MAX_MB = 1

V4L2_MPEG_VIDEO_MULTI_SLICE_MODE_MAX_BYTES = 2

V4L2_MPEG_VIDEO_MULTI_SICE_MODE_MAX_MB = 1

V4L2_MPEG_VIDEO_MULTI_SICE_MODE_MAX_BYTES = 2

enum_v4l2_mpeg_video_intra_refresh_period_type = c_int

V4L2_CID_MPEG_VIDEO_INTRA_REFRESH_PERIOD_TYPE_RANDOM = 0

V4L2_CID_MPEG_VIDEO_INTRA_REFRESH_PERIOD_TYPE_CYCLIC = 1

enum_v4l2_mpeg_video_mpeg2_level = c_int

V4L2_MPEG_VIDEO_MPEG2_LEVEL_LOW = 0

V4L2_MPEG_VIDEO_MPEG2_LEVEL_MAIN = 1

V4L2_MPEG_VIDEO_MPEG2_LEVEL_HIGH_1440 = 2

V4L2_MPEG_VIDEO_MPEG2_LEVEL_HIGH = 3

enum_v4l2_mpeg_video_mpeg2_profile = c_int

V4L2_MPEG_VIDEO_MPEG2_PROFILE_SIMPLE = 0

V4L2_MPEG_VIDEO_MPEG2_PROFILE_MAIN = 1

V4L2_MPEG_VIDEO_MPEG2_PROFILE_SNR_SCALABLE = 2

V4L2_MPEG_VIDEO_MPEG2_PROFILE_SPATIALLY_SCALABLE = 3

V4L2_MPEG_VIDEO_MPEG2_PROFILE_HIGH = 4

V4L2_MPEG_VIDEO_MPEG2_PROFILE_MULTIVIEW = 5

enum_v4l2_mpeg_video_h264_entropy_mode = c_int

V4L2_MPEG_VIDEO_H264_ENTROPY_MODE_CAVLC = 0

V4L2_MPEG_VIDEO_H264_ENTROPY_MODE_CABAC = 1

enum_v4l2_mpeg_video_h264_level = c_int

V4L2_MPEG_VIDEO_H264_LEVEL_1_0 = 0

V4L2_MPEG_VIDEO_H264_LEVEL_1B = 1

V4L2_MPEG_VIDEO_H264_LEVEL_1_1 = 2

V4L2_MPEG_VIDEO_H264_LEVEL_1_2 = 3

V4L2_MPEG_VIDEO_H264_LEVEL_1_3 = 4

V4L2_MPEG_VIDEO_H264_LEVEL_2_0 = 5

V4L2_MPEG_VIDEO_H264_LEVEL_2_1 = 6

V4L2_MPEG_VIDEO_H264_LEVEL_2_2 = 7

V4L2_MPEG_VIDEO_H264_LEVEL_3_0 = 8

V4L2_MPEG_VIDEO_H264_LEVEL_3_1 = 9

V4L2_MPEG_VIDEO_H264_LEVEL_3_2 = 10

V4L2_MPEG_VIDEO_H264_LEVEL_4_0 = 11

V4L2_MPEG_VIDEO_H264_LEVEL_4_1 = 12

V4L2_MPEG_VIDEO_H264_LEVEL_4_2 = 13

V4L2_MPEG_VIDEO_H264_LEVEL_5_0 = 14

V4L2_MPEG_VIDEO_H264_LEVEL_5_1 = 15

V4L2_MPEG_VIDEO_H264_LEVEL_5_2 = 16

V4L2_MPEG_VIDEO_H264_LEVEL_6_0 = 17

V4L2_MPEG_VIDEO_H264_LEVEL_6_1 = 18

V4L2_MPEG_VIDEO_H264_LEVEL_6_2 = 19

enum_v4l2_mpeg_video_h264_loop_filter_mode = c_int

V4L2_MPEG_VIDEO_H264_LOOP_FILTER_MODE_ENABLED = 0

V4L2_MPEG_VIDEO_H264_LOOP_FILTER_MODE_DISABLED = 1

V4L2_MPEG_VIDEO_H264_LOOP_FILTER_MODE_DISABLED_AT_SLICE_BOUNDARY = 2

enum_v4l2_mpeg_video_h264_profile = c_int

V4L2_MPEG_VIDEO_H264_PROFILE_BASELINE = 0

V4L2_MPEG_VIDEO_H264_PROFILE_CONSTRAINED_BASELINE = 1

V4L2_MPEG_VIDEO_H264_PROFILE_MAIN = 2

V4L2_MPEG_VIDEO_H264_PROFILE_EXTENDED = 3

V4L2_MPEG_VIDEO_H264_PROFILE_HIGH = 4

V4L2_MPEG_VIDEO_H264_PROFILE_HIGH_10 = 5

V4L2_MPEG_VIDEO_H264_PROFILE_HIGH_422 = 6

V4L2_MPEG_VIDEO_H264_PROFILE_HIGH_444_PREDICTIVE = 7

V4L2_MPEG_VIDEO_H264_PROFILE_HIGH_10_INTRA = 8

V4L2_MPEG_VIDEO_H264_PROFILE_HIGH_422_INTRA = 9

V4L2_MPEG_VIDEO_H264_PROFILE_HIGH_444_INTRA = 10

V4L2_MPEG_VIDEO_H264_PROFILE_CAVLC_444_INTRA = 11

V4L2_MPEG_VIDEO_H264_PROFILE_SCALABLE_BASELINE = 12

V4L2_MPEG_VIDEO_H264_PROFILE_SCALABLE_HIGH = 13

V4L2_MPEG_VIDEO_H264_PROFILE_SCALABLE_HIGH_INTRA = 14

V4L2_MPEG_VIDEO_H264_PROFILE_STEREO_HIGH = 15

V4L2_MPEG_VIDEO_H264_PROFILE_MULTIVIEW_HIGH = 16

V4L2_MPEG_VIDEO_H264_PROFILE_CONSTRAINED_HIGH = 17

enum_v4l2_mpeg_video_h264_vui_sar_idc = c_int

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_UNSPECIFIED = 0

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_1x1 = 1

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_12x11 = 2

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_10x11 = 3

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_16x11 = 4

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_40x33 = 5

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_24x11 = 6

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_20x11 = 7

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_32x11 = 8

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_80x33 = 9

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_18x11 = 10

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_15x11 = 11

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_64x33 = 12

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_160x99 = 13

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_4x3 = 14

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_3x2 = 15

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_2x1 = 16

V4L2_MPEG_VIDEO_H264_VUI_SAR_IDC_EXTENDED = 17

enum_v4l2_mpeg_video_h264_sei_fp_arrangement_type = c_int

V4L2_MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE_CHECKERBOARD = 0

V4L2_MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE_COLUMN = 1

V4L2_MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE_ROW = 2

V4L2_MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE_SIDE_BY_SIDE = 3

V4L2_MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE_TOP_BOTTOM = 4

V4L2_MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE_TEMPORAL = 5

enum_v4l2_mpeg_video_h264_fmo_map_type = c_int

V4L2_MPEG_VIDEO_H264_FMO_MAP_TYPE_INTERLEAVED_SLICES = 0

V4L2_MPEG_VIDEO_H264_FMO_MAP_TYPE_SCATTERED_SLICES = 1

V4L2_MPEG_VIDEO_H264_FMO_MAP_TYPE_FOREGROUND_WITH_LEFT_OVER = 2

V4L2_MPEG_VIDEO_H264_FMO_MAP_TYPE_BOX_OUT = 3

V4L2_MPEG_VIDEO_H264_FMO_MAP_TYPE_RASTER_SCAN = 4

V4L2_MPEG_VIDEO_H264_FMO_MAP_TYPE_WIPE_SCAN = 5

V4L2_MPEG_VIDEO_H264_FMO_MAP_TYPE_EXPLICIT = 6

enum_v4l2_mpeg_video_h264_fmo_change_dir = c_int

V4L2_MPEG_VIDEO_H264_FMO_CHANGE_DIR_RIGHT = 0

V4L2_MPEG_VIDEO_H264_FMO_CHANGE_DIR_LEFT = 1

enum_v4l2_mpeg_video_h264_hierarchical_coding_type = c_int

V4L2_MPEG_VIDEO_H264_HIERARCHICAL_CODING_B = 0

V4L2_MPEG_VIDEO_H264_HIERARCHICAL_CODING_P = 1

enum_v4l2_mpeg_video_mpeg4_level = c_int

V4L2_MPEG_VIDEO_MPEG4_LEVEL_0 = 0

V4L2_MPEG_VIDEO_MPEG4_LEVEL_0B = 1

V4L2_MPEG_VIDEO_MPEG4_LEVEL_1 = 2

V4L2_MPEG_VIDEO_MPEG4_LEVEL_2 = 3

V4L2_MPEG_VIDEO_MPEG4_LEVEL_3 = 4

V4L2_MPEG_VIDEO_MPEG4_LEVEL_3B = 5

V4L2_MPEG_VIDEO_MPEG4_LEVEL_4 = 6

V4L2_MPEG_VIDEO_MPEG4_LEVEL_5 = 7

enum_v4l2_mpeg_video_mpeg4_profile = c_int

V4L2_MPEG_VIDEO_MPEG4_PROFILE_SIMPLE = 0

V4L2_MPEG_VIDEO_MPEG4_PROFILE_ADVANCED_SIMPLE = 1

V4L2_MPEG_VIDEO_MPEG4_PROFILE_CORE = 2

V4L2_MPEG_VIDEO_MPEG4_PROFILE_SIMPLE_SCALABLE = 3

V4L2_MPEG_VIDEO_MPEG4_PROFILE_ADVANCED_CODING_EFFICIENCY = 4

enum_v4l2_vp8_num_partitions = c_int

V4L2_CID_MPEG_VIDEO_VPX_1_PARTITION = 0

V4L2_CID_MPEG_VIDEO_VPX_2_PARTITIONS = 1

V4L2_CID_MPEG_VIDEO_VPX_4_PARTITIONS = 2

V4L2_CID_MPEG_VIDEO_VPX_8_PARTITIONS = 3

enum_v4l2_vp8_num_ref_frames = c_int

V4L2_CID_MPEG_VIDEO_VPX_1_REF_FRAME = 0

V4L2_CID_MPEG_VIDEO_VPX_2_REF_FRAME = 1

V4L2_CID_MPEG_VIDEO_VPX_3_REF_FRAME = 2

enum_v4l2_vp8_golden_frame_sel = c_int

V4L2_CID_MPEG_VIDEO_VPX_GOLDEN_FRAME_USE_PREV = 0

V4L2_CID_MPEG_VIDEO_VPX_GOLDEN_FRAME_USE_REF_PERIOD = 1

enum_v4l2_mpeg_video_vp8_profile = c_int

V4L2_MPEG_VIDEO_VP8_PROFILE_0 = 0

V4L2_MPEG_VIDEO_VP8_PROFILE_1 = 1

V4L2_MPEG_VIDEO_VP8_PROFILE_2 = 2

V4L2_MPEG_VIDEO_VP8_PROFILE_3 = 3

enum_v4l2_mpeg_video_vp9_profile = c_int

V4L2_MPEG_VIDEO_VP9_PROFILE_0 = 0

V4L2_MPEG_VIDEO_VP9_PROFILE_1 = 1

V4L2_MPEG_VIDEO_VP9_PROFILE_2 = 2

V4L2_MPEG_VIDEO_VP9_PROFILE_3 = 3

enum_v4l2_mpeg_video_vp9_level = c_int

V4L2_MPEG_VIDEO_VP9_LEVEL_1_0 = 0

V4L2_MPEG_VIDEO_VP9_LEVEL_1_1 = 1

V4L2_MPEG_VIDEO_VP9_LEVEL_2_0 = 2

V4L2_MPEG_VIDEO_VP9_LEVEL_2_1 = 3

V4L2_MPEG_VIDEO_VP9_LEVEL_3_0 = 4

V4L2_MPEG_VIDEO_VP9_LEVEL_3_1 = 5

V4L2_MPEG_VIDEO_VP9_LEVEL_4_0 = 6

V4L2_MPEG_VIDEO_VP9_LEVEL_4_1 = 7

V4L2_MPEG_VIDEO_VP9_LEVEL_5_0 = 8

V4L2_MPEG_VIDEO_VP9_LEVEL_5_1 = 9

V4L2_MPEG_VIDEO_VP9_LEVEL_5_2 = 10

V4L2_MPEG_VIDEO_VP9_LEVEL_6_0 = 11

V4L2_MPEG_VIDEO_VP9_LEVEL_6_1 = 12

V4L2_MPEG_VIDEO_VP9_LEVEL_6_2 = 13

enum_v4l2_mpeg_video_hevc_hier_coding_type = c_int

V4L2_MPEG_VIDEO_HEVC_HIERARCHICAL_CODING_B = 0

V4L2_MPEG_VIDEO_HEVC_HIERARCHICAL_CODING_P = 1

enum_v4l2_mpeg_video_hevc_profile = c_int

V4L2_MPEG_VIDEO_HEVC_PROFILE_MAIN = 0

V4L2_MPEG_VIDEO_HEVC_PROFILE_MAIN_STILL_PICTURE = 1

V4L2_MPEG_VIDEO_HEVC_PROFILE_MAIN_10 = 2

enum_v4l2_mpeg_video_hevc_level = c_int

V4L2_MPEG_VIDEO_HEVC_LEVEL_1 = 0

V4L2_MPEG_VIDEO_HEVC_LEVEL_2 = 1

V4L2_MPEG_VIDEO_HEVC_LEVEL_2_1 = 2

V4L2_MPEG_VIDEO_HEVC_LEVEL_3 = 3

V4L2_MPEG_VIDEO_HEVC_LEVEL_3_1 = 4

V4L2_MPEG_VIDEO_HEVC_LEVEL_4 = 5

V4L2_MPEG_VIDEO_HEVC_LEVEL_4_1 = 6

V4L2_MPEG_VIDEO_HEVC_LEVEL_5 = 7

V4L2_MPEG_VIDEO_HEVC_LEVEL_5_1 = 8

V4L2_MPEG_VIDEO_HEVC_LEVEL_5_2 = 9

V4L2_MPEG_VIDEO_HEVC_LEVEL_6 = 10

V4L2_MPEG_VIDEO_HEVC_LEVEL_6_1 = 11

V4L2_MPEG_VIDEO_HEVC_LEVEL_6_2 = 12

enum_v4l2_mpeg_video_hevc_tier = c_int

V4L2_MPEG_VIDEO_HEVC_TIER_MAIN = 0

V4L2_MPEG_VIDEO_HEVC_TIER_HIGH = 1

enum_v4l2_cid_mpeg_video_hevc_loop_filter_mode = c_int

V4L2_MPEG_VIDEO_HEVC_LOOP_FILTER_MODE_DISABLED = 0

V4L2_MPEG_VIDEO_HEVC_LOOP_FILTER_MODE_ENABLED = 1

V4L2_MPEG_VIDEO_HEVC_LOOP_FILTER_MODE_DISABLED_AT_SLICE_BOUNDARY = 2

enum_v4l2_cid_mpeg_video_hevc_refresh_type = c_int

V4L2_MPEG_VIDEO_HEVC_REFRESH_NONE = 0

V4L2_MPEG_VIDEO_HEVC_REFRESH_CRA = 1

V4L2_MPEG_VIDEO_HEVC_REFRESH_IDR = 2

enum_v4l2_cid_mpeg_video_hevc_size_of_length_field = c_int

V4L2_MPEG_VIDEO_HEVC_SIZE_0 = 0

V4L2_MPEG_VIDEO_HEVC_SIZE_1 = 1

V4L2_MPEG_VIDEO_HEVC_SIZE_2 = 2

V4L2_MPEG_VIDEO_HEVC_SIZE_4 = 3

enum_v4l2_mpeg_video_frame_skip_mode = c_int

V4L2_MPEG_VIDEO_FRAME_SKIP_MODE_DISABLED = 0

V4L2_MPEG_VIDEO_FRAME_SKIP_MODE_LEVEL_LIMIT = 1

V4L2_MPEG_VIDEO_FRAME_SKIP_MODE_BUF_LIMIT = 2

enum_v4l2_mpeg_video_av1_profile = c_int

V4L2_MPEG_VIDEO_AV1_PROFILE_MAIN = 0

V4L2_MPEG_VIDEO_AV1_PROFILE_HIGH = 1

V4L2_MPEG_VIDEO_AV1_PROFILE_PROFESSIONAL = 2

enum_v4l2_mpeg_video_av1_level = c_int

V4L2_MPEG_VIDEO_AV1_LEVEL_2_0 = 0

V4L2_MPEG_VIDEO_AV1_LEVEL_2_1 = 1

V4L2_MPEG_VIDEO_AV1_LEVEL_2_2 = 2

V4L2_MPEG_VIDEO_AV1_LEVEL_2_3 = 3

V4L2_MPEG_VIDEO_AV1_LEVEL_3_0 = 4

V4L2_MPEG_VIDEO_AV1_LEVEL_3_1 = 5

V4L2_MPEG_VIDEO_AV1_LEVEL_3_2 = 6

V4L2_MPEG_VIDEO_AV1_LEVEL_3_3 = 7

V4L2_MPEG_VIDEO_AV1_LEVEL_4_0 = 8

V4L2_MPEG_VIDEO_AV1_LEVEL_4_1 = 9

V4L2_MPEG_VIDEO_AV1_LEVEL_4_2 = 10

V4L2_MPEG_VIDEO_AV1_LEVEL_4_3 = 11

V4L2_MPEG_VIDEO_AV1_LEVEL_5_0 = 12

V4L2_MPEG_VIDEO_AV1_LEVEL_5_1 = 13

V4L2_MPEG_VIDEO_AV1_LEVEL_5_2 = 14

V4L2_MPEG_VIDEO_AV1_LEVEL_5_3 = 15

V4L2_MPEG_VIDEO_AV1_LEVEL_6_0 = 16

V4L2_MPEG_VIDEO_AV1_LEVEL_6_1 = 17

V4L2_MPEG_VIDEO_AV1_LEVEL_6_2 = 18

V4L2_MPEG_VIDEO_AV1_LEVEL_6_3 = 19

V4L2_MPEG_VIDEO_AV1_LEVEL_7_0 = 20

V4L2_MPEG_VIDEO_AV1_LEVEL_7_1 = 21

V4L2_MPEG_VIDEO_AV1_LEVEL_7_2 = 22

V4L2_MPEG_VIDEO_AV1_LEVEL_7_3 = 23

enum_v4l2_mpeg_cx2341x_video_spatial_filter_mode = c_int

V4L2_MPEG_CX2341X_VIDEO_SPATIAL_FILTER_MODE_MANUAL = 0

V4L2_MPEG_CX2341X_VIDEO_SPATIAL_FILTER_MODE_AUTO = 1

enum_v4l2_mpeg_cx2341x_video_luma_spatial_filter_type = c_int

V4L2_MPEG_CX2341X_VIDEO_LUMA_SPATIAL_FILTER_TYPE_OFF = 0

V4L2_MPEG_CX2341X_VIDEO_LUMA_SPATIAL_FILTER_TYPE_1D_HOR = 1

V4L2_MPEG_CX2341X_VIDEO_LUMA_SPATIAL_FILTER_TYPE_1D_VERT = 2

V4L2_MPEG_CX2341X_VIDEO_LUMA_SPATIAL_FILTER_TYPE_2D_HV_SEPARABLE = 3

V4L2_MPEG_CX2341X_VIDEO_LUMA_SPATIAL_FILTER_TYPE_2D_SYM_NON_SEPARABLE = 4

enum_v4l2_mpeg_cx2341x_video_chroma_spatial_filter_type = c_int

V4L2_MPEG_CX2341X_VIDEO_CHROMA_SPATIAL_FILTER_TYPE_OFF = 0

V4L2_MPEG_CX2341X_VIDEO_CHROMA_SPATIAL_FILTER_TYPE_1D_HOR = 1

enum_v4l2_mpeg_cx2341x_video_temporal_filter_mode = c_int

V4L2_MPEG_CX2341X_VIDEO_TEMPORAL_FILTER_MODE_MANUAL = 0

V4L2_MPEG_CX2341X_VIDEO_TEMPORAL_FILTER_MODE_AUTO = 1

enum_v4l2_mpeg_cx2341x_video_median_filter_type = c_int

V4L2_MPEG_CX2341X_VIDEO_MEDIAN_FILTER_TYPE_OFF = 0

V4L2_MPEG_CX2341X_VIDEO_MEDIAN_FILTER_TYPE_HOR = 1

V4L2_MPEG_CX2341X_VIDEO_MEDIAN_FILTER_TYPE_VERT = 2

V4L2_MPEG_CX2341X_VIDEO_MEDIAN_FILTER_TYPE_HOR_VERT = 3

V4L2_MPEG_CX2341X_VIDEO_MEDIAN_FILTER_TYPE_DIAG = 4

enum_v4l2_mpeg_mfc51_video_frame_skip_mode = c_int

V4L2_MPEG_MFC51_VIDEO_FRAME_SKIP_MODE_DISABLED = 0

V4L2_MPEG_MFC51_VIDEO_FRAME_SKIP_MODE_LEVEL_LIMIT = 1

V4L2_MPEG_MFC51_VIDEO_FRAME_SKIP_MODE_BUF_LIMIT = 2

enum_v4l2_mpeg_mfc51_video_force_frame_type = c_int

V4L2_MPEG_MFC51_VIDEO_FORCE_FRAME_TYPE_DISABLED = 0

V4L2_MPEG_MFC51_VIDEO_FORCE_FRAME_TYPE_I_FRAME = 1

V4L2_MPEG_MFC51_VIDEO_FORCE_FRAME_TYPE_NOT_CODED = 2

enum_v4l2_exposure_auto_type = c_int

V4L2_EXPOSURE_AUTO = 0

V4L2_EXPOSURE_MANUAL = 1

V4L2_EXPOSURE_SHUTTER_PRIORITY = 2

V4L2_EXPOSURE_APERTURE_PRIORITY = 3

enum_v4l2_auto_n_preset_white_balance = c_int

V4L2_WHITE_BALANCE_MANUAL = 0

V4L2_WHITE_BALANCE_AUTO = 1

V4L2_WHITE_BALANCE_INCANDESCENT = 2

V4L2_WHITE_BALANCE_FLUORESCENT = 3

V4L2_WHITE_BALANCE_FLUORESCENT_H = 4

V4L2_WHITE_BALANCE_HORIZON = 5

V4L2_WHITE_BALANCE_DAYLIGHT = 6

V4L2_WHITE_BALANCE_FLASH = 7

V4L2_WHITE_BALANCE_CLOUDY = 8

V4L2_WHITE_BALANCE_SHADE = 9

enum_v4l2_iso_sensitivity_auto_type = c_int

V4L2_ISO_SENSITIVITY_MANUAL = 0

V4L2_ISO_SENSITIVITY_AUTO = 1

enum_v4l2_exposure_metering = c_int

V4L2_EXPOSURE_METERING_AVERAGE = 0

V4L2_EXPOSURE_METERING_CENTER_WEIGHTED = 1

V4L2_EXPOSURE_METERING_SPOT = 2

V4L2_EXPOSURE_METERING_MATRIX = 3

enum_v4l2_scene_mode = c_int

V4L2_SCENE_MODE_NONE = 0

V4L2_SCENE_MODE_BACKLIGHT = 1

V4L2_SCENE_MODE_BEACH_SNOW = 2

V4L2_SCENE_MODE_CANDLE_LIGHT = 3

V4L2_SCENE_MODE_DAWN_DUSK = 4

V4L2_SCENE_MODE_FALL_COLORS = 5

V4L2_SCENE_MODE_FIREWORKS = 6

V4L2_SCENE_MODE_LANDSCAPE = 7

V4L2_SCENE_MODE_NIGHT = 8

V4L2_SCENE_MODE_PARTY_INDOOR = 9

V4L2_SCENE_MODE_PORTRAIT = 10

V4L2_SCENE_MODE_SPORTS = 11

V4L2_SCENE_MODE_SUNSET = 12

V4L2_SCENE_MODE_TEXT = 13

enum_v4l2_auto_focus_range = c_int

V4L2_AUTO_FOCUS_RANGE_AUTO = 0

V4L2_AUTO_FOCUS_RANGE_NORMAL = 1

V4L2_AUTO_FOCUS_RANGE_MACRO = 2

V4L2_AUTO_FOCUS_RANGE_INFINITY = 3

enum_v4l2_preemphasis = c_int

V4L2_PREEMPHASIS_DISABLED = 0

V4L2_PREEMPHASIS_50_uS = 1

V4L2_PREEMPHASIS_75_uS = 2

enum_v4l2_flash_led_mode = c_int

V4L2_FLASH_LED_MODE_NONE = 0

V4L2_FLASH_LED_MODE_FLASH = (V4L2_FLASH_LED_MODE_NONE + 1)

V4L2_FLASH_LED_MODE_TORCH = (V4L2_FLASH_LED_MODE_FLASH + 1)

enum_v4l2_flash_strobe_source = c_int

V4L2_FLASH_STROBE_SOURCE_SOFTWARE = 0

V4L2_FLASH_STROBE_SOURCE_EXTERNAL = (V4L2_FLASH_STROBE_SOURCE_SOFTWARE + 1)

enum_v4l2_jpeg_chroma_subsampling = c_int

V4L2_JPEG_CHROMA_SUBSAMPLING_444 = 0

V4L2_JPEG_CHROMA_SUBSAMPLING_422 = 1

V4L2_JPEG_CHROMA_SUBSAMPLING_420 = 2

V4L2_JPEG_CHROMA_SUBSAMPLING_411 = 3

V4L2_JPEG_CHROMA_SUBSAMPLING_410 = 4

V4L2_JPEG_CHROMA_SUBSAMPLING_GRAY = 5

enum_v4l2_dv_tx_mode = c_int

V4L2_DV_TX_MODE_DVI_D = 0

V4L2_DV_TX_MODE_HDMI = 1

enum_v4l2_dv_rgb_range = c_int

V4L2_DV_RGB_RANGE_AUTO = 0

V4L2_DV_RGB_RANGE_LIMITED = 1

V4L2_DV_RGB_RANGE_FULL = 2

enum_v4l2_dv_it_content_type = c_int

V4L2_DV_IT_CONTENT_TYPE_GRAPHICS = 0

V4L2_DV_IT_CONTENT_TYPE_PHOTO = 1

V4L2_DV_IT_CONTENT_TYPE_CINEMA = 2

V4L2_DV_IT_CONTENT_TYPE_GAME = 3

V4L2_DV_IT_CONTENT_TYPE_NO_ITC = 4

enum_v4l2_deemphasis = c_int

V4L2_DEEMPHASIS_DISABLED = V4L2_PREEMPHASIS_DISABLED

V4L2_DEEMPHASIS_50_uS = V4L2_PREEMPHASIS_50_uS

V4L2_DEEMPHASIS_75_uS = V4L2_PREEMPHASIS_75_uS

enum_v4l2_detect_md_mode = c_int

V4L2_DETECT_MD_MODE_DISABLED = 0

V4L2_DETECT_MD_MODE_GLOBAL = 1

V4L2_DETECT_MD_MODE_THRESHOLD_GRID = 2

V4L2_DETECT_MD_MODE_REGION_GRID = 3

enum_v4l2_stateless_h264_decode_mode = c_int

V4L2_STATELESS_H264_DECODE_MODE_SLICE_BASED = 0

V4L2_STATELESS_H264_DECODE_MODE_FRAME_BASED = (V4L2_STATELESS_H264_DECODE_MODE_SLICE_BASED + 1)

enum_v4l2_stateless_h264_start_code = c_int

V4L2_STATELESS_H264_START_CODE_NONE = 0

V4L2_STATELESS_H264_START_CODE_ANNEX_B = (V4L2_STATELESS_H264_START_CODE_NONE + 1)


class struct_v4l2_ctrl_h264_sps(Structure):
    pass

struct_v4l2_ctrl_h264_sps.__slots__ = [
    'profile_idc',
    'constraint_set_flags',
    'level_idc',
    'seq_parameter_set_id',
    'chroma_format_idc',
    'bit_depth_luma_minus8',
    'bit_depth_chroma_minus8',
    'log2_max_frame_num_minus4',
    'pic_order_cnt_type',
    'log2_max_pic_order_cnt_lsb_minus4',
    'max_num_ref_frames',
    'num_ref_frames_in_pic_order_cnt_cycle',
    'offset_for_ref_frame',
    'offset_for_non_ref_pic',
    'offset_for_top_to_bottom_field',
    'pic_width_in_mbs_minus1',
    'pic_height_in_map_units_minus1',
    'flags',
]
struct_v4l2_ctrl_h264_sps._fields_ = [
    ('profile_idc', __u8),
    ('constraint_set_flags', __u8),
    ('level_idc', __u8),
    ('seq_parameter_set_id', __u8),
    ('chroma_format_idc', __u8),
    ('bit_depth_luma_minus8', __u8),
    ('bit_depth_chroma_minus8', __u8),
    ('log2_max_frame_num_minus4', __u8),
    ('pic_order_cnt_type', __u8),
    ('log2_max_pic_order_cnt_lsb_minus4', __u8),
    ('max_num_ref_frames', __u8),
    ('num_ref_frames_in_pic_order_cnt_cycle', __u8),
    ('offset_for_ref_frame', __s32 * int(255)),
    ('offset_for_non_ref_pic', __s32),
    ('offset_for_top_to_bottom_field', __s32),
    ('pic_width_in_mbs_minus1', __u16),
    ('pic_height_in_map_units_minus1', __u16),
    ('flags', __u32),
]


class struct_v4l2_ctrl_h264_pps(Structure):
    pass

struct_v4l2_ctrl_h264_pps.__slots__ = [
    'pic_parameter_set_id',
    'seq_parameter_set_id',
    'num_slice_groups_minus1',
    'num_ref_idx_l0_default_active_minus1',
    'num_ref_idx_l1_default_active_minus1',
    'weighted_bipred_idc',
    'pic_init_qp_minus26',
    'pic_init_qs_minus26',
    'chroma_qp_index_offset',
    'second_chroma_qp_index_offset',
    'flags',
]
struct_v4l2_ctrl_h264_pps._fields_ = [
    ('pic_parameter_set_id', __u8),
    ('seq_parameter_set_id', __u8),
    ('num_slice_groups_minus1', __u8),
    ('num_ref_idx_l0_default_active_minus1', __u8),
    ('num_ref_idx_l1_default_active_minus1', __u8),
    ('weighted_bipred_idc', __u8),
    ('pic_init_qp_minus26', __s8),
    ('pic_init_qs_minus26', __s8),
    ('chroma_qp_index_offset', __s8),
    ('second_chroma_qp_index_offset', __s8),
    ('flags', __u16),
]


class struct_v4l2_ctrl_h264_scaling_matrix(Structure):
    pass

struct_v4l2_ctrl_h264_scaling_matrix.__slots__ = [
    'scaling_list_4x4',
    'scaling_list_8x8',
]
struct_v4l2_ctrl_h264_scaling_matrix._fields_ = [
    ('scaling_list_4x4', (__u8 * int(16)) * int(6)),
    ('scaling_list_8x8', (__u8 * int(64)) * int(6)),
]


class struct_v4l2_h264_weight_factors(Structure):
    pass

struct_v4l2_h264_weight_factors.__slots__ = [
    'luma_weight',
    'luma_offset',
    'chroma_weight',
    'chroma_offset',
]
struct_v4l2_h264_weight_factors._fields_ = [
    ('luma_weight', __s16 * int(32)),
    ('luma_offset', __s16 * int(32)),
    ('chroma_weight', (__s16 * int(2)) * int(32)),
    ('chroma_offset', (__s16 * int(2)) * int(32)),
]


class struct_v4l2_ctrl_h264_pred_weights(Structure):
    pass

struct_v4l2_ctrl_h264_pred_weights.__slots__ = [
    'luma_log2_weight_denom',
    'chroma_log2_weight_denom',
    'weight_factors',
]
struct_v4l2_ctrl_h264_pred_weights._fields_ = [
    ('luma_log2_weight_denom', __u16),
    ('chroma_log2_weight_denom', __u16),
    ('weight_factors', struct_v4l2_h264_weight_factors * int(2)),
]


class struct_v4l2_h264_reference(Structure):
    pass

struct_v4l2_h264_reference.__slots__ = [
    'fields',
    'index',
]
struct_v4l2_h264_reference._fields_ = [
    ('fields', __u8),
    ('index', __u8),
]


class struct_v4l2_ctrl_h264_slice_params(Structure):
    pass

struct_v4l2_ctrl_h264_slice_params.__slots__ = [
    'header_bit_size',
    'first_mb_in_slice',
    'slice_type',
    'colour_plane_id',
    'redundant_pic_cnt',
    'cabac_init_idc',
    'slice_qp_delta',
    'slice_qs_delta',
    'disable_deblocking_filter_idc',
    'slice_alpha_c0_offset_div2',
    'slice_beta_offset_div2',
    'num_ref_idx_l0_active_minus1',
    'num_ref_idx_l1_active_minus1',
    'reserved',
    'ref_pic_list0',
    'ref_pic_list1',
    'flags',
]
struct_v4l2_ctrl_h264_slice_params._fields_ = [
    ('header_bit_size', __u32),
    ('first_mb_in_slice', __u32),
    ('slice_type', __u8),
    ('colour_plane_id', __u8),
    ('redundant_pic_cnt', __u8),
    ('cabac_init_idc', __u8),
    ('slice_qp_delta', __s8),
    ('slice_qs_delta', __s8),
    ('disable_deblocking_filter_idc', __u8),
    ('slice_alpha_c0_offset_div2', __s8),
    ('slice_beta_offset_div2', __s8),
    ('num_ref_idx_l0_active_minus1', __u8),
    ('num_ref_idx_l1_active_minus1', __u8),
    ('reserved', __u8),
    ('ref_pic_list0', struct_v4l2_h264_reference * int((2 * 16))),
    ('ref_pic_list1', struct_v4l2_h264_reference * int((2 * 16))),
    ('flags', __u32),
]


class struct_v4l2_h264_dpb_entry(Structure):
    pass

struct_v4l2_h264_dpb_entry.__slots__ = [
    'reference_ts',
    'pic_num',
    'frame_num',
    'fields',
    'reserved',
    'top_field_order_cnt',
    'bottom_field_order_cnt',
    'flags',
]
struct_v4l2_h264_dpb_entry._fields_ = [
    ('reference_ts', __u64),
    ('pic_num', __u32),
    ('frame_num', __u16),
    ('fields', __u8),
    ('reserved', __u8 * int(5)),
    ('top_field_order_cnt', __s32),
    ('bottom_field_order_cnt', __s32),
    ('flags', __u32),
]


class struct_v4l2_ctrl_h264_decode_params(Structure):
    pass

struct_v4l2_ctrl_h264_decode_params.__slots__ = [
    'dpb',
    'nal_ref_idc',
    'frame_num',
    'top_field_order_cnt',
    'bottom_field_order_cnt',
    'idr_pic_id',
    'pic_order_cnt_lsb',
    'delta_pic_order_cnt_bottom',
    'delta_pic_order_cnt0',
    'delta_pic_order_cnt1',
    'dec_ref_pic_marking_bit_size',
    'pic_order_cnt_bit_size',
    'slice_group_change_cycle',
    'reserved',
    'flags',
]
struct_v4l2_ctrl_h264_decode_params._fields_ = [
    ('dpb', struct_v4l2_h264_dpb_entry * int(16)),
    ('nal_ref_idc', __u16),
    ('frame_num', __u16),
    ('top_field_order_cnt', __s32),
    ('bottom_field_order_cnt', __s32),
    ('idr_pic_id', __u16),
    ('pic_order_cnt_lsb', __u16),
    ('delta_pic_order_cnt_bottom', __s32),
    ('delta_pic_order_cnt0', __s32),
    ('delta_pic_order_cnt1', __s32),
    ('dec_ref_pic_marking_bit_size', __u32),
    ('pic_order_cnt_bit_size', __u32),
    ('slice_group_change_cycle', __u32),
    ('reserved', __u32),
    ('flags', __u32),
]


class struct_v4l2_ctrl_fwht_params(Structure):
    pass

struct_v4l2_ctrl_fwht_params.__slots__ = [
    'backward_ref_ts',
    'version',
    'width',
    'height',
    'flags',
    'colorspace',
    'xfer_func',
    'ycbcr_enc',
    'quantization',
]
struct_v4l2_ctrl_fwht_params._fields_ = [
    ('backward_ref_ts', __u64),
    ('version', __u32),
    ('width', __u32),
    ('height', __u32),
    ('flags', __u32),
    ('colorspace', __u32),
    ('xfer_func', __u32),
    ('ycbcr_enc', __u32),
    ('quantization', __u32),
]


class struct_v4l2_vp8_segment(Structure):
    pass

struct_v4l2_vp8_segment.__slots__ = [
    'quant_update',
    'lf_update',
    'segment_probs',
    'padding',
    'flags',
]
struct_v4l2_vp8_segment._fields_ = [
    ('quant_update', __s8 * int(4)),
    ('lf_update', __s8 * int(4)),
    ('segment_probs', __u8 * int(3)),
    ('padding', __u8),
    ('flags', __u32),
]


class struct_v4l2_vp8_loop_filter(Structure):
    pass

struct_v4l2_vp8_loop_filter.__slots__ = [
    'ref_frm_delta',
    'mb_mode_delta',
    'sharpness_level',
    'level',
    'padding',
    'flags',
]
struct_v4l2_vp8_loop_filter._fields_ = [
    ('ref_frm_delta', __s8 * int(4)),
    ('mb_mode_delta', __s8 * int(4)),
    ('sharpness_level', __u8),
    ('level', __u8),
    ('padding', __u16),
    ('flags', __u32),
]


class struct_v4l2_vp8_quantization(Structure):
    pass

struct_v4l2_vp8_quantization.__slots__ = [
    'y_ac_qi',
    'y_dc_delta',
    'y2_dc_delta',
    'y2_ac_delta',
    'uv_dc_delta',
    'uv_ac_delta',
    'padding',
]
struct_v4l2_vp8_quantization._fields_ = [
    ('y_ac_qi', __u8),
    ('y_dc_delta', __s8),
    ('y2_dc_delta', __s8),
    ('y2_ac_delta', __s8),
    ('uv_dc_delta', __s8),
    ('uv_ac_delta', __s8),
    ('padding', __u16),
]


class struct_v4l2_vp8_entropy(Structure):
    pass

struct_v4l2_vp8_entropy.__slots__ = [
    'coeff_probs',
    'y_mode_probs',
    'uv_mode_probs',
    'mv_probs',
    'padding',
]
struct_v4l2_vp8_entropy._fields_ = [
    ('coeff_probs', (((__u8 * int(11)) * int(3)) * int(8)) * int(4)),
    ('y_mode_probs', __u8 * int(4)),
    ('uv_mode_probs', __u8 * int(3)),
    ('mv_probs', (__u8 * int(19)) * int(2)),
    ('padding', __u8 * int(3)),
]


class struct_v4l2_vp8_entropy_coder_state(Structure):
    pass

struct_v4l2_vp8_entropy_coder_state.__slots__ = [
    'range',
    'value',
    'bit_count',
    'padding',
]
struct_v4l2_vp8_entropy_coder_state._fields_ = [
    ('range', __u8),
    ('value', __u8),
    ('bit_count', __u8),
    ('padding', __u8),
]


class struct_v4l2_ctrl_vp8_frame(Structure):
    pass

struct_v4l2_ctrl_vp8_frame.__slots__ = [
    'segment',
    'lf',
    'quant',
    'entropy',
    'coder_state',
    'width',
    'height',
    'horizontal_scale',
    'vertical_scale',
    'version',
    'prob_skip_false',
    'prob_intra',
    'prob_last',
    'prob_gf',
    'num_dct_parts',
    'first_part_size',
    'first_part_header_bits',
    'dct_part_sizes',
    'last_frame_ts',
    'golden_frame_ts',
    'alt_frame_ts',
    'flags',
]
struct_v4l2_ctrl_vp8_frame._fields_ = [
    ('segment', struct_v4l2_vp8_segment),
    ('lf', struct_v4l2_vp8_loop_filter),
    ('quant', struct_v4l2_vp8_quantization),
    ('entropy', struct_v4l2_vp8_entropy),
    ('coder_state', struct_v4l2_vp8_entropy_coder_state),
    ('width', __u16),
    ('height', __u16),
    ('horizontal_scale', __u8),
    ('vertical_scale', __u8),
    ('version', __u8),
    ('prob_skip_false', __u8),
    ('prob_intra', __u8),
    ('prob_last', __u8),
    ('prob_gf', __u8),
    ('num_dct_parts', __u8),
    ('first_part_size', __u32),
    ('first_part_header_bits', __u32),
    ('dct_part_sizes', __u32 * int(8)),
    ('last_frame_ts', __u64),
    ('golden_frame_ts', __u64),
    ('alt_frame_ts', __u64),
    ('flags', __u64),
]


class struct_v4l2_ctrl_mpeg2_sequence(Structure):
    pass

struct_v4l2_ctrl_mpeg2_sequence.__slots__ = [
    'horizontal_size',
    'vertical_size',
    'vbv_buffer_size',
    'profile_and_level_indication',
    'chroma_format',
    'flags',
]
struct_v4l2_ctrl_mpeg2_sequence._fields_ = [
    ('horizontal_size', __u16),
    ('vertical_size', __u16),
    ('vbv_buffer_size', __u32),
    ('profile_and_level_indication', __u16),
    ('chroma_format', __u8),
    ('flags', __u8),
]


class struct_v4l2_ctrl_mpeg2_picture(Structure):
    pass

struct_v4l2_ctrl_mpeg2_picture.__slots__ = [
    'backward_ref_ts',
    'forward_ref_ts',
    'flags',
    'f_code',
    'picture_coding_type',
    'picture_structure',
    'intra_dc_precision',
    'reserved',
]
struct_v4l2_ctrl_mpeg2_picture._fields_ = [
    ('backward_ref_ts', __u64),
    ('forward_ref_ts', __u64),
    ('flags', __u32),
    ('f_code', (__u8 * int(2)) * int(2)),
    ('picture_coding_type', __u8),
    ('picture_structure', __u8),
    ('intra_dc_precision', __u8),
    ('reserved', __u8 * int(5)),
]


class struct_v4l2_ctrl_mpeg2_quantisation(Structure):
    pass

struct_v4l2_ctrl_mpeg2_quantisation.__slots__ = [
    'intra_quantiser_matrix',
    'non_intra_quantiser_matrix',
    'chroma_intra_quantiser_matrix',
    'chroma_non_intra_quantiser_matrix',
]
struct_v4l2_ctrl_mpeg2_quantisation._fields_ = [
    ('intra_quantiser_matrix', __u8 * int(64)),
    ('non_intra_quantiser_matrix', __u8 * int(64)),
    ('chroma_intra_quantiser_matrix', __u8 * int(64)),
    ('chroma_non_intra_quantiser_matrix', __u8 * int(64)),
]

enum_v4l2_stateless_hevc_decode_mode = c_int

V4L2_STATELESS_HEVC_DECODE_MODE_SLICE_BASED = 0

V4L2_STATELESS_HEVC_DECODE_MODE_FRAME_BASED = (V4L2_STATELESS_HEVC_DECODE_MODE_SLICE_BASED + 1)

enum_v4l2_stateless_hevc_start_code = c_int

V4L2_STATELESS_HEVC_START_CODE_NONE = 0

V4L2_STATELESS_HEVC_START_CODE_ANNEX_B = (V4L2_STATELESS_HEVC_START_CODE_NONE + 1)


class struct_v4l2_ctrl_hevc_sps(Structure):
    pass

struct_v4l2_ctrl_hevc_sps.__slots__ = [
    'video_parameter_set_id',
    'seq_parameter_set_id',
    'pic_width_in_luma_samples',
    'pic_height_in_luma_samples',
    'bit_depth_luma_minus8',
    'bit_depth_chroma_minus8',
    'log2_max_pic_order_cnt_lsb_minus4',
    'sps_max_dec_pic_buffering_minus1',
    'sps_max_num_reorder_pics',
    'sps_max_latency_increase_plus1',
    'log2_min_luma_coding_block_size_minus3',
    'log2_diff_max_min_luma_coding_block_size',
    'log2_min_luma_transform_block_size_minus2',
    'log2_diff_max_min_luma_transform_block_size',
    'max_transform_hierarchy_depth_inter',
    'max_transform_hierarchy_depth_intra',
    'pcm_sample_bit_depth_luma_minus1',
    'pcm_sample_bit_depth_chroma_minus1',
    'log2_min_pcm_luma_coding_block_size_minus3',
    'log2_diff_max_min_pcm_luma_coding_block_size',
    'num_short_term_ref_pic_sets',
    'num_long_term_ref_pics_sps',
    'chroma_format_idc',
    'sps_max_sub_layers_minus1',
    'reserved',
    'flags',
]
struct_v4l2_ctrl_hevc_sps._fields_ = [
    ('video_parameter_set_id', __u8),
    ('seq_parameter_set_id', __u8),
    ('pic_width_in_luma_samples', __u16),
    ('pic_height_in_luma_samples', __u16),
    ('bit_depth_luma_minus8', __u8),
    ('bit_depth_chroma_minus8', __u8),
    ('log2_max_pic_order_cnt_lsb_minus4', __u8),
    ('sps_max_dec_pic_buffering_minus1', __u8),
    ('sps_max_num_reorder_pics', __u8),
    ('sps_max_latency_increase_plus1', __u8),
    ('log2_min_luma_coding_block_size_minus3', __u8),
    ('log2_diff_max_min_luma_coding_block_size', __u8),
    ('log2_min_luma_transform_block_size_minus2', __u8),
    ('log2_diff_max_min_luma_transform_block_size', __u8),
    ('max_transform_hierarchy_depth_inter', __u8),
    ('max_transform_hierarchy_depth_intra', __u8),
    ('pcm_sample_bit_depth_luma_minus1', __u8),
    ('pcm_sample_bit_depth_chroma_minus1', __u8),
    ('log2_min_pcm_luma_coding_block_size_minus3', __u8),
    ('log2_diff_max_min_pcm_luma_coding_block_size', __u8),
    ('num_short_term_ref_pic_sets', __u8),
    ('num_long_term_ref_pics_sps', __u8),
    ('chroma_format_idc', __u8),
    ('sps_max_sub_layers_minus1', __u8),
    ('reserved', __u8 * int(6)),
    ('flags', __u64),
]


class struct_v4l2_ctrl_hevc_pps(Structure):
    pass

struct_v4l2_ctrl_hevc_pps.__slots__ = [
    'pic_parameter_set_id',
    'num_extra_slice_header_bits',
    'num_ref_idx_l0_default_active_minus1',
    'num_ref_idx_l1_default_active_minus1',
    'init_qp_minus26',
    'diff_cu_qp_delta_depth',
    'pps_cb_qp_offset',
    'pps_cr_qp_offset',
    'num_tile_columns_minus1',
    'num_tile_rows_minus1',
    'column_width_minus1',
    'row_height_minus1',
    'pps_beta_offset_div2',
    'pps_tc_offset_div2',
    'log2_parallel_merge_level_minus2',
    'reserved',
    'flags',
]
struct_v4l2_ctrl_hevc_pps._fields_ = [
    ('pic_parameter_set_id', __u8),
    ('num_extra_slice_header_bits', __u8),
    ('num_ref_idx_l0_default_active_minus1', __u8),
    ('num_ref_idx_l1_default_active_minus1', __u8),
    ('init_qp_minus26', __s8),
    ('diff_cu_qp_delta_depth', __u8),
    ('pps_cb_qp_offset', __s8),
    ('pps_cr_qp_offset', __s8),
    ('num_tile_columns_minus1', __u8),
    ('num_tile_rows_minus1', __u8),
    ('column_width_minus1', __u8 * int(20)),
    ('row_height_minus1', __u8 * int(22)),
    ('pps_beta_offset_div2', __s8),
    ('pps_tc_offset_div2', __s8),
    ('log2_parallel_merge_level_minus2', __u8),
    ('reserved', __u8),
    ('flags', __u64),
]


class struct_v4l2_hevc_dpb_entry(Structure):
    pass

struct_v4l2_hevc_dpb_entry.__slots__ = [
    'timestamp',
    'flags',
    'field_pic',
    'reserved',
    'pic_order_cnt_val',
]
struct_v4l2_hevc_dpb_entry._fields_ = [
    ('timestamp', __u64),
    ('flags', __u8),
    ('field_pic', __u8),
    ('reserved', __u16),
    ('pic_order_cnt_val', __s32),
]


class struct_v4l2_hevc_pred_weight_table(Structure):
    pass

struct_v4l2_hevc_pred_weight_table.__slots__ = [
    'delta_luma_weight_l0',
    'luma_offset_l0',
    'delta_chroma_weight_l0',
    'chroma_offset_l0',
    'delta_luma_weight_l1',
    'luma_offset_l1',
    'delta_chroma_weight_l1',
    'chroma_offset_l1',
    'luma_log2_weight_denom',
    'delta_chroma_log2_weight_denom',
]
struct_v4l2_hevc_pred_weight_table._fields_ = [
    ('delta_luma_weight_l0', __s8 * int(16)),
    ('luma_offset_l0', __s8 * int(16)),
    ('delta_chroma_weight_l0', (__s8 * int(2)) * int(16)),
    ('chroma_offset_l0', (__s8 * int(2)) * int(16)),
    ('delta_luma_weight_l1', __s8 * int(16)),
    ('luma_offset_l1', __s8 * int(16)),
    ('delta_chroma_weight_l1', (__s8 * int(2)) * int(16)),
    ('chroma_offset_l1', (__s8 * int(2)) * int(16)),
    ('luma_log2_weight_denom', __u8),
    ('delta_chroma_log2_weight_denom', __s8),
]


class struct_v4l2_ctrl_hevc_slice_params(Structure):
    pass

struct_v4l2_ctrl_hevc_slice_params.__slots__ = [
    'bit_size',
    'data_byte_offset',
    'num_entry_point_offsets',
    'nal_unit_type',
    'nuh_temporal_id_plus1',
    'slice_type',
    'colour_plane_id',
    'slice_pic_order_cnt',
    'num_ref_idx_l0_active_minus1',
    'num_ref_idx_l1_active_minus1',
    'collocated_ref_idx',
    'five_minus_max_num_merge_cand',
    'slice_qp_delta',
    'slice_cb_qp_offset',
    'slice_cr_qp_offset',
    'slice_act_y_qp_offset',
    'slice_act_cb_qp_offset',
    'slice_act_cr_qp_offset',
    'slice_beta_offset_div2',
    'slice_tc_offset_div2',
    'pic_struct',
    'reserved0',
    'slice_segment_addr',
    'ref_idx_l0',
    'ref_idx_l1',
    'short_term_ref_pic_set_size',
    'long_term_ref_pic_set_size',
    'pred_weight_table',
    'reserved1',
    'flags',
]
struct_v4l2_ctrl_hevc_slice_params._fields_ = [
    ('bit_size', __u32),
    ('data_byte_offset', __u32),
    ('num_entry_point_offsets', __u32),
    ('nal_unit_type', __u8),
    ('nuh_temporal_id_plus1', __u8),
    ('slice_type', __u8),
    ('colour_plane_id', __u8),
    ('slice_pic_order_cnt', __s32),
    ('num_ref_idx_l0_active_minus1', __u8),
    ('num_ref_idx_l1_active_minus1', __u8),
    ('collocated_ref_idx', __u8),
    ('five_minus_max_num_merge_cand', __u8),
    ('slice_qp_delta', __s8),
    ('slice_cb_qp_offset', __s8),
    ('slice_cr_qp_offset', __s8),
    ('slice_act_y_qp_offset', __s8),
    ('slice_act_cb_qp_offset', __s8),
    ('slice_act_cr_qp_offset', __s8),
    ('slice_beta_offset_div2', __s8),
    ('slice_tc_offset_div2', __s8),
    ('pic_struct', __u8),
    ('reserved0', __u8 * int(3)),
    ('slice_segment_addr', __u32),
    ('ref_idx_l0', __u8 * int(16)),
    ('ref_idx_l1', __u8 * int(16)),
    ('short_term_ref_pic_set_size', __u16),
    ('long_term_ref_pic_set_size', __u16),
    ('pred_weight_table', struct_v4l2_hevc_pred_weight_table),
    ('reserved1', __u8 * int(2)),
    ('flags', __u64),
]


class struct_v4l2_ctrl_hevc_decode_params(Structure):
    pass

struct_v4l2_ctrl_hevc_decode_params.__slots__ = [
    'pic_order_cnt_val',
    'short_term_ref_pic_set_size',
    'long_term_ref_pic_set_size',
    'num_active_dpb_entries',
    'num_poc_st_curr_before',
    'num_poc_st_curr_after',
    'num_poc_lt_curr',
    'poc_st_curr_before',
    'poc_st_curr_after',
    'poc_lt_curr',
    'num_delta_pocs_of_ref_rps_idx',
    'reserved',
    'dpb',
    'flags',
]
struct_v4l2_ctrl_hevc_decode_params._fields_ = [
    ('pic_order_cnt_val', __s32),
    ('short_term_ref_pic_set_size', __u16),
    ('long_term_ref_pic_set_size', __u16),
    ('num_active_dpb_entries', __u8),
    ('num_poc_st_curr_before', __u8),
    ('num_poc_st_curr_after', __u8),
    ('num_poc_lt_curr', __u8),
    ('poc_st_curr_before', __u8 * int(16)),
    ('poc_st_curr_after', __u8 * int(16)),
    ('poc_lt_curr', __u8 * int(16)),
    ('num_delta_pocs_of_ref_rps_idx', __u8),
    ('reserved', __u8 * int(3)),
    ('dpb', struct_v4l2_hevc_dpb_entry * int(16)),
    ('flags', __u64),
]


class struct_v4l2_ctrl_hevc_scaling_matrix(Structure):
    pass

struct_v4l2_ctrl_hevc_scaling_matrix.__slots__ = [
    'scaling_list_4x4',
    'scaling_list_8x8',
    'scaling_list_16x16',
    'scaling_list_32x32',
    'scaling_list_dc_coef_16x16',
    'scaling_list_dc_coef_32x32',
]
struct_v4l2_ctrl_hevc_scaling_matrix._fields_ = [
    ('scaling_list_4x4', (__u8 * int(16)) * int(6)),
    ('scaling_list_8x8', (__u8 * int(64)) * int(6)),
    ('scaling_list_16x16', (__u8 * int(64)) * int(6)),
    ('scaling_list_32x32', (__u8 * int(64)) * int(2)),
    ('scaling_list_dc_coef_16x16', __u8 * int(6)),
    ('scaling_list_dc_coef_32x32', __u8 * int(2)),
]


class struct_v4l2_ctrl_hdr10_cll_info(Structure):
    pass

struct_v4l2_ctrl_hdr10_cll_info.__slots__ = [
    'max_content_light_level',
    'max_pic_average_light_level',
]
struct_v4l2_ctrl_hdr10_cll_info._fields_ = [
    ('max_content_light_level', __u16),
    ('max_pic_average_light_level', __u16),
]


class struct_v4l2_ctrl_hdr10_mastering_display(Structure):
    pass

struct_v4l2_ctrl_hdr10_mastering_display.__slots__ = [
    'display_primaries_x',
    'display_primaries_y',
    'white_point_x',
    'white_point_y',
    'max_display_mastering_luminance',
    'min_display_mastering_luminance',
]
struct_v4l2_ctrl_hdr10_mastering_display._fields_ = [
    ('display_primaries_x', __u16 * int(3)),
    ('display_primaries_y', __u16 * int(3)),
    ('white_point_x', __u16),
    ('white_point_y', __u16),
    ('max_display_mastering_luminance', __u32),
    ('min_display_mastering_luminance', __u32),
]


class struct_v4l2_vp9_loop_filter(Structure):
    pass

struct_v4l2_vp9_loop_filter.__slots__ = [
    'ref_deltas',
    'mode_deltas',
    'level',
    'sharpness',
    'flags',
    'reserved',
]
struct_v4l2_vp9_loop_filter._fields_ = [
    ('ref_deltas', __s8 * int(4)),
    ('mode_deltas', __s8 * int(2)),
    ('level', __u8),
    ('sharpness', __u8),
    ('flags', __u8),
    ('reserved', __u8 * int(7)),
]


class struct_v4l2_vp9_quantization(Structure):
    pass

struct_v4l2_vp9_quantization.__slots__ = [
    'base_q_idx',
    'delta_q_y_dc',
    'delta_q_uv_dc',
    'delta_q_uv_ac',
    'reserved',
]
struct_v4l2_vp9_quantization._fields_ = [
    ('base_q_idx', __u8),
    ('delta_q_y_dc', __s8),
    ('delta_q_uv_dc', __s8),
    ('delta_q_uv_ac', __s8),
    ('reserved', __u8 * int(4)),
]


class struct_v4l2_vp9_segmentation(Structure):
    pass

struct_v4l2_vp9_segmentation.__slots__ = [
    'feature_data',
    'feature_enabled',
    'tree_probs',
    'pred_probs',
    'flags',
    'reserved',
]
struct_v4l2_vp9_segmentation._fields_ = [
    ('feature_data', (__s16 * int(4)) * int(8)),
    ('feature_enabled', __u8 * int(8)),
    ('tree_probs', __u8 * int(7)),
    ('pred_probs', __u8 * int(3)),
    ('flags', __u8),
    ('reserved', __u8 * int(5)),
]


class struct_v4l2_ctrl_vp9_frame(Structure):
    pass

struct_v4l2_ctrl_vp9_frame.__slots__ = [
    'lf',
    'quant',
    'seg',
    'flags',
    'compressed_header_size',
    'uncompressed_header_size',
    'frame_width_minus_1',
    'frame_height_minus_1',
    'render_width_minus_1',
    'render_height_minus_1',
    'last_frame_ts',
    'golden_frame_ts',
    'alt_frame_ts',
    'ref_frame_sign_bias',
    'reset_frame_context',
    'frame_context_idx',
    'profile',
    'bit_depth',
    'interpolation_filter',
    'tile_cols_log2',
    'tile_rows_log2',
    'reference_mode',
    'reserved',
]
struct_v4l2_ctrl_vp9_frame._fields_ = [
    ('lf', struct_v4l2_vp9_loop_filter),
    ('quant', struct_v4l2_vp9_quantization),
    ('seg', struct_v4l2_vp9_segmentation),
    ('flags', __u32),
    ('compressed_header_size', __u16),
    ('uncompressed_header_size', __u16),
    ('frame_width_minus_1', __u16),
    ('frame_height_minus_1', __u16),
    ('render_width_minus_1', __u16),
    ('render_height_minus_1', __u16),
    ('last_frame_ts', __u64),
    ('golden_frame_ts', __u64),
    ('alt_frame_ts', __u64),
    ('ref_frame_sign_bias', __u8),
    ('reset_frame_context', __u8),
    ('frame_context_idx', __u8),
    ('profile', __u8),
    ('bit_depth', __u8),
    ('interpolation_filter', __u8),
    ('tile_cols_log2', __u8),
    ('tile_rows_log2', __u8),
    ('reference_mode', __u8),
    ('reserved', __u8 * int(7)),
]


class struct_v4l2_vp9_mv_probs(Structure):
    pass

struct_v4l2_vp9_mv_probs.__slots__ = [
    'joint',
    'sign',
    'classes',
    'class0_bit',
    'bits',
    'class0_fr',
    'fr',
    'class0_hp',
    'hp',
]
struct_v4l2_vp9_mv_probs._fields_ = [
    ('joint', __u8 * int(3)),
    ('sign', __u8 * int(2)),
    ('classes', (__u8 * int(10)) * int(2)),
    ('class0_bit', __u8 * int(2)),
    ('bits', (__u8 * int(10)) * int(2)),
    ('class0_fr', ((__u8 * int(3)) * int(2)) * int(2)),
    ('fr', (__u8 * int(3)) * int(2)),
    ('class0_hp', __u8 * int(2)),
    ('hp', __u8 * int(2)),
]


class struct_v4l2_ctrl_vp9_compressed_hdr(Structure):
    pass

struct_v4l2_ctrl_vp9_compressed_hdr.__slots__ = [
    'tx_mode',
    'tx8',
    'tx16',
    'tx32',
    'coef',
    'skip',
    'inter_mode',
    'interp_filter',
    'is_inter',
    'comp_mode',
    'single_ref',
    'comp_ref',
    'y_mode',
    'uv_mode',
    'partition',
    'mv',
]
struct_v4l2_ctrl_vp9_compressed_hdr._fields_ = [
    ('tx_mode', __u8),
    ('tx8', (__u8 * int(1)) * int(2)),
    ('tx16', (__u8 * int(2)) * int(2)),
    ('tx32', (__u8 * int(3)) * int(2)),
    ('coef', (((((__u8 * int(3)) * int(6)) * int(6)) * int(2)) * int(2)) * int(4)),
    ('skip', __u8 * int(3)),
    ('inter_mode', (__u8 * int(3)) * int(7)),
    ('interp_filter', (__u8 * int(2)) * int(4)),
    ('is_inter', __u8 * int(4)),
    ('comp_mode', __u8 * int(5)),
    ('single_ref', (__u8 * int(2)) * int(5)),
    ('comp_ref', __u8 * int(5)),
    ('y_mode', (__u8 * int(9)) * int(4)),
    ('uv_mode', (__u8 * int(9)) * int(10)),
    ('partition', (__u8 * int(3)) * int(16)),
    ('mv', struct_v4l2_vp9_mv_probs),
]


class struct_v4l2_ctrl_av1_sequence(Structure):
    pass

struct_v4l2_ctrl_av1_sequence.__slots__ = [
    'flags',
    'seq_profile',
    'order_hint_bits',
    'bit_depth',
    'reserved',
    'max_frame_width_minus_1',
    'max_frame_height_minus_1',
]
struct_v4l2_ctrl_av1_sequence._fields_ = [
    ('flags', __u32),
    ('seq_profile', __u8),
    ('order_hint_bits', __u8),
    ('bit_depth', __u8),
    ('reserved', __u8),
    ('max_frame_width_minus_1', __u16),
    ('max_frame_height_minus_1', __u16),
]


class struct_v4l2_ctrl_av1_tile_group_entry(Structure):
    pass

struct_v4l2_ctrl_av1_tile_group_entry.__slots__ = [
    'tile_offset',
    'tile_size',
    'tile_row',
    'tile_col',
]
struct_v4l2_ctrl_av1_tile_group_entry._fields_ = [
    ('tile_offset', __u32),
    ('tile_size', __u32),
    ('tile_row', __u32),
    ('tile_col', __u32),
]

enum_v4l2_av1_warp_model = c_int

V4L2_AV1_WARP_MODEL_IDENTITY = 0

V4L2_AV1_WARP_MODEL_TRANSLATION = 1

V4L2_AV1_WARP_MODEL_ROTZOOM = 2

V4L2_AV1_WARP_MODEL_AFFINE = 3

enum_v4l2_av1_reference_frame = c_int

V4L2_AV1_REF_INTRA_FRAME = 0

V4L2_AV1_REF_LAST_FRAME = 1

V4L2_AV1_REF_LAST2_FRAME = 2

V4L2_AV1_REF_LAST3_FRAME = 3

V4L2_AV1_REF_GOLDEN_FRAME = 4

V4L2_AV1_REF_BWDREF_FRAME = 5

V4L2_AV1_REF_ALTREF2_FRAME = 6

V4L2_AV1_REF_ALTREF_FRAME = 7


class struct_v4l2_av1_global_motion(Structure):
    pass

struct_v4l2_av1_global_motion.__slots__ = [
    'flags',
    'type',
    'params',
    'invalid',
    'reserved',
]
struct_v4l2_av1_global_motion._fields_ = [
    ('flags', __u8 * int(8)),
    ('type', enum_v4l2_av1_warp_model * int(8)),
    ('params', (__s32 * int(6)) * int(8)),
    ('invalid', __u8),
    ('reserved', __u8 * int(3)),
]

enum_v4l2_av1_frame_restoration_type = c_int

V4L2_AV1_FRAME_RESTORE_NONE = 0

V4L2_AV1_FRAME_RESTORE_WIENER = 1

V4L2_AV1_FRAME_RESTORE_SGRPROJ = 2

V4L2_AV1_FRAME_RESTORE_SWITCHABLE = 3


class struct_v4l2_av1_loop_restoration(Structure):
    pass

struct_v4l2_av1_loop_restoration.__slots__ = [
    'flags',
    'lr_unit_shift',
    'lr_uv_shift',
    'reserved',
    'frame_restoration_type',
    'loop_restoration_size',
]
struct_v4l2_av1_loop_restoration._fields_ = [
    ('flags', __u8),
    ('lr_unit_shift', __u8),
    ('lr_uv_shift', __u8),
    ('reserved', __u8),
    ('frame_restoration_type', enum_v4l2_av1_frame_restoration_type * int(3)),
    ('loop_restoration_size', __u32 * int(3)),
]


class struct_v4l2_av1_cdef(Structure):
    pass

struct_v4l2_av1_cdef.__slots__ = [
    'damping_minus_3',
    'bits',
    'y_pri_strength',
    'y_sec_strength',
    'uv_pri_strength',
    'uv_sec_strength',
]
struct_v4l2_av1_cdef._fields_ = [
    ('damping_minus_3', __u8),
    ('bits', __u8),
    ('y_pri_strength', __u8 * int(8)),
    ('y_sec_strength', __u8 * int(8)),
    ('uv_pri_strength', __u8 * int(8)),
    ('uv_sec_strength', __u8 * int(8)),
]

enum_v4l2_av1_segment_feature = c_int

V4L2_AV1_SEG_LVL_ALT_Q = 0

V4L2_AV1_SEG_LVL_ALT_LF_Y_V = 1

V4L2_AV1_SEG_LVL_REF_FRAME = 5

V4L2_AV1_SEG_LVL_REF_SKIP = 6

V4L2_AV1_SEG_LVL_REF_GLOBALMV = 7

V4L2_AV1_SEG_LVL_MAX = 8


class struct_v4l2_av1_segmentation(Structure):
    pass

struct_v4l2_av1_segmentation.__slots__ = [
    'flags',
    'last_active_seg_id',
    'feature_enabled',
    'feature_data',
]
struct_v4l2_av1_segmentation._fields_ = [
    ('flags', __u8),
    ('last_active_seg_id', __u8),
    ('feature_enabled', __u8 * int(8)),
    ('feature_data', (__s16 * int(V4L2_AV1_SEG_LVL_MAX)) * int(8)),
]


class struct_v4l2_av1_loop_filter(Structure):
    pass

struct_v4l2_av1_loop_filter.__slots__ = [
    'flags',
    'level',
    'sharpness',
    'ref_deltas',
    'mode_deltas',
    'delta_lf_res',
]
struct_v4l2_av1_loop_filter._fields_ = [
    ('flags', __u8),
    ('level', __u8 * int(4)),
    ('sharpness', __u8),
    ('ref_deltas', __s8 * int(8)),
    ('mode_deltas', __s8 * int(2)),
    ('delta_lf_res', __u8),
]


class struct_v4l2_av1_quantization(Structure):
    pass

struct_v4l2_av1_quantization.__slots__ = [
    'flags',
    'base_q_idx',
    'delta_q_y_dc',
    'delta_q_u_dc',
    'delta_q_u_ac',
    'delta_q_v_dc',
    'delta_q_v_ac',
    'qm_y',
    'qm_u',
    'qm_v',
    'delta_q_res',
]
struct_v4l2_av1_quantization._fields_ = [
    ('flags', __u8),
    ('base_q_idx', __u8),
    ('delta_q_y_dc', __s8),
    ('delta_q_u_dc', __s8),
    ('delta_q_u_ac', __s8),
    ('delta_q_v_dc', __s8),
    ('delta_q_v_ac', __s8),
    ('qm_y', __u8),
    ('qm_u', __u8),
    ('qm_v', __u8),
    ('delta_q_res', __u8),
]


class struct_v4l2_av1_tile_info(Structure):
    pass

struct_v4l2_av1_tile_info.__slots__ = [
    'flags',
    'context_update_tile_id',
    'tile_cols',
    'tile_rows',
    'mi_col_starts',
    'mi_row_starts',
    'width_in_sbs_minus_1',
    'height_in_sbs_minus_1',
    'tile_size_bytes',
    'reserved',
]
struct_v4l2_av1_tile_info._fields_ = [
    ('flags', __u8),
    ('context_update_tile_id', __u8),
    ('tile_cols', __u8),
    ('tile_rows', __u8),
    ('mi_col_starts', __u32 * int((64 + 1))),
    ('mi_row_starts', __u32 * int((64 + 1))),
    ('width_in_sbs_minus_1', __u32 * int(64)),
    ('height_in_sbs_minus_1', __u32 * int(64)),
    ('tile_size_bytes', __u8),
    ('reserved', __u8 * int(3)),
]

enum_v4l2_av1_frame_type = c_int

V4L2_AV1_KEY_FRAME = 0

V4L2_AV1_INTER_FRAME = 1

V4L2_AV1_INTRA_ONLY_FRAME = 2

V4L2_AV1_SWITCH_FRAME = 3

enum_v4l2_av1_interpolation_filter = c_int

V4L2_AV1_INTERPOLATION_FILTER_EIGHTTAP = 0

V4L2_AV1_INTERPOLATION_FILTER_EIGHTTAP_SMOOTH = 1

V4L2_AV1_INTERPOLATION_FILTER_EIGHTTAP_SHARP = 2

V4L2_AV1_INTERPOLATION_FILTER_BILINEAR = 3

V4L2_AV1_INTERPOLATION_FILTER_SWITCHABLE = 4

enum_v4l2_av1_tx_mode = c_int

V4L2_AV1_TX_MODE_ONLY_4X4 = 0

V4L2_AV1_TX_MODE_LARGEST = 1

V4L2_AV1_TX_MODE_SELECT = 2


class struct_v4l2_ctrl_av1_frame(Structure):
    pass

struct_v4l2_ctrl_av1_frame.__slots__ = [
    'tile_info',
    'quantization',
    'superres_denom',
    'segmentation',
    'loop_filter',
    'cdef',
    'skip_mode_frame',
    'primary_ref_frame',
    'loop_restoration',
    'global_motion',
    'flags',
    'frame_type',
    'order_hint',
    'upscaled_width',
    'interpolation_filter',
    'tx_mode',
    'frame_width_minus_1',
    'frame_height_minus_1',
    'render_width_minus_1',
    'render_height_minus_1',
    'current_frame_id',
    'buffer_removal_time',
    'reserved',
    'order_hints',
    'reference_frame_ts',
    'ref_frame_idx',
    'refresh_frame_flags',
]
struct_v4l2_ctrl_av1_frame._fields_ = [
    ('tile_info', struct_v4l2_av1_tile_info),
    ('quantization', struct_v4l2_av1_quantization),
    ('superres_denom', __u8),
    ('segmentation', struct_v4l2_av1_segmentation),
    ('loop_filter', struct_v4l2_av1_loop_filter),
    ('cdef', struct_v4l2_av1_cdef),
    ('skip_mode_frame', __u8 * int(2)),
    ('primary_ref_frame', __u8),
    ('loop_restoration', struct_v4l2_av1_loop_restoration),
    ('global_motion', struct_v4l2_av1_global_motion),
    ('flags', __u32),
    ('frame_type', enum_v4l2_av1_frame_type),
    ('order_hint', __u32),
    ('upscaled_width', __u32),
    ('interpolation_filter', enum_v4l2_av1_interpolation_filter),
    ('tx_mode', enum_v4l2_av1_tx_mode),
    ('frame_width_minus_1', __u32),
    ('frame_height_minus_1', __u32),
    ('render_width_minus_1', __u16),
    ('render_height_minus_1', __u16),
    ('current_frame_id', __u32),
    ('buffer_removal_time', __u32 * int((1 << 5))),
    ('reserved', __u8 * int(4)),
    ('order_hints', __u32 * int(8)),
    ('reference_frame_ts', __u64 * int(8)),
    ('ref_frame_idx', __s8 * int(7)),
    ('refresh_frame_flags', __u8),
]


class struct_v4l2_ctrl_av1_film_grain(Structure):
    pass

struct_v4l2_ctrl_av1_film_grain.__slots__ = [
    'flags',
    'cr_mult',
    'grain_seed',
    'film_grain_params_ref_idx',
    'num_y_points',
    'point_y_value',
    'point_y_scaling',
    'num_cb_points',
    'point_cb_value',
    'point_cb_scaling',
    'num_cr_points',
    'point_cr_value',
    'point_cr_scaling',
    'grain_scaling_minus_8',
    'ar_coeff_lag',
    'ar_coeffs_y_plus_128',
    'ar_coeffs_cb_plus_128',
    'ar_coeffs_cr_plus_128',
    'ar_coeff_shift_minus_6',
    'grain_scale_shift',
    'cb_mult',
    'cb_luma_mult',
    'cr_luma_mult',
    'cb_offset',
    'cr_offset',
    'reserved',
]
struct_v4l2_ctrl_av1_film_grain._fields_ = [
    ('flags', __u8),
    ('cr_mult', __u8),
    ('grain_seed', __u16),
    ('film_grain_params_ref_idx', __u8),
    ('num_y_points', __u8),
    ('point_y_value', __u8 * int((1 << 4))),
    ('point_y_scaling', __u8 * int((1 << 4))),
    ('num_cb_points', __u8),
    ('point_cb_value', __u8 * int((1 << 4))),
    ('point_cb_scaling', __u8 * int((1 << 4))),
    ('num_cr_points', __u8),
    ('point_cr_value', __u8 * int((1 << 4))),
    ('point_cr_scaling', __u8 * int((1 << 4))),
    ('grain_scaling_minus_8', __u8),
    ('ar_coeff_lag', __u8),
    ('ar_coeffs_y_plus_128', __u8 * int(25)),
    ('ar_coeffs_cb_plus_128', __u8 * int(25)),
    ('ar_coeffs_cr_plus_128', __u8 * int(25)),
    ('ar_coeff_shift_minus_6', __u8),
    ('grain_scale_shift', __u8),
    ('cb_mult', __u8),
    ('cb_luma_mult', __u8),
    ('cr_luma_mult', __u8),
    ('cb_offset', __u16),
    ('cr_offset', __u16),
    ('reserved', __u8 * int(4)),
]

enum_v4l2_field = c_int

V4L2_FIELD_ANY = 0

V4L2_FIELD_NONE = 1

V4L2_FIELD_TOP = 2

V4L2_FIELD_BOTTOM = 3

V4L2_FIELD_INTERLACED = 4

V4L2_FIELD_SEQ_TB = 5

V4L2_FIELD_SEQ_BT = 6

V4L2_FIELD_ALTERNATE = 7

V4L2_FIELD_INTERLACED_TB = 8

V4L2_FIELD_INTERLACED_BT = 9

enum_v4l2_buf_type = c_int

V4L2_BUF_TYPE_VIDEO_CAPTURE = 1

V4L2_BUF_TYPE_VIDEO_OUTPUT = 2

V4L2_BUF_TYPE_VIDEO_OVERLAY = 3

V4L2_BUF_TYPE_VBI_CAPTURE = 4

V4L2_BUF_TYPE_VBI_OUTPUT = 5

V4L2_BUF_TYPE_SLICED_VBI_CAPTURE = 6

V4L2_BUF_TYPE_SLICED_VBI_OUTPUT = 7

V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY = 8

V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE = 9

V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE = 10

V4L2_BUF_TYPE_SDR_CAPTURE = 11

V4L2_BUF_TYPE_SDR_OUTPUT = 12

V4L2_BUF_TYPE_META_CAPTURE = 13

V4L2_BUF_TYPE_META_OUTPUT = 14

V4L2_BUF_TYPE_PRIVATE = 0x80

enum_v4l2_tuner_type = c_int

V4L2_TUNER_RADIO = 1

V4L2_TUNER_ANALOG_TV = 2

V4L2_TUNER_DIGITAL_TV = 3

V4L2_TUNER_SDR = 4

V4L2_TUNER_RF = 5

enum_v4l2_memory = c_int

V4L2_MEMORY_MMAP = 1

V4L2_MEMORY_USERPTR = 2

V4L2_MEMORY_OVERLAY = 3

V4L2_MEMORY_DMABUF = 4

enum_v4l2_colorspace = c_int

V4L2_COLORSPACE_DEFAULT = 0

V4L2_COLORSPACE_SMPTE170M = 1

V4L2_COLORSPACE_SMPTE240M = 2

V4L2_COLORSPACE_REC709 = 3

V4L2_COLORSPACE_BT878 = 4

V4L2_COLORSPACE_470_SYSTEM_M = 5

V4L2_COLORSPACE_470_SYSTEM_BG = 6

V4L2_COLORSPACE_JPEG = 7

V4L2_COLORSPACE_SRGB = 8

V4L2_COLORSPACE_OPRGB = 9

V4L2_COLORSPACE_BT2020 = 10

V4L2_COLORSPACE_RAW = 11

V4L2_COLORSPACE_DCI_P3 = 12

enum_v4l2_xfer_func = c_int

V4L2_XFER_FUNC_DEFAULT = 0

V4L2_XFER_FUNC_709 = 1

V4L2_XFER_FUNC_SRGB = 2

V4L2_XFER_FUNC_OPRGB = 3

V4L2_XFER_FUNC_SMPTE240M = 4

V4L2_XFER_FUNC_NONE = 5

V4L2_XFER_FUNC_DCI_P3 = 6

V4L2_XFER_FUNC_SMPTE2084 = 7

enum_v4l2_ycbcr_encoding = c_int

V4L2_YCBCR_ENC_DEFAULT = 0

V4L2_YCBCR_ENC_601 = 1

V4L2_YCBCR_ENC_709 = 2

V4L2_YCBCR_ENC_XV601 = 3

V4L2_YCBCR_ENC_XV709 = 4

V4L2_YCBCR_ENC_SYCC = 5

V4L2_YCBCR_ENC_BT2020 = 6

V4L2_YCBCR_ENC_BT2020_CONST_LUM = 7

V4L2_YCBCR_ENC_SMPTE240M = 8

enum_v4l2_hsv_encoding = c_int

V4L2_HSV_ENC_180 = 128

V4L2_HSV_ENC_256 = 129

enum_v4l2_quantization = c_int

V4L2_QUANTIZATION_DEFAULT = 0

V4L2_QUANTIZATION_FULL_RANGE = 1

V4L2_QUANTIZATION_LIM_RANGE = 2

enum_v4l2_priority = c_int

V4L2_PRIORITY_UNSET = 0

V4L2_PRIORITY_BACKGROUND = 1

V4L2_PRIORITY_INTERACTIVE = 2

V4L2_PRIORITY_RECORD = 3

V4L2_PRIORITY_DEFAULT = V4L2_PRIORITY_INTERACTIVE


class struct_v4l2_rect(Structure):
    pass

struct_v4l2_rect.__slots__ = [
    'left',
    'top',
    'width',
    'height',
]
struct_v4l2_rect._fields_ = [
    ('left', __s32),
    ('top', __s32),
    ('width', __u32),
    ('height', __u32),
]


class struct_v4l2_fract(Structure):
    pass

struct_v4l2_fract.__slots__ = [
    'numerator',
    'denominator',
]
struct_v4l2_fract._fields_ = [
    ('numerator', __u32),
    ('denominator', __u32),
]


class struct_v4l2_area(Structure):
    pass

struct_v4l2_area.__slots__ = [
    'width',
    'height',
]
struct_v4l2_area._fields_ = [
    ('width', __u32),
    ('height', __u32),
]


class struct_v4l2_capability(Structure):
    pass

struct_v4l2_capability.__slots__ = [
    'driver',
    'card',
    'bus_info',
    'version',
    'capabilities',
    'device_caps',
    'reserved',
]
struct_v4l2_capability._fields_ = [
    ('driver', __u8 * int(16)),
    ('card', __u8 * int(32)),
    ('bus_info', __u8 * int(32)),
    ('version', __u32),
    ('capabilities', __u32),
    ('device_caps', __u32),
    ('reserved', __u32 * int(3)),
]


class union_anon_6(Union):
    pass

union_anon_6.__slots__ = [
    'ycbcr_enc',
    'hsv_enc',
]
union_anon_6._fields_ = [
    ('ycbcr_enc', __u32),
    ('hsv_enc', __u32),
]


class struct_v4l2_pix_format(Structure):
    pass

struct_v4l2_pix_format.__slots__ = [
    'width',
    'height',
    'pixelformat',
    'field',
    'bytesperline',
    'sizeimage',
    'colorspace',
    'priv',
    'flags',
    'unnamed_1',
    'quantization',
    'xfer_func',
]
struct_v4l2_pix_format._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_pix_format._fields_ = [
    ('width', __u32),
    ('height', __u32),
    ('pixelformat', __u32),
    ('field', __u32),
    ('bytesperline', __u32),
    ('sizeimage', __u32),
    ('colorspace', __u32),
    ('priv', __u32),
    ('flags', __u32),
    ('unnamed_1', union_anon_6),
    ('quantization', __u32),
    ('xfer_func', __u32),
]


class struct_v4l2_fmtdesc(Structure):
    pass

struct_v4l2_fmtdesc.__slots__ = [
    'index',
    'type',
    'flags',
    'description',
    'pixelformat',
    'mbus_code',
    'reserved',
]
struct_v4l2_fmtdesc._fields_ = [
    ('index', __u32),
    ('type', __u32),
    ('flags', __u32),
    ('description', __u8 * int(32)),
    ('pixelformat', __u32),
    ('mbus_code', __u32),
    ('reserved', __u32 * int(3)),
]

enum_v4l2_frmsizetypes = c_int

V4L2_FRMSIZE_TYPE_DISCRETE = 1

V4L2_FRMSIZE_TYPE_CONTINUOUS = 2

V4L2_FRMSIZE_TYPE_STEPWISE = 3


class struct_v4l2_frmsize_discrete(Structure):
    pass

struct_v4l2_frmsize_discrete.__slots__ = [
    'width',
    'height',
]
struct_v4l2_frmsize_discrete._fields_ = [
    ('width', __u32),
    ('height', __u32),
]


class struct_v4l2_frmsize_stepwise(Structure):
    pass

struct_v4l2_frmsize_stepwise.__slots__ = [
    'min_width',
    'max_width',
    'step_width',
    'min_height',
    'max_height',
    'step_height',
]
struct_v4l2_frmsize_stepwise._fields_ = [
    ('min_width', __u32),
    ('max_width', __u32),
    ('step_width', __u32),
    ('min_height', __u32),
    ('max_height', __u32),
    ('step_height', __u32),
]


class union_anon_7(Union):
    pass

union_anon_7.__slots__ = [
    'discrete',
    'stepwise',
]
union_anon_7._fields_ = [
    ('discrete', struct_v4l2_frmsize_discrete),
    ('stepwise', struct_v4l2_frmsize_stepwise),
]


class struct_v4l2_frmsizeenum(Structure):
    pass

struct_v4l2_frmsizeenum.__slots__ = [
    'index',
    'pixel_format',
    'type',
    'unnamed_1',
    'reserved',
]
struct_v4l2_frmsizeenum._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_frmsizeenum._fields_ = [
    ('index', __u32),
    ('pixel_format', __u32),
    ('type', __u32),
    ('unnamed_1', union_anon_7),
    ('reserved', __u32 * int(2)),
]

enum_v4l2_frmivaltypes = c_int

V4L2_FRMIVAL_TYPE_DISCRETE = 1

V4L2_FRMIVAL_TYPE_CONTINUOUS = 2

V4L2_FRMIVAL_TYPE_STEPWISE = 3


class struct_v4l2_frmival_stepwise(Structure):
    pass

struct_v4l2_frmival_stepwise.__slots__ = [
    'min',
    'max',
    'step',
]
struct_v4l2_frmival_stepwise._fields_ = [
    ('min', struct_v4l2_fract),
    ('max', struct_v4l2_fract),
    ('step', struct_v4l2_fract),
]


class union_anon_8(Union):
    pass

union_anon_8.__slots__ = [
    'discrete',
    'stepwise',
]
union_anon_8._fields_ = [
    ('discrete', struct_v4l2_fract),
    ('stepwise', struct_v4l2_frmival_stepwise),
]


class struct_v4l2_frmivalenum(Structure):
    pass

struct_v4l2_frmivalenum.__slots__ = [
    'index',
    'pixel_format',
    'width',
    'height',
    'type',
    'unnamed_1',
    'reserved',
]
struct_v4l2_frmivalenum._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_frmivalenum._fields_ = [
    ('index', __u32),
    ('pixel_format', __u32),
    ('width', __u32),
    ('height', __u32),
    ('type', __u32),
    ('unnamed_1', union_anon_8),
    ('reserved', __u32 * int(2)),
]


class struct_v4l2_timecode(Structure):
    pass

struct_v4l2_timecode.__slots__ = [
    'type',
    'flags',
    'frames',
    'seconds',
    'minutes',
    'hours',
    'userbits',
]
struct_v4l2_timecode._fields_ = [
    ('type', __u32),
    ('flags', __u32),
    ('frames', __u8),
    ('seconds', __u8),
    ('minutes', __u8),
    ('hours', __u8),
    ('userbits', __u8 * int(4)),
]


class struct_v4l2_jpegcompression(Structure):
    pass

struct_v4l2_jpegcompression.__slots__ = [
    'quality',
    'APPn',
    'APP_len',
    'APP_data',
    'COM_len',
    'COM_data',
    'jpeg_markers',
]
struct_v4l2_jpegcompression._fields_ = [
    ('quality', c_int),
    ('APPn', c_int),
    ('APP_len', c_int),
    ('APP_data', c_char * int(60)),
    ('COM_len', c_int),
    ('COM_data', c_char * int(60)),
    ('jpeg_markers', __u32),
]


class struct_v4l2_requestbuffers(Structure):
    pass

struct_v4l2_requestbuffers.__slots__ = [
    'count',
    'type',
    'memory',
    'capabilities',
    'flags',
    'reserved',
]
struct_v4l2_requestbuffers._fields_ = [
    ('count', __u32),
    ('type', __u32),
    ('memory', __u32),
    ('capabilities', __u32),
    ('flags', __u8),
    ('reserved', __u8 * int(3)),
]


class union_anon_9(Union):
    pass

union_anon_9.__slots__ = [
    'mem_offset',
    'userptr',
    'fd',
]
union_anon_9._fields_ = [
    ('mem_offset', __u32),
    ('userptr', c_ulong),
    ('fd', __s32),
]


class struct_v4l2_plane(Structure):
    pass

struct_v4l2_plane.__slots__ = [
    'bytesused',
    'length',
    'm',
    'data_offset',
    'reserved',
]
struct_v4l2_plane._fields_ = [
    ('bytesused', __u32),
    ('length', __u32),
    ('m', union_anon_9),
    ('data_offset', __u32),
    ('reserved', __u32 * int(11)),
]


class union_anon_10(Union):
    pass

union_anon_10.__slots__ = [
    'offset',
    'userptr',
    'planes',
    'fd',
]
union_anon_10._fields_ = [
    ('offset', __u32),
    ('userptr', c_ulong),
    ('planes', POINTER(struct_v4l2_plane)),
    ('fd', __s32),
]


class union_anon_11(Union):
    pass

union_anon_11.__slots__ = [
    'request_fd',
    'reserved',
]
union_anon_11._fields_ = [
    ('request_fd', __s32),
    ('reserved', __u32),
]


class struct_v4l2_buffer(Structure):
    pass

struct_v4l2_buffer.__slots__ = [
    'index',
    'type',
    'bytesused',
    'flags',
    'field',
    'timestamp',
    'timecode',
    'sequence',
    'memory',
    'm',
    'length',
    'reserved2',
    'unnamed_1',
]
struct_v4l2_buffer._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_buffer._fields_ = [
    ('index', __u32),
    ('type', __u32),
    ('bytesused', __u32),
    ('flags', __u32),
    ('field', __u32),
    ('timestamp', struct_timeval),
    ('timecode', struct_v4l2_timecode),
    ('sequence', __u32),
    ('memory', __u32),
    ('m', union_anon_10),
    ('length', __u32),
    ('reserved2', __u32),
    ('unnamed_1', union_anon_11),
]


class struct_v4l2_exportbuffer(Structure):
    pass

struct_v4l2_exportbuffer.__slots__ = [
    'type',
    'index',
    'plane',
    'flags',
    'fd',
    'reserved',
]
struct_v4l2_exportbuffer._fields_ = [
    ('type', __u32),
    ('index', __u32),
    ('plane', __u32),
    ('flags', __u32),
    ('fd', __s32),
    ('reserved', __u32 * int(11)),
]


class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'width',
    'height',
    'pixelformat',
    'field',
    'bytesperline',
    'sizeimage',
    'colorspace',
    'priv',
]
struct_anon_12._fields_ = [
    ('width', __u32),
    ('height', __u32),
    ('pixelformat', __u32),
    ('field', __u32),
    ('bytesperline', __u32),
    ('sizeimage', __u32),
    ('colorspace', __u32),
    ('priv', __u32),
]


class struct_v4l2_framebuffer(Structure):
    pass

struct_v4l2_framebuffer.__slots__ = [
    'capability',
    'flags',
    'base',
    'fmt',
]
struct_v4l2_framebuffer._fields_ = [
    ('capability', __u32),
    ('flags', __u32),
    ('base', POINTER(None)),
    ('fmt', struct_anon_12),
]


class struct_v4l2_clip(Structure):
    pass

struct_v4l2_clip.__slots__ = [
    'c',
    'next',
]
struct_v4l2_clip._fields_ = [
    ('c', struct_v4l2_rect),
    ('next', POINTER(struct_v4l2_clip)),
]


class struct_v4l2_window(Structure):
    pass

struct_v4l2_window.__slots__ = [
    'w',
    'field',
    'chromakey',
    'clips',
    'clipcount',
    'bitmap',
    'global_alpha',
]
struct_v4l2_window._fields_ = [
    ('w', struct_v4l2_rect),
    ('field', __u32),
    ('chromakey', __u32),
    ('clips', POINTER(struct_v4l2_clip)),
    ('clipcount', __u32),
    ('bitmap', POINTER(None)),
    ('global_alpha', __u8),
]


class struct_v4l2_captureparm(Structure):
    pass

struct_v4l2_captureparm.__slots__ = [
    'capability',
    'capturemode',
    'timeperframe',
    'extendedmode',
    'readbuffers',
    'reserved',
]
struct_v4l2_captureparm._fields_ = [
    ('capability', __u32),
    ('capturemode', __u32),
    ('timeperframe', struct_v4l2_fract),
    ('extendedmode', __u32),
    ('readbuffers', __u32),
    ('reserved', __u32 * int(4)),
]


class struct_v4l2_outputparm(Structure):
    pass

struct_v4l2_outputparm.__slots__ = [
    'capability',
    'outputmode',
    'timeperframe',
    'extendedmode',
    'writebuffers',
    'reserved',
]
struct_v4l2_outputparm._fields_ = [
    ('capability', __u32),
    ('outputmode', __u32),
    ('timeperframe', struct_v4l2_fract),
    ('extendedmode', __u32),
    ('writebuffers', __u32),
    ('reserved', __u32 * int(4)),
]


class struct_v4l2_cropcap(Structure):
    pass

struct_v4l2_cropcap.__slots__ = [
    'type',
    'bounds',
    'defrect',
    'pixelaspect',
]
struct_v4l2_cropcap._fields_ = [
    ('type', __u32),
    ('bounds', struct_v4l2_rect),
    ('defrect', struct_v4l2_rect),
    ('pixelaspect', struct_v4l2_fract),
]


class struct_v4l2_crop(Structure):
    pass

struct_v4l2_crop.__slots__ = [
    'type',
    'c',
]
struct_v4l2_crop._fields_ = [
    ('type', __u32),
    ('c', struct_v4l2_rect),
]


class struct_v4l2_selection(Structure):
    pass

struct_v4l2_selection.__slots__ = [
    'type',
    'target',
    'flags',
    'r',
    'reserved',
]
struct_v4l2_selection._fields_ = [
    ('type', __u32),
    ('target', __u32),
    ('flags', __u32),
    ('r', struct_v4l2_rect),
    ('reserved', __u32 * int(9)),
]

v4l2_std_id = __u64


class struct_v4l2_standard(Structure):
    pass

struct_v4l2_standard.__slots__ = [
    'index',
    'id',
    'name',
    'frameperiod',
    'framelines',
    'reserved',
]
struct_v4l2_standard._fields_ = [
    ('index', __u32),
    ('id', v4l2_std_id),
    ('name', __u8 * int(24)),
    ('frameperiod', struct_v4l2_fract),
    ('framelines', __u32),
    ('reserved', __u32 * int(4)),
]


class struct_v4l2_bt_timings(Structure):
    pass

struct_v4l2_bt_timings.__slots__ = [
    'width',
    'height',
    'interlaced',
    'polarities',
    'pixelclock',
    'hfrontporch',
    'hsync',
    'hbackporch',
    'vfrontporch',
    'vsync',
    'vbackporch',
    'il_vfrontporch',
    'il_vsync',
    'il_vbackporch',
    'standards',
    'flags',
    'picture_aspect',
    'cea861_vic',
    'hdmi_vic',
    'reserved',
]
struct_v4l2_bt_timings._fields_ = [
    ('width', __u32),
    ('height', __u32),
    ('interlaced', __u32),
    ('polarities', __u32),
    ('pixelclock', __u64),
    ('hfrontporch', __u32),
    ('hsync', __u32),
    ('hbackporch', __u32),
    ('vfrontporch', __u32),
    ('vsync', __u32),
    ('vbackporch', __u32),
    ('il_vfrontporch', __u32),
    ('il_vsync', __u32),
    ('il_vbackporch', __u32),
    ('standards', __u32),
    ('flags', __u32),
    ('picture_aspect', struct_v4l2_fract),
    ('cea861_vic', __u8),
    ('hdmi_vic', __u8),
    ('reserved', __u8 * int(46)),
]


class union_anon_13(Union):
    pass

union_anon_13.__slots__ = [
    'bt',
    'reserved',
]
union_anon_13._fields_ = [
    ('bt', struct_v4l2_bt_timings),
    ('reserved', __u32 * int(32)),
]


class struct_v4l2_dv_timings(Structure):
    pass

struct_v4l2_dv_timings.__slots__ = [
    'type',
    'unnamed_1',
]
struct_v4l2_dv_timings._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_dv_timings._fields_ = [
    ('type', __u32),
    ('unnamed_1', union_anon_13),
]


class struct_v4l2_enum_dv_timings(Structure):
    pass

struct_v4l2_enum_dv_timings.__slots__ = [
    'index',
    'pad',
    'reserved',
    'timings',
]
struct_v4l2_enum_dv_timings._fields_ = [
    ('index', __u32),
    ('pad', __u32),
    ('reserved', __u32 * int(2)),
    ('timings', struct_v4l2_dv_timings),
]


class struct_v4l2_bt_timings_cap(Structure):
    pass

struct_v4l2_bt_timings_cap.__slots__ = [
    'min_width',
    'max_width',
    'min_height',
    'max_height',
    'min_pixelclock',
    'max_pixelclock',
    'standards',
    'capabilities',
    'reserved',
]
struct_v4l2_bt_timings_cap._fields_ = [
    ('min_width', __u32),
    ('max_width', __u32),
    ('min_height', __u32),
    ('max_height', __u32),
    ('min_pixelclock', __u64),
    ('max_pixelclock', __u64),
    ('standards', __u32),
    ('capabilities', __u32),
    ('reserved', __u32 * int(16)),
]


class union_anon_14(Union):
    pass

union_anon_14.__slots__ = [
    'bt',
    'raw_data',
]
union_anon_14._fields_ = [
    ('bt', struct_v4l2_bt_timings_cap),
    ('raw_data', __u32 * int(32)),
]


class struct_v4l2_dv_timings_cap(Structure):
    pass

struct_v4l2_dv_timings_cap.__slots__ = [
    'type',
    'pad',
    'reserved',
    'unnamed_1',
]
struct_v4l2_dv_timings_cap._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_dv_timings_cap._fields_ = [
    ('type', __u32),
    ('pad', __u32),
    ('reserved', __u32 * int(2)),
    ('unnamed_1', union_anon_14),
]


class struct_v4l2_input(Structure):
    pass

struct_v4l2_input.__slots__ = [
    'index',
    'name',
    'type',
    'audioset',
    'tuner',
    'std',
    'status',
    'capabilities',
    'reserved',
]
struct_v4l2_input._fields_ = [
    ('index', __u32),
    ('name', __u8 * int(32)),
    ('type', __u32),
    ('audioset', __u32),
    ('tuner', __u32),
    ('std', v4l2_std_id),
    ('status', __u32),
    ('capabilities', __u32),
    ('reserved', __u32 * int(3)),
]


class struct_v4l2_output(Structure):
    pass

struct_v4l2_output.__slots__ = [
    'index',
    'name',
    'type',
    'audioset',
    'modulator',
    'std',
    'capabilities',
    'reserved',
]
struct_v4l2_output._fields_ = [
    ('index', __u32),
    ('name', __u8 * int(32)),
    ('type', __u32),
    ('audioset', __u32),
    ('modulator', __u32),
    ('std', v4l2_std_id),
    ('capabilities', __u32),
    ('reserved', __u32 * int(3)),
]


class struct_v4l2_control(Structure):
    pass

struct_v4l2_control.__slots__ = [
    'id',
    'value',
]
struct_v4l2_control._fields_ = [
    ('id', __u32),
    ('value', __s32),
]


class union_anon_15(Union):
    pass

union_anon_15.__slots__ = [
    'value',
    'value64',
    'string',
    'p_u8',
    'p_u16',
    'p_u32',
    'p_s32',
    'p_s64',
    'p_area',
    'p_h264_sps',
    'p_h264_pps',
    'p_h264_scaling_matrix',
    'p_h264_pred_weights',
    'p_h264_slice_params',
    'p_h264_decode_params',
    'p_fwht_params',
    'p_vp8_frame',
    'p_mpeg2_sequence',
    'p_mpeg2_picture',
    'p_mpeg2_quantisation',
    'p_vp9_compressed_hdr_probs',
    'p_vp9_frame',
    'p_hevc_sps',
    'p_hevc_pps',
    'p_hevc_slice_params',
    'p_hevc_scaling_matrix',
    'p_hevc_decode_params',
    'p_av1_sequence',
    'p_av1_tile_group_entry',
    'p_av1_frame',
    'p_av1_film_grain',
    'p_hdr10_cll_info',
    'p_hdr10_mastering_display',
    'ptr',
]
union_anon_15._fields_ = [
    ('value', __s32),
    ('value64', __s64),
    ('string', String),
    ('p_u8', POINTER(__u8)),
    ('p_u16', POINTER(__u16)),
    ('p_u32', POINTER(__u32)),
    ('p_s32', POINTER(__s32)),
    ('p_s64', POINTER(__s64)),
    ('p_area', POINTER(struct_v4l2_area)),
    ('p_h264_sps', POINTER(struct_v4l2_ctrl_h264_sps)),
    ('p_h264_pps', POINTER(struct_v4l2_ctrl_h264_pps)),
    ('p_h264_scaling_matrix', POINTER(struct_v4l2_ctrl_h264_scaling_matrix)),
    ('p_h264_pred_weights', POINTER(struct_v4l2_ctrl_h264_pred_weights)),
    ('p_h264_slice_params', POINTER(struct_v4l2_ctrl_h264_slice_params)),
    ('p_h264_decode_params', POINTER(struct_v4l2_ctrl_h264_decode_params)),
    ('p_fwht_params', POINTER(struct_v4l2_ctrl_fwht_params)),
    ('p_vp8_frame', POINTER(struct_v4l2_ctrl_vp8_frame)),
    ('p_mpeg2_sequence', POINTER(struct_v4l2_ctrl_mpeg2_sequence)),
    ('p_mpeg2_picture', POINTER(struct_v4l2_ctrl_mpeg2_picture)),
    ('p_mpeg2_quantisation', POINTER(struct_v4l2_ctrl_mpeg2_quantisation)),
    ('p_vp9_compressed_hdr_probs', POINTER(struct_v4l2_ctrl_vp9_compressed_hdr)),
    ('p_vp9_frame', POINTER(struct_v4l2_ctrl_vp9_frame)),
    ('p_hevc_sps', POINTER(struct_v4l2_ctrl_hevc_sps)),
    ('p_hevc_pps', POINTER(struct_v4l2_ctrl_hevc_pps)),
    ('p_hevc_slice_params', POINTER(struct_v4l2_ctrl_hevc_slice_params)),
    ('p_hevc_scaling_matrix', POINTER(struct_v4l2_ctrl_hevc_scaling_matrix)),
    ('p_hevc_decode_params', POINTER(struct_v4l2_ctrl_hevc_decode_params)),
    ('p_av1_sequence', POINTER(struct_v4l2_ctrl_av1_sequence)),
    ('p_av1_tile_group_entry', POINTER(struct_v4l2_ctrl_av1_tile_group_entry)),
    ('p_av1_frame', POINTER(struct_v4l2_ctrl_av1_frame)),
    ('p_av1_film_grain', POINTER(struct_v4l2_ctrl_av1_film_grain)),
    ('p_hdr10_cll_info', POINTER(struct_v4l2_ctrl_hdr10_cll_info)),
    ('p_hdr10_mastering_display', POINTER(struct_v4l2_ctrl_hdr10_mastering_display)),
    ('ptr', POINTER(None)),
]


class struct_v4l2_ext_control(Structure):
    pass

struct_v4l2_ext_control.__slots__ = [
    'id',
    'size',
    'reserved2',
    'unnamed_1',
]
struct_v4l2_ext_control._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_ext_control._fields_ = [
    ('id', __u32),
    ('size', __u32),
    ('reserved2', __u32 * int(1)),
    ('unnamed_1', union_anon_15),
]


class union_anon_16(Union):
    pass

union_anon_16.__slots__ = [
    'ctrl_class',
    'which',
]
union_anon_16._fields_ = [
    ('ctrl_class', __u32),
    ('which', __u32),
]


class struct_v4l2_ext_controls(Structure):
    pass

struct_v4l2_ext_controls.__slots__ = [
    'unnamed_1',
    'count',
    'error_idx',
    'request_fd',
    'reserved',
    'controls',
]
struct_v4l2_ext_controls._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_ext_controls._fields_ = [
    ('unnamed_1', union_anon_16),
    ('count', __u32),
    ('error_idx', __u32),
    ('request_fd', __s32),
    ('reserved', __u32 * int(1)),
    ('controls', POINTER(struct_v4l2_ext_control)),
]

enum_v4l2_ctrl_type = c_int

V4L2_CTRL_TYPE_INTEGER = 1

V4L2_CTRL_TYPE_BOOLEAN = 2

V4L2_CTRL_TYPE_MENU = 3

V4L2_CTRL_TYPE_BUTTON = 4

V4L2_CTRL_TYPE_INTEGER64 = 5

V4L2_CTRL_TYPE_CTRL_CLASS = 6

V4L2_CTRL_TYPE_STRING = 7

V4L2_CTRL_TYPE_BITMASK = 8

V4L2_CTRL_TYPE_INTEGER_MENU = 9

V4L2_CTRL_COMPOUND_TYPES = 0x0100

V4L2_CTRL_TYPE_U8 = 0x0100

V4L2_CTRL_TYPE_U16 = 0x0101

V4L2_CTRL_TYPE_U32 = 0x0102

V4L2_CTRL_TYPE_AREA = 0x0106

V4L2_CTRL_TYPE_HDR10_CLL_INFO = 0x0110

V4L2_CTRL_TYPE_HDR10_MASTERING_DISPLAY = 0x0111

V4L2_CTRL_TYPE_H264_SPS = 0x0200

V4L2_CTRL_TYPE_H264_PPS = 0x0201

V4L2_CTRL_TYPE_H264_SCALING_MATRIX = 0x0202

V4L2_CTRL_TYPE_H264_SLICE_PARAMS = 0x0203

V4L2_CTRL_TYPE_H264_DECODE_PARAMS = 0x0204

V4L2_CTRL_TYPE_H264_PRED_WEIGHTS = 0x0205

V4L2_CTRL_TYPE_FWHT_PARAMS = 0x0220

V4L2_CTRL_TYPE_VP8_FRAME = 0x0240

V4L2_CTRL_TYPE_MPEG2_QUANTISATION = 0x0250

V4L2_CTRL_TYPE_MPEG2_SEQUENCE = 0x0251

V4L2_CTRL_TYPE_MPEG2_PICTURE = 0x0252

V4L2_CTRL_TYPE_VP9_COMPRESSED_HDR = 0x0260

V4L2_CTRL_TYPE_VP9_FRAME = 0x0261

V4L2_CTRL_TYPE_HEVC_SPS = 0x0270

V4L2_CTRL_TYPE_HEVC_PPS = 0x0271

V4L2_CTRL_TYPE_HEVC_SLICE_PARAMS = 0x0272

V4L2_CTRL_TYPE_HEVC_SCALING_MATRIX = 0x0273

V4L2_CTRL_TYPE_HEVC_DECODE_PARAMS = 0x0274

V4L2_CTRL_TYPE_AV1_SEQUENCE = 0x280

V4L2_CTRL_TYPE_AV1_TILE_GROUP_ENTRY = 0x281

V4L2_CTRL_TYPE_AV1_FRAME = 0x282

V4L2_CTRL_TYPE_AV1_FILM_GRAIN = 0x283


class struct_v4l2_queryctrl(Structure):
    pass

struct_v4l2_queryctrl.__slots__ = [
    'id',
    'type',
    'name',
    'minimum',
    'maximum',
    'step',
    'default_value',
    'flags',
    'reserved',
]
struct_v4l2_queryctrl._fields_ = [
    ('id', __u32),
    ('type', __u32),
    ('name', __u8 * int(32)),
    ('minimum', __s32),
    ('maximum', __s32),
    ('step', __s32),
    ('default_value', __s32),
    ('flags', __u32),
    ('reserved', __u32 * int(2)),
]


class struct_v4l2_query_ext_ctrl(Structure):
    pass

struct_v4l2_query_ext_ctrl.__slots__ = [
    'id',
    'type',
    'name',
    'minimum',
    'maximum',
    'step',
    'default_value',
    'flags',
    'elem_size',
    'elems',
    'nr_of_dims',
    'dims',
    'reserved',
]
struct_v4l2_query_ext_ctrl._fields_ = [
    ('id', __u32),
    ('type', __u32),
    ('name', c_char * int(32)),
    ('minimum', __s64),
    ('maximum', __s64),
    ('step', __u64),
    ('default_value', __s64),
    ('flags', __u32),
    ('elem_size', __u32),
    ('elems', __u32),
    ('nr_of_dims', __u32),
    ('dims', __u32 * int(4)),
    ('reserved', __u32 * int(32)),
]


class union_anon_17(Union):
    pass

union_anon_17.__slots__ = [
    'name',
    'value',
]
union_anon_17._fields_ = [
    ('name', __u8 * int(32)),
    ('value', __s64),
]


class struct_v4l2_querymenu(Structure):
    pass

struct_v4l2_querymenu.__slots__ = [
    'id',
    'index',
    'unnamed_1',
    'reserved',
]
struct_v4l2_querymenu._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_querymenu._fields_ = [
    ('id', __u32),
    ('index', __u32),
    ('unnamed_1', union_anon_17),
    ('reserved', __u32),
]


class struct_v4l2_tuner(Structure):
    pass

struct_v4l2_tuner.__slots__ = [
    'index',
    'name',
    'type',
    'capability',
    'rangelow',
    'rangehigh',
    'rxsubchans',
    'audmode',
    'signal',
    'afc',
    'reserved',
]
struct_v4l2_tuner._fields_ = [
    ('index', __u32),
    ('name', __u8 * int(32)),
    ('type', __u32),
    ('capability', __u32),
    ('rangelow', __u32),
    ('rangehigh', __u32),
    ('rxsubchans', __u32),
    ('audmode', __u32),
    ('signal', __s32),
    ('afc', __s32),
    ('reserved', __u32 * int(4)),
]


class struct_v4l2_modulator(Structure):
    pass

struct_v4l2_modulator.__slots__ = [
    'index',
    'name',
    'capability',
    'rangelow',
    'rangehigh',
    'txsubchans',
    'type',
    'reserved',
]
struct_v4l2_modulator._fields_ = [
    ('index', __u32),
    ('name', __u8 * int(32)),
    ('capability', __u32),
    ('rangelow', __u32),
    ('rangehigh', __u32),
    ('txsubchans', __u32),
    ('type', __u32),
    ('reserved', __u32 * int(3)),
]


class struct_v4l2_frequency(Structure):
    pass

struct_v4l2_frequency.__slots__ = [
    'tuner',
    'type',
    'frequency',
    'reserved',
]
struct_v4l2_frequency._fields_ = [
    ('tuner', __u32),
    ('type', __u32),
    ('frequency', __u32),
    ('reserved', __u32 * int(8)),
]


class struct_v4l2_frequency_band(Structure):
    pass

struct_v4l2_frequency_band.__slots__ = [
    'tuner',
    'type',
    'index',
    'capability',
    'rangelow',
    'rangehigh',
    'modulation',
    'reserved',
]
struct_v4l2_frequency_band._fields_ = [
    ('tuner', __u32),
    ('type', __u32),
    ('index', __u32),
    ('capability', __u32),
    ('rangelow', __u32),
    ('rangehigh', __u32),
    ('modulation', __u32),
    ('reserved', __u32 * int(9)),
]


class struct_v4l2_hw_freq_seek(Structure):
    pass

struct_v4l2_hw_freq_seek.__slots__ = [
    'tuner',
    'type',
    'seek_upward',
    'wrap_around',
    'spacing',
    'rangelow',
    'rangehigh',
    'reserved',
]
struct_v4l2_hw_freq_seek._fields_ = [
    ('tuner', __u32),
    ('type', __u32),
    ('seek_upward', __u32),
    ('wrap_around', __u32),
    ('spacing', __u32),
    ('rangelow', __u32),
    ('rangehigh', __u32),
    ('reserved', __u32 * int(5)),
]


class struct_v4l2_rds_data(Structure):
    pass

struct_v4l2_rds_data.__slots__ = [
    'lsb',
    'msb',
    'block',
]
struct_v4l2_rds_data._fields_ = [
    ('lsb', __u8),
    ('msb', __u8),
    ('block', __u8),
]


class struct_v4l2_audio(Structure):
    pass

struct_v4l2_audio.__slots__ = [
    'index',
    'name',
    'capability',
    'mode',
    'reserved',
]
struct_v4l2_audio._fields_ = [
    ('index', __u32),
    ('name', __u8 * int(32)),
    ('capability', __u32),
    ('mode', __u32),
    ('reserved', __u32 * int(2)),
]


class struct_v4l2_audioout(Structure):
    pass

struct_v4l2_audioout.__slots__ = [
    'index',
    'name',
    'capability',
    'mode',
    'reserved',
]
struct_v4l2_audioout._fields_ = [
    ('index', __u32),
    ('name', __u8 * int(32)),
    ('capability', __u32),
    ('mode', __u32),
    ('reserved', __u32 * int(2)),
]


class struct_v4l2_enc_idx_entry(Structure):
    pass

struct_v4l2_enc_idx_entry.__slots__ = [
    'offset',
    'pts',
    'length',
    'flags',
    'reserved',
]
struct_v4l2_enc_idx_entry._fields_ = [
    ('offset', __u64),
    ('pts', __u64),
    ('length', __u32),
    ('flags', __u32),
    ('reserved', __u32 * int(2)),
]


class struct_v4l2_enc_idx(Structure):
    pass

struct_v4l2_enc_idx.__slots__ = [
    'entries',
    'entries_cap',
    'reserved',
    'entry',
]
struct_v4l2_enc_idx._fields_ = [
    ('entries', __u32),
    ('entries_cap', __u32),
    ('reserved', __u32 * int(4)),
    ('entry', struct_v4l2_enc_idx_entry * int(64)),
]


class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'data',
]
struct_anon_18._fields_ = [
    ('data', __u32 * int(8)),
]


class union_anon_19(Union):
    pass

union_anon_19.__slots__ = [
    'raw',
]
union_anon_19._fields_ = [
    ('raw', struct_anon_18),
]


class struct_v4l2_encoder_cmd(Structure):
    pass

struct_v4l2_encoder_cmd.__slots__ = [
    'cmd',
    'flags',
    'unnamed_1',
]
struct_v4l2_encoder_cmd._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_encoder_cmd._fields_ = [
    ('cmd', __u32),
    ('flags', __u32),
    ('unnamed_1', union_anon_19),
]


class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'pts',
]
struct_anon_20._fields_ = [
    ('pts', __u64),
]


class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'speed',
    'format',
]
struct_anon_21._fields_ = [
    ('speed', __s32),
    ('format', __u32),
]


class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'data',
]
struct_anon_22._fields_ = [
    ('data', __u32 * int(16)),
]


class union_anon_23(Union):
    pass

union_anon_23.__slots__ = [
    'stop',
    'start',
    'raw',
]
union_anon_23._fields_ = [
    ('stop', struct_anon_20),
    ('start', struct_anon_21),
    ('raw', struct_anon_22),
]


class struct_v4l2_decoder_cmd(Structure):
    pass

struct_v4l2_decoder_cmd.__slots__ = [
    'cmd',
    'flags',
    'unnamed_1',
]
struct_v4l2_decoder_cmd._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_decoder_cmd._fields_ = [
    ('cmd', __u32),
    ('flags', __u32),
    ('unnamed_1', union_anon_23),
]


class struct_v4l2_vbi_format(Structure):
    pass

struct_v4l2_vbi_format.__slots__ = [
    'sampling_rate',
    'offset',
    'samples_per_line',
    'sample_format',
    'start',
    'count',
    'flags',
    'reserved',
]
struct_v4l2_vbi_format._fields_ = [
    ('sampling_rate', __u32),
    ('offset', __u32),
    ('samples_per_line', __u32),
    ('sample_format', __u32),
    ('start', __s32 * int(2)),
    ('count', __u32 * int(2)),
    ('flags', __u32),
    ('reserved', __u32 * int(2)),
]


class struct_v4l2_sliced_vbi_format(Structure):
    pass

struct_v4l2_sliced_vbi_format.__slots__ = [
    'service_set',
    'service_lines',
    'io_size',
    'reserved',
]
struct_v4l2_sliced_vbi_format._fields_ = [
    ('service_set', __u16),
    ('service_lines', (__u16 * int(24)) * int(2)),
    ('io_size', __u32),
    ('reserved', __u32 * int(2)),
]


class struct_v4l2_sliced_vbi_cap(Structure):
    pass

struct_v4l2_sliced_vbi_cap.__slots__ = [
    'service_set',
    'service_lines',
    'type',
    'reserved',
]
struct_v4l2_sliced_vbi_cap._fields_ = [
    ('service_set', __u16),
    ('service_lines', (__u16 * int(24)) * int(2)),
    ('type', __u32),
    ('reserved', __u32 * int(3)),
]


class struct_v4l2_sliced_vbi_data(Structure):
    pass

struct_v4l2_sliced_vbi_data.__slots__ = [
    'id',
    'field',
    'line',
    'reserved',
    'data',
]
struct_v4l2_sliced_vbi_data._fields_ = [
    ('id', __u32),
    ('field', __u32),
    ('line', __u32),
    ('reserved', __u32),
    ('data', __u8 * int(48)),
]


class struct_v4l2_mpeg_vbi_itv0_line(Structure):
    pass

struct_v4l2_mpeg_vbi_itv0_line.__slots__ = [
    'id',
    'data',
]
struct_v4l2_mpeg_vbi_itv0_line._fields_ = [
    ('id', __u8),
    ('data', __u8 * int(42)),
]


class struct_v4l2_mpeg_vbi_itv0(Structure):
    pass

struct_v4l2_mpeg_vbi_itv0.__slots__ = [
    'linemask',
    'line',
]
struct_v4l2_mpeg_vbi_itv0._fields_ = [
    ('linemask', __le32 * int(2)),
    ('line', struct_v4l2_mpeg_vbi_itv0_line * int(35)),
]


class struct_v4l2_mpeg_vbi_ITV0(Structure):
    pass

struct_v4l2_mpeg_vbi_ITV0.__slots__ = [
    'line',
]
struct_v4l2_mpeg_vbi_ITV0._fields_ = [
    ('line', struct_v4l2_mpeg_vbi_itv0_line * int(36)),
]


class union_anon_24(Union):
    pass

union_anon_24.__slots__ = [
    'itv0',
    'ITV0',
]
union_anon_24._fields_ = [
    ('itv0', struct_v4l2_mpeg_vbi_itv0),
    ('ITV0', struct_v4l2_mpeg_vbi_ITV0),
]


class struct_v4l2_mpeg_vbi_fmt_ivtv(Structure):
    pass

struct_v4l2_mpeg_vbi_fmt_ivtv.__slots__ = [
    'magic',
    'unnamed_1',
]
struct_v4l2_mpeg_vbi_fmt_ivtv._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_mpeg_vbi_fmt_ivtv._fields_ = [
    ('magic', __u8 * int(4)),
    ('unnamed_1', union_anon_24),
]


class struct_v4l2_plane_pix_format(Structure):
    pass

struct_v4l2_plane_pix_format.__slots__ = [
    'sizeimage',
    'bytesperline',
    'reserved',
]
struct_v4l2_plane_pix_format._fields_ = [
    ('sizeimage', __u32),
    ('bytesperline', __u32),
    ('reserved', __u16 * int(6)),
]


class union_anon_25(Union):
    pass

union_anon_25.__slots__ = [
    'ycbcr_enc',
    'hsv_enc',
]
union_anon_25._fields_ = [
    ('ycbcr_enc', __u8),
    ('hsv_enc', __u8),
]


class struct_v4l2_pix_format_mplane(Structure):
    pass

struct_v4l2_pix_format_mplane.__slots__ = [
    'width',
    'height',
    'pixelformat',
    'field',
    'colorspace',
    'plane_fmt',
    'num_planes',
    'flags',
    'unnamed_1',
    'quantization',
    'xfer_func',
    'reserved',
]
struct_v4l2_pix_format_mplane._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_pix_format_mplane._fields_ = [
    ('width', __u32),
    ('height', __u32),
    ('pixelformat', __u32),
    ('field', __u32),
    ('colorspace', __u32),
    ('plane_fmt', struct_v4l2_plane_pix_format * int(8)),
    ('num_planes', __u8),
    ('flags', __u8),
    ('unnamed_1', union_anon_25),
    ('quantization', __u8),
    ('xfer_func', __u8),
    ('reserved', __u8 * int(7)),
]


class struct_v4l2_sdr_format(Structure):
    pass

struct_v4l2_sdr_format.__slots__ = [
    'pixelformat',
    'buffersize',
    'reserved',
]
struct_v4l2_sdr_format._fields_ = [
    ('pixelformat', __u32),
    ('buffersize', __u32),
    ('reserved', __u8 * int(24)),
]


class struct_v4l2_meta_format(Structure):
    pass

struct_v4l2_meta_format.__slots__ = [
    'dataformat',
    'buffersize',
    'width',
    'height',
    'bytesperline',
]
struct_v4l2_meta_format._fields_ = [
    ('dataformat', __u32),
    ('buffersize', __u32),
    ('width', __u32),
    ('height', __u32),
    ('bytesperline', __u32),
]


class union_anon_26(Union):
    pass

union_anon_26.__slots__ = [
    'pix',
    'pix_mp',
    'win',
    'vbi',
    'sliced',
    'sdr',
    'meta',
    'raw_data',
]
union_anon_26._fields_ = [
    ('pix', struct_v4l2_pix_format),
    ('pix_mp', struct_v4l2_pix_format_mplane),
    ('win', struct_v4l2_window),
    ('vbi', struct_v4l2_vbi_format),
    ('sliced', struct_v4l2_sliced_vbi_format),
    ('sdr', struct_v4l2_sdr_format),
    ('meta', struct_v4l2_meta_format),
    ('raw_data', __u8 * int(200)),
]


class struct_v4l2_format(Structure):
    pass

struct_v4l2_format.__slots__ = [
    'type',
    'fmt',
]
struct_v4l2_format._fields_ = [
    ('type', __u32),
    ('fmt', union_anon_26),
]


class union_anon_27(Union):
    pass

union_anon_27.__slots__ = [
    'capture',
    'output',
    'raw_data',
]
union_anon_27._fields_ = [
    ('capture', struct_v4l2_captureparm),
    ('output', struct_v4l2_outputparm),
    ('raw_data', __u8 * int(200)),
]


class struct_v4l2_streamparm(Structure):
    pass

struct_v4l2_streamparm.__slots__ = [
    'type',
    'parm',
]
struct_v4l2_streamparm._fields_ = [
    ('type', __u32),
    ('parm', union_anon_27),
]


class struct_v4l2_event_vsync(Structure):
    pass

struct_v4l2_event_vsync.__slots__ = [
    'field',
]
struct_v4l2_event_vsync._fields_ = [
    ('field', __u8),
]


class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'value',
    'value64',
]
union_anon_28._fields_ = [
    ('value', __s32),
    ('value64', __s64),
]


class struct_v4l2_event_ctrl(Structure):
    pass

struct_v4l2_event_ctrl.__slots__ = [
    'changes',
    'type',
    'unnamed_1',
    'flags',
    'minimum',
    'maximum',
    'step',
    'default_value',
]
struct_v4l2_event_ctrl._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_event_ctrl._fields_ = [
    ('changes', __u32),
    ('type', __u32),
    ('unnamed_1', union_anon_28),
    ('flags', __u32),
    ('minimum', __s32),
    ('maximum', __s32),
    ('step', __s32),
    ('default_value', __s32),
]


class struct_v4l2_event_frame_sync(Structure):
    pass

struct_v4l2_event_frame_sync.__slots__ = [
    'frame_sequence',
]
struct_v4l2_event_frame_sync._fields_ = [
    ('frame_sequence', __u32),
]


class struct_v4l2_event_src_change(Structure):
    pass

struct_v4l2_event_src_change.__slots__ = [
    'changes',
]
struct_v4l2_event_src_change._fields_ = [
    ('changes', __u32),
]


class struct_v4l2_event_motion_det(Structure):
    pass

struct_v4l2_event_motion_det.__slots__ = [
    'flags',
    'frame_sequence',
    'region_mask',
]
struct_v4l2_event_motion_det._fields_ = [
    ('flags', __u32),
    ('frame_sequence', __u32),
    ('region_mask', __u32),
]


class union_anon_29(Union):
    pass

union_anon_29.__slots__ = [
    'vsync',
    'ctrl',
    'frame_sync',
    'src_change',
    'motion_det',
    'data',
]
union_anon_29._fields_ = [
    ('vsync', struct_v4l2_event_vsync),
    ('ctrl', struct_v4l2_event_ctrl),
    ('frame_sync', struct_v4l2_event_frame_sync),
    ('src_change', struct_v4l2_event_src_change),
    ('motion_det', struct_v4l2_event_motion_det),
    ('data', __u8 * int(64)),
]


class struct_v4l2_event(Structure):
    pass

struct_v4l2_event.__slots__ = [
    'type',
    'u',
    'pending',
    'sequence',
    'timestamp',
    'id',
    'reserved',
]
struct_v4l2_event._fields_ = [
    ('type', __u32),
    ('u', union_anon_29),
    ('pending', __u32),
    ('sequence', __u32),
    ('timestamp', struct_timespec),
    ('id', __u32),
    ('reserved', __u32 * int(8)),
]


class struct_v4l2_event_subscription(Structure):
    pass

struct_v4l2_event_subscription.__slots__ = [
    'type',
    'id',
    'flags',
    'reserved',
]
struct_v4l2_event_subscription._fields_ = [
    ('type', __u32),
    ('id', __u32),
    ('flags', __u32),
    ('reserved', __u32 * int(5)),
]


class union_anon_30(Union):
    pass

union_anon_30.__slots__ = [
    'addr',
    'name',
]
union_anon_30._fields_ = [
    ('addr', __u32),
    ('name', c_char * int(32)),
]


class struct_v4l2_dbg_match(Structure):
    pass

struct_v4l2_dbg_match.__slots__ = [
    'type',
    'unnamed_1',
]
struct_v4l2_dbg_match._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_dbg_match._fields_ = [
    ('type', __u32),
    ('unnamed_1', union_anon_30),
]


class struct_v4l2_dbg_register(Structure):
    pass

struct_v4l2_dbg_register.__slots__ = [
    'match',
    'size',
    'reg',
    'val',
]
struct_v4l2_dbg_register._fields_ = [
    ('match', struct_v4l2_dbg_match),
    ('size', __u32),
    ('reg', __u64),
    ('val', __u64),
]


class struct_v4l2_dbg_chip_info(Structure):
    pass

struct_v4l2_dbg_chip_info.__slots__ = [
    'match',
    'name',
    'flags',
    'reserved',
]
struct_v4l2_dbg_chip_info._fields_ = [
    ('match', struct_v4l2_dbg_match),
    ('name', c_char * int(32)),
    ('flags', __u32),
    ('reserved', __u32 * int(32)),
]


class struct_v4l2_create_buffers(Structure):
    pass

struct_v4l2_create_buffers.__slots__ = [
    'index',
    'count',
    'memory',
    'format',
    'capabilities',
    'flags',
    'max_num_buffers',
    'reserved',
]
struct_v4l2_create_buffers._fields_ = [
    ('index', __u32),
    ('count', __u32),
    ('memory', __u32),
    ('format', struct_v4l2_format),
    ('capabilities', __u32),
    ('flags', __u32),
    ('max_num_buffers', __u32),
    ('reserved', __u32 * int(5)),
]


class struct_v4l2_remove_buffers(Structure):
    pass

struct_v4l2_remove_buffers.__slots__ = [
    'index',
    'count',
    'type',
    'reserved',
]
struct_v4l2_remove_buffers._fields_ = [
    ('index', __u32),
    ('count', __u32),
    ('type', __u32),
    ('reserved', __u32 * int(13)),
]


class struct_media_device_info(Structure):
    pass

struct_media_device_info.__slots__ = [
    'driver',
    'model',
    'serial',
    'bus_info',
    'media_version',
    'hw_revision',
    'driver_version',
    'reserved',
]
struct_media_device_info._fields_ = [
    ('driver', c_char * int(16)),
    ('model', c_char * int(32)),
    ('serial', c_char * int(40)),
    ('bus_info', c_char * int(32)),
    ('media_version', __u32),
    ('hw_revision', __u32),
    ('driver_version', __u32),
    ('reserved', __u32 * int(31)),
]


class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'major',
    'minor',
]
struct_anon_31._fields_ = [
    ('major', __u32),
    ('minor', __u32),
]


class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'card',
    'device',
    'subdevice',
]
struct_anon_32._fields_ = [
    ('card', __u32),
    ('device', __u32),
    ('subdevice', __u32),
]


class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'major',
    'minor',
]
struct_anon_33._fields_ = [
    ('major', __u32),
    ('minor', __u32),
]


class struct_anon_34(Structure):
    pass

struct_anon_34.__slots__ = [
    'major',
    'minor',
]
struct_anon_34._fields_ = [
    ('major', __u32),
    ('minor', __u32),
]


class union_anon_35(Union):
    pass

union_anon_35.__slots__ = [
    'dev',
    'alsa',
    'v4l',
    'fb',
    'dvb',
    'raw',
]
union_anon_35._fields_ = [
    ('dev', struct_anon_31),
    ('alsa', struct_anon_32),
    ('v4l', struct_anon_33),
    ('fb', struct_anon_34),
    ('dvb', c_int),
    ('raw', __u8 * int(184)),
]


class struct_media_entity_desc(Structure):
    pass

struct_media_entity_desc.__slots__ = [
    'id',
    'name',
    'type',
    'revision',
    'flags',
    'group_id',
    'pads',
    'links',
    'reserved',
    'unnamed_1',
]
struct_media_entity_desc._anonymous_ = [
    'unnamed_1',
]
struct_media_entity_desc._fields_ = [
    ('id', __u32),
    ('name', c_char * int(32)),
    ('type', __u32),
    ('revision', __u32),
    ('flags', __u32),
    ('group_id', __u32),
    ('pads', __u16),
    ('links', __u16),
    ('reserved', __u32 * int(4)),
    ('unnamed_1', union_anon_35),
]


class struct_media_pad_desc(Structure):
    pass

struct_media_pad_desc.__slots__ = [
    'entity',
    'index',
    'flags',
    'reserved',
]
struct_media_pad_desc._fields_ = [
    ('entity', __u32),
    ('index', __u16),
    ('flags', __u32),
    ('reserved', __u32 * int(2)),
]


class struct_media_link_desc(Structure):
    pass

struct_media_link_desc.__slots__ = [
    'source',
    'sink',
    'flags',
    'reserved',
]
struct_media_link_desc._fields_ = [
    ('source', struct_media_pad_desc),
    ('sink', struct_media_pad_desc),
    ('flags', __u32),
    ('reserved', __u32 * int(2)),
]


class struct_media_links_enum(Structure):
    pass

struct_media_links_enum.__slots__ = [
    'entity',
    'pads',
    'links',
    'reserved',
]
struct_media_links_enum._fields_ = [
    ('entity', __u32),
    ('pads', POINTER(struct_media_pad_desc)),
    ('links', POINTER(struct_media_link_desc)),
    ('reserved', __u32 * int(4)),
]


class struct_media_v2_entity(Structure):
    pass

struct_media_v2_entity.__slots__ = [
    'id',
    'name',
    'function',
    'flags',
    'reserved',
]
struct_media_v2_entity._fields_ = [
    ('id', __u32),
    ('name', c_char * int(64)),
    ('function', __u32),
    ('flags', __u32),
    ('reserved', __u32 * int(5)),
]


class struct_media_v2_intf_devnode(Structure):
    pass

struct_media_v2_intf_devnode.__slots__ = [
    'major',
    'minor',
]
struct_media_v2_intf_devnode._fields_ = [
    ('major', __u32),
    ('minor', __u32),
]


class union_anon_36(Union):
    pass

union_anon_36.__slots__ = [
    'devnode',
    'raw',
]
union_anon_36._fields_ = [
    ('devnode', struct_media_v2_intf_devnode),
    ('raw', __u32 * int(16)),
]


class struct_media_v2_interface(Structure):
    pass

struct_media_v2_interface.__slots__ = [
    'id',
    'intf_type',
    'flags',
    'reserved',
    'unnamed_1',
]
struct_media_v2_interface._anonymous_ = [
    'unnamed_1',
]
struct_media_v2_interface._fields_ = [
    ('id', __u32),
    ('intf_type', __u32),
    ('flags', __u32),
    ('reserved', __u32 * int(9)),
    ('unnamed_1', union_anon_36),
]


class struct_media_v2_pad(Structure):
    pass

struct_media_v2_pad.__slots__ = [
    'id',
    'entity_id',
    'flags',
    'index',
    'reserved',
]
struct_media_v2_pad._fields_ = [
    ('id', __u32),
    ('entity_id', __u32),
    ('flags', __u32),
    ('index', __u32),
    ('reserved', __u32 * int(4)),
]


class struct_media_v2_link(Structure):
    pass

struct_media_v2_link.__slots__ = [
    'id',
    'source_id',
    'sink_id',
    'flags',
    'reserved',
]
struct_media_v2_link._fields_ = [
    ('id', __u32),
    ('source_id', __u32),
    ('sink_id', __u32),
    ('flags', __u32),
    ('reserved', __u32 * int(6)),
]


class struct_media_v2_topology(Structure):
    pass

struct_media_v2_topology.__slots__ = [
    'topology_version',
    'num_entities',
    'reserved1',
    'ptr_entities',
    'num_interfaces',
    'reserved2',
    'ptr_interfaces',
    'num_pads',
    'reserved3',
    'ptr_pads',
    'num_links',
    'reserved4',
    'ptr_links',
]
struct_media_v2_topology._fields_ = [
    ('topology_version', __u64),
    ('num_entities', __u32),
    ('reserved1', __u32),
    ('ptr_entities', __u64),
    ('num_interfaces', __u32),
    ('reserved2', __u32),
    ('ptr_interfaces', __u64),
    ('num_pads', __u32),
    ('reserved3', __u32),
    ('ptr_pads', __u64),
    ('num_links', __u32),
    ('reserved4', __u32),
    ('ptr_links', __u64),
]


class union_anon_37(Union):
    pass

union_anon_37.__slots__ = [
    'ycbcr_enc',
    'hsv_enc',
]
union_anon_37._fields_ = [
    ('ycbcr_enc', __u16),
    ('hsv_enc', __u16),
]


class struct_v4l2_mbus_framefmt(Structure):
    pass

struct_v4l2_mbus_framefmt.__slots__ = [
    'width',
    'height',
    'code',
    'field',
    'colorspace',
    'unnamed_1',
    'quantization',
    'xfer_func',
    'flags',
    'reserved',
]
struct_v4l2_mbus_framefmt._anonymous_ = [
    'unnamed_1',
]
struct_v4l2_mbus_framefmt._fields_ = [
    ('width', __u32),
    ('height', __u32),
    ('code', __u32),
    ('field', __u32),
    ('colorspace', __u32),
    ('unnamed_1', union_anon_37),
    ('quantization', __u16),
    ('xfer_func', __u16),
    ('flags', __u16),
    ('reserved', __u16 * int(10)),
]

enum_v4l2_mbus_pixelcode = c_int

V4L2_MBUS_FMT_FIXED = 0x0001

V4L2_MBUS_FMT_RGB444_2X8_PADHI_BE = 0x1001

V4L2_MBUS_FMT_RGB444_2X8_PADHI_LE = 0x1002

V4L2_MBUS_FMT_RGB555_2X8_PADHI_BE = 0x1003

V4L2_MBUS_FMT_RGB555_2X8_PADHI_LE = 0x1004

V4L2_MBUS_FMT_BGR565_2X8_BE = 0x1005

V4L2_MBUS_FMT_BGR565_2X8_LE = 0x1006

V4L2_MBUS_FMT_RGB565_2X8_BE = 0x1007

V4L2_MBUS_FMT_RGB565_2X8_LE = 0x1008

V4L2_MBUS_FMT_RGB666_1X18 = 0x1009

V4L2_MBUS_FMT_RGB888_1X24 = 0x100a

V4L2_MBUS_FMT_RGB888_2X12_BE = 0x100b

V4L2_MBUS_FMT_RGB888_2X12_LE = 0x100c

V4L2_MBUS_FMT_ARGB8888_1X32 = 0x100d

V4L2_MBUS_FMT_Y8_1X8 = 0x2001

V4L2_MBUS_FMT_UV8_1X8 = 0x2015

V4L2_MBUS_FMT_UYVY8_1_5X8 = 0x2002

V4L2_MBUS_FMT_VYUY8_1_5X8 = 0x2003

V4L2_MBUS_FMT_YUYV8_1_5X8 = 0x2004

V4L2_MBUS_FMT_YVYU8_1_5X8 = 0x2005

V4L2_MBUS_FMT_UYVY8_2X8 = 0x2006

V4L2_MBUS_FMT_VYUY8_2X8 = 0x2007

V4L2_MBUS_FMT_YUYV8_2X8 = 0x2008

V4L2_MBUS_FMT_YVYU8_2X8 = 0x2009

V4L2_MBUS_FMT_Y10_1X10 = 0x200a

V4L2_MBUS_FMT_UYVY10_2X10 = 0x2018

V4L2_MBUS_FMT_VYUY10_2X10 = 0x2019

V4L2_MBUS_FMT_YUYV10_2X10 = 0x200b

V4L2_MBUS_FMT_YVYU10_2X10 = 0x200c

V4L2_MBUS_FMT_Y12_1X12 = 0x2013

V4L2_MBUS_FMT_UYVY8_1X16 = 0x200f

V4L2_MBUS_FMT_VYUY8_1X16 = 0x2010

V4L2_MBUS_FMT_YUYV8_1X16 = 0x2011

V4L2_MBUS_FMT_YVYU8_1X16 = 0x2012

V4L2_MBUS_FMT_YDYUYDYV8_1X16 = 0x2014

V4L2_MBUS_FMT_UYVY10_1X20 = 0x201a

V4L2_MBUS_FMT_VYUY10_1X20 = 0x201b

V4L2_MBUS_FMT_YUYV10_1X20 = 0x200d

V4L2_MBUS_FMT_YVYU10_1X20 = 0x200e

V4L2_MBUS_FMT_YUV10_1X30 = 0x2016

V4L2_MBUS_FMT_AYUV8_1X32 = 0x2017

V4L2_MBUS_FMT_UYVY12_2X12 = 0x201c

V4L2_MBUS_FMT_VYUY12_2X12 = 0x201d

V4L2_MBUS_FMT_YUYV12_2X12 = 0x201e

V4L2_MBUS_FMT_YVYU12_2X12 = 0x201f

V4L2_MBUS_FMT_UYVY12_1X24 = 0x2020

V4L2_MBUS_FMT_VYUY12_1X24 = 0x2021

V4L2_MBUS_FMT_YUYV12_1X24 = 0x2022

V4L2_MBUS_FMT_YVYU12_1X24 = 0x2023

V4L2_MBUS_FMT_SBGGR8_1X8 = 0x3001

V4L2_MBUS_FMT_SGBRG8_1X8 = 0x3013

V4L2_MBUS_FMT_SGRBG8_1X8 = 0x3002

V4L2_MBUS_FMT_SRGGB8_1X8 = 0x3014

V4L2_MBUS_FMT_SBGGR10_ALAW8_1X8 = 0x3015

V4L2_MBUS_FMT_SGBRG10_ALAW8_1X8 = 0x3016

V4L2_MBUS_FMT_SGRBG10_ALAW8_1X8 = 0x3017

V4L2_MBUS_FMT_SRGGB10_ALAW8_1X8 = 0x3018

V4L2_MBUS_FMT_SBGGR10_DPCM8_1X8 = 0x300b

V4L2_MBUS_FMT_SGBRG10_DPCM8_1X8 = 0x300c

V4L2_MBUS_FMT_SGRBG10_DPCM8_1X8 = 0x3009

V4L2_MBUS_FMT_SRGGB10_DPCM8_1X8 = 0x300d

V4L2_MBUS_FMT_SBGGR10_2X8_PADHI_BE = 0x3003

V4L2_MBUS_FMT_SBGGR10_2X8_PADHI_LE = 0x3004

V4L2_MBUS_FMT_SBGGR10_2X8_PADLO_BE = 0x3005

V4L2_MBUS_FMT_SBGGR10_2X8_PADLO_LE = 0x3006

V4L2_MBUS_FMT_SBGGR10_1X10 = 0x3007

V4L2_MBUS_FMT_SGBRG10_1X10 = 0x300e

V4L2_MBUS_FMT_SGRBG10_1X10 = 0x300a

V4L2_MBUS_FMT_SRGGB10_1X10 = 0x300f

V4L2_MBUS_FMT_SBGGR12_1X12 = 0x3008

V4L2_MBUS_FMT_SGBRG12_1X12 = 0x3010

V4L2_MBUS_FMT_SGRBG12_1X12 = 0x3011

V4L2_MBUS_FMT_SRGGB12_1X12 = 0x3012

V4L2_MBUS_FMT_JPEG_1X8 = 0x4001

V4L2_MBUS_FMT_S5C_UYVY_JPEG_1X8 = 0x5001

V4L2_MBUS_FMT_AHSV8888_1X32 = 0x6001

enum_v4l2_subdev_format_whence = c_int

V4L2_SUBDEV_FORMAT_TRY = 0

V4L2_SUBDEV_FORMAT_ACTIVE = 1


class struct_v4l2_subdev_format(Structure):
    pass

struct_v4l2_subdev_format.__slots__ = [
    'which',
    'pad',
    'format',
    'stream',
    'reserved',
]
struct_v4l2_subdev_format._fields_ = [
    ('which', __u32),
    ('pad', __u32),
    ('format', struct_v4l2_mbus_framefmt),
    ('stream', __u32),
    ('reserved', __u32 * int(7)),
]


class struct_v4l2_subdev_crop(Structure):
    pass

struct_v4l2_subdev_crop.__slots__ = [
    'which',
    'pad',
    'rect',
    'stream',
    'reserved',
]
struct_v4l2_subdev_crop._fields_ = [
    ('which', __u32),
    ('pad', __u32),
    ('rect', struct_v4l2_rect),
    ('stream', __u32),
    ('reserved', __u32 * int(7)),
]


class struct_v4l2_subdev_mbus_code_enum(Structure):
    pass

struct_v4l2_subdev_mbus_code_enum.__slots__ = [
    'pad',
    'index',
    'code',
    'which',
    'flags',
    'stream',
    'reserved',
]
struct_v4l2_subdev_mbus_code_enum._fields_ = [
    ('pad', __u32),
    ('index', __u32),
    ('code', __u32),
    ('which', __u32),
    ('flags', __u32),
    ('stream', __u32),
    ('reserved', __u32 * int(6)),
]


class struct_v4l2_subdev_frame_size_enum(Structure):
    pass

struct_v4l2_subdev_frame_size_enum.__slots__ = [
    'index',
    'pad',
    'code',
    'min_width',
    'max_width',
    'min_height',
    'max_height',
    'which',
    'stream',
    'reserved',
]
struct_v4l2_subdev_frame_size_enum._fields_ = [
    ('index', __u32),
    ('pad', __u32),
    ('code', __u32),
    ('min_width', __u32),
    ('max_width', __u32),
    ('min_height', __u32),
    ('max_height', __u32),
    ('which', __u32),
    ('stream', __u32),
    ('reserved', __u32 * int(7)),
]


class struct_v4l2_subdev_frame_interval(Structure):
    pass

struct_v4l2_subdev_frame_interval.__slots__ = [
    'pad',
    'interval',
    'stream',
    'which',
    'reserved',
]
struct_v4l2_subdev_frame_interval._fields_ = [
    ('pad', __u32),
    ('interval', struct_v4l2_fract),
    ('stream', __u32),
    ('which', __u32),
    ('reserved', __u32 * int(7)),
]


class struct_v4l2_subdev_frame_interval_enum(Structure):
    pass

struct_v4l2_subdev_frame_interval_enum.__slots__ = [
    'index',
    'pad',
    'code',
    'width',
    'height',
    'interval',
    'which',
    'stream',
    'reserved',
]
struct_v4l2_subdev_frame_interval_enum._fields_ = [
    ('index', __u32),
    ('pad', __u32),
    ('code', __u32),
    ('width', __u32),
    ('height', __u32),
    ('interval', struct_v4l2_fract),
    ('which', __u32),
    ('stream', __u32),
    ('reserved', __u32 * int(7)),
]


class struct_v4l2_subdev_selection(Structure):
    pass

struct_v4l2_subdev_selection.__slots__ = [
    'which',
    'pad',
    'target',
    'flags',
    'r',
    'stream',
    'reserved',
]
struct_v4l2_subdev_selection._fields_ = [
    ('which', __u32),
    ('pad', __u32),
    ('target', __u32),
    ('flags', __u32),
    ('r', struct_v4l2_rect),
    ('stream', __u32),
    ('reserved', __u32 * int(7)),
]


class struct_v4l2_subdev_capability(Structure):
    pass

struct_v4l2_subdev_capability.__slots__ = [
    'version',
    'capabilities',
    'reserved',
]
struct_v4l2_subdev_capability._fields_ = [
    ('version', __u32),
    ('capabilities', __u32),
    ('reserved', __u32 * int(14)),
]


class struct_v4l2_subdev_route(Structure):
    pass

struct_v4l2_subdev_route.__slots__ = [
    'sink_pad',
    'sink_stream',
    'source_pad',
    'source_stream',
    'flags',
    'reserved',
]
struct_v4l2_subdev_route._fields_ = [
    ('sink_pad', __u32),
    ('sink_stream', __u32),
    ('source_pad', __u32),
    ('source_stream', __u32),
    ('flags', __u32),
    ('reserved', __u32 * int(5)),
]


class struct_v4l2_subdev_routing(Structure):
    pass

struct_v4l2_subdev_routing.__slots__ = [
    'which',
    'len_routes',
    'routes',
    'num_routes',
    'reserved',
]
struct_v4l2_subdev_routing._fields_ = [
    ('which', __u32),
    ('len_routes', __u32),
    ('routes', __u64),
    ('num_routes', __u32),
    ('reserved', __u32 * int(11)),
]


class struct_v4l2_subdev_client_capability(Structure):
    pass

struct_v4l2_subdev_client_capability.__slots__ = [
    'capabilities',
]
struct_v4l2_subdev_client_capability._fields_ = [
    ('capabilities', __u64),
]


_IOC_NRBITS = 8


_IOC_TYPEBITS = 8


_IOC_SIZEBITS = 14


_IOC_NRSHIFT = 0


_IOC_TYPESHIFT = (_IOC_NRSHIFT + _IOC_NRBITS)


_IOC_SIZESHIFT = (_IOC_TYPESHIFT + _IOC_TYPEBITS)


_IOC_DIRSHIFT = (_IOC_SIZESHIFT + _IOC_SIZEBITS)


_IOC_NONE = 0


_IOC_WRITE = 1


_IOC_READ = 2


def _IOC(dir, type, nr, size):
    return ((((dir << _IOC_DIRSHIFT) | (ord(type) << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))


def _IOC_TYPECHECK(t):
    return sizeof(t)


def _IO(type, nr):
    return (_IOC (_IOC_NONE, type, nr, 0))


def _IOR(type, nr, size):
    return (_IOC (_IOC_READ, type, nr, (_IOC_TYPECHECK (size))))


def _IOW(type, nr, size):
    return (_IOC (_IOC_WRITE, type, nr, (_IOC_TYPECHECK (size))))


def _IOWR(type, nr, size):
    return (_IOC ((_IOC_READ | _IOC_WRITE), type, nr, (_IOC_TYPECHECK (size))))


V4L2_CTRL_CLASS_USER = 0x00980000


V4L2_CTRL_CLASS_CODEC = 0x00990000


V4L2_CTRL_CLASS_CAMERA = 0x009a0000


V4L2_CTRL_CLASS_FM_TX = 0x009b0000


V4L2_CTRL_CLASS_FLASH = 0x009c0000


V4L2_CTRL_CLASS_JPEG = 0x009d0000


V4L2_CTRL_CLASS_IMAGE_SOURCE = 0x009e0000


V4L2_CTRL_CLASS_IMAGE_PROC = 0x009f0000


V4L2_CTRL_CLASS_DV = 0x00a00000


V4L2_CTRL_CLASS_FM_RX = 0x00a10000


V4L2_CTRL_CLASS_RF_TUNER = 0x00a20000


V4L2_CTRL_CLASS_DETECT = 0x00a30000


V4L2_CTRL_CLASS_CODEC_STATELESS = 0x00a40000


V4L2_CTRL_CLASS_COLORIMETRY = 0x00a50000


V4L2_CID_BASE = (V4L2_CTRL_CLASS_USER | 0x900)


V4L2_CID_USER_BASE = V4L2_CID_BASE


V4L2_CID_USER_CLASS = (V4L2_CTRL_CLASS_USER | 1)


V4L2_CID_BRIGHTNESS = (V4L2_CID_BASE + 0)


V4L2_CID_CONTRAST = (V4L2_CID_BASE + 1)


V4L2_CID_SATURATION = (V4L2_CID_BASE + 2)


V4L2_CID_HUE = (V4L2_CID_BASE + 3)


V4L2_CID_AUDIO_VOLUME = (V4L2_CID_BASE + 5)


V4L2_CID_AUDIO_BALANCE = (V4L2_CID_BASE + 6)


V4L2_CID_AUDIO_BASS = (V4L2_CID_BASE + 7)


V4L2_CID_AUDIO_TREBLE = (V4L2_CID_BASE + 8)


V4L2_CID_AUDIO_MUTE = (V4L2_CID_BASE + 9)


V4L2_CID_AUDIO_LOUDNESS = (V4L2_CID_BASE + 10)


V4L2_CID_BLACK_LEVEL = (V4L2_CID_BASE + 11)


V4L2_CID_AUTO_WHITE_BALANCE = (V4L2_CID_BASE + 12)


V4L2_CID_DO_WHITE_BALANCE = (V4L2_CID_BASE + 13)


V4L2_CID_RED_BALANCE = (V4L2_CID_BASE + 14)


V4L2_CID_BLUE_BALANCE = (V4L2_CID_BASE + 15)


V4L2_CID_GAMMA = (V4L2_CID_BASE + 16)


V4L2_CID_WHITENESS = V4L2_CID_GAMMA


V4L2_CID_EXPOSURE = (V4L2_CID_BASE + 17)


V4L2_CID_AUTOGAIN = (V4L2_CID_BASE + 18)


V4L2_CID_GAIN = (V4L2_CID_BASE + 19)


V4L2_CID_HFLIP = (V4L2_CID_BASE + 20)


V4L2_CID_VFLIP = (V4L2_CID_BASE + 21)


V4L2_CID_POWER_LINE_FREQUENCY = (V4L2_CID_BASE + 24)


V4L2_CID_HUE_AUTO = (V4L2_CID_BASE + 25)


V4L2_CID_WHITE_BALANCE_TEMPERATURE = (V4L2_CID_BASE + 26)


V4L2_CID_SHARPNESS = (V4L2_CID_BASE + 27)


V4L2_CID_BACKLIGHT_COMPENSATION = (V4L2_CID_BASE + 28)


V4L2_CID_CHROMA_AGC = (V4L2_CID_BASE + 29)


V4L2_CID_COLOR_KILLER = (V4L2_CID_BASE + 30)


V4L2_CID_COLORFX = (V4L2_CID_BASE + 31)


V4L2_CID_AUTOBRIGHTNESS = (V4L2_CID_BASE + 32)


V4L2_CID_BAND_STOP_FILTER = (V4L2_CID_BASE + 33)


V4L2_CID_ROTATE = (V4L2_CID_BASE + 34)


V4L2_CID_BG_COLOR = (V4L2_CID_BASE + 35)


V4L2_CID_CHROMA_GAIN = (V4L2_CID_BASE + 36)


V4L2_CID_ILLUMINATORS_1 = (V4L2_CID_BASE + 37)


V4L2_CID_ILLUMINATORS_2 = (V4L2_CID_BASE + 38)


V4L2_CID_MIN_BUFFERS_FOR_CAPTURE = (V4L2_CID_BASE + 39)


V4L2_CID_MIN_BUFFERS_FOR_OUTPUT = (V4L2_CID_BASE + 40)


V4L2_CID_ALPHA_COMPONENT = (V4L2_CID_BASE + 41)


V4L2_CID_COLORFX_CBCR = (V4L2_CID_BASE + 42)


V4L2_CID_COLORFX_RGB = (V4L2_CID_BASE + 43)


V4L2_CID_LASTP1 = (V4L2_CID_BASE + 44)


V4L2_CID_USER_MEYE_BASE = (V4L2_CID_USER_BASE + 0x1000)


V4L2_CID_USER_BTTV_BASE = (V4L2_CID_USER_BASE + 0x1010)


V4L2_CID_USER_S2255_BASE = (V4L2_CID_USER_BASE + 0x1030)


V4L2_CID_USER_SI476X_BASE = (V4L2_CID_USER_BASE + 0x1040)


V4L2_CID_USER_TI_VPE_BASE = (V4L2_CID_USER_BASE + 0x1050)


V4L2_CID_USER_SAA7134_BASE = (V4L2_CID_USER_BASE + 0x1060)


V4L2_CID_USER_ADV7180_BASE = (V4L2_CID_USER_BASE + 0x1070)


V4L2_CID_USER_TC358743_BASE = (V4L2_CID_USER_BASE + 0x1080)


V4L2_CID_USER_MAX217X_BASE = (V4L2_CID_USER_BASE + 0x1090)


V4L2_CID_USER_IMX_BASE = (V4L2_CID_USER_BASE + 0x10b0)


V4L2_CID_USER_ATMEL_ISC_BASE = (V4L2_CID_USER_BASE + 0x10c0)


V4L2_CID_USER_CODA_BASE = (V4L2_CID_USER_BASE + 0x10e0)


V4L2_CID_USER_CCS_BASE = (V4L2_CID_USER_BASE + 0x10f0)


V4L2_CID_USER_ALLEGRO_BASE = (V4L2_CID_USER_BASE + 0x1170)


V4L2_CID_USER_ISL7998X_BASE = (V4L2_CID_USER_BASE + 0x1180)


V4L2_CID_USER_DW100_BASE = (V4L2_CID_USER_BASE + 0x1190)


V4L2_CID_USER_ASPEED_BASE = (V4L2_CID_USER_BASE + 0x11a0)


V4L2_CID_USER_NPCM_BASE = (V4L2_CID_USER_BASE + 0x11b0)


V4L2_CID_USER_THP7312_BASE = (V4L2_CID_USER_BASE + 0x11c0)


V4L2_CID_CODEC_BASE = (V4L2_CTRL_CLASS_CODEC | 0x900)


V4L2_CID_CODEC_CLASS = (V4L2_CTRL_CLASS_CODEC | 1)


V4L2_CID_MPEG_STREAM_TYPE = (V4L2_CID_CODEC_BASE + 0)


V4L2_CID_MPEG_STREAM_PID_PMT = (V4L2_CID_CODEC_BASE + 1)


V4L2_CID_MPEG_STREAM_PID_AUDIO = (V4L2_CID_CODEC_BASE + 2)


V4L2_CID_MPEG_STREAM_PID_VIDEO = (V4L2_CID_CODEC_BASE + 3)


V4L2_CID_MPEG_STREAM_PID_PCR = (V4L2_CID_CODEC_BASE + 4)


V4L2_CID_MPEG_STREAM_PES_ID_AUDIO = (V4L2_CID_CODEC_BASE + 5)


V4L2_CID_MPEG_STREAM_PES_ID_VIDEO = (V4L2_CID_CODEC_BASE + 6)


V4L2_CID_MPEG_STREAM_VBI_FMT = (V4L2_CID_CODEC_BASE + 7)


V4L2_CID_MPEG_AUDIO_SAMPLING_FREQ = (V4L2_CID_CODEC_BASE + 100)


V4L2_CID_MPEG_AUDIO_ENCODING = (V4L2_CID_CODEC_BASE + 101)


V4L2_CID_MPEG_AUDIO_L1_BITRATE = (V4L2_CID_CODEC_BASE + 102)


V4L2_CID_MPEG_AUDIO_L2_BITRATE = (V4L2_CID_CODEC_BASE + 103)


V4L2_CID_MPEG_AUDIO_L3_BITRATE = (V4L2_CID_CODEC_BASE + 104)


V4L2_CID_MPEG_AUDIO_MODE = (V4L2_CID_CODEC_BASE + 105)


V4L2_CID_MPEG_AUDIO_MODE_EXTENSION = (V4L2_CID_CODEC_BASE + 106)


V4L2_CID_MPEG_AUDIO_EMPHASIS = (V4L2_CID_CODEC_BASE + 107)


V4L2_CID_MPEG_AUDIO_CRC = (V4L2_CID_CODEC_BASE + 108)


V4L2_CID_MPEG_AUDIO_MUTE = (V4L2_CID_CODEC_BASE + 109)


V4L2_CID_MPEG_AUDIO_AAC_BITRATE = (V4L2_CID_CODEC_BASE + 110)


V4L2_CID_MPEG_AUDIO_AC3_BITRATE = (V4L2_CID_CODEC_BASE + 111)


V4L2_CID_MPEG_AUDIO_DEC_PLAYBACK = (V4L2_CID_CODEC_BASE + 112)


V4L2_CID_MPEG_AUDIO_DEC_MULTILINGUAL_PLAYBACK = (V4L2_CID_CODEC_BASE + 113)


V4L2_CID_MPEG_VIDEO_ENCODING = (V4L2_CID_CODEC_BASE + 200)


V4L2_CID_MPEG_VIDEO_ASPECT = (V4L2_CID_CODEC_BASE + 201)


V4L2_CID_MPEG_VIDEO_B_FRAMES = (V4L2_CID_CODEC_BASE + 202)


V4L2_CID_MPEG_VIDEO_GOP_SIZE = (V4L2_CID_CODEC_BASE + 203)


V4L2_CID_MPEG_VIDEO_GOP_CLOSURE = (V4L2_CID_CODEC_BASE + 204)


V4L2_CID_MPEG_VIDEO_PULLDOWN = (V4L2_CID_CODEC_BASE + 205)


V4L2_CID_MPEG_VIDEO_BITRATE_MODE = (V4L2_CID_CODEC_BASE + 206)


V4L2_CID_MPEG_VIDEO_BITRATE = (V4L2_CID_CODEC_BASE + 207)


V4L2_CID_MPEG_VIDEO_BITRATE_PEAK = (V4L2_CID_CODEC_BASE + 208)


V4L2_CID_MPEG_VIDEO_TEMPORAL_DECIMATION = (V4L2_CID_CODEC_BASE + 209)


V4L2_CID_MPEG_VIDEO_MUTE = (V4L2_CID_CODEC_BASE + 210)


V4L2_CID_MPEG_VIDEO_MUTE_YUV = (V4L2_CID_CODEC_BASE + 211)


V4L2_CID_MPEG_VIDEO_DECODER_SLICE_INTERFACE = (V4L2_CID_CODEC_BASE + 212)


V4L2_CID_MPEG_VIDEO_DECODER_MPEG4_DEBLOCK_FILTER = (V4L2_CID_CODEC_BASE + 213)


V4L2_CID_MPEG_VIDEO_CYCLIC_INTRA_REFRESH_MB = (V4L2_CID_CODEC_BASE + 214)


V4L2_CID_MPEG_VIDEO_FRAME_RC_ENABLE = (V4L2_CID_CODEC_BASE + 215)


V4L2_CID_MPEG_VIDEO_HEADER_MODE = (V4L2_CID_CODEC_BASE + 216)


V4L2_CID_MPEG_VIDEO_MAX_REF_PIC = (V4L2_CID_CODEC_BASE + 217)


V4L2_CID_MPEG_VIDEO_MB_RC_ENABLE = (V4L2_CID_CODEC_BASE + 218)


V4L2_CID_MPEG_VIDEO_MULTI_SLICE_MAX_BYTES = (V4L2_CID_CODEC_BASE + 219)


V4L2_CID_MPEG_VIDEO_MULTI_SLICE_MAX_MB = (V4L2_CID_CODEC_BASE + 220)


V4L2_CID_MPEG_VIDEO_MULTI_SLICE_MODE = (V4L2_CID_CODEC_BASE + 221)


V4L2_CID_MPEG_VIDEO_VBV_SIZE = (V4L2_CID_CODEC_BASE + 222)


V4L2_CID_MPEG_VIDEO_DEC_PTS = (V4L2_CID_CODEC_BASE + 223)


V4L2_CID_MPEG_VIDEO_DEC_FRAME = (V4L2_CID_CODEC_BASE + 224)


V4L2_CID_MPEG_VIDEO_VBV_DELAY = (V4L2_CID_CODEC_BASE + 225)


V4L2_CID_MPEG_VIDEO_REPEAT_SEQ_HEADER = (V4L2_CID_CODEC_BASE + 226)


V4L2_CID_MPEG_VIDEO_MV_H_SEARCH_RANGE = (V4L2_CID_CODEC_BASE + 227)


V4L2_CID_MPEG_VIDEO_MV_V_SEARCH_RANGE = (V4L2_CID_CODEC_BASE + 228)


V4L2_CID_MPEG_VIDEO_FORCE_KEY_FRAME = (V4L2_CID_CODEC_BASE + 229)


V4L2_CID_MPEG_VIDEO_BASELAYER_PRIORITY_ID = (V4L2_CID_CODEC_BASE + 230)


V4L2_CID_MPEG_VIDEO_AU_DELIMITER = (V4L2_CID_CODEC_BASE + 231)


V4L2_CID_MPEG_VIDEO_LTR_COUNT = (V4L2_CID_CODEC_BASE + 232)


V4L2_CID_MPEG_VIDEO_FRAME_LTR_INDEX = (V4L2_CID_CODEC_BASE + 233)


V4L2_CID_MPEG_VIDEO_USE_LTR_FRAMES = (V4L2_CID_CODEC_BASE + 234)


V4L2_CID_MPEG_VIDEO_DEC_CONCEAL_COLOR = (V4L2_CID_CODEC_BASE + 235)


V4L2_CID_MPEG_VIDEO_INTRA_REFRESH_PERIOD = (V4L2_CID_CODEC_BASE + 236)


V4L2_CID_MPEG_VIDEO_INTRA_REFRESH_PERIOD_TYPE = (V4L2_CID_CODEC_BASE + 237)


V4L2_CID_MPEG_VIDEO_MPEG2_LEVEL = (V4L2_CID_CODEC_BASE + 270)


V4L2_CID_MPEG_VIDEO_MPEG2_PROFILE = (V4L2_CID_CODEC_BASE + 271)


V4L2_CID_FWHT_I_FRAME_QP = (V4L2_CID_CODEC_BASE + 290)


V4L2_CID_FWHT_P_FRAME_QP = (V4L2_CID_CODEC_BASE + 291)


V4L2_CID_MPEG_VIDEO_H263_I_FRAME_QP = (V4L2_CID_CODEC_BASE + 300)


V4L2_CID_MPEG_VIDEO_H263_P_FRAME_QP = (V4L2_CID_CODEC_BASE + 301)


V4L2_CID_MPEG_VIDEO_H263_B_FRAME_QP = (V4L2_CID_CODEC_BASE + 302)


V4L2_CID_MPEG_VIDEO_H263_MIN_QP = (V4L2_CID_CODEC_BASE + 303)


V4L2_CID_MPEG_VIDEO_H263_MAX_QP = (V4L2_CID_CODEC_BASE + 304)


V4L2_CID_MPEG_VIDEO_H264_I_FRAME_QP = (V4L2_CID_CODEC_BASE + 350)


V4L2_CID_MPEG_VIDEO_H264_P_FRAME_QP = (V4L2_CID_CODEC_BASE + 351)


V4L2_CID_MPEG_VIDEO_H264_B_FRAME_QP = (V4L2_CID_CODEC_BASE + 352)


V4L2_CID_MPEG_VIDEO_H264_MIN_QP = (V4L2_CID_CODEC_BASE + 353)


V4L2_CID_MPEG_VIDEO_H264_MAX_QP = (V4L2_CID_CODEC_BASE + 354)


V4L2_CID_MPEG_VIDEO_H264_8X8_TRANSFORM = (V4L2_CID_CODEC_BASE + 355)


V4L2_CID_MPEG_VIDEO_H264_CPB_SIZE = (V4L2_CID_CODEC_BASE + 356)


V4L2_CID_MPEG_VIDEO_H264_ENTROPY_MODE = (V4L2_CID_CODEC_BASE + 357)


V4L2_CID_MPEG_VIDEO_H264_I_PERIOD = (V4L2_CID_CODEC_BASE + 358)


V4L2_CID_MPEG_VIDEO_H264_LEVEL = (V4L2_CID_CODEC_BASE + 359)


V4L2_CID_MPEG_VIDEO_H264_LOOP_FILTER_ALPHA = (V4L2_CID_CODEC_BASE + 360)


V4L2_CID_MPEG_VIDEO_H264_LOOP_FILTER_BETA = (V4L2_CID_CODEC_BASE + 361)


V4L2_CID_MPEG_VIDEO_H264_LOOP_FILTER_MODE = (V4L2_CID_CODEC_BASE + 362)


V4L2_CID_MPEG_VIDEO_H264_PROFILE = (V4L2_CID_CODEC_BASE + 363)


V4L2_CID_MPEG_VIDEO_H264_VUI_EXT_SAR_HEIGHT = (V4L2_CID_CODEC_BASE + 364)


V4L2_CID_MPEG_VIDEO_H264_VUI_EXT_SAR_WIDTH = (V4L2_CID_CODEC_BASE + 365)


V4L2_CID_MPEG_VIDEO_H264_VUI_SAR_ENABLE = (V4L2_CID_CODEC_BASE + 366)


V4L2_CID_MPEG_VIDEO_H264_VUI_SAR_IDC = (V4L2_CID_CODEC_BASE + 367)


V4L2_CID_MPEG_VIDEO_H264_SEI_FRAME_PACKING = (V4L2_CID_CODEC_BASE + 368)


V4L2_CID_MPEG_VIDEO_H264_SEI_FP_CURRENT_FRAME_0 = (V4L2_CID_CODEC_BASE + 369)


V4L2_CID_MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE = (V4L2_CID_CODEC_BASE + 370)


V4L2_CID_MPEG_VIDEO_H264_FMO = (V4L2_CID_CODEC_BASE + 371)


V4L2_CID_MPEG_VIDEO_H264_FMO_MAP_TYPE = (V4L2_CID_CODEC_BASE + 372)


V4L2_CID_MPEG_VIDEO_H264_FMO_SLICE_GROUP = (V4L2_CID_CODEC_BASE + 373)


V4L2_CID_MPEG_VIDEO_H264_FMO_CHANGE_DIRECTION = (V4L2_CID_CODEC_BASE + 374)


V4L2_CID_MPEG_VIDEO_H264_FMO_CHANGE_RATE = (V4L2_CID_CODEC_BASE + 375)


V4L2_CID_MPEG_VIDEO_H264_FMO_RUN_LENGTH = (V4L2_CID_CODEC_BASE + 376)


V4L2_CID_MPEG_VIDEO_H264_ASO = (V4L2_CID_CODEC_BASE + 377)


V4L2_CID_MPEG_VIDEO_H264_ASO_SLICE_ORDER = (V4L2_CID_CODEC_BASE + 378)


V4L2_CID_MPEG_VIDEO_H264_HIERARCHICAL_CODING = (V4L2_CID_CODEC_BASE + 379)


V4L2_CID_MPEG_VIDEO_H264_HIERARCHICAL_CODING_TYPE = (V4L2_CID_CODEC_BASE + 380)


V4L2_CID_MPEG_VIDEO_H264_HIERARCHICAL_CODING_LAYER = (V4L2_CID_CODEC_BASE + 381)


V4L2_CID_MPEG_VIDEO_H264_HIERARCHICAL_CODING_LAYER_QP = (V4L2_CID_CODEC_BASE + 382)


V4L2_CID_MPEG_VIDEO_H264_CONSTRAINED_INTRA_PREDICTION = (V4L2_CID_CODEC_BASE + 383)


V4L2_CID_MPEG_VIDEO_H264_CHROMA_QP_INDEX_OFFSET = (V4L2_CID_CODEC_BASE + 384)


V4L2_CID_MPEG_VIDEO_H264_I_FRAME_MIN_QP = (V4L2_CID_CODEC_BASE + 385)


V4L2_CID_MPEG_VIDEO_H264_I_FRAME_MAX_QP = (V4L2_CID_CODEC_BASE + 386)


V4L2_CID_MPEG_VIDEO_H264_P_FRAME_MIN_QP = (V4L2_CID_CODEC_BASE + 387)


V4L2_CID_MPEG_VIDEO_H264_P_FRAME_MAX_QP = (V4L2_CID_CODEC_BASE + 388)


V4L2_CID_MPEG_VIDEO_H264_B_FRAME_MIN_QP = (V4L2_CID_CODEC_BASE + 389)


V4L2_CID_MPEG_VIDEO_H264_B_FRAME_MAX_QP = (V4L2_CID_CODEC_BASE + 390)


V4L2_CID_MPEG_VIDEO_H264_HIER_CODING_L0_BR = (V4L2_CID_CODEC_BASE + 391)


V4L2_CID_MPEG_VIDEO_H264_HIER_CODING_L1_BR = (V4L2_CID_CODEC_BASE + 392)


V4L2_CID_MPEG_VIDEO_H264_HIER_CODING_L2_BR = (V4L2_CID_CODEC_BASE + 393)


V4L2_CID_MPEG_VIDEO_H264_HIER_CODING_L3_BR = (V4L2_CID_CODEC_BASE + 394)


V4L2_CID_MPEG_VIDEO_H264_HIER_CODING_L4_BR = (V4L2_CID_CODEC_BASE + 395)


V4L2_CID_MPEG_VIDEO_H264_HIER_CODING_L5_BR = (V4L2_CID_CODEC_BASE + 396)


V4L2_CID_MPEG_VIDEO_H264_HIER_CODING_L6_BR = (V4L2_CID_CODEC_BASE + 397)


V4L2_CID_MPEG_VIDEO_MPEG4_I_FRAME_QP = (V4L2_CID_CODEC_BASE + 400)


V4L2_CID_MPEG_VIDEO_MPEG4_P_FRAME_QP = (V4L2_CID_CODEC_BASE + 401)


V4L2_CID_MPEG_VIDEO_MPEG4_B_FRAME_QP = (V4L2_CID_CODEC_BASE + 402)


V4L2_CID_MPEG_VIDEO_MPEG4_MIN_QP = (V4L2_CID_CODEC_BASE + 403)


V4L2_CID_MPEG_VIDEO_MPEG4_MAX_QP = (V4L2_CID_CODEC_BASE + 404)


V4L2_CID_MPEG_VIDEO_MPEG4_LEVEL = (V4L2_CID_CODEC_BASE + 405)


V4L2_CID_MPEG_VIDEO_MPEG4_PROFILE = (V4L2_CID_CODEC_BASE + 406)


V4L2_CID_MPEG_VIDEO_MPEG4_QPEL = (V4L2_CID_CODEC_BASE + 407)


V4L2_CID_MPEG_VIDEO_VPX_NUM_PARTITIONS = (V4L2_CID_CODEC_BASE + 500)


V4L2_CID_MPEG_VIDEO_VPX_IMD_DISABLE_4X4 = (V4L2_CID_CODEC_BASE + 501)


V4L2_CID_MPEG_VIDEO_VPX_NUM_REF_FRAMES = (V4L2_CID_CODEC_BASE + 502)


V4L2_CID_MPEG_VIDEO_VPX_FILTER_LEVEL = (V4L2_CID_CODEC_BASE + 503)


V4L2_CID_MPEG_VIDEO_VPX_FILTER_SHARPNESS = (V4L2_CID_CODEC_BASE + 504)


V4L2_CID_MPEG_VIDEO_VPX_GOLDEN_FRAME_REF_PERIOD = (V4L2_CID_CODEC_BASE + 505)


V4L2_CID_MPEG_VIDEO_VPX_GOLDEN_FRAME_SEL = (V4L2_CID_CODEC_BASE + 506)


V4L2_CID_MPEG_VIDEO_VPX_MIN_QP = (V4L2_CID_CODEC_BASE + 507)


V4L2_CID_MPEG_VIDEO_VPX_MAX_QP = (V4L2_CID_CODEC_BASE + 508)


V4L2_CID_MPEG_VIDEO_VPX_I_FRAME_QP = (V4L2_CID_CODEC_BASE + 509)


V4L2_CID_MPEG_VIDEO_VPX_P_FRAME_QP = (V4L2_CID_CODEC_BASE + 510)


V4L2_CID_MPEG_VIDEO_VP8_PROFILE = (V4L2_CID_CODEC_BASE + 511)


V4L2_CID_MPEG_VIDEO_VPX_PROFILE = V4L2_CID_MPEG_VIDEO_VP8_PROFILE


V4L2_CID_MPEG_VIDEO_VP9_PROFILE = (V4L2_CID_CODEC_BASE + 512)


V4L2_CID_MPEG_VIDEO_VP9_LEVEL = (V4L2_CID_CODEC_BASE + 513)


V4L2_CID_MPEG_VIDEO_HEVC_MIN_QP = (V4L2_CID_CODEC_BASE + 600)


V4L2_CID_MPEG_VIDEO_HEVC_MAX_QP = (V4L2_CID_CODEC_BASE + 601)


V4L2_CID_MPEG_VIDEO_HEVC_I_FRAME_QP = (V4L2_CID_CODEC_BASE + 602)


V4L2_CID_MPEG_VIDEO_HEVC_P_FRAME_QP = (V4L2_CID_CODEC_BASE + 603)


V4L2_CID_MPEG_VIDEO_HEVC_B_FRAME_QP = (V4L2_CID_CODEC_BASE + 604)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_QP = (V4L2_CID_CODEC_BASE + 605)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_TYPE = (V4L2_CID_CODEC_BASE + 606)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_LAYER = (V4L2_CID_CODEC_BASE + 607)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L0_QP = (V4L2_CID_CODEC_BASE + 608)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L1_QP = (V4L2_CID_CODEC_BASE + 609)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L2_QP = (V4L2_CID_CODEC_BASE + 610)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L3_QP = (V4L2_CID_CODEC_BASE + 611)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L4_QP = (V4L2_CID_CODEC_BASE + 612)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L5_QP = (V4L2_CID_CODEC_BASE + 613)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L6_QP = (V4L2_CID_CODEC_BASE + 614)


V4L2_CID_MPEG_VIDEO_HEVC_PROFILE = (V4L2_CID_CODEC_BASE + 615)


V4L2_CID_MPEG_VIDEO_HEVC_LEVEL = (V4L2_CID_CODEC_BASE + 616)


V4L2_CID_MPEG_VIDEO_HEVC_FRAME_RATE_RESOLUTION = (V4L2_CID_CODEC_BASE + 617)


V4L2_CID_MPEG_VIDEO_HEVC_TIER = (V4L2_CID_CODEC_BASE + 618)


V4L2_CID_MPEG_VIDEO_HEVC_MAX_PARTITION_DEPTH = (V4L2_CID_CODEC_BASE + 619)


V4L2_CID_MPEG_VIDEO_HEVC_LOOP_FILTER_MODE = (V4L2_CID_CODEC_BASE + 620)


V4L2_CID_MPEG_VIDEO_HEVC_LF_BETA_OFFSET_DIV2 = (V4L2_CID_CODEC_BASE + 621)


V4L2_CID_MPEG_VIDEO_HEVC_LF_TC_OFFSET_DIV2 = (V4L2_CID_CODEC_BASE + 622)


V4L2_CID_MPEG_VIDEO_HEVC_REFRESH_TYPE = (V4L2_CID_CODEC_BASE + 623)


V4L2_CID_MPEG_VIDEO_HEVC_REFRESH_PERIOD = (V4L2_CID_CODEC_BASE + 624)


V4L2_CID_MPEG_VIDEO_HEVC_LOSSLESS_CU = (V4L2_CID_CODEC_BASE + 625)


V4L2_CID_MPEG_VIDEO_HEVC_CONST_INTRA_PRED = (V4L2_CID_CODEC_BASE + 626)


V4L2_CID_MPEG_VIDEO_HEVC_WAVEFRONT = (V4L2_CID_CODEC_BASE + 627)


V4L2_CID_MPEG_VIDEO_HEVC_GENERAL_PB = (V4L2_CID_CODEC_BASE + 628)


V4L2_CID_MPEG_VIDEO_HEVC_TEMPORAL_ID = (V4L2_CID_CODEC_BASE + 629)


V4L2_CID_MPEG_VIDEO_HEVC_STRONG_SMOOTHING = (V4L2_CID_CODEC_BASE + 630)


V4L2_CID_MPEG_VIDEO_HEVC_MAX_NUM_MERGE_MV_MINUS1 = (V4L2_CID_CODEC_BASE + 631)


V4L2_CID_MPEG_VIDEO_HEVC_INTRA_PU_SPLIT = (V4L2_CID_CODEC_BASE + 632)


V4L2_CID_MPEG_VIDEO_HEVC_TMV_PREDICTION = (V4L2_CID_CODEC_BASE + 633)


V4L2_CID_MPEG_VIDEO_HEVC_WITHOUT_STARTCODE = (V4L2_CID_CODEC_BASE + 634)


V4L2_CID_MPEG_VIDEO_HEVC_SIZE_OF_LENGTH_FIELD = (V4L2_CID_CODEC_BASE + 635)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L0_BR = (V4L2_CID_CODEC_BASE + 636)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L1_BR = (V4L2_CID_CODEC_BASE + 637)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L2_BR = (V4L2_CID_CODEC_BASE + 638)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L3_BR = (V4L2_CID_CODEC_BASE + 639)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L4_BR = (V4L2_CID_CODEC_BASE + 640)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L5_BR = (V4L2_CID_CODEC_BASE + 641)


V4L2_CID_MPEG_VIDEO_HEVC_HIER_CODING_L6_BR = (V4L2_CID_CODEC_BASE + 642)


V4L2_CID_MPEG_VIDEO_REF_NUMBER_FOR_PFRAMES = (V4L2_CID_CODEC_BASE + 643)


V4L2_CID_MPEG_VIDEO_PREPEND_SPSPPS_TO_IDR = (V4L2_CID_CODEC_BASE + 644)


V4L2_CID_MPEG_VIDEO_CONSTANT_QUALITY = (V4L2_CID_CODEC_BASE + 645)


V4L2_CID_MPEG_VIDEO_FRAME_SKIP_MODE = (V4L2_CID_CODEC_BASE + 646)


V4L2_CID_MPEG_VIDEO_HEVC_I_FRAME_MIN_QP = (V4L2_CID_CODEC_BASE + 647)


V4L2_CID_MPEG_VIDEO_HEVC_I_FRAME_MAX_QP = (V4L2_CID_CODEC_BASE + 648)


V4L2_CID_MPEG_VIDEO_HEVC_P_FRAME_MIN_QP = (V4L2_CID_CODEC_BASE + 649)


V4L2_CID_MPEG_VIDEO_HEVC_P_FRAME_MAX_QP = (V4L2_CID_CODEC_BASE + 650)


V4L2_CID_MPEG_VIDEO_HEVC_B_FRAME_MIN_QP = (V4L2_CID_CODEC_BASE + 651)


V4L2_CID_MPEG_VIDEO_HEVC_B_FRAME_MAX_QP = (V4L2_CID_CODEC_BASE + 652)


V4L2_CID_MPEG_VIDEO_DEC_DISPLAY_DELAY = (V4L2_CID_CODEC_BASE + 653)


V4L2_CID_MPEG_VIDEO_DEC_DISPLAY_DELAY_ENABLE = (V4L2_CID_CODEC_BASE + 654)


V4L2_CID_MPEG_VIDEO_AV1_PROFILE = (V4L2_CID_CODEC_BASE + 655)


V4L2_CID_MPEG_VIDEO_AV1_LEVEL = (V4L2_CID_CODEC_BASE + 656)


V4L2_CID_MPEG_VIDEO_AVERAGE_QP = (V4L2_CID_CODEC_BASE + 657)


V4L2_CID_CODEC_CX2341X_BASE = (V4L2_CTRL_CLASS_CODEC | 0x1000)


V4L2_CID_MPEG_CX2341X_VIDEO_SPATIAL_FILTER_MODE = (V4L2_CID_CODEC_CX2341X_BASE + 0)


V4L2_CID_MPEG_CX2341X_VIDEO_SPATIAL_FILTER = (V4L2_CID_CODEC_CX2341X_BASE + 1)


V4L2_CID_MPEG_CX2341X_VIDEO_LUMA_SPATIAL_FILTER_TYPE = (V4L2_CID_CODEC_CX2341X_BASE + 2)


V4L2_CID_MPEG_CX2341X_VIDEO_CHROMA_SPATIAL_FILTER_TYPE = (V4L2_CID_CODEC_CX2341X_BASE + 3)


V4L2_CID_MPEG_CX2341X_VIDEO_TEMPORAL_FILTER_MODE = (V4L2_CID_CODEC_CX2341X_BASE + 4)


V4L2_CID_MPEG_CX2341X_VIDEO_TEMPORAL_FILTER = (V4L2_CID_CODEC_CX2341X_BASE + 5)


V4L2_CID_MPEG_CX2341X_VIDEO_MEDIAN_FILTER_TYPE = (V4L2_CID_CODEC_CX2341X_BASE + 6)


V4L2_CID_MPEG_CX2341X_VIDEO_LUMA_MEDIAN_FILTER_BOTTOM = (V4L2_CID_CODEC_CX2341X_BASE + 7)


V4L2_CID_MPEG_CX2341X_VIDEO_LUMA_MEDIAN_FILTER_TOP = (V4L2_CID_CODEC_CX2341X_BASE + 8)


V4L2_CID_MPEG_CX2341X_VIDEO_CHROMA_MEDIAN_FILTER_BOTTOM = (V4L2_CID_CODEC_CX2341X_BASE + 9)


V4L2_CID_MPEG_CX2341X_VIDEO_CHROMA_MEDIAN_FILTER_TOP = (V4L2_CID_CODEC_CX2341X_BASE + 10)


V4L2_CID_MPEG_CX2341X_STREAM_INSERT_NAV_PACKETS = (V4L2_CID_CODEC_CX2341X_BASE + 11)


V4L2_CID_CODEC_MFC51_BASE = (V4L2_CTRL_CLASS_CODEC | 0x1100)


V4L2_CID_MPEG_MFC51_VIDEO_DECODER_H264_DISPLAY_DELAY = (V4L2_CID_CODEC_MFC51_BASE + 0)


V4L2_CID_MPEG_MFC51_VIDEO_DECODER_H264_DISPLAY_DELAY_ENABLE = (V4L2_CID_CODEC_MFC51_BASE + 1)


V4L2_CID_MPEG_MFC51_VIDEO_FRAME_SKIP_MODE = (V4L2_CID_CODEC_MFC51_BASE + 2)


V4L2_CID_MPEG_MFC51_VIDEO_FORCE_FRAME_TYPE = (V4L2_CID_CODEC_MFC51_BASE + 3)


V4L2_CID_MPEG_MFC51_VIDEO_PADDING = (V4L2_CID_CODEC_MFC51_BASE + 4)


V4L2_CID_MPEG_MFC51_VIDEO_PADDING_YUV = (V4L2_CID_CODEC_MFC51_BASE + 5)


V4L2_CID_MPEG_MFC51_VIDEO_RC_FIXED_TARGET_BIT = (V4L2_CID_CODEC_MFC51_BASE + 6)


V4L2_CID_MPEG_MFC51_VIDEO_RC_REACTION_COEFF = (V4L2_CID_CODEC_MFC51_BASE + 7)


V4L2_CID_MPEG_MFC51_VIDEO_H264_ADAPTIVE_RC_ACTIVITY = (V4L2_CID_CODEC_MFC51_BASE + 50)


V4L2_CID_MPEG_MFC51_VIDEO_H264_ADAPTIVE_RC_DARK = (V4L2_CID_CODEC_MFC51_BASE + 51)


V4L2_CID_MPEG_MFC51_VIDEO_H264_ADAPTIVE_RC_SMOOTH = (V4L2_CID_CODEC_MFC51_BASE + 52)


V4L2_CID_MPEG_MFC51_VIDEO_H264_ADAPTIVE_RC_STATIC = (V4L2_CID_CODEC_MFC51_BASE + 53)


V4L2_CID_MPEG_MFC51_VIDEO_H264_NUM_REF_PIC_FOR_P = (V4L2_CID_CODEC_MFC51_BASE + 54)


V4L2_CID_CAMERA_CLASS_BASE = (V4L2_CTRL_CLASS_CAMERA | 0x900)


V4L2_CID_CAMERA_CLASS = (V4L2_CTRL_CLASS_CAMERA | 1)


V4L2_CID_EXPOSURE_AUTO = (V4L2_CID_CAMERA_CLASS_BASE + 1)


V4L2_CID_EXPOSURE_ABSOLUTE = (V4L2_CID_CAMERA_CLASS_BASE + 2)


V4L2_CID_EXPOSURE_AUTO_PRIORITY = (V4L2_CID_CAMERA_CLASS_BASE + 3)


V4L2_CID_PAN_RELATIVE = (V4L2_CID_CAMERA_CLASS_BASE + 4)


V4L2_CID_TILT_RELATIVE = (V4L2_CID_CAMERA_CLASS_BASE + 5)


V4L2_CID_PAN_RESET = (V4L2_CID_CAMERA_CLASS_BASE + 6)


V4L2_CID_TILT_RESET = (V4L2_CID_CAMERA_CLASS_BASE + 7)


V4L2_CID_PAN_ABSOLUTE = (V4L2_CID_CAMERA_CLASS_BASE + 8)


V4L2_CID_TILT_ABSOLUTE = (V4L2_CID_CAMERA_CLASS_BASE + 9)


V4L2_CID_FOCUS_ABSOLUTE = (V4L2_CID_CAMERA_CLASS_BASE + 10)


V4L2_CID_FOCUS_RELATIVE = (V4L2_CID_CAMERA_CLASS_BASE + 11)


V4L2_CID_FOCUS_AUTO = (V4L2_CID_CAMERA_CLASS_BASE + 12)


V4L2_CID_ZOOM_ABSOLUTE = (V4L2_CID_CAMERA_CLASS_BASE + 13)


V4L2_CID_ZOOM_RELATIVE = (V4L2_CID_CAMERA_CLASS_BASE + 14)


V4L2_CID_ZOOM_CONTINUOUS = (V4L2_CID_CAMERA_CLASS_BASE + 15)


V4L2_CID_PRIVACY = (V4L2_CID_CAMERA_CLASS_BASE + 16)


V4L2_CID_IRIS_ABSOLUTE = (V4L2_CID_CAMERA_CLASS_BASE + 17)


V4L2_CID_IRIS_RELATIVE = (V4L2_CID_CAMERA_CLASS_BASE + 18)


V4L2_CID_AUTO_EXPOSURE_BIAS = (V4L2_CID_CAMERA_CLASS_BASE + 19)


V4L2_CID_AUTO_N_PRESET_WHITE_BALANCE = (V4L2_CID_CAMERA_CLASS_BASE + 20)


V4L2_CID_WIDE_DYNAMIC_RANGE = (V4L2_CID_CAMERA_CLASS_BASE + 21)


V4L2_CID_IMAGE_STABILIZATION = (V4L2_CID_CAMERA_CLASS_BASE + 22)


V4L2_CID_ISO_SENSITIVITY = (V4L2_CID_CAMERA_CLASS_BASE + 23)


V4L2_CID_ISO_SENSITIVITY_AUTO = (V4L2_CID_CAMERA_CLASS_BASE + 24)


V4L2_CID_EXPOSURE_METERING = (V4L2_CID_CAMERA_CLASS_BASE + 25)


V4L2_CID_SCENE_MODE = (V4L2_CID_CAMERA_CLASS_BASE + 26)


V4L2_CID_3A_LOCK = (V4L2_CID_CAMERA_CLASS_BASE + 27)


V4L2_LOCK_EXPOSURE = (1 << 0)


V4L2_LOCK_WHITE_BALANCE = (1 << 1)


V4L2_LOCK_FOCUS = (1 << 2)


V4L2_CID_AUTO_FOCUS_START = (V4L2_CID_CAMERA_CLASS_BASE + 28)


V4L2_CID_AUTO_FOCUS_STOP = (V4L2_CID_CAMERA_CLASS_BASE + 29)


V4L2_CID_AUTO_FOCUS_STATUS = (V4L2_CID_CAMERA_CLASS_BASE + 30)


V4L2_AUTO_FOCUS_STATUS_IDLE = (0 << 0)


V4L2_AUTO_FOCUS_STATUS_BUSY = (1 << 0)


V4L2_AUTO_FOCUS_STATUS_REACHED = (1 << 1)


V4L2_AUTO_FOCUS_STATUS_FAILED = (1 << 2)


V4L2_CID_AUTO_FOCUS_RANGE = (V4L2_CID_CAMERA_CLASS_BASE + 31)


V4L2_CID_PAN_SPEED = (V4L2_CID_CAMERA_CLASS_BASE + 32)


V4L2_CID_TILT_SPEED = (V4L2_CID_CAMERA_CLASS_BASE + 33)


V4L2_CID_CAMERA_ORIENTATION = (V4L2_CID_CAMERA_CLASS_BASE + 34)


V4L2_CAMERA_ORIENTATION_FRONT = 0


V4L2_CAMERA_ORIENTATION_BACK = 1


V4L2_CAMERA_ORIENTATION_EXTERNAL = 2


V4L2_CID_CAMERA_SENSOR_ROTATION = (V4L2_CID_CAMERA_CLASS_BASE + 35)


V4L2_CID_HDR_SENSOR_MODE = (V4L2_CID_CAMERA_CLASS_BASE + 36)


V4L2_CID_FM_TX_CLASS_BASE = (V4L2_CTRL_CLASS_FM_TX | 0x900)


V4L2_CID_FM_TX_CLASS = (V4L2_CTRL_CLASS_FM_TX | 1)


V4L2_CID_RDS_TX_DEVIATION = (V4L2_CID_FM_TX_CLASS_BASE + 1)


V4L2_CID_RDS_TX_PI = (V4L2_CID_FM_TX_CLASS_BASE + 2)


V4L2_CID_RDS_TX_PTY = (V4L2_CID_FM_TX_CLASS_BASE + 3)


V4L2_CID_RDS_TX_PS_NAME = (V4L2_CID_FM_TX_CLASS_BASE + 5)


V4L2_CID_RDS_TX_RADIO_TEXT = (V4L2_CID_FM_TX_CLASS_BASE + 6)


V4L2_CID_RDS_TX_MONO_STEREO = (V4L2_CID_FM_TX_CLASS_BASE + 7)


V4L2_CID_RDS_TX_ARTIFICIAL_HEAD = (V4L2_CID_FM_TX_CLASS_BASE + 8)


V4L2_CID_RDS_TX_COMPRESSED = (V4L2_CID_FM_TX_CLASS_BASE + 9)


V4L2_CID_RDS_TX_DYNAMIC_PTY = (V4L2_CID_FM_TX_CLASS_BASE + 10)


V4L2_CID_RDS_TX_TRAFFIC_ANNOUNCEMENT = (V4L2_CID_FM_TX_CLASS_BASE + 11)


V4L2_CID_RDS_TX_TRAFFIC_PROGRAM = (V4L2_CID_FM_TX_CLASS_BASE + 12)


V4L2_CID_RDS_TX_MUSIC_SPEECH = (V4L2_CID_FM_TX_CLASS_BASE + 13)


V4L2_CID_RDS_TX_ALT_FREQS_ENABLE = (V4L2_CID_FM_TX_CLASS_BASE + 14)


V4L2_CID_RDS_TX_ALT_FREQS = (V4L2_CID_FM_TX_CLASS_BASE + 15)


V4L2_CID_AUDIO_LIMITER_ENABLED = (V4L2_CID_FM_TX_CLASS_BASE + 64)


V4L2_CID_AUDIO_LIMITER_RELEASE_TIME = (V4L2_CID_FM_TX_CLASS_BASE + 65)


V4L2_CID_AUDIO_LIMITER_DEVIATION = (V4L2_CID_FM_TX_CLASS_BASE + 66)


V4L2_CID_AUDIO_COMPRESSION_ENABLED = (V4L2_CID_FM_TX_CLASS_BASE + 80)


V4L2_CID_AUDIO_COMPRESSION_GAIN = (V4L2_CID_FM_TX_CLASS_BASE + 81)


V4L2_CID_AUDIO_COMPRESSION_THRESHOLD = (V4L2_CID_FM_TX_CLASS_BASE + 82)


V4L2_CID_AUDIO_COMPRESSION_ATTACK_TIME = (V4L2_CID_FM_TX_CLASS_BASE + 83)


V4L2_CID_AUDIO_COMPRESSION_RELEASE_TIME = (V4L2_CID_FM_TX_CLASS_BASE + 84)


V4L2_CID_PILOT_TONE_ENABLED = (V4L2_CID_FM_TX_CLASS_BASE + 96)


V4L2_CID_PILOT_TONE_DEVIATION = (V4L2_CID_FM_TX_CLASS_BASE + 97)


V4L2_CID_PILOT_TONE_FREQUENCY = (V4L2_CID_FM_TX_CLASS_BASE + 98)


V4L2_CID_TUNE_PREEMPHASIS = (V4L2_CID_FM_TX_CLASS_BASE + 112)


V4L2_CID_TUNE_POWER_LEVEL = (V4L2_CID_FM_TX_CLASS_BASE + 113)


V4L2_CID_TUNE_ANTENNA_CAPACITOR = (V4L2_CID_FM_TX_CLASS_BASE + 114)


V4L2_CID_FLASH_CLASS_BASE = (V4L2_CTRL_CLASS_FLASH | 0x900)


V4L2_CID_FLASH_CLASS = (V4L2_CTRL_CLASS_FLASH | 1)


V4L2_CID_FLASH_LED_MODE = (V4L2_CID_FLASH_CLASS_BASE + 1)


V4L2_CID_FLASH_STROBE_SOURCE = (V4L2_CID_FLASH_CLASS_BASE + 2)


V4L2_CID_FLASH_STROBE = (V4L2_CID_FLASH_CLASS_BASE + 3)


V4L2_CID_FLASH_STROBE_STOP = (V4L2_CID_FLASH_CLASS_BASE + 4)


V4L2_CID_FLASH_STROBE_STATUS = (V4L2_CID_FLASH_CLASS_BASE + 5)


V4L2_CID_FLASH_TIMEOUT = (V4L2_CID_FLASH_CLASS_BASE + 6)


V4L2_CID_FLASH_INTENSITY = (V4L2_CID_FLASH_CLASS_BASE + 7)


V4L2_CID_FLASH_TORCH_INTENSITY = (V4L2_CID_FLASH_CLASS_BASE + 8)


V4L2_CID_FLASH_INDICATOR_INTENSITY = (V4L2_CID_FLASH_CLASS_BASE + 9)


V4L2_CID_FLASH_FAULT = (V4L2_CID_FLASH_CLASS_BASE + 10)


V4L2_FLASH_FAULT_OVER_VOLTAGE = (1 << 0)


V4L2_FLASH_FAULT_TIMEOUT = (1 << 1)


V4L2_FLASH_FAULT_OVER_TEMPERATURE = (1 << 2)


V4L2_FLASH_FAULT_SHORT_CIRCUIT = (1 << 3)


V4L2_FLASH_FAULT_OVER_CURRENT = (1 << 4)


V4L2_FLASH_FAULT_INDICATOR = (1 << 5)


V4L2_FLASH_FAULT_UNDER_VOLTAGE = (1 << 6)


V4L2_FLASH_FAULT_INPUT_VOLTAGE = (1 << 7)


V4L2_FLASH_FAULT_LED_OVER_TEMPERATURE = (1 << 8)


V4L2_CID_FLASH_CHARGE = (V4L2_CID_FLASH_CLASS_BASE + 11)


V4L2_CID_FLASH_READY = (V4L2_CID_FLASH_CLASS_BASE + 12)


V4L2_CID_JPEG_CLASS_BASE = (V4L2_CTRL_CLASS_JPEG | 0x900)


V4L2_CID_JPEG_CLASS = (V4L2_CTRL_CLASS_JPEG | 1)


V4L2_CID_JPEG_CHROMA_SUBSAMPLING = (V4L2_CID_JPEG_CLASS_BASE + 1)


V4L2_CID_JPEG_RESTART_INTERVAL = (V4L2_CID_JPEG_CLASS_BASE + 2)


V4L2_CID_JPEG_COMPRESSION_QUALITY = (V4L2_CID_JPEG_CLASS_BASE + 3)


V4L2_CID_JPEG_ACTIVE_MARKER = (V4L2_CID_JPEG_CLASS_BASE + 4)


V4L2_JPEG_ACTIVE_MARKER_APP0 = (1 << 0)


V4L2_JPEG_ACTIVE_MARKER_APP1 = (1 << 1)


V4L2_JPEG_ACTIVE_MARKER_COM = (1 << 16)


V4L2_JPEG_ACTIVE_MARKER_DQT = (1 << 17)


V4L2_JPEG_ACTIVE_MARKER_DHT = (1 << 18)


V4L2_CID_IMAGE_SOURCE_CLASS_BASE = (V4L2_CTRL_CLASS_IMAGE_SOURCE | 0x900)


V4L2_CID_IMAGE_SOURCE_CLASS = (V4L2_CTRL_CLASS_IMAGE_SOURCE | 1)


V4L2_CID_VBLANK = (V4L2_CID_IMAGE_SOURCE_CLASS_BASE + 1)


V4L2_CID_HBLANK = (V4L2_CID_IMAGE_SOURCE_CLASS_BASE + 2)


V4L2_CID_ANALOGUE_GAIN = (V4L2_CID_IMAGE_SOURCE_CLASS_BASE + 3)


V4L2_CID_TEST_PATTERN_RED = (V4L2_CID_IMAGE_SOURCE_CLASS_BASE + 4)


V4L2_CID_TEST_PATTERN_GREENR = (V4L2_CID_IMAGE_SOURCE_CLASS_BASE + 5)


V4L2_CID_TEST_PATTERN_BLUE = (V4L2_CID_IMAGE_SOURCE_CLASS_BASE + 6)


V4L2_CID_TEST_PATTERN_GREENB = (V4L2_CID_IMAGE_SOURCE_CLASS_BASE + 7)


V4L2_CID_UNIT_CELL_SIZE = (V4L2_CID_IMAGE_SOURCE_CLASS_BASE + 8)


V4L2_CID_NOTIFY_GAINS = (V4L2_CID_IMAGE_SOURCE_CLASS_BASE + 9)


V4L2_CID_IMAGE_PROC_CLASS_BASE = (V4L2_CTRL_CLASS_IMAGE_PROC | 0x900)


V4L2_CID_IMAGE_PROC_CLASS = (V4L2_CTRL_CLASS_IMAGE_PROC | 1)


V4L2_CID_LINK_FREQ = (V4L2_CID_IMAGE_PROC_CLASS_BASE + 1)


V4L2_CID_PIXEL_RATE = (V4L2_CID_IMAGE_PROC_CLASS_BASE + 2)


V4L2_CID_TEST_PATTERN = (V4L2_CID_IMAGE_PROC_CLASS_BASE + 3)


V4L2_CID_DEINTERLACING_MODE = (V4L2_CID_IMAGE_PROC_CLASS_BASE + 4)


V4L2_CID_DIGITAL_GAIN = (V4L2_CID_IMAGE_PROC_CLASS_BASE + 5)


V4L2_CID_DV_CLASS_BASE = (V4L2_CTRL_CLASS_DV | 0x900)


V4L2_CID_DV_CLASS = (V4L2_CTRL_CLASS_DV | 1)


V4L2_CID_DV_TX_HOTPLUG = (V4L2_CID_DV_CLASS_BASE + 1)


V4L2_CID_DV_TX_RXSENSE = (V4L2_CID_DV_CLASS_BASE + 2)


V4L2_CID_DV_TX_EDID_PRESENT = (V4L2_CID_DV_CLASS_BASE + 3)


V4L2_CID_DV_TX_MODE = (V4L2_CID_DV_CLASS_BASE + 4)


V4L2_CID_DV_TX_RGB_RANGE = (V4L2_CID_DV_CLASS_BASE + 5)


V4L2_CID_DV_TX_IT_CONTENT_TYPE = (V4L2_CID_DV_CLASS_BASE + 6)


V4L2_CID_DV_RX_POWER_PRESENT = (V4L2_CID_DV_CLASS_BASE + 100)


V4L2_CID_DV_RX_RGB_RANGE = (V4L2_CID_DV_CLASS_BASE + 101)


V4L2_CID_DV_RX_IT_CONTENT_TYPE = (V4L2_CID_DV_CLASS_BASE + 102)


V4L2_CID_FM_RX_CLASS_BASE = (V4L2_CTRL_CLASS_FM_RX | 0x900)


V4L2_CID_FM_RX_CLASS = (V4L2_CTRL_CLASS_FM_RX | 1)


V4L2_CID_TUNE_DEEMPHASIS = (V4L2_CID_FM_RX_CLASS_BASE + 1)


V4L2_CID_RDS_RECEPTION = (V4L2_CID_FM_RX_CLASS_BASE + 2)


V4L2_CID_RDS_RX_PTY = (V4L2_CID_FM_RX_CLASS_BASE + 3)


V4L2_CID_RDS_RX_PS_NAME = (V4L2_CID_FM_RX_CLASS_BASE + 4)


V4L2_CID_RDS_RX_RADIO_TEXT = (V4L2_CID_FM_RX_CLASS_BASE + 5)


V4L2_CID_RDS_RX_TRAFFIC_ANNOUNCEMENT = (V4L2_CID_FM_RX_CLASS_BASE + 6)


V4L2_CID_RDS_RX_TRAFFIC_PROGRAM = (V4L2_CID_FM_RX_CLASS_BASE + 7)


V4L2_CID_RDS_RX_MUSIC_SPEECH = (V4L2_CID_FM_RX_CLASS_BASE + 8)


V4L2_CID_RF_TUNER_CLASS_BASE = (V4L2_CTRL_CLASS_RF_TUNER | 0x900)


V4L2_CID_RF_TUNER_CLASS = (V4L2_CTRL_CLASS_RF_TUNER | 1)


V4L2_CID_RF_TUNER_BANDWIDTH_AUTO = (V4L2_CID_RF_TUNER_CLASS_BASE + 11)


V4L2_CID_RF_TUNER_BANDWIDTH = (V4L2_CID_RF_TUNER_CLASS_BASE + 12)


V4L2_CID_RF_TUNER_RF_GAIN = (V4L2_CID_RF_TUNER_CLASS_BASE + 32)


V4L2_CID_RF_TUNER_LNA_GAIN_AUTO = (V4L2_CID_RF_TUNER_CLASS_BASE + 41)


V4L2_CID_RF_TUNER_LNA_GAIN = (V4L2_CID_RF_TUNER_CLASS_BASE + 42)


V4L2_CID_RF_TUNER_MIXER_GAIN_AUTO = (V4L2_CID_RF_TUNER_CLASS_BASE + 51)


V4L2_CID_RF_TUNER_MIXER_GAIN = (V4L2_CID_RF_TUNER_CLASS_BASE + 52)


V4L2_CID_RF_TUNER_IF_GAIN_AUTO = (V4L2_CID_RF_TUNER_CLASS_BASE + 61)


V4L2_CID_RF_TUNER_IF_GAIN = (V4L2_CID_RF_TUNER_CLASS_BASE + 62)


V4L2_CID_RF_TUNER_PLL_LOCK = (V4L2_CID_RF_TUNER_CLASS_BASE + 91)


V4L2_CID_DETECT_CLASS_BASE = (V4L2_CTRL_CLASS_DETECT | 0x900)


V4L2_CID_DETECT_CLASS = (V4L2_CTRL_CLASS_DETECT | 1)


V4L2_CID_DETECT_MD_MODE = (V4L2_CID_DETECT_CLASS_BASE + 1)


V4L2_CID_DETECT_MD_GLOBAL_THRESHOLD = (V4L2_CID_DETECT_CLASS_BASE + 2)


V4L2_CID_DETECT_MD_THRESHOLD_GRID = (V4L2_CID_DETECT_CLASS_BASE + 3)


V4L2_CID_DETECT_MD_REGION_GRID = (V4L2_CID_DETECT_CLASS_BASE + 4)


V4L2_CID_CODEC_STATELESS_BASE = (V4L2_CTRL_CLASS_CODEC_STATELESS | 0x900)


V4L2_CID_CODEC_STATELESS_CLASS = (V4L2_CTRL_CLASS_CODEC_STATELESS | 1)


V4L2_CID_STATELESS_H264_DECODE_MODE = (V4L2_CID_CODEC_STATELESS_BASE + 0)


V4L2_CID_STATELESS_H264_START_CODE = (V4L2_CID_CODEC_STATELESS_BASE + 1)


V4L2_H264_SPS_CONSTRAINT_SET0_FLAG = 0x01


V4L2_H264_SPS_CONSTRAINT_SET1_FLAG = 0x02


V4L2_H264_SPS_CONSTRAINT_SET2_FLAG = 0x04


V4L2_H264_SPS_CONSTRAINT_SET3_FLAG = 0x08


V4L2_H264_SPS_CONSTRAINT_SET4_FLAG = 0x10


V4L2_H264_SPS_CONSTRAINT_SET5_FLAG = 0x20


V4L2_H264_SPS_FLAG_SEPARATE_COLOUR_PLANE = 0x01


V4L2_H264_SPS_FLAG_QPPRIME_Y_ZERO_TRANSFORM_BYPASS = 0x02


V4L2_H264_SPS_FLAG_DELTA_PIC_ORDER_ALWAYS_ZERO = 0x04


V4L2_H264_SPS_FLAG_GAPS_IN_FRAME_NUM_VALUE_ALLOWED = 0x08


V4L2_H264_SPS_FLAG_FRAME_MBS_ONLY = 0x10


V4L2_H264_SPS_FLAG_MB_ADAPTIVE_FRAME_FIELD = 0x20


V4L2_H264_SPS_FLAG_DIRECT_8X8_INFERENCE = 0x40


def V4L2_H264_SPS_HAS_CHROMA_FORMAT(sps):
    return (((((((((((((((sps.contents.profile_idc).value) == 100) or (((sps.contents.profile_idc).value) == 110)) or (((sps.contents.profile_idc).value) == 122)) or (((sps.contents.profile_idc).value) == 244)) or (((sps.contents.profile_idc).value) == 44)) or (((sps.contents.profile_idc).value) == 83)) or (((sps.contents.profile_idc).value) == 86)) or (((sps.contents.profile_idc).value) == 118)) or (((sps.contents.profile_idc).value) == 128)) or (((sps.contents.profile_idc).value) == 138)) or (((sps.contents.profile_idc).value) == 139)) or (((sps.contents.profile_idc).value) == 134)) or (((sps.contents.profile_idc).value) == 135))


V4L2_CID_STATELESS_H264_SPS = (V4L2_CID_CODEC_STATELESS_BASE + 2)


V4L2_H264_PPS_FLAG_ENTROPY_CODING_MODE = 0x0001


V4L2_H264_PPS_FLAG_BOTTOM_FIELD_PIC_ORDER_IN_FRAME_PRESENT = 0x0002


V4L2_H264_PPS_FLAG_WEIGHTED_PRED = 0x0004


V4L2_H264_PPS_FLAG_DEBLOCKING_FILTER_CONTROL_PRESENT = 0x0008


V4L2_H264_PPS_FLAG_CONSTRAINED_INTRA_PRED = 0x0010


V4L2_H264_PPS_FLAG_REDUNDANT_PIC_CNT_PRESENT = 0x0020


V4L2_H264_PPS_FLAG_TRANSFORM_8X8_MODE = 0x0040


V4L2_H264_PPS_FLAG_SCALING_MATRIX_PRESENT = 0x0080


V4L2_CID_STATELESS_H264_PPS = (V4L2_CID_CODEC_STATELESS_BASE + 3)


V4L2_CID_STATELESS_H264_SCALING_MATRIX = (V4L2_CID_CODEC_STATELESS_BASE + 4)


def V4L2_H264_CTRL_PRED_WEIGHTS_REQUIRED(pps, slice):
    return (((((pps.contents.flags).value) & V4L2_H264_PPS_FLAG_WEIGHTED_PRED) and ((((slice.contents.slice_type).value) == V4L2_H264_SLICE_TYPE_P) or (((slice.contents.slice_type).value) == V4L2_H264_SLICE_TYPE_SP))) or ((((pps.contents.weighted_bipred_idc).value) == 1) and (((slice.contents.slice_type).value) == V4L2_H264_SLICE_TYPE_B)))


V4L2_CID_STATELESS_H264_PRED_WEIGHTS = (V4L2_CID_CODEC_STATELESS_BASE + 5)


V4L2_H264_SLICE_TYPE_P = 0


V4L2_H264_SLICE_TYPE_B = 1


V4L2_H264_SLICE_TYPE_I = 2


V4L2_H264_SLICE_TYPE_SP = 3


V4L2_H264_SLICE_TYPE_SI = 4


V4L2_H264_SLICE_FLAG_DIRECT_SPATIAL_MV_PRED = 0x01


V4L2_H264_SLICE_FLAG_SP_FOR_SWITCH = 0x02


V4L2_H264_TOP_FIELD_REF = 0x1


V4L2_H264_BOTTOM_FIELD_REF = 0x2


V4L2_H264_FRAME_REF = 0x3


V4L2_H264_NUM_DPB_ENTRIES = 16


V4L2_H264_REF_LIST_LEN = (2 * V4L2_H264_NUM_DPB_ENTRIES)


V4L2_CID_STATELESS_H264_SLICE_PARAMS = (V4L2_CID_CODEC_STATELESS_BASE + 6)


V4L2_H264_DPB_ENTRY_FLAG_VALID = 0x01


V4L2_H264_DPB_ENTRY_FLAG_ACTIVE = 0x02


V4L2_H264_DPB_ENTRY_FLAG_LONG_TERM = 0x04


V4L2_H264_DPB_ENTRY_FLAG_FIELD = 0x08


V4L2_H264_DECODE_PARAM_FLAG_IDR_PIC = 0x01


V4L2_H264_DECODE_PARAM_FLAG_FIELD_PIC = 0x02


V4L2_H264_DECODE_PARAM_FLAG_BOTTOM_FIELD = 0x04


V4L2_H264_DECODE_PARAM_FLAG_PFRAME = 0x08


V4L2_H264_DECODE_PARAM_FLAG_BFRAME = 0x10


V4L2_CID_STATELESS_H264_DECODE_PARAMS = (V4L2_CID_CODEC_STATELESS_BASE + 7)


V4L2_FWHT_VERSION = 3


V4L2_FWHT_FL_COMPONENTS_NUM_OFFSET = 16


V4L2_FWHT_FL_PIXENC_OFFSET = 19


V4L2_FWHT_FL_PIXENC_YUV = (1 << V4L2_FWHT_FL_PIXENC_OFFSET)


V4L2_FWHT_FL_PIXENC_RGB = (2 << V4L2_FWHT_FL_PIXENC_OFFSET)


V4L2_FWHT_FL_PIXENC_HSV = (3 << V4L2_FWHT_FL_PIXENC_OFFSET)


V4L2_CID_STATELESS_FWHT_PARAMS = (V4L2_CID_CODEC_STATELESS_BASE + 100)


V4L2_VP8_SEGMENT_FLAG_ENABLED = 0x01


V4L2_VP8_SEGMENT_FLAG_UPDATE_MAP = 0x02


V4L2_VP8_SEGMENT_FLAG_UPDATE_FEATURE_DATA = 0x04


V4L2_VP8_SEGMENT_FLAG_DELTA_VALUE_MODE = 0x08


V4L2_VP8_LF_ADJ_ENABLE = 0x01


V4L2_VP8_LF_DELTA_UPDATE = 0x02


V4L2_VP8_LF_FILTER_TYPE_SIMPLE = 0x04


V4L2_VP8_COEFF_PROB_CNT = 11


V4L2_VP8_MV_PROB_CNT = 19


V4L2_VP8_FRAME_FLAG_KEY_FRAME = 0x01


V4L2_VP8_FRAME_FLAG_EXPERIMENTAL = 0x02


V4L2_VP8_FRAME_FLAG_SHOW_FRAME = 0x04


V4L2_VP8_FRAME_FLAG_MB_NO_SKIP_COEFF = 0x08


V4L2_VP8_FRAME_FLAG_SIGN_BIAS_GOLDEN = 0x10


V4L2_VP8_FRAME_FLAG_SIGN_BIAS_ALT = 0x20


def V4L2_VP8_FRAME_IS_KEY_FRAME(hdr):
    return (not (not (((hdr.contents.flags).value) & V4L2_VP8_FRAME_FLAG_KEY_FRAME)))


V4L2_CID_STATELESS_VP8_FRAME = (V4L2_CID_CODEC_STATELESS_BASE + 200)


V4L2_MPEG2_SEQ_FLAG_PROGRESSIVE = 0x01


V4L2_CID_STATELESS_MPEG2_SEQUENCE = (V4L2_CID_CODEC_STATELESS_BASE + 220)


V4L2_MPEG2_PIC_CODING_TYPE_I = 1


V4L2_MPEG2_PIC_CODING_TYPE_P = 2


V4L2_MPEG2_PIC_CODING_TYPE_B = 3


V4L2_MPEG2_PIC_CODING_TYPE_D = 4


V4L2_MPEG2_PIC_TOP_FIELD = 0x1


V4L2_MPEG2_PIC_BOTTOM_FIELD = 0x2


V4L2_MPEG2_PIC_FRAME = 0x3


V4L2_MPEG2_PIC_FLAG_TOP_FIELD_FIRST = 0x0001


V4L2_MPEG2_PIC_FLAG_FRAME_PRED_DCT = 0x0002


V4L2_MPEG2_PIC_FLAG_CONCEALMENT_MV = 0x0004


V4L2_MPEG2_PIC_FLAG_Q_SCALE_TYPE = 0x0008


V4L2_MPEG2_PIC_FLAG_INTRA_VLC = 0x0010


V4L2_MPEG2_PIC_FLAG_ALT_SCAN = 0x0020


V4L2_MPEG2_PIC_FLAG_REPEAT_FIRST = 0x0040


V4L2_MPEG2_PIC_FLAG_PROGRESSIVE = 0x0080


V4L2_CID_STATELESS_MPEG2_PICTURE = (V4L2_CID_CODEC_STATELESS_BASE + 221)


V4L2_CID_STATELESS_MPEG2_QUANTISATION = (V4L2_CID_CODEC_STATELESS_BASE + 222)


V4L2_CID_STATELESS_HEVC_SPS = (V4L2_CID_CODEC_STATELESS_BASE + 400)


V4L2_CID_STATELESS_HEVC_PPS = (V4L2_CID_CODEC_STATELESS_BASE + 401)


V4L2_CID_STATELESS_HEVC_SLICE_PARAMS = (V4L2_CID_CODEC_STATELESS_BASE + 402)


V4L2_CID_STATELESS_HEVC_SCALING_MATRIX = (V4L2_CID_CODEC_STATELESS_BASE + 403)


V4L2_CID_STATELESS_HEVC_DECODE_PARAMS = (V4L2_CID_CODEC_STATELESS_BASE + 404)


V4L2_CID_STATELESS_HEVC_DECODE_MODE = (V4L2_CID_CODEC_STATELESS_BASE + 405)


V4L2_CID_STATELESS_HEVC_START_CODE = (V4L2_CID_CODEC_STATELESS_BASE + 406)


V4L2_CID_STATELESS_HEVC_ENTRY_POINT_OFFSETS = (V4L2_CID_CODEC_STATELESS_BASE + 407)


V4L2_HEVC_SLICE_TYPE_B = 0


V4L2_HEVC_SLICE_TYPE_P = 1


V4L2_HEVC_SLICE_TYPE_I = 2


V4L2_HEVC_SPS_FLAG_SEPARATE_COLOUR_PLANE = (1 << 0)


V4L2_HEVC_SPS_FLAG_SCALING_LIST_ENABLED = (1 << 1)


V4L2_HEVC_SPS_FLAG_AMP_ENABLED = (1 << 2)


V4L2_HEVC_SPS_FLAG_SAMPLE_ADAPTIVE_OFFSET = (1 << 3)


V4L2_HEVC_SPS_FLAG_PCM_ENABLED = (1 << 4)


V4L2_HEVC_SPS_FLAG_PCM_LOOP_FILTER_DISABLED = (1 << 5)


V4L2_HEVC_SPS_FLAG_LONG_TERM_REF_PICS_PRESENT = (1 << 6)


V4L2_HEVC_SPS_FLAG_SPS_TEMPORAL_MVP_ENABLED = (1 << 7)


V4L2_HEVC_SPS_FLAG_STRONG_INTRA_SMOOTHING_ENABLED = (1 << 8)


V4L2_HEVC_PPS_FLAG_DEPENDENT_SLICE_SEGMENT_ENABLED = (1 << 0)


V4L2_HEVC_PPS_FLAG_OUTPUT_FLAG_PRESENT = (1 << 1)


V4L2_HEVC_PPS_FLAG_SIGN_DATA_HIDING_ENABLED = (1 << 2)


V4L2_HEVC_PPS_FLAG_CABAC_INIT_PRESENT = (1 << 3)


V4L2_HEVC_PPS_FLAG_CONSTRAINED_INTRA_PRED = (1 << 4)


V4L2_HEVC_PPS_FLAG_TRANSFORM_SKIP_ENABLED = (1 << 5)


V4L2_HEVC_PPS_FLAG_CU_QP_DELTA_ENABLED = (1 << 6)


V4L2_HEVC_PPS_FLAG_PPS_SLICE_CHROMA_QP_OFFSETS_PRESENT = (1 << 7)


V4L2_HEVC_PPS_FLAG_WEIGHTED_PRED = (1 << 8)


V4L2_HEVC_PPS_FLAG_WEIGHTED_BIPRED = (1 << 9)


V4L2_HEVC_PPS_FLAG_TRANSQUANT_BYPASS_ENABLED = (1 << 10)


V4L2_HEVC_PPS_FLAG_TILES_ENABLED = (1 << 11)


V4L2_HEVC_PPS_FLAG_ENTROPY_CODING_SYNC_ENABLED = (1 << 12)


V4L2_HEVC_PPS_FLAG_LOOP_FILTER_ACROSS_TILES_ENABLED = (1 << 13)


V4L2_HEVC_PPS_FLAG_PPS_LOOP_FILTER_ACROSS_SLICES_ENABLED = (1 << 14)


V4L2_HEVC_PPS_FLAG_DEBLOCKING_FILTER_OVERRIDE_ENABLED = (1 << 15)


V4L2_HEVC_PPS_FLAG_PPS_DISABLE_DEBLOCKING_FILTER = (1 << 16)


V4L2_HEVC_PPS_FLAG_LISTS_MODIFICATION_PRESENT = (1 << 17)


V4L2_HEVC_PPS_FLAG_SLICE_SEGMENT_HEADER_EXTENSION_PRESENT = (1 << 18)


V4L2_HEVC_PPS_FLAG_DEBLOCKING_FILTER_CONTROL_PRESENT = (1 << 19)


V4L2_HEVC_PPS_FLAG_UNIFORM_SPACING = (1 << 20)


V4L2_HEVC_DPB_ENTRY_LONG_TERM_REFERENCE = 0x01


V4L2_HEVC_SEI_PIC_STRUCT_FRAME = 0


V4L2_HEVC_SEI_PIC_STRUCT_TOP_FIELD = 1


V4L2_HEVC_SEI_PIC_STRUCT_BOTTOM_FIELD = 2


V4L2_HEVC_SEI_PIC_STRUCT_TOP_BOTTOM = 3


V4L2_HEVC_SEI_PIC_STRUCT_BOTTOM_TOP = 4


V4L2_HEVC_SEI_PIC_STRUCT_TOP_BOTTOM_TOP = 5


V4L2_HEVC_SEI_PIC_STRUCT_BOTTOM_TOP_BOTTOM = 6


V4L2_HEVC_SEI_PIC_STRUCT_FRAME_DOUBLING = 7


V4L2_HEVC_SEI_PIC_STRUCT_FRAME_TRIPLING = 8


V4L2_HEVC_SEI_PIC_STRUCT_TOP_PAIRED_PREVIOUS_BOTTOM = 9


V4L2_HEVC_SEI_PIC_STRUCT_BOTTOM_PAIRED_PREVIOUS_TOP = 10


V4L2_HEVC_SEI_PIC_STRUCT_TOP_PAIRED_NEXT_BOTTOM = 11


V4L2_HEVC_SEI_PIC_STRUCT_BOTTOM_PAIRED_NEXT_TOP = 12


V4L2_HEVC_DPB_ENTRIES_NUM_MAX = 16


V4L2_HEVC_SLICE_PARAMS_FLAG_SLICE_SAO_LUMA = (1 << 0)


V4L2_HEVC_SLICE_PARAMS_FLAG_SLICE_SAO_CHROMA = (1 << 1)


V4L2_HEVC_SLICE_PARAMS_FLAG_SLICE_TEMPORAL_MVP_ENABLED = (1 << 2)


V4L2_HEVC_SLICE_PARAMS_FLAG_MVD_L1_ZERO = (1 << 3)


V4L2_HEVC_SLICE_PARAMS_FLAG_CABAC_INIT = (1 << 4)


V4L2_HEVC_SLICE_PARAMS_FLAG_COLLOCATED_FROM_L0 = (1 << 5)


V4L2_HEVC_SLICE_PARAMS_FLAG_USE_INTEGER_MV = (1 << 6)


V4L2_HEVC_SLICE_PARAMS_FLAG_SLICE_DEBLOCKING_FILTER_DISABLED = (1 << 7)


V4L2_HEVC_SLICE_PARAMS_FLAG_SLICE_LOOP_FILTER_ACROSS_SLICES_ENABLED = (1 << 8)


V4L2_HEVC_SLICE_PARAMS_FLAG_DEPENDENT_SLICE_SEGMENT = (1 << 9)


V4L2_HEVC_DECODE_PARAM_FLAG_IRAP_PIC = 0x1


V4L2_HEVC_DECODE_PARAM_FLAG_IDR_PIC = 0x2


V4L2_HEVC_DECODE_PARAM_FLAG_NO_OUTPUT_OF_PRIOR = 0x4


V4L2_CID_COLORIMETRY_CLASS_BASE = (V4L2_CTRL_CLASS_COLORIMETRY | 0x900)


V4L2_CID_COLORIMETRY_CLASS = (V4L2_CTRL_CLASS_COLORIMETRY | 1)


V4L2_CID_COLORIMETRY_HDR10_CLL_INFO = (V4L2_CID_COLORIMETRY_CLASS_BASE + 0)


V4L2_CID_COLORIMETRY_HDR10_MASTERING_DISPLAY = (V4L2_CID_COLORIMETRY_CLASS_BASE + 1)


V4L2_HDR10_MASTERING_PRIMARIES_X_LOW = 5


V4L2_HDR10_MASTERING_PRIMARIES_X_HIGH = 37000


V4L2_HDR10_MASTERING_PRIMARIES_Y_LOW = 5


V4L2_HDR10_MASTERING_PRIMARIES_Y_HIGH = 42000


V4L2_HDR10_MASTERING_WHITE_POINT_X_LOW = 5


V4L2_HDR10_MASTERING_WHITE_POINT_X_HIGH = 37000


V4L2_HDR10_MASTERING_WHITE_POINT_Y_LOW = 5


V4L2_HDR10_MASTERING_WHITE_POINT_Y_HIGH = 42000


V4L2_HDR10_MASTERING_MAX_LUMA_LOW = 50000


V4L2_HDR10_MASTERING_MAX_LUMA_HIGH = 100000000


V4L2_HDR10_MASTERING_MIN_LUMA_LOW = 1


V4L2_HDR10_MASTERING_MIN_LUMA_HIGH = 50000


V4L2_VP9_LOOP_FILTER_FLAG_DELTA_ENABLED = 0x1


V4L2_VP9_LOOP_FILTER_FLAG_DELTA_UPDATE = 0x2


V4L2_VP9_SEGMENTATION_FLAG_ENABLED = 0x01


V4L2_VP9_SEGMENTATION_FLAG_UPDATE_MAP = 0x02


V4L2_VP9_SEGMENTATION_FLAG_TEMPORAL_UPDATE = 0x04


V4L2_VP9_SEGMENTATION_FLAG_UPDATE_DATA = 0x08


V4L2_VP9_SEGMENTATION_FLAG_ABS_OR_DELTA_UPDATE = 0x10


V4L2_VP9_SEG_LVL_ALT_Q = 0


V4L2_VP9_SEG_LVL_ALT_L = 1


V4L2_VP9_SEG_LVL_REF_FRAME = 2


V4L2_VP9_SEG_LVL_SKIP = 3


V4L2_VP9_SEG_LVL_MAX = 4


def V4L2_VP9_SEGMENT_FEATURE_ENABLED(id):
    return (1 << id)


V4L2_VP9_SEGMENT_FEATURE_ENABLED_MASK = 0xf


V4L2_VP9_FRAME_FLAG_KEY_FRAME = 0x001


V4L2_VP9_FRAME_FLAG_SHOW_FRAME = 0x002


V4L2_VP9_FRAME_FLAG_ERROR_RESILIENT = 0x004


V4L2_VP9_FRAME_FLAG_INTRA_ONLY = 0x008


V4L2_VP9_FRAME_FLAG_ALLOW_HIGH_PREC_MV = 0x010


V4L2_VP9_FRAME_FLAG_REFRESH_FRAME_CTX = 0x020


V4L2_VP9_FRAME_FLAG_PARALLEL_DEC_MODE = 0x040


V4L2_VP9_FRAME_FLAG_X_SUBSAMPLING = 0x080


V4L2_VP9_FRAME_FLAG_Y_SUBSAMPLING = 0x100


V4L2_VP9_FRAME_FLAG_COLOR_RANGE_FULL_SWING = 0x200


V4L2_VP9_SIGN_BIAS_LAST = 0x1


V4L2_VP9_SIGN_BIAS_GOLDEN = 0x2


V4L2_VP9_SIGN_BIAS_ALT = 0x4


V4L2_VP9_RESET_FRAME_CTX_NONE = 0


V4L2_VP9_RESET_FRAME_CTX_SPEC = 1


V4L2_VP9_RESET_FRAME_CTX_ALL = 2


V4L2_VP9_INTERP_FILTER_EIGHTTAP = 0


V4L2_VP9_INTERP_FILTER_EIGHTTAP_SMOOTH = 1


V4L2_VP9_INTERP_FILTER_EIGHTTAP_SHARP = 2


V4L2_VP9_INTERP_FILTER_BILINEAR = 3


V4L2_VP9_INTERP_FILTER_SWITCHABLE = 4


V4L2_VP9_REFERENCE_MODE_SINGLE_REFERENCE = 0


V4L2_VP9_REFERENCE_MODE_COMPOUND_REFERENCE = 1


V4L2_VP9_REFERENCE_MODE_SELECT = 2


V4L2_VP9_PROFILE_MAX = 3


V4L2_CID_STATELESS_VP9_FRAME = (V4L2_CID_CODEC_STATELESS_BASE + 300)


V4L2_VP9_NUM_FRAME_CTX = 4


V4L2_CID_STATELESS_VP9_COMPRESSED_HDR = (V4L2_CID_CODEC_STATELESS_BASE + 301)


V4L2_VP9_TX_MODE_ONLY_4X4 = 0


V4L2_VP9_TX_MODE_ALLOW_8X8 = 1


V4L2_VP9_TX_MODE_ALLOW_16X16 = 2


V4L2_VP9_TX_MODE_ALLOW_32X32 = 3


V4L2_VP9_TX_MODE_SELECT = 4


V4L2_AV1_TOTAL_REFS_PER_FRAME = 8


V4L2_AV1_CDEF_MAX = 8


V4L2_AV1_NUM_PLANES_MAX = 3


V4L2_AV1_MAX_SEGMENTS = 8


V4L2_AV1_MAX_OPERATING_POINTS = (1 << 5)


V4L2_AV1_REFS_PER_FRAME = 7


V4L2_AV1_MAX_NUM_Y_POINTS = (1 << 4)


V4L2_AV1_MAX_NUM_CB_POINTS = (1 << 4)


V4L2_AV1_MAX_NUM_CR_POINTS = (1 << 4)


V4L2_AV1_AR_COEFFS_SIZE = 25


V4L2_AV1_MAX_NUM_PLANES = 3


V4L2_AV1_MAX_TILE_COLS = 64


V4L2_AV1_MAX_TILE_ROWS = 64


V4L2_AV1_MAX_TILE_COUNT = 512


V4L2_AV1_SEQUENCE_FLAG_STILL_PICTURE = 0x00000001


V4L2_AV1_SEQUENCE_FLAG_USE_128X128_SUPERBLOCK = 0x00000002


V4L2_AV1_SEQUENCE_FLAG_ENABLE_FILTER_INTRA = 0x00000004


V4L2_AV1_SEQUENCE_FLAG_ENABLE_INTRA_EDGE_FILTER = 0x00000008


V4L2_AV1_SEQUENCE_FLAG_ENABLE_INTERINTRA_COMPOUND = 0x00000010


V4L2_AV1_SEQUENCE_FLAG_ENABLE_MASKED_COMPOUND = 0x00000020


V4L2_AV1_SEQUENCE_FLAG_ENABLE_WARPED_MOTION = 0x00000040


V4L2_AV1_SEQUENCE_FLAG_ENABLE_DUAL_FILTER = 0x00000080


V4L2_AV1_SEQUENCE_FLAG_ENABLE_ORDER_HINT = 0x00000100


V4L2_AV1_SEQUENCE_FLAG_ENABLE_JNT_COMP = 0x00000200


V4L2_AV1_SEQUENCE_FLAG_ENABLE_REF_FRAME_MVS = 0x00000400


V4L2_AV1_SEQUENCE_FLAG_ENABLE_SUPERRES = 0x00000800


V4L2_AV1_SEQUENCE_FLAG_ENABLE_CDEF = 0x00001000


V4L2_AV1_SEQUENCE_FLAG_ENABLE_RESTORATION = 0x00002000


V4L2_AV1_SEQUENCE_FLAG_MONO_CHROME = 0x00004000


V4L2_AV1_SEQUENCE_FLAG_COLOR_RANGE = 0x00008000


V4L2_AV1_SEQUENCE_FLAG_SUBSAMPLING_X = 0x00010000


V4L2_AV1_SEQUENCE_FLAG_SUBSAMPLING_Y = 0x00020000


V4L2_AV1_SEQUENCE_FLAG_FILM_GRAIN_PARAMS_PRESENT = 0x00040000


V4L2_AV1_SEQUENCE_FLAG_SEPARATE_UV_DELTA_Q = 0x00080000


V4L2_CID_STATELESS_AV1_SEQUENCE = (V4L2_CID_CODEC_STATELESS_BASE + 500)


V4L2_CID_STATELESS_AV1_TILE_GROUP_ENTRY = (V4L2_CID_CODEC_STATELESS_BASE + 501)


def V4L2_AV1_GLOBAL_MOTION_IS_INVALID(ref):
    return (1 << ref)


V4L2_AV1_GLOBAL_MOTION_FLAG_IS_GLOBAL = 0x1


V4L2_AV1_GLOBAL_MOTION_FLAG_IS_ROT_ZOOM = 0x2


V4L2_AV1_GLOBAL_MOTION_FLAG_IS_TRANSLATION = 0x4


V4L2_AV1_LOOP_RESTORATION_FLAG_USES_LR = 0x1


V4L2_AV1_LOOP_RESTORATION_FLAG_USES_CHROMA_LR = 0x2


V4L2_AV1_SEGMENTATION_FLAG_ENABLED = 0x1


V4L2_AV1_SEGMENTATION_FLAG_UPDATE_MAP = 0x2


V4L2_AV1_SEGMENTATION_FLAG_TEMPORAL_UPDATE = 0x4


V4L2_AV1_SEGMENTATION_FLAG_UPDATE_DATA = 0x8


V4L2_AV1_SEGMENTATION_FLAG_SEG_ID_PRE_SKIP = 0x10


def V4L2_AV1_SEGMENT_FEATURE_ENABLED(id):
    return (1 << id)


V4L2_AV1_LOOP_FILTER_FLAG_DELTA_ENABLED = 0x1


V4L2_AV1_LOOP_FILTER_FLAG_DELTA_UPDATE = 0x2


V4L2_AV1_LOOP_FILTER_FLAG_DELTA_LF_PRESENT = 0x4


V4L2_AV1_LOOP_FILTER_FLAG_DELTA_LF_MULTI = 0x8


V4L2_AV1_QUANTIZATION_FLAG_DIFF_UV_DELTA = 0x1


V4L2_AV1_QUANTIZATION_FLAG_USING_QMATRIX = 0x2


V4L2_AV1_QUANTIZATION_FLAG_DELTA_Q_PRESENT = 0x4


V4L2_AV1_TILE_INFO_FLAG_UNIFORM_TILE_SPACING = 0x1


V4L2_AV1_FRAME_FLAG_SHOW_FRAME = 0x00000001


V4L2_AV1_FRAME_FLAG_SHOWABLE_FRAME = 0x00000002


V4L2_AV1_FRAME_FLAG_ERROR_RESILIENT_MODE = 0x00000004


V4L2_AV1_FRAME_FLAG_DISABLE_CDF_UPDATE = 0x00000008


V4L2_AV1_FRAME_FLAG_ALLOW_SCREEN_CONTENT_TOOLS = 0x00000010


V4L2_AV1_FRAME_FLAG_FORCE_INTEGER_MV = 0x00000020


V4L2_AV1_FRAME_FLAG_ALLOW_INTRABC = 0x00000040


V4L2_AV1_FRAME_FLAG_USE_SUPERRES = 0x00000080


V4L2_AV1_FRAME_FLAG_ALLOW_HIGH_PRECISION_MV = 0x00000100


V4L2_AV1_FRAME_FLAG_IS_MOTION_MODE_SWITCHABLE = 0x00000200


V4L2_AV1_FRAME_FLAG_USE_REF_FRAME_MVS = 0x00000400


V4L2_AV1_FRAME_FLAG_DISABLE_FRAME_END_UPDATE_CDF = 0x00000800


V4L2_AV1_FRAME_FLAG_ALLOW_WARPED_MOTION = 0x00001000


V4L2_AV1_FRAME_FLAG_REFERENCE_SELECT = 0x00002000


V4L2_AV1_FRAME_FLAG_REDUCED_TX_SET = 0x00004000


V4L2_AV1_FRAME_FLAG_SKIP_MODE_ALLOWED = 0x00008000


V4L2_AV1_FRAME_FLAG_SKIP_MODE_PRESENT = 0x00010000


V4L2_AV1_FRAME_FLAG_FRAME_SIZE_OVERRIDE = 0x00020000


V4L2_AV1_FRAME_FLAG_BUFFER_REMOVAL_TIME_PRESENT = 0x00040000


V4L2_AV1_FRAME_FLAG_FRAME_REFS_SHORT_SIGNALING = 0x00080000


V4L2_CID_STATELESS_AV1_FRAME = (V4L2_CID_CODEC_STATELESS_BASE + 502)


V4L2_AV1_FILM_GRAIN_FLAG_APPLY_GRAIN = 0x1


V4L2_AV1_FILM_GRAIN_FLAG_UPDATE_GRAIN = 0x2


V4L2_AV1_FILM_GRAIN_FLAG_CHROMA_SCALING_FROM_LUMA = 0x4


V4L2_AV1_FILM_GRAIN_FLAG_OVERLAP = 0x8


V4L2_AV1_FILM_GRAIN_FLAG_CLIP_TO_RESTRICTED_RANGE = 0x10


V4L2_CID_STATELESS_AV1_FILM_GRAIN = (V4L2_CID_CODEC_STATELESS_BASE + 505)


V4L2_CTRL_CLASS_MPEG = V4L2_CTRL_CLASS_CODEC


V4L2_CID_MPEG_CLASS = V4L2_CID_CODEC_CLASS


V4L2_CID_MPEG_BASE = V4L2_CID_CODEC_BASE


V4L2_CID_MPEG_CX2341X_BASE = V4L2_CID_CODEC_CX2341X_BASE


V4L2_CID_MPEG_MFC51_BASE = V4L2_CID_CODEC_MFC51_BASE


VIDEO_MAX_FRAME = 32


VIDEO_MAX_PLANES = 8


def v4l2_fourcc(a, b, c, d):
    return ((((__u32 (ord_if_char(a))).value | ((__u32 (ord_if_char(b))).value << 8)) | ((__u32 (ord_if_char(c))).value << 16)) | ((__u32 (ord_if_char(d))).value << 24))


def v4l2_fourcc_be(a, b, c, d):
    return ((v4l2_fourcc (a, b, c, d)) | (1 << 31))


def V4L2_FIELD_HAS_TOP(field):
    return ((((((field == V4L2_FIELD_TOP) or (field == V4L2_FIELD_INTERLACED)) or (field == V4L2_FIELD_INTERLACED_TB)) or (field == V4L2_FIELD_INTERLACED_BT)) or (field == V4L2_FIELD_SEQ_TB)) or (field == V4L2_FIELD_SEQ_BT))


def V4L2_FIELD_HAS_BOTTOM(field):
    return ((((((field == V4L2_FIELD_BOTTOM) or (field == V4L2_FIELD_INTERLACED)) or (field == V4L2_FIELD_INTERLACED_TB)) or (field == V4L2_FIELD_INTERLACED_BT)) or (field == V4L2_FIELD_SEQ_TB)) or (field == V4L2_FIELD_SEQ_BT))


def V4L2_FIELD_HAS_BOTH(field):
    return (((((field == V4L2_FIELD_INTERLACED) or (field == V4L2_FIELD_INTERLACED_TB)) or (field == V4L2_FIELD_INTERLACED_BT)) or (field == V4L2_FIELD_SEQ_TB)) or (field == V4L2_FIELD_SEQ_BT))


def V4L2_FIELD_HAS_T_OR_B(field):
    return (((field == V4L2_FIELD_BOTTOM) or (field == V4L2_FIELD_TOP)) or (field == V4L2_FIELD_ALTERNATE))


def V4L2_FIELD_IS_INTERLACED(field):
    return (((field == V4L2_FIELD_INTERLACED) or (field == V4L2_FIELD_INTERLACED_TB)) or (field == V4L2_FIELD_INTERLACED_BT))


def V4L2_FIELD_IS_SEQUENTIAL(field):
    return ((field == V4L2_FIELD_SEQ_TB) or (field == V4L2_FIELD_SEQ_BT))


def V4L2_TYPE_IS_MULTIPLANAR(type):
    return ((type == V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE) or (type == V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE))


def V4L2_TYPE_IS_OUTPUT(type):
    return ((((((((type == V4L2_BUF_TYPE_VIDEO_OUTPUT) or (type == V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE)) or (type == V4L2_BUF_TYPE_VIDEO_OVERLAY)) or (type == V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY)) or (type == V4L2_BUF_TYPE_VBI_OUTPUT)) or (type == V4L2_BUF_TYPE_SLICED_VBI_OUTPUT)) or (type == V4L2_BUF_TYPE_SDR_OUTPUT)) or (type == V4L2_BUF_TYPE_META_OUTPUT))


def V4L2_TYPE_IS_CAPTURE(type):
    return (not (V4L2_TYPE_IS_OUTPUT (type)))


V4L2_TUNER_ADC = V4L2_TUNER_SDR


def V4L2_MAP_COLORSPACE_DEFAULT(is_sdtv, is_hdtv):
    return is_sdtv and V4L2_COLORSPACE_SMPTE170M or is_hdtv and V4L2_COLORSPACE_REC709 or V4L2_COLORSPACE_SRGB


def V4L2_MAP_XFER_FUNC_DEFAULT(colsp):
    return (colsp == V4L2_COLORSPACE_OPRGB) and V4L2_XFER_FUNC_OPRGB or (colsp == V4L2_COLORSPACE_SMPTE240M) and V4L2_XFER_FUNC_SMPTE240M or (colsp == V4L2_COLORSPACE_DCI_P3) and V4L2_XFER_FUNC_DCI_P3 or (colsp == V4L2_COLORSPACE_RAW) and V4L2_XFER_FUNC_NONE or ((colsp == V4L2_COLORSPACE_SRGB) or (colsp == V4L2_COLORSPACE_JPEG)) and V4L2_XFER_FUNC_SRGB or V4L2_XFER_FUNC_709


def V4L2_MAP_YCBCR_ENC_DEFAULT(colsp):
    return ((colsp == V4L2_COLORSPACE_REC709) or (colsp == V4L2_COLORSPACE_DCI_P3)) and V4L2_YCBCR_ENC_709 or (colsp == V4L2_COLORSPACE_BT2020) and V4L2_YCBCR_ENC_BT2020 or (colsp == V4L2_COLORSPACE_SMPTE240M) and V4L2_YCBCR_ENC_SMPTE240M or V4L2_YCBCR_ENC_601


def V4L2_MAP_QUANTIZATION_DEFAULT(is_rgb_or_hsv, colsp, ycbcr_enc):
    return (is_rgb_or_hsv or (colsp == V4L2_COLORSPACE_JPEG)) and V4L2_QUANTIZATION_FULL_RANGE or V4L2_QUANTIZATION_LIM_RANGE


V4L2_COLORSPACE_ADOBERGB = V4L2_COLORSPACE_OPRGB


V4L2_XFER_FUNC_ADOBERGB = V4L2_XFER_FUNC_OPRGB


V4L2_CAP_VIDEO_CAPTURE = 0x00000001


V4L2_CAP_VIDEO_OUTPUT = 0x00000002


V4L2_CAP_VIDEO_OVERLAY = 0x00000004


V4L2_CAP_VBI_CAPTURE = 0x00000010


V4L2_CAP_VBI_OUTPUT = 0x00000020


V4L2_CAP_SLICED_VBI_CAPTURE = 0x00000040


V4L2_CAP_SLICED_VBI_OUTPUT = 0x00000080


V4L2_CAP_RDS_CAPTURE = 0x00000100


V4L2_CAP_VIDEO_OUTPUT_OVERLAY = 0x00000200


V4L2_CAP_HW_FREQ_SEEK = 0x00000400


V4L2_CAP_RDS_OUTPUT = 0x00000800


V4L2_CAP_VIDEO_CAPTURE_MPLANE = 0x00001000


V4L2_CAP_VIDEO_OUTPUT_MPLANE = 0x00002000


V4L2_CAP_VIDEO_M2M_MPLANE = 0x00004000


V4L2_CAP_VIDEO_M2M = 0x00008000


V4L2_CAP_TUNER = 0x00010000


V4L2_CAP_AUDIO = 0x00020000


V4L2_CAP_RADIO = 0x00040000


V4L2_CAP_MODULATOR = 0x00080000


V4L2_CAP_SDR_CAPTURE = 0x00100000


V4L2_CAP_EXT_PIX_FORMAT = 0x00200000


V4L2_CAP_SDR_OUTPUT = 0x00400000


V4L2_CAP_META_CAPTURE = 0x00800000


V4L2_CAP_READWRITE = 0x01000000


V4L2_CAP_STREAMING = 0x04000000


V4L2_CAP_META_OUTPUT = 0x08000000


V4L2_CAP_TOUCH = 0x10000000


V4L2_CAP_IO_MC = 0x20000000


V4L2_CAP_DEVICE_CAPS = 0x80000000


V4L2_PIX_FMT_RGB332 = (v4l2_fourcc ('R', 'G', 'B', '1'))


V4L2_PIX_FMT_RGB444 = (v4l2_fourcc ('R', '4', '4', '4'))


V4L2_PIX_FMT_ARGB444 = (v4l2_fourcc ('A', 'R', '1', '2'))


V4L2_PIX_FMT_XRGB444 = (v4l2_fourcc ('X', 'R', '1', '2'))


V4L2_PIX_FMT_RGBA444 = (v4l2_fourcc ('R', 'A', '1', '2'))


V4L2_PIX_FMT_RGBX444 = (v4l2_fourcc ('R', 'X', '1', '2'))


V4L2_PIX_FMT_ABGR444 = (v4l2_fourcc ('A', 'B', '1', '2'))


V4L2_PIX_FMT_XBGR444 = (v4l2_fourcc ('X', 'B', '1', '2'))


V4L2_PIX_FMT_BGRA444 = (v4l2_fourcc ('G', 'A', '1', '2'))


V4L2_PIX_FMT_BGRX444 = (v4l2_fourcc ('B', 'X', '1', '2'))


V4L2_PIX_FMT_RGB555 = (v4l2_fourcc ('R', 'G', 'B', 'O'))


V4L2_PIX_FMT_ARGB555 = (v4l2_fourcc ('A', 'R', '1', '5'))


V4L2_PIX_FMT_XRGB555 = (v4l2_fourcc ('X', 'R', '1', '5'))


V4L2_PIX_FMT_RGBA555 = (v4l2_fourcc ('R', 'A', '1', '5'))


V4L2_PIX_FMT_RGBX555 = (v4l2_fourcc ('R', 'X', '1', '5'))


V4L2_PIX_FMT_ABGR555 = (v4l2_fourcc ('A', 'B', '1', '5'))


V4L2_PIX_FMT_XBGR555 = (v4l2_fourcc ('X', 'B', '1', '5'))


V4L2_PIX_FMT_BGRA555 = (v4l2_fourcc ('B', 'A', '1', '5'))


V4L2_PIX_FMT_BGRX555 = (v4l2_fourcc ('B', 'X', '1', '5'))


V4L2_PIX_FMT_RGB565 = (v4l2_fourcc ('R', 'G', 'B', 'P'))


V4L2_PIX_FMT_RGB555X = (v4l2_fourcc ('R', 'G', 'B', 'Q'))


V4L2_PIX_FMT_ARGB555X = (v4l2_fourcc_be ('A', 'R', '1', '5'))


V4L2_PIX_FMT_XRGB555X = (v4l2_fourcc_be ('X', 'R', '1', '5'))


V4L2_PIX_FMT_RGB565X = (v4l2_fourcc ('R', 'G', 'B', 'R'))


V4L2_PIX_FMT_BGR666 = (v4l2_fourcc ('B', 'G', 'R', 'H'))


V4L2_PIX_FMT_BGR24 = (v4l2_fourcc ('B', 'G', 'R', '3'))


V4L2_PIX_FMT_RGB24 = (v4l2_fourcc ('R', 'G', 'B', '3'))


V4L2_PIX_FMT_BGR32 = (v4l2_fourcc ('B', 'G', 'R', '4'))


V4L2_PIX_FMT_ABGR32 = (v4l2_fourcc ('A', 'R', '2', '4'))


V4L2_PIX_FMT_XBGR32 = (v4l2_fourcc ('X', 'R', '2', '4'))


V4L2_PIX_FMT_BGRA32 = (v4l2_fourcc ('R', 'A', '2', '4'))


V4L2_PIX_FMT_BGRX32 = (v4l2_fourcc ('R', 'X', '2', '4'))


V4L2_PIX_FMT_RGB32 = (v4l2_fourcc ('R', 'G', 'B', '4'))


V4L2_PIX_FMT_RGBA32 = (v4l2_fourcc ('A', 'B', '2', '4'))


V4L2_PIX_FMT_RGBX32 = (v4l2_fourcc ('X', 'B', '2', '4'))


V4L2_PIX_FMT_ARGB32 = (v4l2_fourcc ('B', 'A', '2', '4'))


V4L2_PIX_FMT_XRGB32 = (v4l2_fourcc ('B', 'X', '2', '4'))


V4L2_PIX_FMT_RGBX1010102 = (v4l2_fourcc ('R', 'X', '3', '0'))


V4L2_PIX_FMT_RGBA1010102 = (v4l2_fourcc ('R', 'A', '3', '0'))


V4L2_PIX_FMT_ARGB2101010 = (v4l2_fourcc ('A', 'R', '3', '0'))


V4L2_PIX_FMT_BGR48_12 = (v4l2_fourcc ('B', '3', '1', '2'))


V4L2_PIX_FMT_BGR48 = (v4l2_fourcc ('B', 'G', 'R', '6'))


V4L2_PIX_FMT_RGB48 = (v4l2_fourcc ('R', 'G', 'B', '6'))


V4L2_PIX_FMT_ABGR64_12 = (v4l2_fourcc ('B', '4', '1', '2'))


V4L2_PIX_FMT_GREY = (v4l2_fourcc ('G', 'R', 'E', 'Y'))


V4L2_PIX_FMT_Y4 = (v4l2_fourcc ('Y', '0', '4', ' '))


V4L2_PIX_FMT_Y6 = (v4l2_fourcc ('Y', '0', '6', ' '))


V4L2_PIX_FMT_Y10 = (v4l2_fourcc ('Y', '1', '0', ' '))


V4L2_PIX_FMT_Y12 = (v4l2_fourcc ('Y', '1', '2', ' '))


V4L2_PIX_FMT_Y012 = (v4l2_fourcc ('Y', '0', '1', '2'))


V4L2_PIX_FMT_Y14 = (v4l2_fourcc ('Y', '1', '4', ' '))


V4L2_PIX_FMT_Y16 = (v4l2_fourcc ('Y', '1', '6', ' '))


V4L2_PIX_FMT_Y16_BE = (v4l2_fourcc_be ('Y', '1', '6', ' '))


V4L2_PIX_FMT_Y10BPACK = (v4l2_fourcc ('Y', '1', '0', 'B'))


V4L2_PIX_FMT_Y10P = (v4l2_fourcc ('Y', '1', '0', 'P'))


V4L2_PIX_FMT_IPU3_Y10 = (v4l2_fourcc ('i', 'p', '3', 'y'))


V4L2_PIX_FMT_Y12P = (v4l2_fourcc ('Y', '1', '2', 'P'))


V4L2_PIX_FMT_Y14P = (v4l2_fourcc ('Y', '1', '4', 'P'))


V4L2_PIX_FMT_PAL8 = (v4l2_fourcc ('P', 'A', 'L', '8'))


V4L2_PIX_FMT_UV8 = (v4l2_fourcc ('U', 'V', '8', ' '))


V4L2_PIX_FMT_YUYV = (v4l2_fourcc ('Y', 'U', 'Y', 'V'))


V4L2_PIX_FMT_YYUV = (v4l2_fourcc ('Y', 'Y', 'U', 'V'))


V4L2_PIX_FMT_YVYU = (v4l2_fourcc ('Y', 'V', 'Y', 'U'))


V4L2_PIX_FMT_UYVY = (v4l2_fourcc ('U', 'Y', 'V', 'Y'))


V4L2_PIX_FMT_VYUY = (v4l2_fourcc ('V', 'Y', 'U', 'Y'))


V4L2_PIX_FMT_Y41P = (v4l2_fourcc ('Y', '4', '1', 'P'))


V4L2_PIX_FMT_YUV444 = (v4l2_fourcc ('Y', '4', '4', '4'))


V4L2_PIX_FMT_YUV555 = (v4l2_fourcc ('Y', 'U', 'V', 'O'))


V4L2_PIX_FMT_YUV565 = (v4l2_fourcc ('Y', 'U', 'V', 'P'))


V4L2_PIX_FMT_YUV24 = (v4l2_fourcc ('Y', 'U', 'V', '3'))


V4L2_PIX_FMT_YUV32 = (v4l2_fourcc ('Y', 'U', 'V', '4'))


V4L2_PIX_FMT_AYUV32 = (v4l2_fourcc ('A', 'Y', 'U', 'V'))


V4L2_PIX_FMT_XYUV32 = (v4l2_fourcc ('X', 'Y', 'U', 'V'))


V4L2_PIX_FMT_VUYA32 = (v4l2_fourcc ('V', 'U', 'Y', 'A'))


V4L2_PIX_FMT_VUYX32 = (v4l2_fourcc ('V', 'U', 'Y', 'X'))


V4L2_PIX_FMT_YUVA32 = (v4l2_fourcc ('Y', 'U', 'V', 'A'))


V4L2_PIX_FMT_YUVX32 = (v4l2_fourcc ('Y', 'U', 'V', 'X'))


V4L2_PIX_FMT_M420 = (v4l2_fourcc ('M', '4', '2', '0'))


V4L2_PIX_FMT_YUV48_12 = (v4l2_fourcc ('Y', '3', '1', '2'))


V4L2_PIX_FMT_Y210 = (v4l2_fourcc ('Y', '2', '1', '0'))


V4L2_PIX_FMT_Y212 = (v4l2_fourcc ('Y', '2', '1', '2'))


V4L2_PIX_FMT_Y216 = (v4l2_fourcc ('Y', '2', '1', '6'))


V4L2_PIX_FMT_NV12 = (v4l2_fourcc ('N', 'V', '1', '2'))


V4L2_PIX_FMT_NV21 = (v4l2_fourcc ('N', 'V', '2', '1'))


V4L2_PIX_FMT_NV16 = (v4l2_fourcc ('N', 'V', '1', '6'))


V4L2_PIX_FMT_NV61 = (v4l2_fourcc ('N', 'V', '6', '1'))


V4L2_PIX_FMT_NV24 = (v4l2_fourcc ('N', 'V', '2', '4'))


V4L2_PIX_FMT_NV42 = (v4l2_fourcc ('N', 'V', '4', '2'))


V4L2_PIX_FMT_P010 = (v4l2_fourcc ('P', '0', '1', '0'))


V4L2_PIX_FMT_P012 = (v4l2_fourcc ('P', '0', '1', '2'))


V4L2_PIX_FMT_NV12M = (v4l2_fourcc ('N', 'M', '1', '2'))


V4L2_PIX_FMT_NV21M = (v4l2_fourcc ('N', 'M', '2', '1'))


V4L2_PIX_FMT_NV16M = (v4l2_fourcc ('N', 'M', '1', '6'))


V4L2_PIX_FMT_NV61M = (v4l2_fourcc ('N', 'M', '6', '1'))


V4L2_PIX_FMT_P012M = (v4l2_fourcc ('P', 'M', '1', '2'))


V4L2_PIX_FMT_YUV410 = (v4l2_fourcc ('Y', 'U', 'V', '9'))


V4L2_PIX_FMT_YVU410 = (v4l2_fourcc ('Y', 'V', 'U', '9'))


V4L2_PIX_FMT_YUV411P = (v4l2_fourcc ('4', '1', '1', 'P'))


V4L2_PIX_FMT_YUV420 = (v4l2_fourcc ('Y', 'U', '1', '2'))


V4L2_PIX_FMT_YVU420 = (v4l2_fourcc ('Y', 'V', '1', '2'))


V4L2_PIX_FMT_YUV422P = (v4l2_fourcc ('4', '2', '2', 'P'))


V4L2_PIX_FMT_YUV420M = (v4l2_fourcc ('Y', 'M', '1', '2'))


V4L2_PIX_FMT_YVU420M = (v4l2_fourcc ('Y', 'M', '2', '1'))


V4L2_PIX_FMT_YUV422M = (v4l2_fourcc ('Y', 'M', '1', '6'))


V4L2_PIX_FMT_YVU422M = (v4l2_fourcc ('Y', 'M', '6', '1'))


V4L2_PIX_FMT_YUV444M = (v4l2_fourcc ('Y', 'M', '2', '4'))


V4L2_PIX_FMT_YVU444M = (v4l2_fourcc ('Y', 'M', '4', '2'))


V4L2_PIX_FMT_NV12_4L4 = (v4l2_fourcc ('V', 'T', '1', '2'))


V4L2_PIX_FMT_NV12_16L16 = (v4l2_fourcc ('H', 'M', '1', '2'))


V4L2_PIX_FMT_NV12_32L32 = (v4l2_fourcc ('S', 'T', '1', '2'))


V4L2_PIX_FMT_NV15_4L4 = (v4l2_fourcc ('V', 'T', '1', '5'))


V4L2_PIX_FMT_P010_4L4 = (v4l2_fourcc ('T', '0', '1', '0'))


V4L2_PIX_FMT_NV12_8L128 = (v4l2_fourcc ('A', 'T', '1', '2'))


V4L2_PIX_FMT_NV12_10BE_8L128 = (v4l2_fourcc_be ('A', 'X', '1', '2'))


V4L2_PIX_FMT_NV12MT = (v4l2_fourcc ('T', 'M', '1', '2'))


V4L2_PIX_FMT_NV12MT_16X16 = (v4l2_fourcc ('V', 'M', '1', '2'))


V4L2_PIX_FMT_NV12M_8L128 = (v4l2_fourcc ('N', 'A', '1', '2'))


V4L2_PIX_FMT_NV12M_10BE_8L128 = (v4l2_fourcc_be ('N', 'T', '1', '2'))


V4L2_PIX_FMT_SBGGR8 = (v4l2_fourcc ('B', 'A', '8', '1'))


V4L2_PIX_FMT_SGBRG8 = (v4l2_fourcc ('G', 'B', 'R', 'G'))


V4L2_PIX_FMT_SGRBG8 = (v4l2_fourcc ('G', 'R', 'B', 'G'))


V4L2_PIX_FMT_SRGGB8 = (v4l2_fourcc ('R', 'G', 'G', 'B'))


V4L2_PIX_FMT_SBGGR10 = (v4l2_fourcc ('B', 'G', '1', '0'))


V4L2_PIX_FMT_SGBRG10 = (v4l2_fourcc ('G', 'B', '1', '0'))


V4L2_PIX_FMT_SGRBG10 = (v4l2_fourcc ('B', 'A', '1', '0'))


V4L2_PIX_FMT_SRGGB10 = (v4l2_fourcc ('R', 'G', '1', '0'))


V4L2_PIX_FMT_SBGGR10P = (v4l2_fourcc ('p', 'B', 'A', 'A'))


V4L2_PIX_FMT_SGBRG10P = (v4l2_fourcc ('p', 'G', 'A', 'A'))


V4L2_PIX_FMT_SGRBG10P = (v4l2_fourcc ('p', 'g', 'A', 'A'))


V4L2_PIX_FMT_SRGGB10P = (v4l2_fourcc ('p', 'R', 'A', 'A'))


V4L2_PIX_FMT_SBGGR10ALAW8 = (v4l2_fourcc ('a', 'B', 'A', '8'))


V4L2_PIX_FMT_SGBRG10ALAW8 = (v4l2_fourcc ('a', 'G', 'A', '8'))


V4L2_PIX_FMT_SGRBG10ALAW8 = (v4l2_fourcc ('a', 'g', 'A', '8'))


V4L2_PIX_FMT_SRGGB10ALAW8 = (v4l2_fourcc ('a', 'R', 'A', '8'))


V4L2_PIX_FMT_SBGGR10DPCM8 = (v4l2_fourcc ('b', 'B', 'A', '8'))


V4L2_PIX_FMT_SGBRG10DPCM8 = (v4l2_fourcc ('b', 'G', 'A', '8'))


V4L2_PIX_FMT_SGRBG10DPCM8 = (v4l2_fourcc ('B', 'D', '1', '0'))


V4L2_PIX_FMT_SRGGB10DPCM8 = (v4l2_fourcc ('b', 'R', 'A', '8'))


V4L2_PIX_FMT_SBGGR12 = (v4l2_fourcc ('B', 'G', '1', '2'))


V4L2_PIX_FMT_SGBRG12 = (v4l2_fourcc ('G', 'B', '1', '2'))


V4L2_PIX_FMT_SGRBG12 = (v4l2_fourcc ('B', 'A', '1', '2'))


V4L2_PIX_FMT_SRGGB12 = (v4l2_fourcc ('R', 'G', '1', '2'))


V4L2_PIX_FMT_SBGGR12P = (v4l2_fourcc ('p', 'B', 'C', 'C'))


V4L2_PIX_FMT_SGBRG12P = (v4l2_fourcc ('p', 'G', 'C', 'C'))


V4L2_PIX_FMT_SGRBG12P = (v4l2_fourcc ('p', 'g', 'C', 'C'))


V4L2_PIX_FMT_SRGGB12P = (v4l2_fourcc ('p', 'R', 'C', 'C'))


V4L2_PIX_FMT_SBGGR14 = (v4l2_fourcc ('B', 'G', '1', '4'))


V4L2_PIX_FMT_SGBRG14 = (v4l2_fourcc ('G', 'B', '1', '4'))


V4L2_PIX_FMT_SGRBG14 = (v4l2_fourcc ('G', 'R', '1', '4'))


V4L2_PIX_FMT_SRGGB14 = (v4l2_fourcc ('R', 'G', '1', '4'))


V4L2_PIX_FMT_SBGGR14P = (v4l2_fourcc ('p', 'B', 'E', 'E'))


V4L2_PIX_FMT_SGBRG14P = (v4l2_fourcc ('p', 'G', 'E', 'E'))


V4L2_PIX_FMT_SGRBG14P = (v4l2_fourcc ('p', 'g', 'E', 'E'))


V4L2_PIX_FMT_SRGGB14P = (v4l2_fourcc ('p', 'R', 'E', 'E'))


V4L2_PIX_FMT_SBGGR16 = (v4l2_fourcc ('B', 'Y', 'R', '2'))


V4L2_PIX_FMT_SGBRG16 = (v4l2_fourcc ('G', 'B', '1', '6'))


V4L2_PIX_FMT_SGRBG16 = (v4l2_fourcc ('G', 'R', '1', '6'))


V4L2_PIX_FMT_SRGGB16 = (v4l2_fourcc ('R', 'G', '1', '6'))


V4L2_PIX_FMT_HSV24 = (v4l2_fourcc ('H', 'S', 'V', '3'))


V4L2_PIX_FMT_HSV32 = (v4l2_fourcc ('H', 'S', 'V', '4'))


V4L2_PIX_FMT_MJPEG = (v4l2_fourcc ('M', 'J', 'P', 'G'))


V4L2_PIX_FMT_JPEG = (v4l2_fourcc ('J', 'P', 'E', 'G'))


V4L2_PIX_FMT_DV = (v4l2_fourcc ('d', 'v', 's', 'd'))


V4L2_PIX_FMT_MPEG = (v4l2_fourcc ('M', 'P', 'E', 'G'))


V4L2_PIX_FMT_H264 = (v4l2_fourcc ('H', '2', '6', '4'))


V4L2_PIX_FMT_H264_NO_SC = (v4l2_fourcc ('A', 'V', 'C', '1'))


V4L2_PIX_FMT_H264_MVC = (v4l2_fourcc ('M', '2', '6', '4'))


V4L2_PIX_FMT_H263 = (v4l2_fourcc ('H', '2', '6', '3'))


V4L2_PIX_FMT_MPEG1 = (v4l2_fourcc ('M', 'P', 'G', '1'))


V4L2_PIX_FMT_MPEG2 = (v4l2_fourcc ('M', 'P', 'G', '2'))


V4L2_PIX_FMT_MPEG2_SLICE = (v4l2_fourcc ('M', 'G', '2', 'S'))


V4L2_PIX_FMT_MPEG4 = (v4l2_fourcc ('M', 'P', 'G', '4'))


V4L2_PIX_FMT_XVID = (v4l2_fourcc ('X', 'V', 'I', 'D'))


V4L2_PIX_FMT_VC1_ANNEX_G = (v4l2_fourcc ('V', 'C', '1', 'G'))


V4L2_PIX_FMT_VC1_ANNEX_L = (v4l2_fourcc ('V', 'C', '1', 'L'))


V4L2_PIX_FMT_VP8 = (v4l2_fourcc ('V', 'P', '8', '0'))


V4L2_PIX_FMT_VP8_FRAME = (v4l2_fourcc ('V', 'P', '8', 'F'))


V4L2_PIX_FMT_VP9 = (v4l2_fourcc ('V', 'P', '9', '0'))


V4L2_PIX_FMT_VP9_FRAME = (v4l2_fourcc ('V', 'P', '9', 'F'))


V4L2_PIX_FMT_HEVC = (v4l2_fourcc ('H', 'E', 'V', 'C'))


V4L2_PIX_FMT_FWHT = (v4l2_fourcc ('F', 'W', 'H', 'T'))


V4L2_PIX_FMT_FWHT_STATELESS = (v4l2_fourcc ('S', 'F', 'W', 'H'))


V4L2_PIX_FMT_H264_SLICE = (v4l2_fourcc ('S', '2', '6', '4'))


V4L2_PIX_FMT_HEVC_SLICE = (v4l2_fourcc ('S', '2', '6', '5'))


V4L2_PIX_FMT_AV1_FRAME = (v4l2_fourcc ('A', 'V', '1', 'F'))


V4L2_PIX_FMT_SPK = (v4l2_fourcc ('S', 'P', 'K', '0'))


V4L2_PIX_FMT_RV30 = (v4l2_fourcc ('R', 'V', '3', '0'))


V4L2_PIX_FMT_RV40 = (v4l2_fourcc ('R', 'V', '4', '0'))


V4L2_PIX_FMT_CPIA1 = (v4l2_fourcc ('C', 'P', 'I', 'A'))


V4L2_PIX_FMT_WNVA = (v4l2_fourcc ('W', 'N', 'V', 'A'))


V4L2_PIX_FMT_SN9C10X = (v4l2_fourcc ('S', '9', '1', '0'))


V4L2_PIX_FMT_SN9C20X_I420 = (v4l2_fourcc ('S', '9', '2', '0'))


V4L2_PIX_FMT_PWC1 = (v4l2_fourcc ('P', 'W', 'C', '1'))


V4L2_PIX_FMT_PWC2 = (v4l2_fourcc ('P', 'W', 'C', '2'))


V4L2_PIX_FMT_ET61X251 = (v4l2_fourcc ('E', '6', '2', '5'))


V4L2_PIX_FMT_SPCA501 = (v4l2_fourcc ('S', '5', '0', '1'))


V4L2_PIX_FMT_SPCA505 = (v4l2_fourcc ('S', '5', '0', '5'))


V4L2_PIX_FMT_SPCA508 = (v4l2_fourcc ('S', '5', '0', '8'))


V4L2_PIX_FMT_SPCA561 = (v4l2_fourcc ('S', '5', '6', '1'))


V4L2_PIX_FMT_PAC207 = (v4l2_fourcc ('P', '2', '0', '7'))


V4L2_PIX_FMT_MR97310A = (v4l2_fourcc ('M', '3', '1', '0'))


V4L2_PIX_FMT_JL2005BCD = (v4l2_fourcc ('J', 'L', '2', '0'))


V4L2_PIX_FMT_SN9C2028 = (v4l2_fourcc ('S', 'O', 'N', 'X'))


V4L2_PIX_FMT_SQ905C = (v4l2_fourcc ('9', '0', '5', 'C'))


V4L2_PIX_FMT_PJPG = (v4l2_fourcc ('P', 'J', 'P', 'G'))


V4L2_PIX_FMT_OV511 = (v4l2_fourcc ('O', '5', '1', '1'))


V4L2_PIX_FMT_OV518 = (v4l2_fourcc ('O', '5', '1', '8'))


V4L2_PIX_FMT_STV0680 = (v4l2_fourcc ('S', '6', '8', '0'))


V4L2_PIX_FMT_TM6000 = (v4l2_fourcc ('T', 'M', '6', '0'))


V4L2_PIX_FMT_CIT_YYVYUY = (v4l2_fourcc ('C', 'I', 'T', 'V'))


V4L2_PIX_FMT_KONICA420 = (v4l2_fourcc ('K', 'O', 'N', 'I'))


V4L2_PIX_FMT_JPGL = (v4l2_fourcc ('J', 'P', 'G', 'L'))


V4L2_PIX_FMT_SE401 = (v4l2_fourcc ('S', '4', '0', '1'))


V4L2_PIX_FMT_S5C_UYVY_JPG = (v4l2_fourcc ('S', '5', 'C', 'I'))


V4L2_PIX_FMT_Y8I = (v4l2_fourcc ('Y', '8', 'I', ' '))


V4L2_PIX_FMT_Y12I = (v4l2_fourcc ('Y', '1', '2', 'I'))


V4L2_PIX_FMT_Z16 = (v4l2_fourcc ('Z', '1', '6', ' '))


V4L2_PIX_FMT_MT21C = (v4l2_fourcc ('M', 'T', '2', '1'))


V4L2_PIX_FMT_MM21 = (v4l2_fourcc ('M', 'M', '2', '1'))


V4L2_PIX_FMT_MT2110T = (v4l2_fourcc ('M', 'T', '2', 'T'))


V4L2_PIX_FMT_MT2110R = (v4l2_fourcc ('M', 'T', '2', 'R'))


V4L2_PIX_FMT_INZI = (v4l2_fourcc ('I', 'N', 'Z', 'I'))


V4L2_PIX_FMT_CNF4 = (v4l2_fourcc ('C', 'N', 'F', '4'))


V4L2_PIX_FMT_HI240 = (v4l2_fourcc ('H', 'I', '2', '4'))


V4L2_PIX_FMT_QC08C = (v4l2_fourcc ('Q', '0', '8', 'C'))


V4L2_PIX_FMT_QC10C = (v4l2_fourcc ('Q', '1', '0', 'C'))


V4L2_PIX_FMT_AJPG = (v4l2_fourcc ('A', 'J', 'P', 'G'))


V4L2_PIX_FMT_HEXTILE = (v4l2_fourcc ('H', 'X', 'T', 'L'))


V4L2_PIX_FMT_IPU3_SBGGR10 = (v4l2_fourcc ('i', 'p', '3', 'b'))


V4L2_PIX_FMT_IPU3_SGBRG10 = (v4l2_fourcc ('i', 'p', '3', 'g'))


V4L2_PIX_FMT_IPU3_SGRBG10 = (v4l2_fourcc ('i', 'p', '3', 'G'))


V4L2_PIX_FMT_IPU3_SRGGB10 = (v4l2_fourcc ('i', 'p', '3', 'r'))


V4L2_PIX_FMT_PISP_COMP1_RGGB = (v4l2_fourcc ('P', 'C', '1', 'R'))


V4L2_PIX_FMT_PISP_COMP1_GRBG = (v4l2_fourcc ('P', 'C', '1', 'G'))


V4L2_PIX_FMT_PISP_COMP1_GBRG = (v4l2_fourcc ('P', 'C', '1', 'g'))


V4L2_PIX_FMT_PISP_COMP1_BGGR = (v4l2_fourcc ('P', 'C', '1', 'B'))


V4L2_PIX_FMT_PISP_COMP1_MONO = (v4l2_fourcc ('P', 'C', '1', 'M'))


V4L2_PIX_FMT_PISP_COMP2_RGGB = (v4l2_fourcc ('P', 'C', '2', 'R'))


V4L2_PIX_FMT_PISP_COMP2_GRBG = (v4l2_fourcc ('P', 'C', '2', 'G'))


V4L2_PIX_FMT_PISP_COMP2_GBRG = (v4l2_fourcc ('P', 'C', '2', 'g'))


V4L2_PIX_FMT_PISP_COMP2_BGGR = (v4l2_fourcc ('P', 'C', '2', 'B'))


V4L2_PIX_FMT_PISP_COMP2_MONO = (v4l2_fourcc ('P', 'C', '2', 'M'))


V4L2_SDR_FMT_CU8 = (v4l2_fourcc ('C', 'U', '0', '8'))


V4L2_SDR_FMT_CU16LE = (v4l2_fourcc ('C', 'U', '1', '6'))


V4L2_SDR_FMT_CS8 = (v4l2_fourcc ('C', 'S', '0', '8'))


V4L2_SDR_FMT_CS14LE = (v4l2_fourcc ('C', 'S', '1', '4'))


V4L2_SDR_FMT_RU12LE = (v4l2_fourcc ('R', 'U', '1', '2'))


V4L2_SDR_FMT_PCU16BE = (v4l2_fourcc ('P', 'C', '1', '6'))


V4L2_SDR_FMT_PCU18BE = (v4l2_fourcc ('P', 'C', '1', '8'))


V4L2_SDR_FMT_PCU20BE = (v4l2_fourcc ('P', 'C', '2', '0'))


V4L2_TCH_FMT_DELTA_TD16 = (v4l2_fourcc ('T', 'D', '1', '6'))


V4L2_TCH_FMT_DELTA_TD08 = (v4l2_fourcc ('T', 'D', '0', '8'))


V4L2_TCH_FMT_TU16 = (v4l2_fourcc ('T', 'U', '1', '6'))


V4L2_TCH_FMT_TU08 = (v4l2_fourcc ('T', 'U', '0', '8'))


V4L2_META_FMT_VSP1_HGO = (v4l2_fourcc ('V', 'S', 'P', 'H'))


V4L2_META_FMT_VSP1_HGT = (v4l2_fourcc ('V', 'S', 'P', 'T'))


V4L2_META_FMT_UVC = (v4l2_fourcc ('U', 'V', 'C', 'H'))


V4L2_META_FMT_D4XX = (v4l2_fourcc ('D', '4', 'X', 'X'))


V4L2_META_FMT_VIVID = (v4l2_fourcc ('V', 'I', 'V', 'D'))


V4L2_META_FMT_RK_ISP1_PARAMS = (v4l2_fourcc ('R', 'K', '1', 'P'))


V4L2_META_FMT_RK_ISP1_STAT_3A = (v4l2_fourcc ('R', 'K', '1', 'S'))


V4L2_META_FMT_RPI_BE_CFG = (v4l2_fourcc ('R', 'P', 'B', 'C'))


V4L2_META_FMT_RPI_FE_CFG = (v4l2_fourcc ('R', 'P', 'F', 'C'))


V4L2_META_FMT_RPI_FE_STATS = (v4l2_fourcc ('R', 'P', 'F', 'S'))


V4L2_META_FMT_GENERIC_8 = (v4l2_fourcc ('M', 'E', 'T', '8'))


V4L2_META_FMT_GENERIC_CSI2_10 = (v4l2_fourcc ('M', 'C', '1', 'A'))


V4L2_META_FMT_GENERIC_CSI2_12 = (v4l2_fourcc ('M', 'C', '1', 'C'))


V4L2_META_FMT_GENERIC_CSI2_14 = (v4l2_fourcc ('M', 'C', '1', 'E'))


V4L2_META_FMT_GENERIC_CSI2_16 = (v4l2_fourcc ('M', 'C', '1', 'G'))


V4L2_META_FMT_GENERIC_CSI2_20 = (v4l2_fourcc ('M', 'C', '1', 'K'))


V4L2_META_FMT_GENERIC_CSI2_24 = (v4l2_fourcc ('M', 'C', '1', 'O'))


V4L2_PIX_FMT_PRIV_MAGIC = 0xfeedcafe


V4L2_PIX_FMT_FLAG_PREMUL_ALPHA = 0x00000001


V4L2_PIX_FMT_FLAG_SET_CSC = 0x00000002


V4L2_FMT_FLAG_COMPRESSED = 0x0001


V4L2_FMT_FLAG_EMULATED = 0x0002


V4L2_FMT_FLAG_CONTINUOUS_BYTESTREAM = 0x0004


V4L2_FMT_FLAG_DYN_RESOLUTION = 0x0008


V4L2_FMT_FLAG_ENC_CAP_FRAME_INTERVAL = 0x0010


V4L2_FMT_FLAG_CSC_COLORSPACE = 0x0020


V4L2_FMT_FLAG_CSC_XFER_FUNC = 0x0040


V4L2_FMT_FLAG_CSC_YCBCR_ENC = 0x0080


V4L2_FMT_FLAG_CSC_HSV_ENC = V4L2_FMT_FLAG_CSC_YCBCR_ENC


V4L2_FMT_FLAG_CSC_QUANTIZATION = 0x0100


V4L2_FMT_FLAG_META_LINE_BASED = 0x0200


V4L2_TC_TYPE_24FPS = 1


V4L2_TC_TYPE_25FPS = 2


V4L2_TC_TYPE_30FPS = 3


V4L2_TC_TYPE_50FPS = 4


V4L2_TC_TYPE_60FPS = 5


V4L2_TC_FLAG_DROPFRAME = 0x0001


V4L2_TC_FLAG_COLORFRAME = 0x0002


V4L2_TC_USERBITS_field = 0x000C


V4L2_TC_USERBITS_USERDEFINED = 0x0000


V4L2_TC_USERBITS_8BITCHARS = 0x0008


V4L2_JPEG_MARKER_DHT = (1 << 3)


V4L2_JPEG_MARKER_DQT = (1 << 4)


V4L2_JPEG_MARKER_DRI = (1 << 5)


V4L2_JPEG_MARKER_COM = (1 << 6)


V4L2_JPEG_MARKER_APP = (1 << 7)


V4L2_MEMORY_FLAG_NON_COHERENT = (1 << 0)


V4L2_BUF_CAP_SUPPORTS_MMAP = (1 << 0)


V4L2_BUF_CAP_SUPPORTS_USERPTR = (1 << 1)


V4L2_BUF_CAP_SUPPORTS_DMABUF = (1 << 2)


V4L2_BUF_CAP_SUPPORTS_REQUESTS = (1 << 3)


V4L2_BUF_CAP_SUPPORTS_ORPHANED_BUFS = (1 << 4)


V4L2_BUF_CAP_SUPPORTS_M2M_HOLD_CAPTURE_BUF = (1 << 5)


V4L2_BUF_CAP_SUPPORTS_MMAP_CACHE_HINTS = (1 << 6)


V4L2_BUF_CAP_SUPPORTS_MAX_NUM_BUFFERS = (1 << 7)


V4L2_BUF_CAP_SUPPORTS_REMOVE_BUFS = (1 << 8)


V4L2_BUF_FLAG_MAPPED = 0x00000001


V4L2_BUF_FLAG_QUEUED = 0x00000002


V4L2_BUF_FLAG_DONE = 0x00000004


V4L2_BUF_FLAG_KEYFRAME = 0x00000008


V4L2_BUF_FLAG_PFRAME = 0x00000010


V4L2_BUF_FLAG_BFRAME = 0x00000020


V4L2_BUF_FLAG_ERROR = 0x00000040


V4L2_BUF_FLAG_IN_REQUEST = 0x00000080


V4L2_BUF_FLAG_TIMECODE = 0x00000100


V4L2_BUF_FLAG_M2M_HOLD_CAPTURE_BUF = 0x00000200


V4L2_BUF_FLAG_PREPARED = 0x00000400


V4L2_BUF_FLAG_NO_CACHE_INVALIDATE = 0x00000800


V4L2_BUF_FLAG_NO_CACHE_CLEAN = 0x00001000


V4L2_BUF_FLAG_TIMESTAMP_MASK = 0x0000e000


V4L2_BUF_FLAG_TIMESTAMP_UNKNOWN = 0x00000000


V4L2_BUF_FLAG_TIMESTAMP_MONOTONIC = 0x00002000


V4L2_BUF_FLAG_TIMESTAMP_COPY = 0x00004000


V4L2_BUF_FLAG_TSTAMP_SRC_MASK = 0x00070000


V4L2_BUF_FLAG_TSTAMP_SRC_EOF = 0x00000000


V4L2_BUF_FLAG_TSTAMP_SRC_SOE = 0x00010000


V4L2_BUF_FLAG_LAST = 0x00100000


V4L2_BUF_FLAG_REQUEST_FD = 0x00800000


V4L2_FBUF_CAP_EXTERNOVERLAY = 0x0001


V4L2_FBUF_CAP_CHROMAKEY = 0x0002


V4L2_FBUF_CAP_LIST_CLIPPING = 0x0004


V4L2_FBUF_CAP_BITMAP_CLIPPING = 0x0008


V4L2_FBUF_CAP_LOCAL_ALPHA = 0x0010


V4L2_FBUF_CAP_GLOBAL_ALPHA = 0x0020


V4L2_FBUF_CAP_LOCAL_INV_ALPHA = 0x0040


V4L2_FBUF_CAP_SRC_CHROMAKEY = 0x0080


V4L2_FBUF_FLAG_PRIMARY = 0x0001


V4L2_FBUF_FLAG_OVERLAY = 0x0002


V4L2_FBUF_FLAG_CHROMAKEY = 0x0004


V4L2_FBUF_FLAG_LOCAL_ALPHA = 0x0008


V4L2_FBUF_FLAG_GLOBAL_ALPHA = 0x0010


V4L2_FBUF_FLAG_LOCAL_INV_ALPHA = 0x0020


V4L2_FBUF_FLAG_SRC_CHROMAKEY = 0x0040


V4L2_MODE_HIGHQUALITY = 0x0001


V4L2_CAP_TIMEPERFRAME = 0x1000


V4L2_STD_PAL_B = (v4l2_std_id (ord_if_char(0x00000001))).value


V4L2_STD_PAL_B1 = (v4l2_std_id (ord_if_char(0x00000002))).value


V4L2_STD_PAL_G = (v4l2_std_id (ord_if_char(0x00000004))).value


V4L2_STD_PAL_H = (v4l2_std_id (ord_if_char(0x00000008))).value


V4L2_STD_PAL_I = (v4l2_std_id (ord_if_char(0x00000010))).value


V4L2_STD_PAL_D = (v4l2_std_id (ord_if_char(0x00000020))).value


V4L2_STD_PAL_D1 = (v4l2_std_id (ord_if_char(0x00000040))).value


V4L2_STD_PAL_K = (v4l2_std_id (ord_if_char(0x00000080))).value


V4L2_STD_PAL_M = (v4l2_std_id (ord_if_char(0x00000100))).value


V4L2_STD_PAL_N = (v4l2_std_id (ord_if_char(0x00000200))).value


V4L2_STD_PAL_Nc = (v4l2_std_id (ord_if_char(0x00000400))).value


V4L2_STD_PAL_60 = (v4l2_std_id (ord_if_char(0x00000800))).value


V4L2_STD_NTSC_M = (v4l2_std_id (ord_if_char(0x00001000))).value


V4L2_STD_NTSC_M_JP = (v4l2_std_id (ord_if_char(0x00002000))).value


V4L2_STD_NTSC_443 = (v4l2_std_id (ord_if_char(0x00004000))).value


V4L2_STD_NTSC_M_KR = (v4l2_std_id (ord_if_char(0x00008000))).value


V4L2_STD_SECAM_B = (v4l2_std_id (ord_if_char(0x00010000))).value


V4L2_STD_SECAM_D = (v4l2_std_id (ord_if_char(0x00020000))).value


V4L2_STD_SECAM_G = (v4l2_std_id (ord_if_char(0x00040000))).value


V4L2_STD_SECAM_H = (v4l2_std_id (ord_if_char(0x00080000))).value


V4L2_STD_SECAM_K = (v4l2_std_id (ord_if_char(0x00100000))).value


V4L2_STD_SECAM_K1 = (v4l2_std_id (ord_if_char(0x00200000))).value


V4L2_STD_SECAM_L = (v4l2_std_id (ord_if_char(0x00400000))).value


V4L2_STD_SECAM_LC = (v4l2_std_id (ord_if_char(0x00800000))).value


V4L2_STD_ATSC_8_VSB = (v4l2_std_id (ord_if_char(0x01000000))).value


V4L2_STD_ATSC_16_VSB = (v4l2_std_id (ord_if_char(0x02000000))).value


V4L2_STD_NTSC = ((V4L2_STD_NTSC_M | V4L2_STD_NTSC_M_JP) | V4L2_STD_NTSC_M_KR)


V4L2_STD_SECAM_DK = ((V4L2_STD_SECAM_D | V4L2_STD_SECAM_K) | V4L2_STD_SECAM_K1)


V4L2_STD_SECAM = (((((V4L2_STD_SECAM_B | V4L2_STD_SECAM_G) | V4L2_STD_SECAM_H) | V4L2_STD_SECAM_DK) | V4L2_STD_SECAM_L) | V4L2_STD_SECAM_LC)


V4L2_STD_PAL_BG = ((V4L2_STD_PAL_B | V4L2_STD_PAL_B1) | V4L2_STD_PAL_G)


V4L2_STD_PAL_DK = ((V4L2_STD_PAL_D | V4L2_STD_PAL_D1) | V4L2_STD_PAL_K)


V4L2_STD_PAL = (((V4L2_STD_PAL_BG | V4L2_STD_PAL_DK) | V4L2_STD_PAL_H) | V4L2_STD_PAL_I)


V4L2_STD_B = ((V4L2_STD_PAL_B | V4L2_STD_PAL_B1) | V4L2_STD_SECAM_B)


V4L2_STD_G = (V4L2_STD_PAL_G | V4L2_STD_SECAM_G)


V4L2_STD_H = (V4L2_STD_PAL_H | V4L2_STD_SECAM_H)


V4L2_STD_L = (V4L2_STD_SECAM_L | V4L2_STD_SECAM_LC)


V4L2_STD_GH = (V4L2_STD_G | V4L2_STD_H)


V4L2_STD_DK = (V4L2_STD_PAL_DK | V4L2_STD_SECAM_DK)


V4L2_STD_BG = (V4L2_STD_B | V4L2_STD_G)


V4L2_STD_MN = (((V4L2_STD_PAL_M | V4L2_STD_PAL_N) | V4L2_STD_PAL_Nc) | V4L2_STD_NTSC)


V4L2_STD_MTS = (((V4L2_STD_NTSC_M | V4L2_STD_PAL_M) | V4L2_STD_PAL_N) | V4L2_STD_PAL_Nc)


V4L2_STD_525_60 = (((V4L2_STD_PAL_M | V4L2_STD_PAL_60) | V4L2_STD_NTSC) | V4L2_STD_NTSC_443)


V4L2_STD_625_50 = (((V4L2_STD_PAL | V4L2_STD_PAL_N) | V4L2_STD_PAL_Nc) | V4L2_STD_SECAM)


V4L2_STD_ATSC = (V4L2_STD_ATSC_8_VSB | V4L2_STD_ATSC_16_VSB)


V4L2_STD_UNKNOWN = 0


V4L2_STD_ALL = (V4L2_STD_525_60 | V4L2_STD_625_50)


V4L2_DV_PROGRESSIVE = 0


V4L2_DV_INTERLACED = 1


V4L2_DV_VSYNC_POS_POL = 0x00000001


V4L2_DV_HSYNC_POS_POL = 0x00000002


V4L2_DV_BT_STD_CEA861 = (1 << 0)


V4L2_DV_BT_STD_DMT = (1 << 1)


V4L2_DV_BT_STD_CVT = (1 << 2)


V4L2_DV_BT_STD_GTF = (1 << 3)


V4L2_DV_BT_STD_SDI = (1 << 4)


V4L2_DV_FL_REDUCED_BLANKING = (1 << 0)


V4L2_DV_FL_CAN_REDUCE_FPS = (1 << 1)


V4L2_DV_FL_REDUCED_FPS = (1 << 2)


V4L2_DV_FL_HALF_LINE = (1 << 3)


V4L2_DV_FL_IS_CE_VIDEO = (1 << 4)


V4L2_DV_FL_FIRST_FIELD_EXTRA_LINE = (1 << 5)


V4L2_DV_FL_HAS_PICTURE_ASPECT = (1 << 6)


V4L2_DV_FL_HAS_CEA861_VIC = (1 << 7)


V4L2_DV_FL_HAS_HDMI_VIC = (1 << 8)


V4L2_DV_FL_CAN_DETECT_REDUCED_FPS = (1 << 9)


def V4L2_DV_BT_BLANKING_WIDTH(bt):
    return ((((bt.contents.hfrontporch).value) + ((bt.contents.hsync).value)) + ((bt.contents.hbackporch).value))


def V4L2_DV_BT_FRAME_WIDTH(bt):
    return (((bt.contents.width).value) + (V4L2_DV_BT_BLANKING_WIDTH (bt)))


def V4L2_DV_BT_BLANKING_HEIGHT(bt):
    return (((((bt.contents.vfrontporch).value) + ((bt.contents.vsync).value)) + ((bt.contents.vbackporch).value)) + (bt.contents.interlaced) and ((((bt.contents.il_vfrontporch).value) + ((bt.contents.il_vsync).value)) + ((bt.contents.il_vbackporch).value)) or 0)


def V4L2_DV_BT_FRAME_HEIGHT(bt):
    return (((bt.contents.height).value) + (V4L2_DV_BT_BLANKING_HEIGHT (bt)))


V4L2_DV_BT_656_1120 = 0


V4L2_DV_BT_CAP_INTERLACED = (1 << 0)


V4L2_DV_BT_CAP_PROGRESSIVE = (1 << 1)


V4L2_DV_BT_CAP_REDUCED_BLANKING = (1 << 2)


V4L2_DV_BT_CAP_CUSTOM = (1 << 3)


V4L2_INPUT_TYPE_TUNER = 1


V4L2_INPUT_TYPE_CAMERA = 2


V4L2_INPUT_TYPE_TOUCH = 3


V4L2_IN_ST_NO_POWER = 0x00000001


V4L2_IN_ST_NO_SIGNAL = 0x00000002


V4L2_IN_ST_NO_COLOR = 0x00000004


V4L2_IN_ST_HFLIP = 0x00000010


V4L2_IN_ST_VFLIP = 0x00000020


V4L2_IN_ST_NO_H_LOCK = 0x00000100


V4L2_IN_ST_COLOR_KILL = 0x00000200


V4L2_IN_ST_NO_V_LOCK = 0x00000400


V4L2_IN_ST_NO_STD_LOCK = 0x00000800


V4L2_IN_ST_NO_SYNC = 0x00010000


V4L2_IN_ST_NO_EQU = 0x00020000


V4L2_IN_ST_NO_CARRIER = 0x00040000


V4L2_IN_ST_MACROVISION = 0x01000000


V4L2_IN_ST_NO_ACCESS = 0x02000000


V4L2_IN_ST_VTR = 0x04000000


V4L2_IN_CAP_DV_TIMINGS = 0x00000002


V4L2_IN_CAP_CUSTOM_TIMINGS = V4L2_IN_CAP_DV_TIMINGS


V4L2_IN_CAP_STD = 0x00000004


V4L2_IN_CAP_NATIVE_SIZE = 0x00000008


V4L2_OUTPUT_TYPE_MODULATOR = 1


V4L2_OUTPUT_TYPE_ANALOG = 2


V4L2_OUTPUT_TYPE_ANALOGVGAOVERLAY = 3


V4L2_OUT_CAP_DV_TIMINGS = 0x00000002


V4L2_OUT_CAP_CUSTOM_TIMINGS = V4L2_OUT_CAP_DV_TIMINGS


V4L2_OUT_CAP_STD = 0x00000004


V4L2_OUT_CAP_NATIVE_SIZE = 0x00000008


V4L2_CTRL_ID_MASK = 0x0fffffff


def V4L2_CTRL_ID2CLASS(id):
    return (id & 0x0fff0000)


def V4L2_CTRL_ID2WHICH(id):
    return (id & 0x0fff0000)


def V4L2_CTRL_DRIVER_PRIV(id):
    return ((id & 0xffff) >= 0x1000)


V4L2_CTRL_MAX_DIMS = 4


V4L2_CTRL_WHICH_CUR_VAL = 0


V4L2_CTRL_WHICH_DEF_VAL = 0x0f000000


V4L2_CTRL_WHICH_REQUEST_VAL = 0x0f010000


V4L2_CTRL_FLAG_DISABLED = 0x0001


V4L2_CTRL_FLAG_GRABBED = 0x0002


V4L2_CTRL_FLAG_READ_ONLY = 0x0004


V4L2_CTRL_FLAG_UPDATE = 0x0008


V4L2_CTRL_FLAG_INACTIVE = 0x0010


V4L2_CTRL_FLAG_SLIDER = 0x0020


V4L2_CTRL_FLAG_WRITE_ONLY = 0x0040


V4L2_CTRL_FLAG_VOLATILE = 0x0080


V4L2_CTRL_FLAG_HAS_PAYLOAD = 0x0100


V4L2_CTRL_FLAG_EXECUTE_ON_WRITE = 0x0200


V4L2_CTRL_FLAG_MODIFY_LAYOUT = 0x0400


V4L2_CTRL_FLAG_DYNAMIC_ARRAY = 0x0800


V4L2_CTRL_FLAG_NEXT_CTRL = 0x80000000


V4L2_CTRL_FLAG_NEXT_COMPOUND = 0x40000000


V4L2_CID_MAX_CTRLS = 1024


V4L2_CID_PRIVATE_BASE = 0x08000000


V4L2_TUNER_CAP_LOW = 0x0001


V4L2_TUNER_CAP_NORM = 0x0002


V4L2_TUNER_CAP_HWSEEK_BOUNDED = 0x0004


V4L2_TUNER_CAP_HWSEEK_WRAP = 0x0008


V4L2_TUNER_CAP_STEREO = 0x0010


V4L2_TUNER_CAP_LANG2 = 0x0020


V4L2_TUNER_CAP_SAP = 0x0020


V4L2_TUNER_CAP_LANG1 = 0x0040


V4L2_TUNER_CAP_RDS = 0x0080


V4L2_TUNER_CAP_RDS_BLOCK_IO = 0x0100


V4L2_TUNER_CAP_RDS_CONTROLS = 0x0200


V4L2_TUNER_CAP_FREQ_BANDS = 0x0400


V4L2_TUNER_CAP_HWSEEK_PROG_LIM = 0x0800


V4L2_TUNER_CAP_1HZ = 0x1000


V4L2_TUNER_SUB_MONO = 0x0001


V4L2_TUNER_SUB_STEREO = 0x0002


V4L2_TUNER_SUB_LANG2 = 0x0004


V4L2_TUNER_SUB_SAP = 0x0004


V4L2_TUNER_SUB_LANG1 = 0x0008


V4L2_TUNER_SUB_RDS = 0x0010


V4L2_TUNER_MODE_MONO = 0x0000


V4L2_TUNER_MODE_STEREO = 0x0001


V4L2_TUNER_MODE_LANG2 = 0x0002


V4L2_TUNER_MODE_SAP = 0x0002


V4L2_TUNER_MODE_LANG1 = 0x0003


V4L2_TUNER_MODE_LANG1_LANG2 = 0x0004


V4L2_BAND_MODULATION_VSB = (1 << 1)


V4L2_BAND_MODULATION_FM = (1 << 2)


V4L2_BAND_MODULATION_AM = (1 << 3)


V4L2_RDS_BLOCK_MSK = 0x7


V4L2_RDS_BLOCK_A = 0


V4L2_RDS_BLOCK_B = 1


V4L2_RDS_BLOCK_C = 2


V4L2_RDS_BLOCK_D = 3


V4L2_RDS_BLOCK_C_ALT = 4


V4L2_RDS_BLOCK_INVALID = 7


V4L2_RDS_BLOCK_CORRECTED = 0x40


V4L2_RDS_BLOCK_ERROR = 0x80


V4L2_AUDCAP_STEREO = 0x00001


V4L2_AUDCAP_AVL = 0x00002


V4L2_AUDMODE_AVL = 0x00001


V4L2_ENC_IDX_FRAME_I = 0


V4L2_ENC_IDX_FRAME_P = 1


V4L2_ENC_IDX_FRAME_B = 2


V4L2_ENC_IDX_FRAME_MASK = 0xf


V4L2_ENC_IDX_ENTRIES = 64


V4L2_ENC_CMD_START = 0


V4L2_ENC_CMD_STOP = 1


V4L2_ENC_CMD_PAUSE = 2


V4L2_ENC_CMD_RESUME = 3


V4L2_ENC_CMD_STOP_AT_GOP_END = (1 << 0)


V4L2_DEC_CMD_START = 0


V4L2_DEC_CMD_STOP = 1


V4L2_DEC_CMD_PAUSE = 2


V4L2_DEC_CMD_RESUME = 3


V4L2_DEC_CMD_FLUSH = 4


V4L2_DEC_CMD_START_MUTE_AUDIO = (1 << 0)


V4L2_DEC_CMD_PAUSE_TO_BLACK = (1 << 0)


V4L2_DEC_CMD_STOP_TO_BLACK = (1 << 0)


V4L2_DEC_CMD_STOP_IMMEDIATELY = (1 << 1)


V4L2_DEC_START_FMT_NONE = 0


V4L2_DEC_START_FMT_GOP = 1


V4L2_VBI_UNSYNC = (1 << 0)


V4L2_VBI_INTERLACED = (1 << 1)


V4L2_VBI_ITU_525_F1_START = 1


V4L2_VBI_ITU_525_F2_START = 264


V4L2_VBI_ITU_625_F1_START = 1


V4L2_VBI_ITU_625_F2_START = 314


V4L2_SLICED_TELETEXT_B = 0x0001


V4L2_SLICED_VPS = 0x0400


V4L2_SLICED_CAPTION_525 = 0x1000


V4L2_SLICED_WSS_625 = 0x4000


V4L2_SLICED_VBI_525 = V4L2_SLICED_CAPTION_525


V4L2_SLICED_VBI_625 = ((V4L2_SLICED_TELETEXT_B | V4L2_SLICED_VPS) | V4L2_SLICED_WSS_625)


V4L2_MPEG_VBI_IVTV_TELETEXT_B = 1


V4L2_MPEG_VBI_IVTV_CAPTION_525 = 4


V4L2_MPEG_VBI_IVTV_WSS_625 = 5


V4L2_MPEG_VBI_IVTV_VPS = 7


V4L2_MPEG_VBI_IVTV_MAGIC0 = 'itv0'


V4L2_MPEG_VBI_IVTV_MAGIC1 = 'ITV0'


V4L2_EVENT_ALL = 0


V4L2_EVENT_VSYNC = 1


V4L2_EVENT_EOS = 2


V4L2_EVENT_CTRL = 3


V4L2_EVENT_FRAME_SYNC = 4


V4L2_EVENT_SOURCE_CHANGE = 5


V4L2_EVENT_MOTION_DET = 6


V4L2_EVENT_PRIVATE_START = 0x08000000


V4L2_EVENT_CTRL_CH_VALUE = (1 << 0)


V4L2_EVENT_CTRL_CH_FLAGS = (1 << 1)


V4L2_EVENT_CTRL_CH_RANGE = (1 << 2)


V4L2_EVENT_CTRL_CH_DIMENSIONS = (1 << 3)


V4L2_EVENT_SRC_CH_RESOLUTION = (1 << 0)


V4L2_EVENT_MD_FL_HAVE_FRAME_SEQ = (1 << 0)


V4L2_EVENT_SUB_FL_SEND_INITIAL = (1 << 0)


V4L2_EVENT_SUB_FL_ALLOW_FEEDBACK = (1 << 1)


V4L2_CHIP_MATCH_BRIDGE = 0


V4L2_CHIP_MATCH_SUBDEV = 4


V4L2_CHIP_MATCH_HOST = V4L2_CHIP_MATCH_BRIDGE


V4L2_CHIP_MATCH_I2C_DRIVER = 1


V4L2_CHIP_MATCH_I2C_ADDR = 2


V4L2_CHIP_MATCH_AC97 = 3


V4L2_CHIP_FL_READABLE = (1 << 0)


V4L2_CHIP_FL_WRITABLE = (1 << 1)


VIDIOC_QUERYCAP = (_IOR ('V', 0, struct_v4l2_capability))


VIDIOC_ENUM_FMT = (_IOWR ('V', 2, struct_v4l2_fmtdesc))


VIDIOC_G_FMT = (_IOWR ('V', 4, struct_v4l2_format))


VIDIOC_S_FMT = (_IOWR ('V', 5, struct_v4l2_format))


VIDIOC_REQBUFS = (_IOWR ('V', 8, struct_v4l2_requestbuffers))


VIDIOC_QUERYBUF = (_IOWR ('V', 9, struct_v4l2_buffer))


VIDIOC_G_FBUF = (_IOR ('V', 10, struct_v4l2_framebuffer))


VIDIOC_S_FBUF = (_IOW ('V', 11, struct_v4l2_framebuffer))


VIDIOC_OVERLAY = (_IOW ('V', 14, c_int))


VIDIOC_QBUF = (_IOWR ('V', 15, struct_v4l2_buffer))


VIDIOC_EXPBUF = (_IOWR ('V', 16, struct_v4l2_exportbuffer))


VIDIOC_DQBUF = (_IOWR ('V', 17, struct_v4l2_buffer))


VIDIOC_STREAMON = (_IOW ('V', 18, c_int))


VIDIOC_STREAMOFF = (_IOW ('V', 19, c_int))


VIDIOC_G_PARM = (_IOWR ('V', 21, struct_v4l2_streamparm))


VIDIOC_S_PARM = (_IOWR ('V', 22, struct_v4l2_streamparm))


VIDIOC_G_STD = (_IOR ('V', 23, v4l2_std_id))


VIDIOC_S_STD = (_IOW ('V', 24, v4l2_std_id))


VIDIOC_ENUMSTD = (_IOWR ('V', 25, struct_v4l2_standard))


VIDIOC_ENUMINPUT = (_IOWR ('V', 26, struct_v4l2_input))


VIDIOC_G_CTRL = (_IOWR ('V', 27, struct_v4l2_control))


VIDIOC_S_CTRL = (_IOWR ('V', 28, struct_v4l2_control))


VIDIOC_G_TUNER = (_IOWR ('V', 29, struct_v4l2_tuner))


VIDIOC_S_TUNER = (_IOW ('V', 30, struct_v4l2_tuner))


VIDIOC_G_AUDIO = (_IOR ('V', 33, struct_v4l2_audio))


VIDIOC_S_AUDIO = (_IOW ('V', 34, struct_v4l2_audio))


VIDIOC_QUERYCTRL = (_IOWR ('V', 36, struct_v4l2_queryctrl))


VIDIOC_QUERYMENU = (_IOWR ('V', 37, struct_v4l2_querymenu))


VIDIOC_G_INPUT = (_IOR ('V', 38, c_int))


VIDIOC_S_INPUT = (_IOWR ('V', 39, c_int))


VIDIOC_G_EDID = (_IOWR ('V', 40, struct_v4l2_edid))


VIDIOC_S_EDID = (_IOWR ('V', 41, struct_v4l2_edid))


VIDIOC_G_OUTPUT = (_IOR ('V', 46, c_int))


VIDIOC_S_OUTPUT = (_IOWR ('V', 47, c_int))


VIDIOC_ENUMOUTPUT = (_IOWR ('V', 48, struct_v4l2_output))


VIDIOC_G_AUDOUT = (_IOR ('V', 49, struct_v4l2_audioout))


VIDIOC_S_AUDOUT = (_IOW ('V', 50, struct_v4l2_audioout))


VIDIOC_G_MODULATOR = (_IOWR ('V', 54, struct_v4l2_modulator))


VIDIOC_S_MODULATOR = (_IOW ('V', 55, struct_v4l2_modulator))


VIDIOC_G_FREQUENCY = (_IOWR ('V', 56, struct_v4l2_frequency))


VIDIOC_S_FREQUENCY = (_IOW ('V', 57, struct_v4l2_frequency))


VIDIOC_CROPCAP = (_IOWR ('V', 58, struct_v4l2_cropcap))


VIDIOC_G_CROP = (_IOWR ('V', 59, struct_v4l2_crop))


VIDIOC_S_CROP = (_IOW ('V', 60, struct_v4l2_crop))


VIDIOC_G_JPEGCOMP = (_IOR ('V', 61, struct_v4l2_jpegcompression))


VIDIOC_S_JPEGCOMP = (_IOW ('V', 62, struct_v4l2_jpegcompression))


VIDIOC_QUERYSTD = (_IOR ('V', 63, v4l2_std_id))


VIDIOC_TRY_FMT = (_IOWR ('V', 64, struct_v4l2_format))


VIDIOC_ENUMAUDIO = (_IOWR ('V', 65, struct_v4l2_audio))


VIDIOC_ENUMAUDOUT = (_IOWR ('V', 66, struct_v4l2_audioout))


VIDIOC_G_PRIORITY = (_IOR ('V', 67, __u32))


VIDIOC_S_PRIORITY = (_IOW ('V', 68, __u32))


VIDIOC_G_SLICED_VBI_CAP = (_IOWR ('V', 69, struct_v4l2_sliced_vbi_cap))


VIDIOC_LOG_STATUS = (_IO ('V', 70))


VIDIOC_G_EXT_CTRLS = (_IOWR ('V', 71, struct_v4l2_ext_controls))


VIDIOC_S_EXT_CTRLS = (_IOWR ('V', 72, struct_v4l2_ext_controls))


VIDIOC_TRY_EXT_CTRLS = (_IOWR ('V', 73, struct_v4l2_ext_controls))


VIDIOC_ENUM_FRAMESIZES = (_IOWR ('V', 74, struct_v4l2_frmsizeenum))


VIDIOC_ENUM_FRAMEINTERVALS = (_IOWR ('V', 75, struct_v4l2_frmivalenum))


VIDIOC_G_ENC_INDEX = (_IOR ('V', 76, struct_v4l2_enc_idx))


VIDIOC_ENCODER_CMD = (_IOWR ('V', 77, struct_v4l2_encoder_cmd))


VIDIOC_TRY_ENCODER_CMD = (_IOWR ('V', 78, struct_v4l2_encoder_cmd))


VIDIOC_DBG_S_REGISTER = (_IOW ('V', 79, struct_v4l2_dbg_register))


VIDIOC_DBG_G_REGISTER = (_IOWR ('V', 80, struct_v4l2_dbg_register))


VIDIOC_S_HW_FREQ_SEEK = (_IOW ('V', 82, struct_v4l2_hw_freq_seek))


VIDIOC_S_DV_TIMINGS = (_IOWR ('V', 87, struct_v4l2_dv_timings))


VIDIOC_G_DV_TIMINGS = (_IOWR ('V', 88, struct_v4l2_dv_timings))


VIDIOC_DQEVENT = (_IOR ('V', 89, struct_v4l2_event))


VIDIOC_SUBSCRIBE_EVENT = (_IOW ('V', 90, struct_v4l2_event_subscription))


VIDIOC_UNSUBSCRIBE_EVENT = (_IOW ('V', 91, struct_v4l2_event_subscription))


VIDIOC_CREATE_BUFS = (_IOWR ('V', 92, struct_v4l2_create_buffers))


VIDIOC_PREPARE_BUF = (_IOWR ('V', 93, struct_v4l2_buffer))


VIDIOC_G_SELECTION = (_IOWR ('V', 94, struct_v4l2_selection))


VIDIOC_S_SELECTION = (_IOWR ('V', 95, struct_v4l2_selection))


VIDIOC_DECODER_CMD = (_IOWR ('V', 96, struct_v4l2_decoder_cmd))


VIDIOC_TRY_DECODER_CMD = (_IOWR ('V', 97, struct_v4l2_decoder_cmd))


VIDIOC_ENUM_DV_TIMINGS = (_IOWR ('V', 98, struct_v4l2_enum_dv_timings))


VIDIOC_QUERY_DV_TIMINGS = (_IOR ('V', 99, struct_v4l2_dv_timings))


VIDIOC_DV_TIMINGS_CAP = (_IOWR ('V', 100, struct_v4l2_dv_timings_cap))


VIDIOC_ENUM_FREQ_BANDS = (_IOWR ('V', 101, struct_v4l2_frequency_band))


VIDIOC_DBG_G_CHIP_INFO = (_IOWR ('V', 102, struct_v4l2_dbg_chip_info))


VIDIOC_QUERY_EXT_CTRL = (_IOWR ('V', 103, struct_v4l2_query_ext_ctrl))


VIDIOC_REMOVE_BUFS = (_IOWR ('V', 104, struct_v4l2_remove_buffers))


BASE_VIDIOC_PRIVATE = 192


V4L2_PIX_FMT_HM12 = V4L2_PIX_FMT_NV12_16L16


V4L2_PIX_FMT_SUNXI_TILED_NV12 = V4L2_PIX_FMT_NV12_32L32


V4L2_CAP_ASYNCIO = 0x02000000


MEDIA_ENT_F_BASE = 0x00000000


MEDIA_ENT_F_OLD_BASE = 0x00010000


MEDIA_ENT_F_OLD_SUBDEV_BASE = 0x00020000


MEDIA_ENT_F_UNKNOWN = MEDIA_ENT_F_BASE


MEDIA_ENT_F_V4L2_SUBDEV_UNKNOWN = MEDIA_ENT_F_OLD_SUBDEV_BASE


MEDIA_ENT_F_DTV_DEMOD = (MEDIA_ENT_F_BASE + 0x00001)


MEDIA_ENT_F_TS_DEMUX = (MEDIA_ENT_F_BASE + 0x00002)


MEDIA_ENT_F_DTV_CA = (MEDIA_ENT_F_BASE + 0x00003)


MEDIA_ENT_F_DTV_NET_DECAP = (MEDIA_ENT_F_BASE + 0x00004)


MEDIA_ENT_F_IO_V4L = (MEDIA_ENT_F_OLD_BASE + 1)


MEDIA_ENT_F_IO_DTV = (MEDIA_ENT_F_BASE + 0x01001)


MEDIA_ENT_F_IO_VBI = (MEDIA_ENT_F_BASE + 0x01002)


MEDIA_ENT_F_IO_SWRADIO = (MEDIA_ENT_F_BASE + 0x01003)


MEDIA_ENT_F_CAM_SENSOR = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 1)


MEDIA_ENT_F_FLASH = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 2)


MEDIA_ENT_F_LENS = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 3)


MEDIA_ENT_F_TUNER = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 5)


MEDIA_ENT_F_IF_VID_DECODER = (MEDIA_ENT_F_BASE + 0x02001)


MEDIA_ENT_F_IF_AUD_DECODER = (MEDIA_ENT_F_BASE + 0x02002)


MEDIA_ENT_F_AUDIO_CAPTURE = (MEDIA_ENT_F_BASE + 0x03001)


MEDIA_ENT_F_AUDIO_PLAYBACK = (MEDIA_ENT_F_BASE + 0x03002)


MEDIA_ENT_F_AUDIO_MIXER = (MEDIA_ENT_F_BASE + 0x03003)


MEDIA_ENT_F_PROC_VIDEO_COMPOSER = (MEDIA_ENT_F_BASE + 0x4001)


MEDIA_ENT_F_PROC_VIDEO_PIXEL_FORMATTER = (MEDIA_ENT_F_BASE + 0x4002)


MEDIA_ENT_F_PROC_VIDEO_PIXEL_ENC_CONV = (MEDIA_ENT_F_BASE + 0x4003)


MEDIA_ENT_F_PROC_VIDEO_LUT = (MEDIA_ENT_F_BASE + 0x4004)


MEDIA_ENT_F_PROC_VIDEO_SCALER = (MEDIA_ENT_F_BASE + 0x4005)


MEDIA_ENT_F_PROC_VIDEO_STATISTICS = (MEDIA_ENT_F_BASE + 0x4006)


MEDIA_ENT_F_PROC_VIDEO_ENCODER = (MEDIA_ENT_F_BASE + 0x4007)


MEDIA_ENT_F_PROC_VIDEO_DECODER = (MEDIA_ENT_F_BASE + 0x4008)


MEDIA_ENT_F_PROC_VIDEO_ISP = (MEDIA_ENT_F_BASE + 0x4009)


MEDIA_ENT_F_VID_MUX = (MEDIA_ENT_F_BASE + 0x5001)


MEDIA_ENT_F_VID_IF_BRIDGE = (MEDIA_ENT_F_BASE + 0x5002)


MEDIA_ENT_F_ATV_DECODER = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 4)


MEDIA_ENT_F_DV_DECODER = (MEDIA_ENT_F_BASE + 0x6001)


MEDIA_ENT_F_DV_ENCODER = (MEDIA_ENT_F_BASE + 0x6002)


MEDIA_ENT_FL_DEFAULT = (1 << 0)


MEDIA_ENT_FL_CONNECTOR = (1 << 1)


MEDIA_ENT_ID_FLAG_NEXT = (1 << 31)


MEDIA_PAD_FL_SINK = (1 << 0)


MEDIA_PAD_FL_SOURCE = (1 << 1)


MEDIA_PAD_FL_MUST_CONNECT = (1 << 2)


MEDIA_PAD_FL_INTERNAL = (1 << 3)


MEDIA_LNK_FL_ENABLED = (1 << 0)


MEDIA_LNK_FL_IMMUTABLE = (1 << 1)


MEDIA_LNK_FL_DYNAMIC = (1 << 2)


MEDIA_LNK_FL_LINK_TYPE = (0xf << 28)


MEDIA_LNK_FL_DATA_LINK = (0 << 28)


MEDIA_LNK_FL_INTERFACE_LINK = (1 << 28)


MEDIA_LNK_FL_ANCILLARY_LINK = (2 << 28)


MEDIA_INTF_T_DVB_BASE = 0x00000100


MEDIA_INTF_T_V4L_BASE = 0x00000200


MEDIA_INTF_T_DVB_FE = MEDIA_INTF_T_DVB_BASE


MEDIA_INTF_T_DVB_DEMUX = (MEDIA_INTF_T_DVB_BASE + 1)


MEDIA_INTF_T_DVB_DVR = (MEDIA_INTF_T_DVB_BASE + 2)


MEDIA_INTF_T_DVB_CA = (MEDIA_INTF_T_DVB_BASE + 3)


MEDIA_INTF_T_DVB_NET = (MEDIA_INTF_T_DVB_BASE + 4)


MEDIA_INTF_T_V4L_VIDEO = MEDIA_INTF_T_V4L_BASE


MEDIA_INTF_T_V4L_VBI = (MEDIA_INTF_T_V4L_BASE + 1)


MEDIA_INTF_T_V4L_RADIO = (MEDIA_INTF_T_V4L_BASE + 2)


MEDIA_INTF_T_V4L_SUBDEV = (MEDIA_INTF_T_V4L_BASE + 3)


MEDIA_INTF_T_V4L_SWRADIO = (MEDIA_INTF_T_V4L_BASE + 4)


MEDIA_INTF_T_V4L_TOUCH = (MEDIA_INTF_T_V4L_BASE + 5)


MEDIA_INTF_T_ALSA_BASE = 0x00000300


MEDIA_INTF_T_ALSA_PCM_CAPTURE = MEDIA_INTF_T_ALSA_BASE


MEDIA_INTF_T_ALSA_PCM_PLAYBACK = (MEDIA_INTF_T_ALSA_BASE + 1)


MEDIA_INTF_T_ALSA_CONTROL = (MEDIA_INTF_T_ALSA_BASE + 2)


def MEDIA_V2_ENTITY_HAS_FLAGS(media_version):
    return (media_version >= (((4 << 16) | (19 << 8)) | 0))


def MEDIA_V2_PAD_HAS_INDEX(media_version):
    return (media_version >= (((4 << 16) | (19 << 8)) | 0))


MEDIA_IOC_DEVICE_INFO = (_IOWR ('|', 0x00, struct_media_device_info))


MEDIA_IOC_ENUM_ENTITIES = (_IOWR ('|', 0x01, struct_media_entity_desc))


MEDIA_IOC_ENUM_LINKS = (_IOWR ('|', 0x02, struct_media_links_enum))


MEDIA_IOC_SETUP_LINK = (_IOWR ('|', 0x03, struct_media_link_desc))


MEDIA_IOC_G_TOPOLOGY = (_IOWR ('|', 0x04, struct_media_v2_topology))


MEDIA_IOC_REQUEST_ALLOC = (_IOR ('|', 0x05, c_int))


MEDIA_REQUEST_IOC_QUEUE = (_IO ('|', 0x80))


MEDIA_REQUEST_IOC_REINIT = (_IO ('|', 0x81))


MEDIA_ENT_TYPE_SHIFT = 16


MEDIA_ENT_TYPE_MASK = 0x00ff0000


MEDIA_ENT_SUBTYPE_MASK = 0x0000ffff


MEDIA_ENT_T_DEVNODE_UNKNOWN = (MEDIA_ENT_F_OLD_BASE | MEDIA_ENT_SUBTYPE_MASK)


MEDIA_ENT_T_DEVNODE = MEDIA_ENT_F_OLD_BASE


MEDIA_ENT_T_DEVNODE_V4L = MEDIA_ENT_F_IO_V4L


MEDIA_ENT_T_DEVNODE_FB = (MEDIA_ENT_F_OLD_BASE + 2)


MEDIA_ENT_T_DEVNODE_ALSA = (MEDIA_ENT_F_OLD_BASE + 3)


MEDIA_ENT_T_DEVNODE_DVB = (MEDIA_ENT_F_OLD_BASE + 4)


MEDIA_ENT_T_UNKNOWN = MEDIA_ENT_F_UNKNOWN


MEDIA_ENT_T_V4L2_VIDEO = MEDIA_ENT_F_IO_V4L


MEDIA_ENT_T_V4L2_SUBDEV = MEDIA_ENT_F_V4L2_SUBDEV_UNKNOWN


MEDIA_ENT_T_V4L2_SUBDEV_SENSOR = MEDIA_ENT_F_CAM_SENSOR


MEDIA_ENT_T_V4L2_SUBDEV_FLASH = MEDIA_ENT_F_FLASH


MEDIA_ENT_T_V4L2_SUBDEV_LENS = MEDIA_ENT_F_LENS


MEDIA_ENT_T_V4L2_SUBDEV_DECODER = MEDIA_ENT_F_ATV_DECODER


MEDIA_ENT_T_V4L2_SUBDEV_TUNER = MEDIA_ENT_F_TUNER


MEDIA_ENT_F_DTV_DECODER = MEDIA_ENT_F_DV_DECODER


MEDIA_INTF_T_ALSA_COMPRESS = (MEDIA_INTF_T_ALSA_BASE + 3)


MEDIA_INTF_T_ALSA_RAWMIDI = (MEDIA_INTF_T_ALSA_BASE + 4)


MEDIA_INTF_T_ALSA_HWDEP = (MEDIA_INTF_T_ALSA_BASE + 5)


MEDIA_INTF_T_ALSA_SEQUENCER = (MEDIA_INTF_T_ALSA_BASE + 6)


MEDIA_INTF_T_ALSA_TIMER = (MEDIA_INTF_T_ALSA_BASE + 7)


MEDIA_API_VERSION = (((0 << 16) | (1 << 8)) | 0)


MEDIA_BUS_FMT_FIXED = 0x0001


MEDIA_BUS_FMT_RGB444_1X12 = 0x1016


MEDIA_BUS_FMT_RGB444_2X8_PADHI_BE = 0x1001


MEDIA_BUS_FMT_RGB444_2X8_PADHI_LE = 0x1002


MEDIA_BUS_FMT_RGB555_2X8_PADHI_BE = 0x1003


MEDIA_BUS_FMT_RGB555_2X8_PADHI_LE = 0x1004


MEDIA_BUS_FMT_RGB565_1X16 = 0x1017


MEDIA_BUS_FMT_BGR565_2X8_BE = 0x1005


MEDIA_BUS_FMT_BGR565_2X8_LE = 0x1006


MEDIA_BUS_FMT_RGB565_2X8_BE = 0x1007


MEDIA_BUS_FMT_RGB565_2X8_LE = 0x1008


MEDIA_BUS_FMT_RGB666_1X18 = 0x1009


MEDIA_BUS_FMT_RGB666_2X9_BE = 0x1025


MEDIA_BUS_FMT_BGR666_1X18 = 0x1023


MEDIA_BUS_FMT_RBG888_1X24 = 0x100e


MEDIA_BUS_FMT_RGB666_1X24_CPADHI = 0x1015


MEDIA_BUS_FMT_BGR666_1X24_CPADHI = 0x1024


MEDIA_BUS_FMT_RGB565_1X24_CPADHI = 0x1022


MEDIA_BUS_FMT_RGB666_1X7X3_SPWG = 0x1010


MEDIA_BUS_FMT_BGR888_1X24 = 0x1013


MEDIA_BUS_FMT_BGR888_3X8 = 0x101b


MEDIA_BUS_FMT_GBR888_1X24 = 0x1014


MEDIA_BUS_FMT_RGB888_1X24 = 0x100a


MEDIA_BUS_FMT_RGB888_2X12_BE = 0x100b


MEDIA_BUS_FMT_RGB888_2X12_LE = 0x100c


MEDIA_BUS_FMT_RGB888_3X8 = 0x101c


MEDIA_BUS_FMT_RGB888_3X8_DELTA = 0x101d


MEDIA_BUS_FMT_RGB888_1X7X4_SPWG = 0x1011


MEDIA_BUS_FMT_RGB888_1X7X4_JEIDA = 0x1012


MEDIA_BUS_FMT_RGB666_1X30_CPADLO = 0x101e


MEDIA_BUS_FMT_RGB888_1X30_CPADLO = 0x101f


MEDIA_BUS_FMT_ARGB8888_1X32 = 0x100d


MEDIA_BUS_FMT_RGB888_1X32_PADHI = 0x100f


MEDIA_BUS_FMT_RGB101010_1X30 = 0x1018


MEDIA_BUS_FMT_RGB666_1X36_CPADLO = 0x1020


MEDIA_BUS_FMT_RGB888_1X36_CPADLO = 0x1021


MEDIA_BUS_FMT_RGB121212_1X36 = 0x1019


MEDIA_BUS_FMT_RGB161616_1X48 = 0x101a


MEDIA_BUS_FMT_Y8_1X8 = 0x2001


MEDIA_BUS_FMT_UV8_1X8 = 0x2015


MEDIA_BUS_FMT_UYVY8_1_5X8 = 0x2002


MEDIA_BUS_FMT_VYUY8_1_5X8 = 0x2003


MEDIA_BUS_FMT_YUYV8_1_5X8 = 0x2004


MEDIA_BUS_FMT_YVYU8_1_5X8 = 0x2005


MEDIA_BUS_FMT_UYVY8_2X8 = 0x2006


MEDIA_BUS_FMT_VYUY8_2X8 = 0x2007


MEDIA_BUS_FMT_YUYV8_2X8 = 0x2008


MEDIA_BUS_FMT_YVYU8_2X8 = 0x2009


MEDIA_BUS_FMT_Y10_1X10 = 0x200a


MEDIA_BUS_FMT_Y10_2X8_PADHI_LE = 0x202c


MEDIA_BUS_FMT_UYVY10_2X10 = 0x2018


MEDIA_BUS_FMT_VYUY10_2X10 = 0x2019


MEDIA_BUS_FMT_YUYV10_2X10 = 0x200b


MEDIA_BUS_FMT_YVYU10_2X10 = 0x200c


MEDIA_BUS_FMT_Y12_1X12 = 0x2013


MEDIA_BUS_FMT_UYVY12_2X12 = 0x201c


MEDIA_BUS_FMT_VYUY12_2X12 = 0x201d


MEDIA_BUS_FMT_YUYV12_2X12 = 0x201e


MEDIA_BUS_FMT_YVYU12_2X12 = 0x201f


MEDIA_BUS_FMT_Y14_1X14 = 0x202d


MEDIA_BUS_FMT_Y16_1X16 = 0x202e


MEDIA_BUS_FMT_UYVY8_1X16 = 0x200f


MEDIA_BUS_FMT_VYUY8_1X16 = 0x2010


MEDIA_BUS_FMT_YUYV8_1X16 = 0x2011


MEDIA_BUS_FMT_YVYU8_1X16 = 0x2012


MEDIA_BUS_FMT_YDYUYDYV8_1X16 = 0x2014


MEDIA_BUS_FMT_UYVY10_1X20 = 0x201a


MEDIA_BUS_FMT_VYUY10_1X20 = 0x201b


MEDIA_BUS_FMT_YUYV10_1X20 = 0x200d


MEDIA_BUS_FMT_YVYU10_1X20 = 0x200e


MEDIA_BUS_FMT_VUY8_1X24 = 0x2024


MEDIA_BUS_FMT_YUV8_1X24 = 0x2025


MEDIA_BUS_FMT_UYYVYY8_0_5X24 = 0x2026


MEDIA_BUS_FMT_UYVY12_1X24 = 0x2020


MEDIA_BUS_FMT_VYUY12_1X24 = 0x2021


MEDIA_BUS_FMT_YUYV12_1X24 = 0x2022


MEDIA_BUS_FMT_YVYU12_1X24 = 0x2023


MEDIA_BUS_FMT_YUV10_1X30 = 0x2016


MEDIA_BUS_FMT_UYYVYY10_0_5X30 = 0x2027


MEDIA_BUS_FMT_AYUV8_1X32 = 0x2017


MEDIA_BUS_FMT_UYYVYY12_0_5X36 = 0x2028


MEDIA_BUS_FMT_YUV12_1X36 = 0x2029


MEDIA_BUS_FMT_YUV16_1X48 = 0x202a


MEDIA_BUS_FMT_UYYVYY16_0_5X48 = 0x202b


MEDIA_BUS_FMT_SBGGR8_1X8 = 0x3001


MEDIA_BUS_FMT_SGBRG8_1X8 = 0x3013


MEDIA_BUS_FMT_SGRBG8_1X8 = 0x3002


MEDIA_BUS_FMT_SRGGB8_1X8 = 0x3014


MEDIA_BUS_FMT_SBGGR10_ALAW8_1X8 = 0x3015


MEDIA_BUS_FMT_SGBRG10_ALAW8_1X8 = 0x3016


MEDIA_BUS_FMT_SGRBG10_ALAW8_1X8 = 0x3017


MEDIA_BUS_FMT_SRGGB10_ALAW8_1X8 = 0x3018


MEDIA_BUS_FMT_SBGGR10_DPCM8_1X8 = 0x300b


MEDIA_BUS_FMT_SGBRG10_DPCM8_1X8 = 0x300c


MEDIA_BUS_FMT_SGRBG10_DPCM8_1X8 = 0x3009


MEDIA_BUS_FMT_SRGGB10_DPCM8_1X8 = 0x300d


MEDIA_BUS_FMT_SBGGR10_2X8_PADHI_BE = 0x3003


MEDIA_BUS_FMT_SBGGR10_2X8_PADHI_LE = 0x3004


MEDIA_BUS_FMT_SBGGR10_2X8_PADLO_BE = 0x3005


MEDIA_BUS_FMT_SBGGR10_2X8_PADLO_LE = 0x3006


MEDIA_BUS_FMT_SBGGR10_1X10 = 0x3007


MEDIA_BUS_FMT_SGBRG10_1X10 = 0x300e


MEDIA_BUS_FMT_SGRBG10_1X10 = 0x300a


MEDIA_BUS_FMT_SRGGB10_1X10 = 0x300f


MEDIA_BUS_FMT_SBGGR12_1X12 = 0x3008


MEDIA_BUS_FMT_SGBRG12_1X12 = 0x3010


MEDIA_BUS_FMT_SGRBG12_1X12 = 0x3011


MEDIA_BUS_FMT_SRGGB12_1X12 = 0x3012


MEDIA_BUS_FMT_SBGGR14_1X14 = 0x3019


MEDIA_BUS_FMT_SGBRG14_1X14 = 0x301a


MEDIA_BUS_FMT_SGRBG14_1X14 = 0x301b


MEDIA_BUS_FMT_SRGGB14_1X14 = 0x301c


MEDIA_BUS_FMT_SBGGR16_1X16 = 0x301d


MEDIA_BUS_FMT_SGBRG16_1X16 = 0x301e


MEDIA_BUS_FMT_SGRBG16_1X16 = 0x301f


MEDIA_BUS_FMT_SRGGB16_1X16 = 0x3020


MEDIA_BUS_FMT_JPEG_1X8 = 0x4001


MEDIA_BUS_FMT_S5C_UYVY_JPEG_1X8 = 0x5001


MEDIA_BUS_FMT_AHSV8888_1X32 = 0x6001


MEDIA_BUS_FMT_METADATA_FIXED = 0x7001


MEDIA_BUS_FMT_META_8 = 0x8001


MEDIA_BUS_FMT_META_10 = 0x8002


MEDIA_BUS_FMT_META_12 = 0x8003


MEDIA_BUS_FMT_META_14 = 0x8004


MEDIA_BUS_FMT_META_16 = 0x8005


MEDIA_BUS_FMT_META_20 = 0x8006


MEDIA_BUS_FMT_META_24 = 0x8007


MEDIA_BUS_FMT_CCS_EMBEDDED = 0x9001


V4L2_MBUS_FRAMEFMT_SET_CSC = 0x0001


V4L2_SUBDEV_MBUS_CODE_CSC_COLORSPACE = 0x00000001


V4L2_SUBDEV_MBUS_CODE_CSC_XFER_FUNC = 0x00000002


V4L2_SUBDEV_MBUS_CODE_CSC_YCBCR_ENC = 0x00000004


V4L2_SUBDEV_MBUS_CODE_CSC_HSV_ENC = V4L2_SUBDEV_MBUS_CODE_CSC_YCBCR_ENC


V4L2_SUBDEV_MBUS_CODE_CSC_QUANTIZATION = 0x00000008


V4L2_SUBDEV_CAP_RO_SUBDEV = 0x00000001


V4L2_SUBDEV_CAP_STREAMS = 0x00000002


V4L2_SUBDEV_ROUTE_FL_ACTIVE = (1 << 0)


V4L2_SUBDEV_ROUTE_FL_IMMUTABLE = (1 << 1)


V4L2_SUBDEV_CLIENT_CAP_STREAMS = (1 << 0)


V4L2_SUBDEV_CLIENT_CAP_INTERVAL_USES_WHICH = (1 << 1)


VIDIOC_SUBDEV_QUERYCAP = (_IOR ('V', 0, struct_v4l2_subdev_capability))


VIDIOC_SUBDEV_G_FMT = (_IOWR ('V', 4, struct_v4l2_subdev_format))


VIDIOC_SUBDEV_S_FMT = (_IOWR ('V', 5, struct_v4l2_subdev_format))


VIDIOC_SUBDEV_G_FRAME_INTERVAL = (_IOWR ('V', 21, struct_v4l2_subdev_frame_interval))


VIDIOC_SUBDEV_S_FRAME_INTERVAL = (_IOWR ('V', 22, struct_v4l2_subdev_frame_interval))


VIDIOC_SUBDEV_ENUM_MBUS_CODE = (_IOWR ('V', 2, struct_v4l2_subdev_mbus_code_enum))


VIDIOC_SUBDEV_ENUM_FRAME_SIZE = (_IOWR ('V', 74, struct_v4l2_subdev_frame_size_enum))


VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL = (_IOWR ('V', 75, struct_v4l2_subdev_frame_interval_enum))


VIDIOC_SUBDEV_G_CROP = (_IOWR ('V', 59, struct_v4l2_subdev_crop))


VIDIOC_SUBDEV_S_CROP = (_IOWR ('V', 60, struct_v4l2_subdev_crop))


VIDIOC_SUBDEV_G_SELECTION = (_IOWR ('V', 61, struct_v4l2_subdev_selection))


VIDIOC_SUBDEV_S_SELECTION = (_IOWR ('V', 62, struct_v4l2_subdev_selection))


VIDIOC_SUBDEV_G_ROUTING = (_IOWR ('V', 38, struct_v4l2_subdev_routing))


VIDIOC_SUBDEV_S_ROUTING = (_IOWR ('V', 39, struct_v4l2_subdev_routing))


VIDIOC_SUBDEV_G_CLIENT_CAP = (_IOR ('V', 101, struct_v4l2_subdev_client_capability))


VIDIOC_SUBDEV_S_CLIENT_CAP = (_IOWR ('V', 102, struct_v4l2_subdev_client_capability))


VIDIOC_SUBDEV_G_STD = (_IOR ('V', 23, v4l2_std_id))


VIDIOC_SUBDEV_S_STD = (_IOW ('V', 24, v4l2_std_id))


VIDIOC_SUBDEV_ENUMSTD = (_IOWR ('V', 25, struct_v4l2_standard))


VIDIOC_SUBDEV_G_EDID = (_IOWR ('V', 40, struct_v4l2_edid))


VIDIOC_SUBDEV_S_EDID = (_IOWR ('V', 41, struct_v4l2_edid))


VIDIOC_SUBDEV_QUERYSTD = (_IOR ('V', 63, v4l2_std_id))


VIDIOC_SUBDEV_S_DV_TIMINGS = (_IOWR ('V', 87, struct_v4l2_dv_timings))


VIDIOC_SUBDEV_G_DV_TIMINGS = (_IOWR ('V', 88, struct_v4l2_dv_timings))


VIDIOC_SUBDEV_ENUM_DV_TIMINGS = (_IOWR ('V', 98, struct_v4l2_enum_dv_timings))


VIDIOC_SUBDEV_QUERY_DV_TIMINGS = (_IOR ('V', 99, struct_v4l2_dv_timings))


VIDIOC_SUBDEV_DV_TIMINGS_CAP = (_IOWR ('V', 100, struct_v4l2_dv_timings_cap))

v4l2_ctrl_h264_sps = struct_v4l2_ctrl_h264_sps

v4l2_ctrl_h264_pps = struct_v4l2_ctrl_h264_pps

v4l2_ctrl_h264_scaling_matrix = struct_v4l2_ctrl_h264_scaling_matrix

v4l2_h264_weight_factors = struct_v4l2_h264_weight_factors

v4l2_ctrl_h264_pred_weights = struct_v4l2_ctrl_h264_pred_weights

v4l2_h264_reference = struct_v4l2_h264_reference

v4l2_ctrl_h264_slice_params = struct_v4l2_ctrl_h264_slice_params

v4l2_h264_dpb_entry = struct_v4l2_h264_dpb_entry

v4l2_ctrl_h264_decode_params = struct_v4l2_ctrl_h264_decode_params

v4l2_ctrl_fwht_params = struct_v4l2_ctrl_fwht_params

v4l2_vp8_segment = struct_v4l2_vp8_segment

v4l2_vp8_loop_filter = struct_v4l2_vp8_loop_filter

v4l2_vp8_quantization = struct_v4l2_vp8_quantization

v4l2_vp8_entropy = struct_v4l2_vp8_entropy

v4l2_vp8_entropy_coder_state = struct_v4l2_vp8_entropy_coder_state

v4l2_ctrl_vp8_frame = struct_v4l2_ctrl_vp8_frame

v4l2_ctrl_mpeg2_sequence = struct_v4l2_ctrl_mpeg2_sequence

v4l2_ctrl_mpeg2_picture = struct_v4l2_ctrl_mpeg2_picture

v4l2_ctrl_mpeg2_quantisation = struct_v4l2_ctrl_mpeg2_quantisation

v4l2_ctrl_hevc_sps = struct_v4l2_ctrl_hevc_sps

v4l2_ctrl_hevc_pps = struct_v4l2_ctrl_hevc_pps

v4l2_hevc_dpb_entry = struct_v4l2_hevc_dpb_entry

v4l2_hevc_pred_weight_table = struct_v4l2_hevc_pred_weight_table

v4l2_ctrl_hevc_slice_params = struct_v4l2_ctrl_hevc_slice_params

v4l2_ctrl_hevc_decode_params = struct_v4l2_ctrl_hevc_decode_params

v4l2_ctrl_hevc_scaling_matrix = struct_v4l2_ctrl_hevc_scaling_matrix

v4l2_ctrl_hdr10_cll_info = struct_v4l2_ctrl_hdr10_cll_info

v4l2_ctrl_hdr10_mastering_display = struct_v4l2_ctrl_hdr10_mastering_display

v4l2_vp9_loop_filter = struct_v4l2_vp9_loop_filter

v4l2_vp9_quantization = struct_v4l2_vp9_quantization

v4l2_vp9_segmentation = struct_v4l2_vp9_segmentation

v4l2_ctrl_vp9_frame = struct_v4l2_ctrl_vp9_frame

v4l2_vp9_mv_probs = struct_v4l2_vp9_mv_probs

v4l2_ctrl_vp9_compressed_hdr = struct_v4l2_ctrl_vp9_compressed_hdr

v4l2_ctrl_av1_sequence = struct_v4l2_ctrl_av1_sequence

v4l2_ctrl_av1_tile_group_entry = struct_v4l2_ctrl_av1_tile_group_entry

v4l2_av1_global_motion = struct_v4l2_av1_global_motion

v4l2_av1_loop_restoration = struct_v4l2_av1_loop_restoration

v4l2_av1_cdef = struct_v4l2_av1_cdef

v4l2_av1_segmentation = struct_v4l2_av1_segmentation

v4l2_av1_loop_filter = struct_v4l2_av1_loop_filter

v4l2_av1_quantization = struct_v4l2_av1_quantization

v4l2_av1_tile_info = struct_v4l2_av1_tile_info

v4l2_ctrl_av1_frame = struct_v4l2_ctrl_av1_frame

v4l2_ctrl_av1_film_grain = struct_v4l2_ctrl_av1_film_grain

v4l2_rect = struct_v4l2_rect

v4l2_fract = struct_v4l2_fract

v4l2_area = struct_v4l2_area

v4l2_capability = struct_v4l2_capability

v4l2_pix_format = struct_v4l2_pix_format

v4l2_fmtdesc = struct_v4l2_fmtdesc

v4l2_frmsize_discrete = struct_v4l2_frmsize_discrete

v4l2_frmsize_stepwise = struct_v4l2_frmsize_stepwise

v4l2_frmsizeenum = struct_v4l2_frmsizeenum

v4l2_frmival_stepwise = struct_v4l2_frmival_stepwise

v4l2_frmivalenum = struct_v4l2_frmivalenum

v4l2_timecode = struct_v4l2_timecode

v4l2_jpegcompression = struct_v4l2_jpegcompression

v4l2_requestbuffers = struct_v4l2_requestbuffers

v4l2_plane = struct_v4l2_plane

v4l2_buffer = struct_v4l2_buffer

v4l2_exportbuffer = struct_v4l2_exportbuffer

v4l2_framebuffer = struct_v4l2_framebuffer

v4l2_clip = struct_v4l2_clip

v4l2_window = struct_v4l2_window

v4l2_captureparm = struct_v4l2_captureparm

v4l2_outputparm = struct_v4l2_outputparm

v4l2_cropcap = struct_v4l2_cropcap

v4l2_crop = struct_v4l2_crop

v4l2_selection = struct_v4l2_selection

v4l2_standard = struct_v4l2_standard

v4l2_bt_timings = struct_v4l2_bt_timings

v4l2_dv_timings = struct_v4l2_dv_timings

v4l2_enum_dv_timings = struct_v4l2_enum_dv_timings

v4l2_bt_timings_cap = struct_v4l2_bt_timings_cap

v4l2_dv_timings_cap = struct_v4l2_dv_timings_cap

v4l2_input = struct_v4l2_input

v4l2_output = struct_v4l2_output

v4l2_control = struct_v4l2_control

v4l2_ext_control = struct_v4l2_ext_control

v4l2_ext_controls = struct_v4l2_ext_controls

v4l2_queryctrl = struct_v4l2_queryctrl

v4l2_query_ext_ctrl = struct_v4l2_query_ext_ctrl

v4l2_querymenu = struct_v4l2_querymenu

v4l2_tuner = struct_v4l2_tuner

v4l2_modulator = struct_v4l2_modulator

v4l2_frequency = struct_v4l2_frequency

v4l2_frequency_band = struct_v4l2_frequency_band

v4l2_hw_freq_seek = struct_v4l2_hw_freq_seek

v4l2_rds_data = struct_v4l2_rds_data

v4l2_audio = struct_v4l2_audio

v4l2_audioout = struct_v4l2_audioout

v4l2_enc_idx_entry = struct_v4l2_enc_idx_entry

v4l2_enc_idx = struct_v4l2_enc_idx

v4l2_encoder_cmd = struct_v4l2_encoder_cmd

v4l2_decoder_cmd = struct_v4l2_decoder_cmd

v4l2_vbi_format = struct_v4l2_vbi_format

v4l2_sliced_vbi_format = struct_v4l2_sliced_vbi_format

v4l2_sliced_vbi_cap = struct_v4l2_sliced_vbi_cap

v4l2_sliced_vbi_data = struct_v4l2_sliced_vbi_data

v4l2_mpeg_vbi_itv0_line = struct_v4l2_mpeg_vbi_itv0_line

v4l2_mpeg_vbi_itv0 = struct_v4l2_mpeg_vbi_itv0

v4l2_mpeg_vbi_ITV0 = struct_v4l2_mpeg_vbi_ITV0

v4l2_mpeg_vbi_fmt_ivtv = struct_v4l2_mpeg_vbi_fmt_ivtv

v4l2_plane_pix_format = struct_v4l2_plane_pix_format

v4l2_pix_format_mplane = struct_v4l2_pix_format_mplane

v4l2_sdr_format = struct_v4l2_sdr_format

v4l2_meta_format = struct_v4l2_meta_format

v4l2_format = struct_v4l2_format

v4l2_streamparm = struct_v4l2_streamparm

v4l2_event_vsync = struct_v4l2_event_vsync

v4l2_event_ctrl = struct_v4l2_event_ctrl

v4l2_event_frame_sync = struct_v4l2_event_frame_sync

v4l2_event_src_change = struct_v4l2_event_src_change

v4l2_event_motion_det = struct_v4l2_event_motion_det

v4l2_event = struct_v4l2_event

v4l2_event_subscription = struct_v4l2_event_subscription

v4l2_dbg_match = struct_v4l2_dbg_match

v4l2_dbg_register = struct_v4l2_dbg_register

v4l2_dbg_chip_info = struct_v4l2_dbg_chip_info

v4l2_create_buffers = struct_v4l2_create_buffers

v4l2_remove_buffers = struct_v4l2_remove_buffers

media_device_info = struct_media_device_info

media_entity_desc = struct_media_entity_desc

media_pad_desc = struct_media_pad_desc

media_link_desc = struct_media_link_desc

media_links_enum = struct_media_links_enum

media_v2_entity = struct_media_v2_entity

media_v2_intf_devnode = struct_media_v2_intf_devnode

media_v2_interface = struct_media_v2_interface

media_v2_pad = struct_media_v2_pad

media_v2_link = struct_media_v2_link

media_v2_topology = struct_media_v2_topology

v4l2_mbus_framefmt = struct_v4l2_mbus_framefmt

v4l2_subdev_format = struct_v4l2_subdev_format

v4l2_subdev_crop = struct_v4l2_subdev_crop

v4l2_subdev_mbus_code_enum = struct_v4l2_subdev_mbus_code_enum

v4l2_subdev_frame_size_enum = struct_v4l2_subdev_frame_size_enum

v4l2_subdev_frame_interval = struct_v4l2_subdev_frame_interval

v4l2_subdev_frame_interval_enum = struct_v4l2_subdev_frame_interval_enum

v4l2_subdev_selection = struct_v4l2_subdev_selection

v4l2_subdev_capability = struct_v4l2_subdev_capability

v4l2_subdev_route = struct_v4l2_subdev_route

v4l2_subdev_routing = struct_v4l2_subdev_routing

v4l2_subdev_client_capability = struct_v4l2_subdev_client_capability

# No inserted files

# No prefix-stripping

