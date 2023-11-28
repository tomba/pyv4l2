r"""Wrapper for videodev2.h

Generated with:
/home/tomba/.local/bin/ctypesgen -I/home/tomba/tmp/khdrs/include -D__signed__= -U__SIZEOF_INT128__ -o v4l2/v4l2_kernel.py --no-embed-preamble /home/tomba/tmp/khdrs/include/linux/videodev2.h /home/tomba/tmp/khdrs/include/linux/media.h /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h /home/tomba/tmp/khdrs/include/linux/media-bus-format.h /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

from .ctypes_preamble import *
from .ctypes_preamble import _variadic_function

# End preamble

_libs = {}
_libdirs = []

# Begin loader

from .ctypes_loader import *

# End loader

add_library_search_dirs([])

# No libraries

# No modules

__time_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 160

__suseconds_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 162

__syscall_slong_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 197

# /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h: 8
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

# /usr/include/x86_64-linux-gnu/bits/types/struct_timespec.h: 11
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

__s8 = c_char# /home/tomba/tmp/khdrs/include/asm-generic/int-ll64.h: 20

__u8 = c_ubyte# /home/tomba/tmp/khdrs/include/asm-generic/int-ll64.h: 21

__s16 = c_short# /home/tomba/tmp/khdrs/include/asm-generic/int-ll64.h: 23

__u16 = c_ushort# /home/tomba/tmp/khdrs/include/asm-generic/int-ll64.h: 24

__s32 = c_int# /home/tomba/tmp/khdrs/include/asm-generic/int-ll64.h: 26

__u32 = c_uint# /home/tomba/tmp/khdrs/include/asm-generic/int-ll64.h: 27

__s64 = c_longlong# /home/tomba/tmp/khdrs/include/asm-generic/int-ll64.h: 33

__u64 = c_ulonglong# /home/tomba/tmp/khdrs/include/asm-generic/int-ll64.h: 34

__le32 = __u32# /home/tomba/tmp/khdrs/include/linux/types.h: 33

# /home/tomba/tmp/khdrs/include/linux/v4l2-common.h: 48
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1385
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1441
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1473
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1478
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1503
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1529
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1576
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1621
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1660
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1738
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1771
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1798
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1823
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1850
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1869
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1915
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 1971
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2018
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2051
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2153
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2242
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2289
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2322
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2399
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2473
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2512
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2577
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2598
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2642
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2727
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2771
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2819
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2897
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2926
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

enum_v4l2_av1_warp_model = c_int# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2943

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 2994
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

enum_v4l2_av1_frame_restoration_type = c_int# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3009

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3032
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3053
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

V4L2_AV1_SEG_LVL_MAX = 8# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3080

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3104
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3139
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3173
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3209
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

enum_v4l2_av1_frame_type = c_int# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3230

enum_v4l2_av1_interpolation_filter = c_int# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3250

enum_v4l2_av1_tx_mode = c_int# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3268

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3346
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-controls.h: 3449
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

enum_v4l2_field = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_ANY = 0# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_NONE = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_TOP = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_BOTTOM = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_INTERLACED = 4# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_SEQ_TB = 5# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_SEQ_BT = 6# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_ALTERNATE = 7# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_INTERLACED_TB = 8# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

V4L2_FIELD_INTERLACED_BT = 9# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 86

enum_v4l2_buf_type = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_VIDEO_CAPTURE = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_VIDEO_OUTPUT = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_VIDEO_OVERLAY = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_VBI_CAPTURE = 4# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_VBI_OUTPUT = 5# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_SLICED_VBI_CAPTURE = 6# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_SLICED_VBI_OUTPUT = 7# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY = 8# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE = 9# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE = 10# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_SDR_CAPTURE = 11# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_SDR_OUTPUT = 12# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_META_CAPTURE = 13# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_META_OUTPUT = 14# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

V4L2_BUF_TYPE_PRIVATE = 0x80# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 139

enum_v4l2_tuner_type = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 174

V4L2_TUNER_RADIO = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 174

V4L2_TUNER_ANALOG_TV = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 174

V4L2_TUNER_DIGITAL_TV = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 174

V4L2_TUNER_SDR = 4# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 174

V4L2_TUNER_RF = 5# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 174

enum_v4l2_memory = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 185

V4L2_MEMORY_MMAP = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 185

V4L2_MEMORY_USERPTR = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 185

V4L2_MEMORY_OVERLAY = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 185

V4L2_MEMORY_DMABUF = 4# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 185

enum_v4l2_colorspace = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_DEFAULT = 0# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_SMPTE170M = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_SMPTE240M = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_REC709 = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_BT878 = 4# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_470_SYSTEM_M = 5# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_470_SYSTEM_BG = 6# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_JPEG = 7# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_SRGB = 8# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_OPRGB = 9# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_BT2020 = 10# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_RAW = 11# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

V4L2_COLORSPACE_DCI_P3 = 12# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 193

enum_v4l2_xfer_func = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 258

V4L2_XFER_FUNC_DEFAULT = 0# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 258

V4L2_XFER_FUNC_709 = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 258

V4L2_XFER_FUNC_SRGB = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 258

V4L2_XFER_FUNC_OPRGB = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 258

V4L2_XFER_FUNC_SMPTE240M = 4# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 258

V4L2_XFER_FUNC_NONE = 5# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 258

V4L2_XFER_FUNC_DCI_P3 = 6# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 258

V4L2_XFER_FUNC_SMPTE2084 = 7# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 258

enum_v4l2_ycbcr_encoding = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

V4L2_YCBCR_ENC_DEFAULT = 0# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

V4L2_YCBCR_ENC_601 = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

V4L2_YCBCR_ENC_709 = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

V4L2_YCBCR_ENC_XV601 = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

V4L2_YCBCR_ENC_XV709 = 4# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

V4L2_YCBCR_ENC_SYCC = 5# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

V4L2_YCBCR_ENC_BT2020 = 6# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

V4L2_YCBCR_ENC_BT2020_CONST_LUM = 7# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

V4L2_YCBCR_ENC_SMPTE240M = 8# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 299

enum_v4l2_hsv_encoding = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 349

V4L2_HSV_ENC_180 = 128# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 349

V4L2_HSV_ENC_256 = 129# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 349

enum_v4l2_quantization = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 369

V4L2_QUANTIZATION_DEFAULT = 0# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 369

V4L2_QUANTIZATION_FULL_RANGE = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 369

V4L2_QUANTIZATION_LIM_RANGE = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 369

enum_v4l2_priority = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 399

V4L2_PRIORITY_UNSET = 0# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 399

V4L2_PRIORITY_BACKGROUND = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 399

V4L2_PRIORITY_INTERACTIVE = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 399

V4L2_PRIORITY_RECORD = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 399

V4L2_PRIORITY_DEFAULT = V4L2_PRIORITY_INTERACTIVE# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 399

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 407
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 414
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 419
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 435
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 500
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 490
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 833
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

enum_v4l2_frmsizetypes = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 859

V4L2_FRMSIZE_TYPE_DISCRETE = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 859

V4L2_FRMSIZE_TYPE_CONTINUOUS = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 859

V4L2_FRMSIZE_TYPE_STEPWISE = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 859

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 865
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 870
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 884
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 879
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

enum_v4l2_frmivaltypes = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 895

V4L2_FRMIVAL_TYPE_DISCRETE = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 895

V4L2_FRMIVAL_TYPE_CONTINUOUS = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 895

V4L2_FRMIVAL_TYPE_STEPWISE = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 895

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 901
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 914
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 907
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 925
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 950
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 984
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1029
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1026
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1085
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1093
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1073
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1170
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1188
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1182
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1217
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1222
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1235
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1248
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1260
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1267
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1285
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

v4l2_std_id = __u64# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1298

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1430
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1478
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1604
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1602
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1621
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1639
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1670
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1666
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1680
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1732
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1756
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1765
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
    ('ptr', POINTER(None)),
]

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1761
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1802
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1801
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

enum_v4l2_ctrl_type = c_int# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_INTEGER = 1# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_BOOLEAN = 2# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_MENU = 3# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_BUTTON = 4# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_INTEGER64 = 5# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_CTRL_CLASS = 6# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_STRING = 7# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_BITMASK = 8# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_INTEGER_MENU = 9# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_COMPOUND_TYPES = 0x0100# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_U8 = 0x0100# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_U16 = 0x0101# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_U32 = 0x0102# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_AREA = 0x0106# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_HDR10_CLL_INFO = 0x0110# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_HDR10_MASTERING_DISPLAY = 0x0111# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_H264_SPS = 0x0200# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_H264_PPS = 0x0201# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_H264_SCALING_MATRIX = 0x0202# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_H264_SLICE_PARAMS = 0x0203# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_H264_DECODE_PARAMS = 0x0204# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_H264_PRED_WEIGHTS = 0x0205# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_FWHT_PARAMS = 0x0220# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_VP8_FRAME = 0x0240# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_MPEG2_QUANTISATION = 0x0250# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_MPEG2_SEQUENCE = 0x0251# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_MPEG2_PICTURE = 0x0252# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_VP9_COMPRESSED_HDR = 0x0260# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_VP9_FRAME = 0x0261# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_HEVC_SPS = 0x0270# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_HEVC_PPS = 0x0271# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_HEVC_SLICE_PARAMS = 0x0272# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_HEVC_SCALING_MATRIX = 0x0273# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_HEVC_DECODE_PARAMS = 0x0274# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_AV1_SEQUENCE = 0x280# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_AV1_TILE_GROUP_ENTRY = 0x281# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_AV1_FRAME = 0x282# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

V4L2_CTRL_TYPE_AV1_FILM_GRAIN = 0x283# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1822

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1874
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1887
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1907
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1904
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1941
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1955
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1998
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2009
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2020
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2035
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2055
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2070
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2087
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2096
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2116
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'data',
]
struct_anon_18._fields_ = [
    ('data', __u32 * int(8)),
]

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2115
class union_anon_19(Union):
    pass

union_anon_19.__slots__ = [
    'raw',
]
union_anon_19._fields_ = [
    ('raw', struct_anon_18),
]

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2112
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2152
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'pts',
]
struct_anon_20._fields_ = [
    ('pts', __u64),
]

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2156
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2166
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'data',
]
struct_anon_22._fields_ = [
    ('data', __u32 * int(16)),
]

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2151
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2148
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2181
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2209
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2233
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2244
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2274
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2279
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2284
class struct_v4l2_mpeg_vbi_ITV0(Structure):
    pass

struct_v4l2_mpeg_vbi_ITV0.__slots__ = [
    'line',
]
struct_v4l2_mpeg_vbi_ITV0._fields_ = [
    ('line', struct_v4l2_mpeg_vbi_itv0_line * int(36)),
]

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2293
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2291
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2311
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2343
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2333
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2358
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2375
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2397
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2395
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2413
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2411
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2434
class struct_v4l2_event_vsync(Structure):
    pass

struct_v4l2_event_vsync.__slots__ = [
    'field',
]
struct_v4l2_event_vsync._fields_ = [
    ('field', __u8),
]

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2448
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2445
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2459
class struct_v4l2_event_frame_sync(Structure):
    pass

struct_v4l2_event_frame_sync.__slots__ = [
    'frame_sequence',
]
struct_v4l2_event_frame_sync._fields_ = [
    ('frame_sequence', __u32),
]

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2465
class struct_v4l2_event_src_change(Structure):
    pass

struct_v4l2_event_src_change.__slots__ = [
    'changes',
]
struct_v4l2_event_src_change._fields_ = [
    ('changes', __u32),
]

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2478
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2486
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2484
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2504
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2531
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2529
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2537
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2548
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

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2568
class struct_v4l2_create_buffers(Structure):
    pass

struct_v4l2_create_buffers.__slots__ = [
    'index',
    'count',
    'memory',
    'format',
    'capabilities',
    'flags',
    'reserved',
]
struct_v4l2_create_buffers._fields_ = [
    ('index', __u32),
    ('count', __u32),
    ('memory', __u32),
    ('format', struct_v4l2_format),
    ('capabilities', __u32),
    ('flags', __u32),
    ('reserved', __u32 * int(6)),
]

# /home/tomba/tmp/khdrs/include/linux/media.h: 26
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 163
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 179
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 190
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 194
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 161
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 149
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 211
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 227
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 234
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 282
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 291
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 302
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 296
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 317
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 325
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

# /home/tomba/tmp/khdrs/include/linux/media.h: 333
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 43
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 37
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

enum_v4l2_mbus_pixelcode = c_int# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_FIXED = 0x0001# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB444_2X8_PADHI_BE = 0x1001# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB444_2X8_PADHI_LE = 0x1002# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB555_2X8_PADHI_BE = 0x1003# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB555_2X8_PADHI_LE = 0x1004# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_BGR565_2X8_BE = 0x1005# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_BGR565_2X8_LE = 0x1006# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB565_2X8_BE = 0x1007# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB565_2X8_LE = 0x1008# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB666_1X18 = 0x1009# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB888_1X24 = 0x100a# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB888_2X12_BE = 0x100b# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_RGB888_2X12_LE = 0x100c# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_ARGB8888_1X32 = 0x100d# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_Y8_1X8 = 0x2001# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_UV8_1X8 = 0x2015# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_UYVY8_1_5X8 = 0x2002# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_VYUY8_1_5X8 = 0x2003# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YUYV8_1_5X8 = 0x2004# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YVYU8_1_5X8 = 0x2005# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_UYVY8_2X8 = 0x2006# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_VYUY8_2X8 = 0x2007# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YUYV8_2X8 = 0x2008# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YVYU8_2X8 = 0x2009# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_Y10_1X10 = 0x200a# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_UYVY10_2X10 = 0x2018# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_VYUY10_2X10 = 0x2019# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YUYV10_2X10 = 0x200b# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YVYU10_2X10 = 0x200c# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_Y12_1X12 = 0x2013# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_UYVY8_1X16 = 0x200f# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_VYUY8_1X16 = 0x2010# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YUYV8_1X16 = 0x2011# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YVYU8_1X16 = 0x2012# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YDYUYDYV8_1X16 = 0x2014# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_UYVY10_1X20 = 0x201a# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_VYUY10_1X20 = 0x201b# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YUYV10_1X20 = 0x200d# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YVYU10_1X20 = 0x200e# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YUV10_1X30 = 0x2016# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_AYUV8_1X32 = 0x2017# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_UYVY12_2X12 = 0x201c# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_VYUY12_2X12 = 0x201d# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YUYV12_2X12 = 0x201e# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YVYU12_2X12 = 0x201f# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_UYVY12_1X24 = 0x2020# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_VYUY12_1X24 = 0x2021# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YUYV12_1X24 = 0x2022# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_YVYU12_1X24 = 0x2023# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SBGGR8_1X8 = 0x3001# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGBRG8_1X8 = 0x3013# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGRBG8_1X8 = 0x3002# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SRGGB8_1X8 = 0x3014# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SBGGR10_ALAW8_1X8 = 0x3015# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGBRG10_ALAW8_1X8 = 0x3016# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGRBG10_ALAW8_1X8 = 0x3017# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SRGGB10_ALAW8_1X8 = 0x3018# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SBGGR10_DPCM8_1X8 = 0x300b# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGBRG10_DPCM8_1X8 = 0x300c# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGRBG10_DPCM8_1X8 = 0x3009# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SRGGB10_DPCM8_1X8 = 0x300d# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SBGGR10_2X8_PADHI_BE = 0x3003# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SBGGR10_2X8_PADHI_LE = 0x3004# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SBGGR10_2X8_PADLO_BE = 0x3005# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SBGGR10_2X8_PADLO_LE = 0x3006# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SBGGR10_1X10 = 0x3007# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGBRG10_1X10 = 0x300e# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGRBG10_1X10 = 0x300a# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SRGGB10_1X10 = 0x300f# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SBGGR12_1X12 = 0x3008# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGBRG12_1X12 = 0x3010# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SGRBG12_1X12 = 0x3011# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_SRGGB12_1X12 = 0x3012# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_JPEG_1X8 = 0x4001# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_S5C_UYVY_JPEG_1X8 = 0x5001# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

V4L2_MBUS_FMT_AHSV8888_1X32 = 0x6001# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 67

enum_v4l2_subdev_format_whence = c_int# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 25

V4L2_SUBDEV_FORMAT_TRY = 0# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 25

V4L2_SUBDEV_FORMAT_ACTIVE = 1# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 25

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 38
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 54
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 78
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 101
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 121
class struct_v4l2_subdev_frame_interval(Structure):
    pass

struct_v4l2_subdev_frame_interval.__slots__ = [
    'pad',
    'interval',
    'stream',
    'reserved',
]
struct_v4l2_subdev_frame_interval._fields_ = [
    ('pad', __u32),
    ('interval', struct_v4l2_fract),
    ('stream', __u32),
    ('reserved', __u32 * int(8)),
]

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 140
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 168
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 184
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 212
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

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 229
class struct_v4l2_subdev_routing(Structure):
    pass

struct_v4l2_subdev_routing.__slots__ = [
    'which',
    'num_routes',
    'routes',
    'reserved',
]
struct_v4l2_subdev_routing._fields_ = [
    ('which', __u32),
    ('num_routes', __u32),
    ('routes', __u64),
    ('reserved', __u32 * int(6)),
]

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 250
class struct_v4l2_subdev_client_capability(Structure):
    pass

struct_v4l2_subdev_client_capability.__slots__ = [
    'capabilities',
]
struct_v4l2_subdev_client_capability._fields_ = [
    ('capabilities', __u64),
]

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 23
try:
    _IOC_NRBITS = 8
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 24
try:
    _IOC_TYPEBITS = 8
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 32
try:
    _IOC_SIZEBITS = 14
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 44
try:
    _IOC_NRSHIFT = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 45
try:
    _IOC_TYPESHIFT = (_IOC_NRSHIFT + _IOC_NRBITS)
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 46
try:
    _IOC_SIZESHIFT = (_IOC_TYPESHIFT + _IOC_TYPEBITS)
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 47
try:
    _IOC_DIRSHIFT = (_IOC_SIZESHIFT + _IOC_SIZEBITS)
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 58
try:
    _IOC_NONE = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 62
try:
    _IOC_WRITE = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 66
try:
    _IOC_READ = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 69
def _IOC(dir, type, nr, size):
    return ((((dir << _IOC_DIRSHIFT) | (ord(type) << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 75
def _IOC_TYPECHECK(t):
    return sizeof(t)

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 83
def _IO(type, nr):
    return (_IOC (_IOC_NONE, type, nr, 0))

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 84
def _IOR(type, nr, size):
    return (_IOC (_IOC_READ, type, nr, (_IOC_TYPECHECK (size))))

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 85
def _IOW(type, nr, size):
    return (_IOC (_IOC_WRITE, type, nr, (_IOC_TYPECHECK (size))))

# /home/tomba/tmp/khdrs/include/asm-generic/ioctl.h: 86
def _IOWR(type, nr, size):
    return (_IOC ((_IOC_READ | _IOC_WRITE), type, nr, (_IOC_TYPECHECK (size))))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 71
try:
    VIDEO_MAX_FRAME = 32
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 72
try:
    VIDEO_MAX_PLANES = 8
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 79
def v4l2_fourcc(a, b, c, d):
    return ((((__u32 (ord_if_char(a))).value | ((__u32 (ord_if_char(b))).value << 8)) | ((__u32 (ord_if_char(c))).value << 16)) | ((__u32 (ord_if_char(d))).value << 24))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 81
def v4l2_fourcc_be(a, b, c, d):
    return ((v4l2_fourcc (a, b, c, d)) | (1 << 31))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 107
def V4L2_FIELD_HAS_TOP(field):
    return ((((((field == V4L2_FIELD_TOP) or (field == V4L2_FIELD_INTERLACED)) or (field == V4L2_FIELD_INTERLACED_TB)) or (field == V4L2_FIELD_INTERLACED_BT)) or (field == V4L2_FIELD_SEQ_TB)) or (field == V4L2_FIELD_SEQ_BT))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 114
def V4L2_FIELD_HAS_BOTTOM(field):
    return ((((((field == V4L2_FIELD_BOTTOM) or (field == V4L2_FIELD_INTERLACED)) or (field == V4L2_FIELD_INTERLACED_TB)) or (field == V4L2_FIELD_INTERLACED_BT)) or (field == V4L2_FIELD_SEQ_TB)) or (field == V4L2_FIELD_SEQ_BT))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 121
def V4L2_FIELD_HAS_BOTH(field):
    return (((((field == V4L2_FIELD_INTERLACED) or (field == V4L2_FIELD_INTERLACED_TB)) or (field == V4L2_FIELD_INTERLACED_BT)) or (field == V4L2_FIELD_SEQ_TB)) or (field == V4L2_FIELD_SEQ_BT))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 127
def V4L2_FIELD_HAS_T_OR_B(field):
    return (((field == V4L2_FIELD_BOTTOM) or (field == V4L2_FIELD_TOP)) or (field == V4L2_FIELD_ALTERNATE))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 131
def V4L2_FIELD_IS_INTERLACED(field):
    return (((field == V4L2_FIELD_INTERLACED) or (field == V4L2_FIELD_INTERLACED_TB)) or (field == V4L2_FIELD_INTERLACED_BT))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 135
def V4L2_FIELD_IS_SEQUENTIAL(field):
    return ((field == V4L2_FIELD_SEQ_TB) or (field == V4L2_FIELD_SEQ_BT))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 158
def V4L2_TYPE_IS_MULTIPLANAR(type):
    return ((type == V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE) or (type == V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 162
def V4L2_TYPE_IS_OUTPUT(type):
    return ((((((((type == V4L2_BUF_TYPE_VIDEO_OUTPUT) or (type == V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE)) or (type == V4L2_BUF_TYPE_VIDEO_OVERLAY)) or (type == V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY)) or (type == V4L2_BUF_TYPE_VBI_OUTPUT)) or (type == V4L2_BUF_TYPE_SLICED_VBI_OUTPUT)) or (type == V4L2_BUF_TYPE_SDR_OUTPUT)) or (type == V4L2_BUF_TYPE_META_OUTPUT))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 172
def V4L2_TYPE_IS_CAPTURE(type):
    return (not (V4L2_TYPE_IS_OUTPUT (type)))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 183
try:
    V4L2_TUNER_ADC = V4L2_TUNER_SDR
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 254
def V4L2_MAP_COLORSPACE_DEFAULT(is_sdtv, is_hdtv):
    return is_sdtv and V4L2_COLORSPACE_SMPTE170M or is_hdtv and V4L2_COLORSPACE_REC709 or V4L2_COLORSPACE_SRGB

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 291
def V4L2_MAP_XFER_FUNC_DEFAULT(colsp):
    return (colsp == V4L2_COLORSPACE_OPRGB) and V4L2_XFER_FUNC_OPRGB or (colsp == V4L2_COLORSPACE_SMPTE240M) and V4L2_XFER_FUNC_SMPTE240M or (colsp == V4L2_COLORSPACE_DCI_P3) and V4L2_XFER_FUNC_DCI_P3 or (colsp == V4L2_COLORSPACE_RAW) and V4L2_XFER_FUNC_NONE or ((colsp == V4L2_COLORSPACE_SRGB) or (colsp == V4L2_COLORSPACE_JPEG)) and V4L2_XFER_FUNC_SRGB or V4L2_XFER_FUNC_709

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 362
def V4L2_MAP_YCBCR_ENC_DEFAULT(colsp):
    return ((colsp == V4L2_COLORSPACE_REC709) or (colsp == V4L2_COLORSPACE_DCI_P3)) and V4L2_YCBCR_ENC_709 or (colsp == V4L2_COLORSPACE_BT2020) and V4L2_YCBCR_ENC_BT2020 or (colsp == V4L2_COLORSPACE_SMPTE240M) and V4L2_YCBCR_ENC_SMPTE240M or V4L2_YCBCR_ENC_601

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 386
def V4L2_MAP_QUANTIZATION_DEFAULT(is_rgb_or_hsv, colsp, ycbcr_enc):
    return (is_rgb_or_hsv or (colsp == V4L2_COLORSPACE_JPEG)) and V4L2_QUANTIZATION_FULL_RANGE or V4L2_QUANTIZATION_LIM_RANGE

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 396
try:
    V4L2_COLORSPACE_ADOBERGB = V4L2_COLORSPACE_OPRGB
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 397
try:
    V4L2_XFER_FUNC_ADOBERGB = V4L2_XFER_FUNC_OPRGB
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 446
try:
    V4L2_CAP_VIDEO_CAPTURE = 0x00000001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 447
try:
    V4L2_CAP_VIDEO_OUTPUT = 0x00000002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 448
try:
    V4L2_CAP_VIDEO_OVERLAY = 0x00000004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 449
try:
    V4L2_CAP_VBI_CAPTURE = 0x00000010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 450
try:
    V4L2_CAP_VBI_OUTPUT = 0x00000020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 451
try:
    V4L2_CAP_SLICED_VBI_CAPTURE = 0x00000040
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 452
try:
    V4L2_CAP_SLICED_VBI_OUTPUT = 0x00000080
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 453
try:
    V4L2_CAP_RDS_CAPTURE = 0x00000100
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 454
try:
    V4L2_CAP_VIDEO_OUTPUT_OVERLAY = 0x00000200
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 455
try:
    V4L2_CAP_HW_FREQ_SEEK = 0x00000400
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 456
try:
    V4L2_CAP_RDS_OUTPUT = 0x00000800
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 459
try:
    V4L2_CAP_VIDEO_CAPTURE_MPLANE = 0x00001000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 461
try:
    V4L2_CAP_VIDEO_OUTPUT_MPLANE = 0x00002000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 463
try:
    V4L2_CAP_VIDEO_M2M_MPLANE = 0x00004000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 465
try:
    V4L2_CAP_VIDEO_M2M = 0x00008000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 467
try:
    V4L2_CAP_TUNER = 0x00010000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 468
try:
    V4L2_CAP_AUDIO = 0x00020000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 469
try:
    V4L2_CAP_RADIO = 0x00040000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 470
try:
    V4L2_CAP_MODULATOR = 0x00080000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 472
try:
    V4L2_CAP_SDR_CAPTURE = 0x00100000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 473
try:
    V4L2_CAP_EXT_PIX_FORMAT = 0x00200000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 474
try:
    V4L2_CAP_SDR_OUTPUT = 0x00400000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 475
try:
    V4L2_CAP_META_CAPTURE = 0x00800000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 477
try:
    V4L2_CAP_READWRITE = 0x01000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 478
try:
    V4L2_CAP_STREAMING = 0x04000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 479
try:
    V4L2_CAP_META_OUTPUT = 0x08000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 481
try:
    V4L2_CAP_TOUCH = 0x10000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 483
try:
    V4L2_CAP_IO_MC = 0x20000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 485
try:
    V4L2_CAP_DEVICE_CAPS = 0x80000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 513
try:
    V4L2_PIX_FMT_RGB332 = (v4l2_fourcc ('R', 'G', 'B', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 514
try:
    V4L2_PIX_FMT_RGB444 = (v4l2_fourcc ('R', '4', '4', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 515
try:
    V4L2_PIX_FMT_ARGB444 = (v4l2_fourcc ('A', 'R', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 516
try:
    V4L2_PIX_FMT_XRGB444 = (v4l2_fourcc ('X', 'R', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 517
try:
    V4L2_PIX_FMT_RGBA444 = (v4l2_fourcc ('R', 'A', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 518
try:
    V4L2_PIX_FMT_RGBX444 = (v4l2_fourcc ('R', 'X', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 519
try:
    V4L2_PIX_FMT_ABGR444 = (v4l2_fourcc ('A', 'B', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 520
try:
    V4L2_PIX_FMT_XBGR444 = (v4l2_fourcc ('X', 'B', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 521
try:
    V4L2_PIX_FMT_BGRA444 = (v4l2_fourcc ('G', 'A', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 522
try:
    V4L2_PIX_FMT_BGRX444 = (v4l2_fourcc ('B', 'X', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 523
try:
    V4L2_PIX_FMT_RGB555 = (v4l2_fourcc ('R', 'G', 'B', 'O'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 524
try:
    V4L2_PIX_FMT_ARGB555 = (v4l2_fourcc ('A', 'R', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 525
try:
    V4L2_PIX_FMT_XRGB555 = (v4l2_fourcc ('X', 'R', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 526
try:
    V4L2_PIX_FMT_RGBA555 = (v4l2_fourcc ('R', 'A', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 527
try:
    V4L2_PIX_FMT_RGBX555 = (v4l2_fourcc ('R', 'X', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 528
try:
    V4L2_PIX_FMT_ABGR555 = (v4l2_fourcc ('A', 'B', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 529
try:
    V4L2_PIX_FMT_XBGR555 = (v4l2_fourcc ('X', 'B', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 530
try:
    V4L2_PIX_FMT_BGRA555 = (v4l2_fourcc ('B', 'A', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 531
try:
    V4L2_PIX_FMT_BGRX555 = (v4l2_fourcc ('B', 'X', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 532
try:
    V4L2_PIX_FMT_RGB565 = (v4l2_fourcc ('R', 'G', 'B', 'P'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 533
try:
    V4L2_PIX_FMT_RGB555X = (v4l2_fourcc ('R', 'G', 'B', 'Q'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 534
try:
    V4L2_PIX_FMT_ARGB555X = (v4l2_fourcc_be ('A', 'R', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 535
try:
    V4L2_PIX_FMT_XRGB555X = (v4l2_fourcc_be ('X', 'R', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 536
try:
    V4L2_PIX_FMT_RGB565X = (v4l2_fourcc ('R', 'G', 'B', 'R'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 539
try:
    V4L2_PIX_FMT_BGR666 = (v4l2_fourcc ('B', 'G', 'R', 'H'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 540
try:
    V4L2_PIX_FMT_BGR24 = (v4l2_fourcc ('B', 'G', 'R', '3'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 541
try:
    V4L2_PIX_FMT_RGB24 = (v4l2_fourcc ('R', 'G', 'B', '3'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 542
try:
    V4L2_PIX_FMT_BGR32 = (v4l2_fourcc ('B', 'G', 'R', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 543
try:
    V4L2_PIX_FMT_ABGR32 = (v4l2_fourcc ('A', 'R', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 544
try:
    V4L2_PIX_FMT_XBGR32 = (v4l2_fourcc ('X', 'R', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 545
try:
    V4L2_PIX_FMT_BGRA32 = (v4l2_fourcc ('R', 'A', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 546
try:
    V4L2_PIX_FMT_BGRX32 = (v4l2_fourcc ('R', 'X', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 547
try:
    V4L2_PIX_FMT_RGB32 = (v4l2_fourcc ('R', 'G', 'B', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 548
try:
    V4L2_PIX_FMT_RGBA32 = (v4l2_fourcc ('A', 'B', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 549
try:
    V4L2_PIX_FMT_RGBX32 = (v4l2_fourcc ('X', 'B', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 550
try:
    V4L2_PIX_FMT_ARGB32 = (v4l2_fourcc ('B', 'A', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 551
try:
    V4L2_PIX_FMT_XRGB32 = (v4l2_fourcc ('B', 'X', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 552
try:
    V4L2_PIX_FMT_RGBX1010102 = (v4l2_fourcc ('R', 'X', '3', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 553
try:
    V4L2_PIX_FMT_RGBA1010102 = (v4l2_fourcc ('R', 'A', '3', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 554
try:
    V4L2_PIX_FMT_ARGB2101010 = (v4l2_fourcc ('A', 'R', '3', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 557
try:
    V4L2_PIX_FMT_BGR48_12 = (v4l2_fourcc ('B', '3', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 558
try:
    V4L2_PIX_FMT_ABGR64_12 = (v4l2_fourcc ('B', '4', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 561
try:
    V4L2_PIX_FMT_GREY = (v4l2_fourcc ('G', 'R', 'E', 'Y'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 562
try:
    V4L2_PIX_FMT_Y4 = (v4l2_fourcc ('Y', '0', '4', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 563
try:
    V4L2_PIX_FMT_Y6 = (v4l2_fourcc ('Y', '0', '6', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 564
try:
    V4L2_PIX_FMT_Y10 = (v4l2_fourcc ('Y', '1', '0', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 565
try:
    V4L2_PIX_FMT_Y12 = (v4l2_fourcc ('Y', '1', '2', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 566
try:
    V4L2_PIX_FMT_Y012 = (v4l2_fourcc ('Y', '0', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 567
try:
    V4L2_PIX_FMT_Y14 = (v4l2_fourcc ('Y', '1', '4', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 568
try:
    V4L2_PIX_FMT_Y16 = (v4l2_fourcc ('Y', '1', '6', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 569
try:
    V4L2_PIX_FMT_Y16_BE = (v4l2_fourcc_be ('Y', '1', '6', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 572
try:
    V4L2_PIX_FMT_Y10BPACK = (v4l2_fourcc ('Y', '1', '0', 'B'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 573
try:
    V4L2_PIX_FMT_Y10P = (v4l2_fourcc ('Y', '1', '0', 'P'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 574
try:
    V4L2_PIX_FMT_IPU3_Y10 = (v4l2_fourcc ('i', 'p', '3', 'y'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 577
try:
    V4L2_PIX_FMT_PAL8 = (v4l2_fourcc ('P', 'A', 'L', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 580
try:
    V4L2_PIX_FMT_UV8 = (v4l2_fourcc ('U', 'V', '8', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 583
try:
    V4L2_PIX_FMT_YUYV = (v4l2_fourcc ('Y', 'U', 'Y', 'V'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 584
try:
    V4L2_PIX_FMT_YYUV = (v4l2_fourcc ('Y', 'Y', 'U', 'V'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 585
try:
    V4L2_PIX_FMT_YVYU = (v4l2_fourcc ('Y', 'V', 'Y', 'U'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 586
try:
    V4L2_PIX_FMT_UYVY = (v4l2_fourcc ('U', 'Y', 'V', 'Y'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 587
try:
    V4L2_PIX_FMT_VYUY = (v4l2_fourcc ('V', 'Y', 'U', 'Y'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 588
try:
    V4L2_PIX_FMT_Y41P = (v4l2_fourcc ('Y', '4', '1', 'P'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 589
try:
    V4L2_PIX_FMT_YUV444 = (v4l2_fourcc ('Y', '4', '4', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 590
try:
    V4L2_PIX_FMT_YUV555 = (v4l2_fourcc ('Y', 'U', 'V', 'O'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 591
try:
    V4L2_PIX_FMT_YUV565 = (v4l2_fourcc ('Y', 'U', 'V', 'P'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 592
try:
    V4L2_PIX_FMT_YUV24 = (v4l2_fourcc ('Y', 'U', 'V', '3'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 593
try:
    V4L2_PIX_FMT_YUV32 = (v4l2_fourcc ('Y', 'U', 'V', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 594
try:
    V4L2_PIX_FMT_AYUV32 = (v4l2_fourcc ('A', 'Y', 'U', 'V'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 595
try:
    V4L2_PIX_FMT_XYUV32 = (v4l2_fourcc ('X', 'Y', 'U', 'V'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 596
try:
    V4L2_PIX_FMT_VUYA32 = (v4l2_fourcc ('V', 'U', 'Y', 'A'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 597
try:
    V4L2_PIX_FMT_VUYX32 = (v4l2_fourcc ('V', 'U', 'Y', 'X'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 598
try:
    V4L2_PIX_FMT_YUVA32 = (v4l2_fourcc ('Y', 'U', 'V', 'A'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 599
try:
    V4L2_PIX_FMT_YUVX32 = (v4l2_fourcc ('Y', 'U', 'V', 'X'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 600
try:
    V4L2_PIX_FMT_M420 = (v4l2_fourcc ('M', '4', '2', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 601
try:
    V4L2_PIX_FMT_YUV48_12 = (v4l2_fourcc ('Y', '3', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 607
try:
    V4L2_PIX_FMT_Y210 = (v4l2_fourcc ('Y', '2', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 608
try:
    V4L2_PIX_FMT_Y212 = (v4l2_fourcc ('Y', '2', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 609
try:
    V4L2_PIX_FMT_Y216 = (v4l2_fourcc ('Y', '2', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 612
try:
    V4L2_PIX_FMT_NV12 = (v4l2_fourcc ('N', 'V', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 613
try:
    V4L2_PIX_FMT_NV21 = (v4l2_fourcc ('N', 'V', '2', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 614
try:
    V4L2_PIX_FMT_NV16 = (v4l2_fourcc ('N', 'V', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 615
try:
    V4L2_PIX_FMT_NV61 = (v4l2_fourcc ('N', 'V', '6', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 616
try:
    V4L2_PIX_FMT_NV24 = (v4l2_fourcc ('N', 'V', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 617
try:
    V4L2_PIX_FMT_NV42 = (v4l2_fourcc ('N', 'V', '4', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 618
try:
    V4L2_PIX_FMT_P010 = (v4l2_fourcc ('P', '0', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 619
try:
    V4L2_PIX_FMT_P012 = (v4l2_fourcc ('P', '0', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 622
try:
    V4L2_PIX_FMT_NV12M = (v4l2_fourcc ('N', 'M', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 623
try:
    V4L2_PIX_FMT_NV21M = (v4l2_fourcc ('N', 'M', '2', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 624
try:
    V4L2_PIX_FMT_NV16M = (v4l2_fourcc ('N', 'M', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 625
try:
    V4L2_PIX_FMT_NV61M = (v4l2_fourcc ('N', 'M', '6', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 626
try:
    V4L2_PIX_FMT_P012M = (v4l2_fourcc ('P', 'M', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 629
try:
    V4L2_PIX_FMT_YUV410 = (v4l2_fourcc ('Y', 'U', 'V', '9'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 630
try:
    V4L2_PIX_FMT_YVU410 = (v4l2_fourcc ('Y', 'V', 'U', '9'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 631
try:
    V4L2_PIX_FMT_YUV411P = (v4l2_fourcc ('4', '1', '1', 'P'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 632
try:
    V4L2_PIX_FMT_YUV420 = (v4l2_fourcc ('Y', 'U', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 633
try:
    V4L2_PIX_FMT_YVU420 = (v4l2_fourcc ('Y', 'V', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 634
try:
    V4L2_PIX_FMT_YUV422P = (v4l2_fourcc ('4', '2', '2', 'P'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 637
try:
    V4L2_PIX_FMT_YUV420M = (v4l2_fourcc ('Y', 'M', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 638
try:
    V4L2_PIX_FMT_YVU420M = (v4l2_fourcc ('Y', 'M', '2', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 639
try:
    V4L2_PIX_FMT_YUV422M = (v4l2_fourcc ('Y', 'M', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 640
try:
    V4L2_PIX_FMT_YVU422M = (v4l2_fourcc ('Y', 'M', '6', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 641
try:
    V4L2_PIX_FMT_YUV444M = (v4l2_fourcc ('Y', 'M', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 642
try:
    V4L2_PIX_FMT_YVU444M = (v4l2_fourcc ('Y', 'M', '4', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 645
try:
    V4L2_PIX_FMT_NV12_4L4 = (v4l2_fourcc ('V', 'T', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 646
try:
    V4L2_PIX_FMT_NV12_16L16 = (v4l2_fourcc ('H', 'M', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 647
try:
    V4L2_PIX_FMT_NV12_32L32 = (v4l2_fourcc ('S', 'T', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 648
try:
    V4L2_PIX_FMT_NV15_4L4 = (v4l2_fourcc ('V', 'T', '1', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 649
try:
    V4L2_PIX_FMT_P010_4L4 = (v4l2_fourcc ('T', '0', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 650
try:
    V4L2_PIX_FMT_NV12_8L128 = (v4l2_fourcc ('A', 'T', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 651
try:
    V4L2_PIX_FMT_NV12_10BE_8L128 = (v4l2_fourcc_be ('A', 'X', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 654
try:
    V4L2_PIX_FMT_NV12MT = (v4l2_fourcc ('T', 'M', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 655
try:
    V4L2_PIX_FMT_NV12MT_16X16 = (v4l2_fourcc ('V', 'M', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 656
try:
    V4L2_PIX_FMT_NV12M_8L128 = (v4l2_fourcc ('N', 'A', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 657
try:
    V4L2_PIX_FMT_NV12M_10BE_8L128 = (v4l2_fourcc_be ('N', 'T', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 660
try:
    V4L2_PIX_FMT_SBGGR8 = (v4l2_fourcc ('B', 'A', '8', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 661
try:
    V4L2_PIX_FMT_SGBRG8 = (v4l2_fourcc ('G', 'B', 'R', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 662
try:
    V4L2_PIX_FMT_SGRBG8 = (v4l2_fourcc ('G', 'R', 'B', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 663
try:
    V4L2_PIX_FMT_SRGGB8 = (v4l2_fourcc ('R', 'G', 'G', 'B'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 664
try:
    V4L2_PIX_FMT_SBGGR10 = (v4l2_fourcc ('B', 'G', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 665
try:
    V4L2_PIX_FMT_SGBRG10 = (v4l2_fourcc ('G', 'B', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 666
try:
    V4L2_PIX_FMT_SGRBG10 = (v4l2_fourcc ('B', 'A', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 667
try:
    V4L2_PIX_FMT_SRGGB10 = (v4l2_fourcc ('R', 'G', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 669
try:
    V4L2_PIX_FMT_SBGGR10P = (v4l2_fourcc ('p', 'B', 'A', 'A'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 670
try:
    V4L2_PIX_FMT_SGBRG10P = (v4l2_fourcc ('p', 'G', 'A', 'A'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 671
try:
    V4L2_PIX_FMT_SGRBG10P = (v4l2_fourcc ('p', 'g', 'A', 'A'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 672
try:
    V4L2_PIX_FMT_SRGGB10P = (v4l2_fourcc ('p', 'R', 'A', 'A'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 674
try:
    V4L2_PIX_FMT_SBGGR10ALAW8 = (v4l2_fourcc ('a', 'B', 'A', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 675
try:
    V4L2_PIX_FMT_SGBRG10ALAW8 = (v4l2_fourcc ('a', 'G', 'A', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 676
try:
    V4L2_PIX_FMT_SGRBG10ALAW8 = (v4l2_fourcc ('a', 'g', 'A', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 677
try:
    V4L2_PIX_FMT_SRGGB10ALAW8 = (v4l2_fourcc ('a', 'R', 'A', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 679
try:
    V4L2_PIX_FMT_SBGGR10DPCM8 = (v4l2_fourcc ('b', 'B', 'A', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 680
try:
    V4L2_PIX_FMT_SGBRG10DPCM8 = (v4l2_fourcc ('b', 'G', 'A', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 681
try:
    V4L2_PIX_FMT_SGRBG10DPCM8 = (v4l2_fourcc ('B', 'D', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 682
try:
    V4L2_PIX_FMT_SRGGB10DPCM8 = (v4l2_fourcc ('b', 'R', 'A', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 683
try:
    V4L2_PIX_FMT_SBGGR12 = (v4l2_fourcc ('B', 'G', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 684
try:
    V4L2_PIX_FMT_SGBRG12 = (v4l2_fourcc ('G', 'B', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 685
try:
    V4L2_PIX_FMT_SGRBG12 = (v4l2_fourcc ('B', 'A', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 686
try:
    V4L2_PIX_FMT_SRGGB12 = (v4l2_fourcc ('R', 'G', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 688
try:
    V4L2_PIX_FMT_SBGGR12P = (v4l2_fourcc ('p', 'B', 'C', 'C'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 689
try:
    V4L2_PIX_FMT_SGBRG12P = (v4l2_fourcc ('p', 'G', 'C', 'C'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 690
try:
    V4L2_PIX_FMT_SGRBG12P = (v4l2_fourcc ('p', 'g', 'C', 'C'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 691
try:
    V4L2_PIX_FMT_SRGGB12P = (v4l2_fourcc ('p', 'R', 'C', 'C'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 692
try:
    V4L2_PIX_FMT_SBGGR14 = (v4l2_fourcc ('B', 'G', '1', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 693
try:
    V4L2_PIX_FMT_SGBRG14 = (v4l2_fourcc ('G', 'B', '1', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 694
try:
    V4L2_PIX_FMT_SGRBG14 = (v4l2_fourcc ('G', 'R', '1', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 695
try:
    V4L2_PIX_FMT_SRGGB14 = (v4l2_fourcc ('R', 'G', '1', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 697
try:
    V4L2_PIX_FMT_SBGGR14P = (v4l2_fourcc ('p', 'B', 'E', 'E'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 698
try:
    V4L2_PIX_FMT_SGBRG14P = (v4l2_fourcc ('p', 'G', 'E', 'E'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 699
try:
    V4L2_PIX_FMT_SGRBG14P = (v4l2_fourcc ('p', 'g', 'E', 'E'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 700
try:
    V4L2_PIX_FMT_SRGGB14P = (v4l2_fourcc ('p', 'R', 'E', 'E'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 701
try:
    V4L2_PIX_FMT_SBGGR16 = (v4l2_fourcc ('B', 'Y', 'R', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 702
try:
    V4L2_PIX_FMT_SGBRG16 = (v4l2_fourcc ('G', 'B', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 703
try:
    V4L2_PIX_FMT_SGRBG16 = (v4l2_fourcc ('G', 'R', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 704
try:
    V4L2_PIX_FMT_SRGGB16 = (v4l2_fourcc ('R', 'G', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 707
try:
    V4L2_PIX_FMT_HSV24 = (v4l2_fourcc ('H', 'S', 'V', '3'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 708
try:
    V4L2_PIX_FMT_HSV32 = (v4l2_fourcc ('H', 'S', 'V', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 711
try:
    V4L2_PIX_FMT_MJPEG = (v4l2_fourcc ('M', 'J', 'P', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 712
try:
    V4L2_PIX_FMT_JPEG = (v4l2_fourcc ('J', 'P', 'E', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 713
try:
    V4L2_PIX_FMT_DV = (v4l2_fourcc ('d', 'v', 's', 'd'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 714
try:
    V4L2_PIX_FMT_MPEG = (v4l2_fourcc ('M', 'P', 'E', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 715
try:
    V4L2_PIX_FMT_H264 = (v4l2_fourcc ('H', '2', '6', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 716
try:
    V4L2_PIX_FMT_H264_NO_SC = (v4l2_fourcc ('A', 'V', 'C', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 717
try:
    V4L2_PIX_FMT_H264_MVC = (v4l2_fourcc ('M', '2', '6', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 718
try:
    V4L2_PIX_FMT_H263 = (v4l2_fourcc ('H', '2', '6', '3'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 719
try:
    V4L2_PIX_FMT_MPEG1 = (v4l2_fourcc ('M', 'P', 'G', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 720
try:
    V4L2_PIX_FMT_MPEG2 = (v4l2_fourcc ('M', 'P', 'G', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 721
try:
    V4L2_PIX_FMT_MPEG2_SLICE = (v4l2_fourcc ('M', 'G', '2', 'S'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 722
try:
    V4L2_PIX_FMT_MPEG4 = (v4l2_fourcc ('M', 'P', 'G', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 723
try:
    V4L2_PIX_FMT_XVID = (v4l2_fourcc ('X', 'V', 'I', 'D'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 724
try:
    V4L2_PIX_FMT_VC1_ANNEX_G = (v4l2_fourcc ('V', 'C', '1', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 725
try:
    V4L2_PIX_FMT_VC1_ANNEX_L = (v4l2_fourcc ('V', 'C', '1', 'L'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 726
try:
    V4L2_PIX_FMT_VP8 = (v4l2_fourcc ('V', 'P', '8', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 727
try:
    V4L2_PIX_FMT_VP8_FRAME = (v4l2_fourcc ('V', 'P', '8', 'F'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 728
try:
    V4L2_PIX_FMT_VP9 = (v4l2_fourcc ('V', 'P', '9', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 729
try:
    V4L2_PIX_FMT_VP9_FRAME = (v4l2_fourcc ('V', 'P', '9', 'F'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 730
try:
    V4L2_PIX_FMT_HEVC = (v4l2_fourcc ('H', 'E', 'V', 'C'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 731
try:
    V4L2_PIX_FMT_FWHT = (v4l2_fourcc ('F', 'W', 'H', 'T'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 732
try:
    V4L2_PIX_FMT_FWHT_STATELESS = (v4l2_fourcc ('S', 'F', 'W', 'H'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 733
try:
    V4L2_PIX_FMT_H264_SLICE = (v4l2_fourcc ('S', '2', '6', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 734
try:
    V4L2_PIX_FMT_HEVC_SLICE = (v4l2_fourcc ('S', '2', '6', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 735
try:
    V4L2_PIX_FMT_AV1_FRAME = (v4l2_fourcc ('A', 'V', '1', 'F'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 736
try:
    V4L2_PIX_FMT_SPK = (v4l2_fourcc ('S', 'P', 'K', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 737
try:
    V4L2_PIX_FMT_RV30 = (v4l2_fourcc ('R', 'V', '3', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 738
try:
    V4L2_PIX_FMT_RV40 = (v4l2_fourcc ('R', 'V', '4', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 741
try:
    V4L2_PIX_FMT_CPIA1 = (v4l2_fourcc ('C', 'P', 'I', 'A'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 742
try:
    V4L2_PIX_FMT_WNVA = (v4l2_fourcc ('W', 'N', 'V', 'A'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 743
try:
    V4L2_PIX_FMT_SN9C10X = (v4l2_fourcc ('S', '9', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 744
try:
    V4L2_PIX_FMT_SN9C20X_I420 = (v4l2_fourcc ('S', '9', '2', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 745
try:
    V4L2_PIX_FMT_PWC1 = (v4l2_fourcc ('P', 'W', 'C', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 746
try:
    V4L2_PIX_FMT_PWC2 = (v4l2_fourcc ('P', 'W', 'C', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 747
try:
    V4L2_PIX_FMT_ET61X251 = (v4l2_fourcc ('E', '6', '2', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 748
try:
    V4L2_PIX_FMT_SPCA501 = (v4l2_fourcc ('S', '5', '0', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 749
try:
    V4L2_PIX_FMT_SPCA505 = (v4l2_fourcc ('S', '5', '0', '5'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 750
try:
    V4L2_PIX_FMT_SPCA508 = (v4l2_fourcc ('S', '5', '0', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 751
try:
    V4L2_PIX_FMT_SPCA561 = (v4l2_fourcc ('S', '5', '6', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 752
try:
    V4L2_PIX_FMT_PAC207 = (v4l2_fourcc ('P', '2', '0', '7'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 753
try:
    V4L2_PIX_FMT_MR97310A = (v4l2_fourcc ('M', '3', '1', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 754
try:
    V4L2_PIX_FMT_JL2005BCD = (v4l2_fourcc ('J', 'L', '2', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 755
try:
    V4L2_PIX_FMT_SN9C2028 = (v4l2_fourcc ('S', 'O', 'N', 'X'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 756
try:
    V4L2_PIX_FMT_SQ905C = (v4l2_fourcc ('9', '0', '5', 'C'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 757
try:
    V4L2_PIX_FMT_PJPG = (v4l2_fourcc ('P', 'J', 'P', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 758
try:
    V4L2_PIX_FMT_OV511 = (v4l2_fourcc ('O', '5', '1', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 759
try:
    V4L2_PIX_FMT_OV518 = (v4l2_fourcc ('O', '5', '1', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 760
try:
    V4L2_PIX_FMT_STV0680 = (v4l2_fourcc ('S', '6', '8', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 761
try:
    V4L2_PIX_FMT_TM6000 = (v4l2_fourcc ('T', 'M', '6', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 762
try:
    V4L2_PIX_FMT_CIT_YYVYUY = (v4l2_fourcc ('C', 'I', 'T', 'V'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 763
try:
    V4L2_PIX_FMT_KONICA420 = (v4l2_fourcc ('K', 'O', 'N', 'I'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 764
try:
    V4L2_PIX_FMT_JPGL = (v4l2_fourcc ('J', 'P', 'G', 'L'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 765
try:
    V4L2_PIX_FMT_SE401 = (v4l2_fourcc ('S', '4', '0', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 766
try:
    V4L2_PIX_FMT_S5C_UYVY_JPG = (v4l2_fourcc ('S', '5', 'C', 'I'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 767
try:
    V4L2_PIX_FMT_Y8I = (v4l2_fourcc ('Y', '8', 'I', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 768
try:
    V4L2_PIX_FMT_Y12I = (v4l2_fourcc ('Y', '1', '2', 'I'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 769
try:
    V4L2_PIX_FMT_Z16 = (v4l2_fourcc ('Z', '1', '6', ' '))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 770
try:
    V4L2_PIX_FMT_MT21C = (v4l2_fourcc ('M', 'T', '2', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 771
try:
    V4L2_PIX_FMT_MM21 = (v4l2_fourcc ('M', 'M', '2', '1'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 772
try:
    V4L2_PIX_FMT_MT2110T = (v4l2_fourcc ('M', 'T', '2', 'T'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 773
try:
    V4L2_PIX_FMT_MT2110R = (v4l2_fourcc ('M', 'T', '2', 'R'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 774
try:
    V4L2_PIX_FMT_INZI = (v4l2_fourcc ('I', 'N', 'Z', 'I'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 775
try:
    V4L2_PIX_FMT_CNF4 = (v4l2_fourcc ('C', 'N', 'F', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 776
try:
    V4L2_PIX_FMT_HI240 = (v4l2_fourcc ('H', 'I', '2', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 777
try:
    V4L2_PIX_FMT_QC08C = (v4l2_fourcc ('Q', '0', '8', 'C'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 778
try:
    V4L2_PIX_FMT_QC10C = (v4l2_fourcc ('Q', '1', '0', 'C'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 779
try:
    V4L2_PIX_FMT_AJPG = (v4l2_fourcc ('A', 'J', 'P', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 782
try:
    V4L2_PIX_FMT_IPU3_SBGGR10 = (v4l2_fourcc ('i', 'p', '3', 'b'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 783
try:
    V4L2_PIX_FMT_IPU3_SGBRG10 = (v4l2_fourcc ('i', 'p', '3', 'g'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 784
try:
    V4L2_PIX_FMT_IPU3_SGRBG10 = (v4l2_fourcc ('i', 'p', '3', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 785
try:
    V4L2_PIX_FMT_IPU3_SRGGB10 = (v4l2_fourcc ('i', 'p', '3', 'r'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 788
try:
    V4L2_SDR_FMT_CU8 = (v4l2_fourcc ('C', 'U', '0', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 789
try:
    V4L2_SDR_FMT_CU16LE = (v4l2_fourcc ('C', 'U', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 790
try:
    V4L2_SDR_FMT_CS8 = (v4l2_fourcc ('C', 'S', '0', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 791
try:
    V4L2_SDR_FMT_CS14LE = (v4l2_fourcc ('C', 'S', '1', '4'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 792
try:
    V4L2_SDR_FMT_RU12LE = (v4l2_fourcc ('R', 'U', '1', '2'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 793
try:
    V4L2_SDR_FMT_PCU16BE = (v4l2_fourcc ('P', 'C', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 794
try:
    V4L2_SDR_FMT_PCU18BE = (v4l2_fourcc ('P', 'C', '1', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 795
try:
    V4L2_SDR_FMT_PCU20BE = (v4l2_fourcc ('P', 'C', '2', '0'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 798
try:
    V4L2_TCH_FMT_DELTA_TD16 = (v4l2_fourcc ('T', 'D', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 799
try:
    V4L2_TCH_FMT_DELTA_TD08 = (v4l2_fourcc ('T', 'D', '0', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 800
try:
    V4L2_TCH_FMT_TU16 = (v4l2_fourcc ('T', 'U', '1', '6'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 801
try:
    V4L2_TCH_FMT_TU08 = (v4l2_fourcc ('T', 'U', '0', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 804
try:
    V4L2_META_FMT_VSP1_HGO = (v4l2_fourcc ('V', 'S', 'P', 'H'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 805
try:
    V4L2_META_FMT_VSP1_HGT = (v4l2_fourcc ('V', 'S', 'P', 'T'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 806
try:
    V4L2_META_FMT_UVC = (v4l2_fourcc ('U', 'V', 'C', 'H'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 807
try:
    V4L2_META_FMT_D4XX = (v4l2_fourcc ('D', '4', 'X', 'X'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 808
try:
    V4L2_META_FMT_VIVID = (v4l2_fourcc ('V', 'I', 'V', 'D'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 811
try:
    V4L2_META_FMT_RK_ISP1_PARAMS = (v4l2_fourcc ('R', 'K', '1', 'P'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 812
try:
    V4L2_META_FMT_RK_ISP1_STAT_3A = (v4l2_fourcc ('R', 'K', '1', 'S'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 814
try:
    V4L2_META_FMT_GENERIC_8 = (v4l2_fourcc ('M', 'E', 'T', '8'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 815
try:
    V4L2_META_FMT_GENERIC_CSI2_10 = (v4l2_fourcc ('M', 'C', '1', 'A'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 816
try:
    V4L2_META_FMT_GENERIC_CSI2_12 = (v4l2_fourcc ('M', 'C', '1', 'C'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 817
try:
    V4L2_META_FMT_GENERIC_CSI2_14 = (v4l2_fourcc ('M', 'C', '1', 'E'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 818
try:
    V4L2_META_FMT_GENERIC_CSI2_16 = (v4l2_fourcc ('M', 'C', '1', 'G'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 819
try:
    V4L2_META_FMT_GENERIC_CSI2_20 = (v4l2_fourcc ('M', 'C', '1', 'K'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 820
try:
    V4L2_META_FMT_GENERIC_CSI2_24 = (v4l2_fourcc ('M', 'C', '1', 'O'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 821
try:
    V4L2_META_FMT_GENERIC_CSI2_2_24 = (v4l2_fourcc ('M', 'C', '2', 'O'))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 824
try:
    V4L2_PIX_FMT_PRIV_MAGIC = 0xfeedcafe
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 827
try:
    V4L2_PIX_FMT_FLAG_PREMUL_ALPHA = 0x00000001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 828
try:
    V4L2_PIX_FMT_FLAG_SET_CSC = 0x00000002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 843
try:
    V4L2_FMT_FLAG_COMPRESSED = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 844
try:
    V4L2_FMT_FLAG_EMULATED = 0x0002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 845
try:
    V4L2_FMT_FLAG_CONTINUOUS_BYTESTREAM = 0x0004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 846
try:
    V4L2_FMT_FLAG_DYN_RESOLUTION = 0x0008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 847
try:
    V4L2_FMT_FLAG_ENC_CAP_FRAME_INTERVAL = 0x0010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 848
try:
    V4L2_FMT_FLAG_CSC_COLORSPACE = 0x0020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 849
try:
    V4L2_FMT_FLAG_CSC_XFER_FUNC = 0x0040
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 850
try:
    V4L2_FMT_FLAG_CSC_YCBCR_ENC = 0x0080
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 851
try:
    V4L2_FMT_FLAG_CSC_HSV_ENC = V4L2_FMT_FLAG_CSC_YCBCR_ENC
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 852
try:
    V4L2_FMT_FLAG_CSC_QUANTIZATION = 0x0100
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 853
try:
    V4L2_FMT_FLAG_META_LINE_BASED = 0x0200
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 936
try:
    V4L2_TC_TYPE_24FPS = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 937
try:
    V4L2_TC_TYPE_25FPS = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 938
try:
    V4L2_TC_TYPE_30FPS = 3
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 939
try:
    V4L2_TC_TYPE_50FPS = 4
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 940
try:
    V4L2_TC_TYPE_60FPS = 5
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 943
try:
    V4L2_TC_FLAG_DROPFRAME = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 944
try:
    V4L2_TC_FLAG_COLORFRAME = 0x0002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 945
try:
    V4L2_TC_USERBITS_field = 0x000C
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 946
try:
    V4L2_TC_USERBITS_USERDEFINED = 0x0000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 947
try:
    V4L2_TC_USERBITS_8BITCHARS = 0x0008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 971
try:
    V4L2_JPEG_MARKER_DHT = (1 << 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 972
try:
    V4L2_JPEG_MARKER_DQT = (1 << 4)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 973
try:
    V4L2_JPEG_MARKER_DRI = (1 << 5)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 974
try:
    V4L2_JPEG_MARKER_COM = (1 << 6)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 975
try:
    V4L2_JPEG_MARKER_APP = (1 << 7)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 993
try:
    V4L2_MEMORY_FLAG_NON_COHERENT = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 996
try:
    V4L2_BUF_CAP_SUPPORTS_MMAP = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 997
try:
    V4L2_BUF_CAP_SUPPORTS_USERPTR = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 998
try:
    V4L2_BUF_CAP_SUPPORTS_DMABUF = (1 << 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 999
try:
    V4L2_BUF_CAP_SUPPORTS_REQUESTS = (1 << 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1000
try:
    V4L2_BUF_CAP_SUPPORTS_ORPHANED_BUFS = (1 << 4)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1001
try:
    V4L2_BUF_CAP_SUPPORTS_M2M_HOLD_CAPTURE_BUF = (1 << 5)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1002
try:
    V4L2_BUF_CAP_SUPPORTS_MMAP_CACHE_HINTS = (1 << 6)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1113
try:
    V4L2_BUF_FLAG_MAPPED = 0x00000001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1115
try:
    V4L2_BUF_FLAG_QUEUED = 0x00000002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1117
try:
    V4L2_BUF_FLAG_DONE = 0x00000004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1119
try:
    V4L2_BUF_FLAG_KEYFRAME = 0x00000008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1121
try:
    V4L2_BUF_FLAG_PFRAME = 0x00000010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1123
try:
    V4L2_BUF_FLAG_BFRAME = 0x00000020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1125
try:
    V4L2_BUF_FLAG_ERROR = 0x00000040
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1127
try:
    V4L2_BUF_FLAG_IN_REQUEST = 0x00000080
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1129
try:
    V4L2_BUF_FLAG_TIMECODE = 0x00000100
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1131
try:
    V4L2_BUF_FLAG_M2M_HOLD_CAPTURE_BUF = 0x00000200
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1133
try:
    V4L2_BUF_FLAG_PREPARED = 0x00000400
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1135
try:
    V4L2_BUF_FLAG_NO_CACHE_INVALIDATE = 0x00000800
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1136
try:
    V4L2_BUF_FLAG_NO_CACHE_CLEAN = 0x00001000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1138
try:
    V4L2_BUF_FLAG_TIMESTAMP_MASK = 0x0000e000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1139
try:
    V4L2_BUF_FLAG_TIMESTAMP_UNKNOWN = 0x00000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1140
try:
    V4L2_BUF_FLAG_TIMESTAMP_MONOTONIC = 0x00002000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1141
try:
    V4L2_BUF_FLAG_TIMESTAMP_COPY = 0x00004000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1143
try:
    V4L2_BUF_FLAG_TSTAMP_SRC_MASK = 0x00070000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1144
try:
    V4L2_BUF_FLAG_TSTAMP_SRC_EOF = 0x00000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1145
try:
    V4L2_BUF_FLAG_TSTAMP_SRC_SOE = 0x00010000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1147
try:
    V4L2_BUF_FLAG_LAST = 0x00100000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1149
try:
    V4L2_BUF_FLAG_REQUEST_FD = 0x00800000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1200
try:
    V4L2_FBUF_CAP_EXTERNOVERLAY = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1201
try:
    V4L2_FBUF_CAP_CHROMAKEY = 0x0002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1202
try:
    V4L2_FBUF_CAP_LIST_CLIPPING = 0x0004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1203
try:
    V4L2_FBUF_CAP_BITMAP_CLIPPING = 0x0008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1204
try:
    V4L2_FBUF_CAP_LOCAL_ALPHA = 0x0010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1205
try:
    V4L2_FBUF_CAP_GLOBAL_ALPHA = 0x0020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1206
try:
    V4L2_FBUF_CAP_LOCAL_INV_ALPHA = 0x0040
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1207
try:
    V4L2_FBUF_CAP_SRC_CHROMAKEY = 0x0080
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1209
try:
    V4L2_FBUF_FLAG_PRIMARY = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1210
try:
    V4L2_FBUF_FLAG_OVERLAY = 0x0002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1211
try:
    V4L2_FBUF_FLAG_CHROMAKEY = 0x0004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1212
try:
    V4L2_FBUF_FLAG_LOCAL_ALPHA = 0x0008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1213
try:
    V4L2_FBUF_FLAG_GLOBAL_ALPHA = 0x0010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1214
try:
    V4L2_FBUF_FLAG_LOCAL_INV_ALPHA = 0x0020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1215
try:
    V4L2_FBUF_FLAG_SRC_CHROMAKEY = 0x0040
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1245
try:
    V4L2_MODE_HIGHQUALITY = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1246
try:
    V4L2_CAP_TIMEPERFRAME = 0x1000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1305
try:
    V4L2_STD_PAL_B = (v4l2_std_id (ord_if_char(0x00000001))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1306
try:
    V4L2_STD_PAL_B1 = (v4l2_std_id (ord_if_char(0x00000002))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1307
try:
    V4L2_STD_PAL_G = (v4l2_std_id (ord_if_char(0x00000004))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1308
try:
    V4L2_STD_PAL_H = (v4l2_std_id (ord_if_char(0x00000008))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1309
try:
    V4L2_STD_PAL_I = (v4l2_std_id (ord_if_char(0x00000010))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1310
try:
    V4L2_STD_PAL_D = (v4l2_std_id (ord_if_char(0x00000020))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1311
try:
    V4L2_STD_PAL_D1 = (v4l2_std_id (ord_if_char(0x00000040))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1312
try:
    V4L2_STD_PAL_K = (v4l2_std_id (ord_if_char(0x00000080))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1314
try:
    V4L2_STD_PAL_M = (v4l2_std_id (ord_if_char(0x00000100))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1315
try:
    V4L2_STD_PAL_N = (v4l2_std_id (ord_if_char(0x00000200))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1316
try:
    V4L2_STD_PAL_Nc = (v4l2_std_id (ord_if_char(0x00000400))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1317
try:
    V4L2_STD_PAL_60 = (v4l2_std_id (ord_if_char(0x00000800))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1319
try:
    V4L2_STD_NTSC_M = (v4l2_std_id (ord_if_char(0x00001000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1320
try:
    V4L2_STD_NTSC_M_JP = (v4l2_std_id (ord_if_char(0x00002000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1321
try:
    V4L2_STD_NTSC_443 = (v4l2_std_id (ord_if_char(0x00004000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1322
try:
    V4L2_STD_NTSC_M_KR = (v4l2_std_id (ord_if_char(0x00008000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1324
try:
    V4L2_STD_SECAM_B = (v4l2_std_id (ord_if_char(0x00010000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1325
try:
    V4L2_STD_SECAM_D = (v4l2_std_id (ord_if_char(0x00020000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1326
try:
    V4L2_STD_SECAM_G = (v4l2_std_id (ord_if_char(0x00040000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1327
try:
    V4L2_STD_SECAM_H = (v4l2_std_id (ord_if_char(0x00080000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1328
try:
    V4L2_STD_SECAM_K = (v4l2_std_id (ord_if_char(0x00100000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1329
try:
    V4L2_STD_SECAM_K1 = (v4l2_std_id (ord_if_char(0x00200000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1330
try:
    V4L2_STD_SECAM_L = (v4l2_std_id (ord_if_char(0x00400000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1331
try:
    V4L2_STD_SECAM_LC = (v4l2_std_id (ord_if_char(0x00800000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1334
try:
    V4L2_STD_ATSC_8_VSB = (v4l2_std_id (ord_if_char(0x01000000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1335
try:
    V4L2_STD_ATSC_16_VSB = (v4l2_std_id (ord_if_char(0x02000000))).value
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1355
try:
    V4L2_STD_NTSC = ((V4L2_STD_NTSC_M | V4L2_STD_NTSC_M_JP) | V4L2_STD_NTSC_M_KR)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1359
try:
    V4L2_STD_SECAM_DK = ((V4L2_STD_SECAM_D | V4L2_STD_SECAM_K) | V4L2_STD_SECAM_K1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1363
try:
    V4L2_STD_SECAM = (((((V4L2_STD_SECAM_B | V4L2_STD_SECAM_G) | V4L2_STD_SECAM_H) | V4L2_STD_SECAM_DK) | V4L2_STD_SECAM_L) | V4L2_STD_SECAM_LC)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1370
try:
    V4L2_STD_PAL_BG = ((V4L2_STD_PAL_B | V4L2_STD_PAL_B1) | V4L2_STD_PAL_G)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1373
try:
    V4L2_STD_PAL_DK = ((V4L2_STD_PAL_D | V4L2_STD_PAL_D1) | V4L2_STD_PAL_K)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1381
try:
    V4L2_STD_PAL = (((V4L2_STD_PAL_BG | V4L2_STD_PAL_DK) | V4L2_STD_PAL_H) | V4L2_STD_PAL_I)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1386
try:
    V4L2_STD_B = ((V4L2_STD_PAL_B | V4L2_STD_PAL_B1) | V4L2_STD_SECAM_B)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1389
try:
    V4L2_STD_G = (V4L2_STD_PAL_G | V4L2_STD_SECAM_G)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1391
try:
    V4L2_STD_H = (V4L2_STD_PAL_H | V4L2_STD_SECAM_H)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1393
try:
    V4L2_STD_L = (V4L2_STD_SECAM_L | V4L2_STD_SECAM_LC)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1395
try:
    V4L2_STD_GH = (V4L2_STD_G | V4L2_STD_H)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1397
try:
    V4L2_STD_DK = (V4L2_STD_PAL_DK | V4L2_STD_SECAM_DK)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1399
try:
    V4L2_STD_BG = (V4L2_STD_B | V4L2_STD_G)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1401
try:
    V4L2_STD_MN = (((V4L2_STD_PAL_M | V4L2_STD_PAL_N) | V4L2_STD_PAL_Nc) | V4L2_STD_NTSC)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1407
try:
    V4L2_STD_MTS = (((V4L2_STD_NTSC_M | V4L2_STD_PAL_M) | V4L2_STD_PAL_N) | V4L2_STD_PAL_Nc)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1413
try:
    V4L2_STD_525_60 = (((V4L2_STD_PAL_M | V4L2_STD_PAL_60) | V4L2_STD_NTSC) | V4L2_STD_NTSC_443)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1418
try:
    V4L2_STD_625_50 = (((V4L2_STD_PAL | V4L2_STD_PAL_N) | V4L2_STD_PAL_Nc) | V4L2_STD_SECAM)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1423
try:
    V4L2_STD_ATSC = (V4L2_STD_ATSC_8_VSB | V4L2_STD_ATSC_16_VSB)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1426
try:
    V4L2_STD_UNKNOWN = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1427
try:
    V4L2_STD_ALL = (V4L2_STD_525_60 | V4L2_STD_625_50)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1502
try:
    V4L2_DV_PROGRESSIVE = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1503
try:
    V4L2_DV_INTERLACED = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1506
try:
    V4L2_DV_VSYNC_POS_POL = 0x00000001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1507
try:
    V4L2_DV_HSYNC_POS_POL = 0x00000002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1510
try:
    V4L2_DV_BT_STD_CEA861 = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1511
try:
    V4L2_DV_BT_STD_DMT = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1512
try:
    V4L2_DV_BT_STD_CVT = (1 << 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1513
try:
    V4L2_DV_BT_STD_GTF = (1 << 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1514
try:
    V4L2_DV_BT_STD_SDI = (1 << 4)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1524
try:
    V4L2_DV_FL_REDUCED_BLANKING = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1530
try:
    V4L2_DV_FL_CAN_REDUCE_FPS = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1540
try:
    V4L2_DV_FL_REDUCED_FPS = (1 << 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1547
try:
    V4L2_DV_FL_HALF_LINE = (1 << 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1555
try:
    V4L2_DV_FL_IS_CE_VIDEO = (1 << 4)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1560
try:
    V4L2_DV_FL_FIRST_FIELD_EXTRA_LINE = (1 << 5)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1566
try:
    V4L2_DV_FL_HAS_PICTURE_ASPECT = (1 << 6)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1571
try:
    V4L2_DV_FL_HAS_CEA861_VIC = (1 << 7)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1577
try:
    V4L2_DV_FL_HAS_HDMI_VIC = (1 << 8)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1584
try:
    V4L2_DV_FL_CAN_DETECT_REDUCED_FPS = (1 << 9)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1587
def V4L2_DV_BT_BLANKING_WIDTH(bt):
    return ((((bt.contents.hfrontporch).value) + ((bt.contents.hsync).value)) + ((bt.contents.hbackporch).value))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1589
def V4L2_DV_BT_FRAME_WIDTH(bt):
    return (((bt.contents.width).value) + (V4L2_DV_BT_BLANKING_WIDTH (bt)))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1591
def V4L2_DV_BT_BLANKING_HEIGHT(bt):
    return (((((bt.contents.vfrontporch).value) + ((bt.contents.vsync).value)) + ((bt.contents.vbackporch).value)) + (bt.contents.interlaced) and ((((bt.contents.il_vfrontporch).value) + ((bt.contents.il_vsync).value)) + ((bt.contents.il_vbackporch).value)) or 0)

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1595
def V4L2_DV_BT_FRAME_HEIGHT(bt):
    return (((bt.contents.height).value) + (V4L2_DV_BT_BLANKING_HEIGHT (bt)))

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1611
try:
    V4L2_DV_BT_656_1120 = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1652
try:
    V4L2_DV_BT_CAP_INTERLACED = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1654
try:
    V4L2_DV_BT_CAP_PROGRESSIVE = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1656
try:
    V4L2_DV_BT_CAP_REDUCED_BLANKING = (1 << 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1658
try:
    V4L2_DV_BT_CAP_CUSTOM = (1 << 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1693
try:
    V4L2_INPUT_TYPE_TUNER = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1694
try:
    V4L2_INPUT_TYPE_CAMERA = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1695
try:
    V4L2_INPUT_TYPE_TOUCH = 3
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1698
try:
    V4L2_IN_ST_NO_POWER = 0x00000001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1699
try:
    V4L2_IN_ST_NO_SIGNAL = 0x00000002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1700
try:
    V4L2_IN_ST_NO_COLOR = 0x00000004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1704
try:
    V4L2_IN_ST_HFLIP = 0x00000010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1705
try:
    V4L2_IN_ST_VFLIP = 0x00000020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1708
try:
    V4L2_IN_ST_NO_H_LOCK = 0x00000100
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1709
try:
    V4L2_IN_ST_COLOR_KILL = 0x00000200
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1710
try:
    V4L2_IN_ST_NO_V_LOCK = 0x00000400
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1711
try:
    V4L2_IN_ST_NO_STD_LOCK = 0x00000800
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1714
try:
    V4L2_IN_ST_NO_SYNC = 0x00010000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1715
try:
    V4L2_IN_ST_NO_EQU = 0x00020000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1716
try:
    V4L2_IN_ST_NO_CARRIER = 0x00040000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1719
try:
    V4L2_IN_ST_MACROVISION = 0x01000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1720
try:
    V4L2_IN_ST_NO_ACCESS = 0x02000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1721
try:
    V4L2_IN_ST_VTR = 0x04000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1724
try:
    V4L2_IN_CAP_DV_TIMINGS = 0x00000002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1725
try:
    V4L2_IN_CAP_CUSTOM_TIMINGS = V4L2_IN_CAP_DV_TIMINGS
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1726
try:
    V4L2_IN_CAP_STD = 0x00000004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1727
try:
    V4L2_IN_CAP_NATIVE_SIZE = 0x00000008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1743
try:
    V4L2_OUTPUT_TYPE_MODULATOR = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1744
try:
    V4L2_OUTPUT_TYPE_ANALOG = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1745
try:
    V4L2_OUTPUT_TYPE_ANALOGVGAOVERLAY = 3
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1748
try:
    V4L2_OUT_CAP_DV_TIMINGS = 0x00000002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1749
try:
    V4L2_OUT_CAP_CUSTOM_TIMINGS = V4L2_OUT_CAP_DV_TIMINGS
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1750
try:
    V4L2_OUT_CAP_STD = 0x00000004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1751
try:
    V4L2_OUT_CAP_NATIVE_SIZE = 0x00000008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1813
try:
    V4L2_CTRL_ID_MASK = 0x0fffffff
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1814
def V4L2_CTRL_ID2CLASS(id):
    return (id & 0x0fff0000)

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1815
def V4L2_CTRL_ID2WHICH(id):
    return (id & 0x0fff0000)

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1816
def V4L2_CTRL_DRIVER_PRIV(id):
    return ((id & 0xffff) >= 0x1000)

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1817
try:
    V4L2_CTRL_MAX_DIMS = 4
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1818
try:
    V4L2_CTRL_WHICH_CUR_VAL = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1819
try:
    V4L2_CTRL_WHICH_DEF_VAL = 0x0f000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1820
try:
    V4L2_CTRL_WHICH_REQUEST_VAL = 0x0f010000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1915
try:
    V4L2_CTRL_FLAG_DISABLED = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1916
try:
    V4L2_CTRL_FLAG_GRABBED = 0x0002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1917
try:
    V4L2_CTRL_FLAG_READ_ONLY = 0x0004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1918
try:
    V4L2_CTRL_FLAG_UPDATE = 0x0008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1919
try:
    V4L2_CTRL_FLAG_INACTIVE = 0x0010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1920
try:
    V4L2_CTRL_FLAG_SLIDER = 0x0020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1921
try:
    V4L2_CTRL_FLAG_WRITE_ONLY = 0x0040
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1922
try:
    V4L2_CTRL_FLAG_VOLATILE = 0x0080
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1923
try:
    V4L2_CTRL_FLAG_HAS_PAYLOAD = 0x0100
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1924
try:
    V4L2_CTRL_FLAG_EXECUTE_ON_WRITE = 0x0200
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1925
try:
    V4L2_CTRL_FLAG_MODIFY_LAYOUT = 0x0400
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1926
try:
    V4L2_CTRL_FLAG_DYNAMIC_ARRAY = 0x0800
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1929
try:
    V4L2_CTRL_FLAG_NEXT_CTRL = 0x80000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1930
try:
    V4L2_CTRL_FLAG_NEXT_COMPOUND = 0x40000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1933
try:
    V4L2_CID_MAX_CTRLS = 1024
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1935
try:
    V4L2_CID_PRIVATE_BASE = 0x08000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1967
try:
    V4L2_TUNER_CAP_LOW = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1968
try:
    V4L2_TUNER_CAP_NORM = 0x0002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1969
try:
    V4L2_TUNER_CAP_HWSEEK_BOUNDED = 0x0004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1970
try:
    V4L2_TUNER_CAP_HWSEEK_WRAP = 0x0008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1971
try:
    V4L2_TUNER_CAP_STEREO = 0x0010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1972
try:
    V4L2_TUNER_CAP_LANG2 = 0x0020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1973
try:
    V4L2_TUNER_CAP_SAP = 0x0020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1974
try:
    V4L2_TUNER_CAP_LANG1 = 0x0040
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1975
try:
    V4L2_TUNER_CAP_RDS = 0x0080
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1976
try:
    V4L2_TUNER_CAP_RDS_BLOCK_IO = 0x0100
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1977
try:
    V4L2_TUNER_CAP_RDS_CONTROLS = 0x0200
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1978
try:
    V4L2_TUNER_CAP_FREQ_BANDS = 0x0400
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1979
try:
    V4L2_TUNER_CAP_HWSEEK_PROG_LIM = 0x0800
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1980
try:
    V4L2_TUNER_CAP_1HZ = 0x1000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1983
try:
    V4L2_TUNER_SUB_MONO = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1984
try:
    V4L2_TUNER_SUB_STEREO = 0x0002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1985
try:
    V4L2_TUNER_SUB_LANG2 = 0x0004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1986
try:
    V4L2_TUNER_SUB_SAP = 0x0004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1987
try:
    V4L2_TUNER_SUB_LANG1 = 0x0008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1988
try:
    V4L2_TUNER_SUB_RDS = 0x0010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1991
try:
    V4L2_TUNER_MODE_MONO = 0x0000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1992
try:
    V4L2_TUNER_MODE_STEREO = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1993
try:
    V4L2_TUNER_MODE_LANG2 = 0x0002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1994
try:
    V4L2_TUNER_MODE_SAP = 0x0002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1995
try:
    V4L2_TUNER_MODE_LANG1 = 0x0003
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1996
try:
    V4L2_TUNER_MODE_LANG1_LANG2 = 0x0004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2005
try:
    V4L2_BAND_MODULATION_VSB = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2006
try:
    V4L2_BAND_MODULATION_FM = (1 << 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2007
try:
    V4L2_BAND_MODULATION_AM = (1 << 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2041
try:
    V4L2_RDS_BLOCK_MSK = 0x7
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2042
try:
    V4L2_RDS_BLOCK_A = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2043
try:
    V4L2_RDS_BLOCK_B = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2044
try:
    V4L2_RDS_BLOCK_C = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2045
try:
    V4L2_RDS_BLOCK_D = 3
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2046
try:
    V4L2_RDS_BLOCK_C_ALT = 4
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2047
try:
    V4L2_RDS_BLOCK_INVALID = 7
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2049
try:
    V4L2_RDS_BLOCK_CORRECTED = 0x40
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2050
try:
    V4L2_RDS_BLOCK_ERROR = 0x80
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2064
try:
    V4L2_AUDCAP_STEREO = 0x00001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2065
try:
    V4L2_AUDCAP_AVL = 0x00002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2068
try:
    V4L2_AUDMODE_AVL = 0x00001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2082
try:
    V4L2_ENC_IDX_FRAME_I = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2083
try:
    V4L2_ENC_IDX_FRAME_P = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2084
try:
    V4L2_ENC_IDX_FRAME_B = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2085
try:
    V4L2_ENC_IDX_FRAME_MASK = 0xf
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2095
try:
    V4L2_ENC_IDX_ENTRIES = 64
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2104
try:
    V4L2_ENC_CMD_START = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2105
try:
    V4L2_ENC_CMD_STOP = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2106
try:
    V4L2_ENC_CMD_PAUSE = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2107
try:
    V4L2_ENC_CMD_RESUME = 3
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2110
try:
    V4L2_ENC_CMD_STOP_AT_GOP_END = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2123
try:
    V4L2_DEC_CMD_START = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2124
try:
    V4L2_DEC_CMD_STOP = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2125
try:
    V4L2_DEC_CMD_PAUSE = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2126
try:
    V4L2_DEC_CMD_RESUME = 3
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2127
try:
    V4L2_DEC_CMD_FLUSH = 4
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2130
try:
    V4L2_DEC_CMD_START_MUTE_AUDIO = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2133
try:
    V4L2_DEC_CMD_PAUSE_TO_BLACK = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2136
try:
    V4L2_DEC_CMD_STOP_TO_BLACK = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2137
try:
    V4L2_DEC_CMD_STOP_IMMEDIATELY = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2142
try:
    V4L2_DEC_START_FMT_NONE = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2144
try:
    V4L2_DEC_START_FMT_GOP = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2193
try:
    V4L2_VBI_UNSYNC = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2194
try:
    V4L2_VBI_INTERLACED = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2197
try:
    V4L2_VBI_ITU_525_F1_START = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2198
try:
    V4L2_VBI_ITU_525_F2_START = 264
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2199
try:
    V4L2_VBI_ITU_625_F1_START = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2200
try:
    V4L2_VBI_ITU_625_F2_START = 314
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2222
try:
    V4L2_SLICED_TELETEXT_B = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2224
try:
    V4L2_SLICED_VPS = 0x0400
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2226
try:
    V4L2_SLICED_CAPTION_525 = 0x1000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2228
try:
    V4L2_SLICED_WSS_625 = 0x4000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2230
try:
    V4L2_SLICED_VBI_525 = V4L2_SLICED_CAPTION_525
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2231
try:
    V4L2_SLICED_VBI_625 = ((V4L2_SLICED_TELETEXT_B | V4L2_SLICED_VPS) | V4L2_SLICED_WSS_625)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2269
try:
    V4L2_MPEG_VBI_IVTV_TELETEXT_B = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2270
try:
    V4L2_MPEG_VBI_IVTV_CAPTION_525 = 4
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2271
try:
    V4L2_MPEG_VBI_IVTV_WSS_625 = 5
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2272
try:
    V4L2_MPEG_VBI_IVTV_VPS = 7
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2288
try:
    V4L2_MPEG_VBI_IVTV_MAGIC0 = 'itv0'
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2289
try:
    V4L2_MPEG_VBI_IVTV_MAGIC1 = 'ITV0'
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2424
try:
    V4L2_EVENT_ALL = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2425
try:
    V4L2_EVENT_VSYNC = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2426
try:
    V4L2_EVENT_EOS = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2427
try:
    V4L2_EVENT_CTRL = 3
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2428
try:
    V4L2_EVENT_FRAME_SYNC = 4
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2429
try:
    V4L2_EVENT_SOURCE_CHANGE = 5
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2430
try:
    V4L2_EVENT_MOTION_DET = 6
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2431
try:
    V4L2_EVENT_PRIVATE_START = 0x08000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2440
try:
    V4L2_EVENT_CTRL_CH_VALUE = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2441
try:
    V4L2_EVENT_CTRL_CH_FLAGS = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2442
try:
    V4L2_EVENT_CTRL_CH_RANGE = (1 << 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2443
try:
    V4L2_EVENT_CTRL_CH_DIMENSIONS = (1 << 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2463
try:
    V4L2_EVENT_SRC_CH_RESOLUTION = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2469
try:
    V4L2_EVENT_MD_FL_HAVE_FRAME_SEQ = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2501
try:
    V4L2_EVENT_SUB_FL_SEND_INITIAL = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2502
try:
    V4L2_EVENT_SUB_FL_ALLOW_FEEDBACK = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2520
try:
    V4L2_CHIP_MATCH_BRIDGE = 0
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2521
try:
    V4L2_CHIP_MATCH_SUBDEV = 4
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2524
try:
    V4L2_CHIP_MATCH_HOST = V4L2_CHIP_MATCH_BRIDGE
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2525
try:
    V4L2_CHIP_MATCH_I2C_DRIVER = 1
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2526
try:
    V4L2_CHIP_MATCH_I2C_ADDR = 2
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2527
try:
    V4L2_CHIP_MATCH_AC97 = 3
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2544
try:
    V4L2_CHIP_FL_READABLE = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2545
try:
    V4L2_CHIP_FL_WRITABLE = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2582
try:
    VIDIOC_QUERYCAP = (_IOR ('V', 0, struct_v4l2_capability))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2583
try:
    VIDIOC_ENUM_FMT = (_IOWR ('V', 2, struct_v4l2_fmtdesc))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2584
try:
    VIDIOC_G_FMT = (_IOWR ('V', 4, struct_v4l2_format))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2585
try:
    VIDIOC_S_FMT = (_IOWR ('V', 5, struct_v4l2_format))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2586
try:
    VIDIOC_REQBUFS = (_IOWR ('V', 8, struct_v4l2_requestbuffers))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2587
try:
    VIDIOC_QUERYBUF = (_IOWR ('V', 9, struct_v4l2_buffer))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2588
try:
    VIDIOC_G_FBUF = (_IOR ('V', 10, struct_v4l2_framebuffer))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2589
try:
    VIDIOC_S_FBUF = (_IOW ('V', 11, struct_v4l2_framebuffer))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2590
try:
    VIDIOC_OVERLAY = (_IOW ('V', 14, c_int))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2591
try:
    VIDIOC_QBUF = (_IOWR ('V', 15, struct_v4l2_buffer))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2592
try:
    VIDIOC_EXPBUF = (_IOWR ('V', 16, struct_v4l2_exportbuffer))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2593
try:
    VIDIOC_DQBUF = (_IOWR ('V', 17, struct_v4l2_buffer))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2594
try:
    VIDIOC_STREAMON = (_IOW ('V', 18, c_int))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2595
try:
    VIDIOC_STREAMOFF = (_IOW ('V', 19, c_int))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2596
try:
    VIDIOC_G_PARM = (_IOWR ('V', 21, struct_v4l2_streamparm))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2597
try:
    VIDIOC_S_PARM = (_IOWR ('V', 22, struct_v4l2_streamparm))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2598
try:
    VIDIOC_G_STD = (_IOR ('V', 23, v4l2_std_id))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2599
try:
    VIDIOC_S_STD = (_IOW ('V', 24, v4l2_std_id))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2600
try:
    VIDIOC_ENUMSTD = (_IOWR ('V', 25, struct_v4l2_standard))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2601
try:
    VIDIOC_ENUMINPUT = (_IOWR ('V', 26, struct_v4l2_input))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2602
try:
    VIDIOC_G_CTRL = (_IOWR ('V', 27, struct_v4l2_control))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2603
try:
    VIDIOC_S_CTRL = (_IOWR ('V', 28, struct_v4l2_control))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2604
try:
    VIDIOC_G_TUNER = (_IOWR ('V', 29, struct_v4l2_tuner))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2605
try:
    VIDIOC_S_TUNER = (_IOW ('V', 30, struct_v4l2_tuner))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2606
try:
    VIDIOC_G_AUDIO = (_IOR ('V', 33, struct_v4l2_audio))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2607
try:
    VIDIOC_S_AUDIO = (_IOW ('V', 34, struct_v4l2_audio))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2608
try:
    VIDIOC_QUERYCTRL = (_IOWR ('V', 36, struct_v4l2_queryctrl))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2609
try:
    VIDIOC_QUERYMENU = (_IOWR ('V', 37, struct_v4l2_querymenu))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2610
try:
    VIDIOC_G_INPUT = (_IOR ('V', 38, c_int))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2611
try:
    VIDIOC_S_INPUT = (_IOWR ('V', 39, c_int))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2612
try:
    VIDIOC_G_EDID = (_IOWR ('V', 40, struct_v4l2_edid))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2613
try:
    VIDIOC_S_EDID = (_IOWR ('V', 41, struct_v4l2_edid))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2614
try:
    VIDIOC_G_OUTPUT = (_IOR ('V', 46, c_int))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2615
try:
    VIDIOC_S_OUTPUT = (_IOWR ('V', 47, c_int))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2616
try:
    VIDIOC_ENUMOUTPUT = (_IOWR ('V', 48, struct_v4l2_output))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2617
try:
    VIDIOC_G_AUDOUT = (_IOR ('V', 49, struct_v4l2_audioout))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2618
try:
    VIDIOC_S_AUDOUT = (_IOW ('V', 50, struct_v4l2_audioout))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2619
try:
    VIDIOC_G_MODULATOR = (_IOWR ('V', 54, struct_v4l2_modulator))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2620
try:
    VIDIOC_S_MODULATOR = (_IOW ('V', 55, struct_v4l2_modulator))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2621
try:
    VIDIOC_G_FREQUENCY = (_IOWR ('V', 56, struct_v4l2_frequency))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2622
try:
    VIDIOC_S_FREQUENCY = (_IOW ('V', 57, struct_v4l2_frequency))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2623
try:
    VIDIOC_CROPCAP = (_IOWR ('V', 58, struct_v4l2_cropcap))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2624
try:
    VIDIOC_G_CROP = (_IOWR ('V', 59, struct_v4l2_crop))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2625
try:
    VIDIOC_S_CROP = (_IOW ('V', 60, struct_v4l2_crop))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2626
try:
    VIDIOC_G_JPEGCOMP = (_IOR ('V', 61, struct_v4l2_jpegcompression))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2627
try:
    VIDIOC_S_JPEGCOMP = (_IOW ('V', 62, struct_v4l2_jpegcompression))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2628
try:
    VIDIOC_QUERYSTD = (_IOR ('V', 63, v4l2_std_id))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2629
try:
    VIDIOC_TRY_FMT = (_IOWR ('V', 64, struct_v4l2_format))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2630
try:
    VIDIOC_ENUMAUDIO = (_IOWR ('V', 65, struct_v4l2_audio))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2631
try:
    VIDIOC_ENUMAUDOUT = (_IOWR ('V', 66, struct_v4l2_audioout))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2632
try:
    VIDIOC_G_PRIORITY = (_IOR ('V', 67, __u32))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2633
try:
    VIDIOC_S_PRIORITY = (_IOW ('V', 68, __u32))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2634
try:
    VIDIOC_G_SLICED_VBI_CAP = (_IOWR ('V', 69, struct_v4l2_sliced_vbi_cap))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2635
try:
    VIDIOC_LOG_STATUS = (_IO ('V', 70))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2636
try:
    VIDIOC_G_EXT_CTRLS = (_IOWR ('V', 71, struct_v4l2_ext_controls))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2637
try:
    VIDIOC_S_EXT_CTRLS = (_IOWR ('V', 72, struct_v4l2_ext_controls))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2638
try:
    VIDIOC_TRY_EXT_CTRLS = (_IOWR ('V', 73, struct_v4l2_ext_controls))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2639
try:
    VIDIOC_ENUM_FRAMESIZES = (_IOWR ('V', 74, struct_v4l2_frmsizeenum))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2640
try:
    VIDIOC_ENUM_FRAMEINTERVALS = (_IOWR ('V', 75, struct_v4l2_frmivalenum))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2641
try:
    VIDIOC_G_ENC_INDEX = (_IOR ('V', 76, struct_v4l2_enc_idx))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2642
try:
    VIDIOC_ENCODER_CMD = (_IOWR ('V', 77, struct_v4l2_encoder_cmd))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2643
try:
    VIDIOC_TRY_ENCODER_CMD = (_IOWR ('V', 78, struct_v4l2_encoder_cmd))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2650
try:
    VIDIOC_DBG_S_REGISTER = (_IOW ('V', 79, struct_v4l2_dbg_register))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2651
try:
    VIDIOC_DBG_G_REGISTER = (_IOWR ('V', 80, struct_v4l2_dbg_register))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2653
try:
    VIDIOC_S_HW_FREQ_SEEK = (_IOW ('V', 82, struct_v4l2_hw_freq_seek))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2654
try:
    VIDIOC_S_DV_TIMINGS = (_IOWR ('V', 87, struct_v4l2_dv_timings))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2655
try:
    VIDIOC_G_DV_TIMINGS = (_IOWR ('V', 88, struct_v4l2_dv_timings))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2656
try:
    VIDIOC_DQEVENT = (_IOR ('V', 89, struct_v4l2_event))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2657
try:
    VIDIOC_SUBSCRIBE_EVENT = (_IOW ('V', 90, struct_v4l2_event_subscription))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2658
try:
    VIDIOC_UNSUBSCRIBE_EVENT = (_IOW ('V', 91, struct_v4l2_event_subscription))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2659
try:
    VIDIOC_CREATE_BUFS = (_IOWR ('V', 92, struct_v4l2_create_buffers))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2660
try:
    VIDIOC_PREPARE_BUF = (_IOWR ('V', 93, struct_v4l2_buffer))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2661
try:
    VIDIOC_G_SELECTION = (_IOWR ('V', 94, struct_v4l2_selection))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2662
try:
    VIDIOC_S_SELECTION = (_IOWR ('V', 95, struct_v4l2_selection))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2663
try:
    VIDIOC_DECODER_CMD = (_IOWR ('V', 96, struct_v4l2_decoder_cmd))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2664
try:
    VIDIOC_TRY_DECODER_CMD = (_IOWR ('V', 97, struct_v4l2_decoder_cmd))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2665
try:
    VIDIOC_ENUM_DV_TIMINGS = (_IOWR ('V', 98, struct_v4l2_enum_dv_timings))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2666
try:
    VIDIOC_QUERY_DV_TIMINGS = (_IOR ('V', 99, struct_v4l2_dv_timings))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2667
try:
    VIDIOC_DV_TIMINGS_CAP = (_IOWR ('V', 100, struct_v4l2_dv_timings_cap))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2668
try:
    VIDIOC_ENUM_FREQ_BANDS = (_IOWR ('V', 101, struct_v4l2_frequency_band))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2674
try:
    VIDIOC_DBG_G_CHIP_INFO = (_IOWR ('V', 102, struct_v4l2_dbg_chip_info))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2676
try:
    VIDIOC_QUERY_EXT_CTRL = (_IOWR ('V', 103, struct_v4l2_query_ext_ctrl))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2681
try:
    BASE_VIDIOC_PRIVATE = 192
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2684
try:
    V4L2_PIX_FMT_HM12 = V4L2_PIX_FMT_NV12_16L16
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2685
try:
    V4L2_PIX_FMT_SUNXI_TILED_NV12 = V4L2_PIX_FMT_NV12_32L32
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2690
try:
    V4L2_CAP_ASYNCIO = 0x02000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 48
try:
    MEDIA_ENT_F_BASE = 0x00000000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 49
try:
    MEDIA_ENT_F_OLD_BASE = 0x00010000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 50
try:
    MEDIA_ENT_F_OLD_SUBDEV_BASE = 0x00020000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 56
try:
    MEDIA_ENT_F_UNKNOWN = MEDIA_ENT_F_BASE
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 63
try:
    MEDIA_ENT_F_V4L2_SUBDEV_UNKNOWN = MEDIA_ENT_F_OLD_SUBDEV_BASE
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 68
try:
    MEDIA_ENT_F_DTV_DEMOD = (MEDIA_ENT_F_BASE + 0x00001)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 69
try:
    MEDIA_ENT_F_TS_DEMUX = (MEDIA_ENT_F_BASE + 0x00002)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 70
try:
    MEDIA_ENT_F_DTV_CA = (MEDIA_ENT_F_BASE + 0x00003)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 71
try:
    MEDIA_ENT_F_DTV_NET_DECAP = (MEDIA_ENT_F_BASE + 0x00004)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 76
try:
    MEDIA_ENT_F_IO_V4L = (MEDIA_ENT_F_OLD_BASE + 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 77
try:
    MEDIA_ENT_F_IO_DTV = (MEDIA_ENT_F_BASE + 0x01001)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 78
try:
    MEDIA_ENT_F_IO_VBI = (MEDIA_ENT_F_BASE + 0x01002)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 79
try:
    MEDIA_ENT_F_IO_SWRADIO = (MEDIA_ENT_F_BASE + 0x01003)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 84
try:
    MEDIA_ENT_F_CAM_SENSOR = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 85
try:
    MEDIA_ENT_F_FLASH = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 86
try:
    MEDIA_ENT_F_LENS = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 98
try:
    MEDIA_ENT_F_TUNER = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 5)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 106
try:
    MEDIA_ENT_F_IF_VID_DECODER = (MEDIA_ENT_F_BASE + 0x02001)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 107
try:
    MEDIA_ENT_F_IF_AUD_DECODER = (MEDIA_ENT_F_BASE + 0x02002)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 112
try:
    MEDIA_ENT_F_AUDIO_CAPTURE = (MEDIA_ENT_F_BASE + 0x03001)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 113
try:
    MEDIA_ENT_F_AUDIO_PLAYBACK = (MEDIA_ENT_F_BASE + 0x03002)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 114
try:
    MEDIA_ENT_F_AUDIO_MIXER = (MEDIA_ENT_F_BASE + 0x03003)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 119
try:
    MEDIA_ENT_F_PROC_VIDEO_COMPOSER = (MEDIA_ENT_F_BASE + 0x4001)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 120
try:
    MEDIA_ENT_F_PROC_VIDEO_PIXEL_FORMATTER = (MEDIA_ENT_F_BASE + 0x4002)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 121
try:
    MEDIA_ENT_F_PROC_VIDEO_PIXEL_ENC_CONV = (MEDIA_ENT_F_BASE + 0x4003)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 122
try:
    MEDIA_ENT_F_PROC_VIDEO_LUT = (MEDIA_ENT_F_BASE + 0x4004)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 123
try:
    MEDIA_ENT_F_PROC_VIDEO_SCALER = (MEDIA_ENT_F_BASE + 0x4005)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 124
try:
    MEDIA_ENT_F_PROC_VIDEO_STATISTICS = (MEDIA_ENT_F_BASE + 0x4006)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 125
try:
    MEDIA_ENT_F_PROC_VIDEO_ENCODER = (MEDIA_ENT_F_BASE + 0x4007)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 126
try:
    MEDIA_ENT_F_PROC_VIDEO_DECODER = (MEDIA_ENT_F_BASE + 0x4008)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 127
try:
    MEDIA_ENT_F_PROC_VIDEO_ISP = (MEDIA_ENT_F_BASE + 0x4009)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 132
try:
    MEDIA_ENT_F_VID_MUX = (MEDIA_ENT_F_BASE + 0x5001)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 133
try:
    MEDIA_ENT_F_VID_IF_BRIDGE = (MEDIA_ENT_F_BASE + 0x5002)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 138
try:
    MEDIA_ENT_F_ATV_DECODER = (MEDIA_ENT_F_OLD_SUBDEV_BASE + 4)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 139
try:
    MEDIA_ENT_F_DV_DECODER = (MEDIA_ENT_F_BASE + 0x6001)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 140
try:
    MEDIA_ENT_F_DV_ENCODER = (MEDIA_ENT_F_BASE + 0x6002)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 143
try:
    MEDIA_ENT_FL_DEFAULT = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 144
try:
    MEDIA_ENT_FL_CONNECTOR = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 147
try:
    MEDIA_ENT_ID_FLAG_NEXT = (1 << 31)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 206
try:
    MEDIA_PAD_FL_SINK = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 207
try:
    MEDIA_PAD_FL_SOURCE = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 208
try:
    MEDIA_PAD_FL_MUST_CONNECT = (1 << 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 209
try:
    MEDIA_PAD_FL_INTERNAL = (1 << 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 218
try:
    MEDIA_LNK_FL_ENABLED = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 219
try:
    MEDIA_LNK_FL_IMMUTABLE = (1 << 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 220
try:
    MEDIA_LNK_FL_DYNAMIC = (1 << 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 222
try:
    MEDIA_LNK_FL_LINK_TYPE = (0xf << 28)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 223
try:
    MEDIA_LNK_FL_DATA_LINK = (0 << 28)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 224
try:
    MEDIA_LNK_FL_INTERFACE_LINK = (1 << 28)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 225
try:
    MEDIA_LNK_FL_ANCILLARY_LINK = (2 << 28)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 245
try:
    MEDIA_INTF_T_DVB_BASE = 0x00000100
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 246
try:
    MEDIA_INTF_T_V4L_BASE = 0x00000200
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 250
try:
    MEDIA_INTF_T_DVB_FE = MEDIA_INTF_T_DVB_BASE
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 251
try:
    MEDIA_INTF_T_DVB_DEMUX = (MEDIA_INTF_T_DVB_BASE + 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 252
try:
    MEDIA_INTF_T_DVB_DVR = (MEDIA_INTF_T_DVB_BASE + 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 253
try:
    MEDIA_INTF_T_DVB_CA = (MEDIA_INTF_T_DVB_BASE + 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 254
try:
    MEDIA_INTF_T_DVB_NET = (MEDIA_INTF_T_DVB_BASE + 4)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 256
try:
    MEDIA_INTF_T_V4L_VIDEO = MEDIA_INTF_T_V4L_BASE
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 257
try:
    MEDIA_INTF_T_V4L_VBI = (MEDIA_INTF_T_V4L_BASE + 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 258
try:
    MEDIA_INTF_T_V4L_RADIO = (MEDIA_INTF_T_V4L_BASE + 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 259
try:
    MEDIA_INTF_T_V4L_SUBDEV = (MEDIA_INTF_T_V4L_BASE + 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 260
try:
    MEDIA_INTF_T_V4L_SWRADIO = (MEDIA_INTF_T_V4L_BASE + 4)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 261
try:
    MEDIA_INTF_T_V4L_TOUCH = (MEDIA_INTF_T_V4L_BASE + 5)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 263
try:
    MEDIA_INTF_T_ALSA_BASE = 0x00000300
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 264
try:
    MEDIA_INTF_T_ALSA_PCM_CAPTURE = MEDIA_INTF_T_ALSA_BASE
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 265
try:
    MEDIA_INTF_T_ALSA_PCM_PLAYBACK = (MEDIA_INTF_T_ALSA_BASE + 1)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 266
try:
    MEDIA_INTF_T_ALSA_CONTROL = (MEDIA_INTF_T_ALSA_BASE + 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 279
def MEDIA_V2_ENTITY_HAS_FLAGS(media_version):
    return (media_version >= (((4 << 16) | (19 << 8)) | 0))

# /home/tomba/tmp/khdrs/include/linux/media.h: 314
def MEDIA_V2_PAD_HAS_INDEX(media_version):
    return (media_version >= (((4 << 16) | (19 << 8)) | 0))

# /home/tomba/tmp/khdrs/include/linux/media.h: 355
try:
    MEDIA_IOC_DEVICE_INFO = (_IOWR ('|', 0x00, struct_media_device_info))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 356
try:
    MEDIA_IOC_ENUM_ENTITIES = (_IOWR ('|', 0x01, struct_media_entity_desc))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 357
try:
    MEDIA_IOC_ENUM_LINKS = (_IOWR ('|', 0x02, struct_media_links_enum))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 358
try:
    MEDIA_IOC_SETUP_LINK = (_IOWR ('|', 0x03, struct_media_link_desc))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 359
try:
    MEDIA_IOC_G_TOPOLOGY = (_IOWR ('|', 0x04, struct_media_v2_topology))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 360
try:
    MEDIA_IOC_REQUEST_ALLOC = (_IOR ('|', 0x05, c_int))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 366
try:
    MEDIA_REQUEST_IOC_QUEUE = (_IO ('|', 0x80))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 367
try:
    MEDIA_REQUEST_IOC_REINIT = (_IO ('|', 0x81))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 378
try:
    MEDIA_ENT_TYPE_SHIFT = 16
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 379
try:
    MEDIA_ENT_TYPE_MASK = 0x00ff0000
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 380
try:
    MEDIA_ENT_SUBTYPE_MASK = 0x0000ffff
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 382
try:
    MEDIA_ENT_T_DEVNODE_UNKNOWN = (MEDIA_ENT_F_OLD_BASE | MEDIA_ENT_SUBTYPE_MASK)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 385
try:
    MEDIA_ENT_T_DEVNODE = MEDIA_ENT_F_OLD_BASE
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 386
try:
    MEDIA_ENT_T_DEVNODE_V4L = MEDIA_ENT_F_IO_V4L
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 387
try:
    MEDIA_ENT_T_DEVNODE_FB = (MEDIA_ENT_F_OLD_BASE + 2)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 388
try:
    MEDIA_ENT_T_DEVNODE_ALSA = (MEDIA_ENT_F_OLD_BASE + 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 389
try:
    MEDIA_ENT_T_DEVNODE_DVB = (MEDIA_ENT_F_OLD_BASE + 4)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 391
try:
    MEDIA_ENT_T_UNKNOWN = MEDIA_ENT_F_UNKNOWN
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 392
try:
    MEDIA_ENT_T_V4L2_VIDEO = MEDIA_ENT_F_IO_V4L
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 393
try:
    MEDIA_ENT_T_V4L2_SUBDEV = MEDIA_ENT_F_V4L2_SUBDEV_UNKNOWN
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 394
try:
    MEDIA_ENT_T_V4L2_SUBDEV_SENSOR = MEDIA_ENT_F_CAM_SENSOR
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 395
try:
    MEDIA_ENT_T_V4L2_SUBDEV_FLASH = MEDIA_ENT_F_FLASH
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 396
try:
    MEDIA_ENT_T_V4L2_SUBDEV_LENS = MEDIA_ENT_F_LENS
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 397
try:
    MEDIA_ENT_T_V4L2_SUBDEV_DECODER = MEDIA_ENT_F_ATV_DECODER
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 398
try:
    MEDIA_ENT_T_V4L2_SUBDEV_TUNER = MEDIA_ENT_F_TUNER
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 400
try:
    MEDIA_ENT_F_DTV_DECODER = MEDIA_ENT_F_DV_DECODER
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 411
try:
    MEDIA_INTF_T_ALSA_COMPRESS = (MEDIA_INTF_T_ALSA_BASE + 3)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 412
try:
    MEDIA_INTF_T_ALSA_RAWMIDI = (MEDIA_INTF_T_ALSA_BASE + 4)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 413
try:
    MEDIA_INTF_T_ALSA_HWDEP = (MEDIA_INTF_T_ALSA_BASE + 5)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 414
try:
    MEDIA_INTF_T_ALSA_SEQUENCER = (MEDIA_INTF_T_ALSA_BASE + 6)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 415
try:
    MEDIA_INTF_T_ALSA_TIMER = (MEDIA_INTF_T_ALSA_BASE + 7)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media.h: 418
try:
    MEDIA_API_VERSION = (((0 << 16) | (1 << 8)) | 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 35
try:
    MEDIA_BUS_FMT_FIXED = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 38
try:
    MEDIA_BUS_FMT_RGB444_1X12 = 0x1016
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 39
try:
    MEDIA_BUS_FMT_RGB444_2X8_PADHI_BE = 0x1001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 40
try:
    MEDIA_BUS_FMT_RGB444_2X8_PADHI_LE = 0x1002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 41
try:
    MEDIA_BUS_FMT_RGB555_2X8_PADHI_BE = 0x1003
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 42
try:
    MEDIA_BUS_FMT_RGB555_2X8_PADHI_LE = 0x1004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 43
try:
    MEDIA_BUS_FMT_RGB565_1X16 = 0x1017
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 44
try:
    MEDIA_BUS_FMT_BGR565_2X8_BE = 0x1005
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 45
try:
    MEDIA_BUS_FMT_BGR565_2X8_LE = 0x1006
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 46
try:
    MEDIA_BUS_FMT_RGB565_2X8_BE = 0x1007
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 47
try:
    MEDIA_BUS_FMT_RGB565_2X8_LE = 0x1008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 48
try:
    MEDIA_BUS_FMT_RGB666_1X18 = 0x1009
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 49
try:
    MEDIA_BUS_FMT_BGR666_1X18 = 0x1023
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 50
try:
    MEDIA_BUS_FMT_RBG888_1X24 = 0x100e
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 51
try:
    MEDIA_BUS_FMT_RGB666_1X24_CPADHI = 0x1015
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 52
try:
    MEDIA_BUS_FMT_BGR666_1X24_CPADHI = 0x1024
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 53
try:
    MEDIA_BUS_FMT_RGB565_1X24_CPADHI = 0x1022
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 54
try:
    MEDIA_BUS_FMT_RGB666_1X7X3_SPWG = 0x1010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 55
try:
    MEDIA_BUS_FMT_BGR888_1X24 = 0x1013
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 56
try:
    MEDIA_BUS_FMT_BGR888_3X8 = 0x101b
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 57
try:
    MEDIA_BUS_FMT_GBR888_1X24 = 0x1014
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 58
try:
    MEDIA_BUS_FMT_RGB888_1X24 = 0x100a
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 59
try:
    MEDIA_BUS_FMT_RGB888_2X12_BE = 0x100b
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 60
try:
    MEDIA_BUS_FMT_RGB888_2X12_LE = 0x100c
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 61
try:
    MEDIA_BUS_FMT_RGB888_3X8 = 0x101c
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 62
try:
    MEDIA_BUS_FMT_RGB888_3X8_DELTA = 0x101d
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 63
try:
    MEDIA_BUS_FMT_RGB888_1X7X4_SPWG = 0x1011
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 64
try:
    MEDIA_BUS_FMT_RGB888_1X7X4_JEIDA = 0x1012
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 65
try:
    MEDIA_BUS_FMT_RGB666_1X30_CPADLO = 0x101e
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 66
try:
    MEDIA_BUS_FMT_RGB888_1X30_CPADLO = 0x101f
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 67
try:
    MEDIA_BUS_FMT_ARGB8888_1X32 = 0x100d
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 68
try:
    MEDIA_BUS_FMT_RGB888_1X32_PADHI = 0x100f
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 69
try:
    MEDIA_BUS_FMT_RGB101010_1X30 = 0x1018
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 70
try:
    MEDIA_BUS_FMT_RGB666_1X36_CPADLO = 0x1020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 71
try:
    MEDIA_BUS_FMT_RGB888_1X36_CPADLO = 0x1021
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 72
try:
    MEDIA_BUS_FMT_RGB121212_1X36 = 0x1019
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 73
try:
    MEDIA_BUS_FMT_RGB161616_1X48 = 0x101a
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 76
try:
    MEDIA_BUS_FMT_Y8_1X8 = 0x2001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 77
try:
    MEDIA_BUS_FMT_UV8_1X8 = 0x2015
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 78
try:
    MEDIA_BUS_FMT_UYVY8_1_5X8 = 0x2002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 79
try:
    MEDIA_BUS_FMT_VYUY8_1_5X8 = 0x2003
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 80
try:
    MEDIA_BUS_FMT_YUYV8_1_5X8 = 0x2004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 81
try:
    MEDIA_BUS_FMT_YVYU8_1_5X8 = 0x2005
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 82
try:
    MEDIA_BUS_FMT_UYVY8_2X8 = 0x2006
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 83
try:
    MEDIA_BUS_FMT_VYUY8_2X8 = 0x2007
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 84
try:
    MEDIA_BUS_FMT_YUYV8_2X8 = 0x2008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 85
try:
    MEDIA_BUS_FMT_YVYU8_2X8 = 0x2009
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 86
try:
    MEDIA_BUS_FMT_Y10_1X10 = 0x200a
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 87
try:
    MEDIA_BUS_FMT_Y10_2X8_PADHI_LE = 0x202c
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 88
try:
    MEDIA_BUS_FMT_UYVY10_2X10 = 0x2018
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 89
try:
    MEDIA_BUS_FMT_VYUY10_2X10 = 0x2019
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 90
try:
    MEDIA_BUS_FMT_YUYV10_2X10 = 0x200b
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 91
try:
    MEDIA_BUS_FMT_YVYU10_2X10 = 0x200c
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 92
try:
    MEDIA_BUS_FMT_Y12_1X12 = 0x2013
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 93
try:
    MEDIA_BUS_FMT_UYVY12_2X12 = 0x201c
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 94
try:
    MEDIA_BUS_FMT_VYUY12_2X12 = 0x201d
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 95
try:
    MEDIA_BUS_FMT_YUYV12_2X12 = 0x201e
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 96
try:
    MEDIA_BUS_FMT_YVYU12_2X12 = 0x201f
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 97
try:
    MEDIA_BUS_FMT_Y14_1X14 = 0x202d
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 98
try:
    MEDIA_BUS_FMT_Y16_1X16 = 0x202e
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 99
try:
    MEDIA_BUS_FMT_UYVY8_1X16 = 0x200f
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 100
try:
    MEDIA_BUS_FMT_VYUY8_1X16 = 0x2010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 101
try:
    MEDIA_BUS_FMT_YUYV8_1X16 = 0x2011
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 102
try:
    MEDIA_BUS_FMT_YVYU8_1X16 = 0x2012
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 103
try:
    MEDIA_BUS_FMT_YDYUYDYV8_1X16 = 0x2014
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 104
try:
    MEDIA_BUS_FMT_UYVY10_1X20 = 0x201a
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 105
try:
    MEDIA_BUS_FMT_VYUY10_1X20 = 0x201b
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 106
try:
    MEDIA_BUS_FMT_YUYV10_1X20 = 0x200d
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 107
try:
    MEDIA_BUS_FMT_YVYU10_1X20 = 0x200e
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 108
try:
    MEDIA_BUS_FMT_VUY8_1X24 = 0x2024
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 109
try:
    MEDIA_BUS_FMT_YUV8_1X24 = 0x2025
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 110
try:
    MEDIA_BUS_FMT_UYYVYY8_0_5X24 = 0x2026
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 111
try:
    MEDIA_BUS_FMT_UYVY12_1X24 = 0x2020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 112
try:
    MEDIA_BUS_FMT_VYUY12_1X24 = 0x2021
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 113
try:
    MEDIA_BUS_FMT_YUYV12_1X24 = 0x2022
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 114
try:
    MEDIA_BUS_FMT_YVYU12_1X24 = 0x2023
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 115
try:
    MEDIA_BUS_FMT_YUV10_1X30 = 0x2016
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 116
try:
    MEDIA_BUS_FMT_UYYVYY10_0_5X30 = 0x2027
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 117
try:
    MEDIA_BUS_FMT_AYUV8_1X32 = 0x2017
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 118
try:
    MEDIA_BUS_FMT_UYYVYY12_0_5X36 = 0x2028
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 119
try:
    MEDIA_BUS_FMT_YUV12_1X36 = 0x2029
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 120
try:
    MEDIA_BUS_FMT_YUV16_1X48 = 0x202a
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 121
try:
    MEDIA_BUS_FMT_UYYVYY16_0_5X48 = 0x202b
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 124
try:
    MEDIA_BUS_FMT_SBGGR8_1X8 = 0x3001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 125
try:
    MEDIA_BUS_FMT_SGBRG8_1X8 = 0x3013
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 126
try:
    MEDIA_BUS_FMT_SGRBG8_1X8 = 0x3002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 127
try:
    MEDIA_BUS_FMT_SRGGB8_1X8 = 0x3014
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 128
try:
    MEDIA_BUS_FMT_SBGGR10_ALAW8_1X8 = 0x3015
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 129
try:
    MEDIA_BUS_FMT_SGBRG10_ALAW8_1X8 = 0x3016
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 130
try:
    MEDIA_BUS_FMT_SGRBG10_ALAW8_1X8 = 0x3017
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 131
try:
    MEDIA_BUS_FMT_SRGGB10_ALAW8_1X8 = 0x3018
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 132
try:
    MEDIA_BUS_FMT_SBGGR10_DPCM8_1X8 = 0x300b
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 133
try:
    MEDIA_BUS_FMT_SGBRG10_DPCM8_1X8 = 0x300c
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 134
try:
    MEDIA_BUS_FMT_SGRBG10_DPCM8_1X8 = 0x3009
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 135
try:
    MEDIA_BUS_FMT_SRGGB10_DPCM8_1X8 = 0x300d
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 136
try:
    MEDIA_BUS_FMT_SBGGR10_2X8_PADHI_BE = 0x3003
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 137
try:
    MEDIA_BUS_FMT_SBGGR10_2X8_PADHI_LE = 0x3004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 138
try:
    MEDIA_BUS_FMT_SBGGR10_2X8_PADLO_BE = 0x3005
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 139
try:
    MEDIA_BUS_FMT_SBGGR10_2X8_PADLO_LE = 0x3006
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 140
try:
    MEDIA_BUS_FMT_SBGGR10_1X10 = 0x3007
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 141
try:
    MEDIA_BUS_FMT_SGBRG10_1X10 = 0x300e
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 142
try:
    MEDIA_BUS_FMT_SGRBG10_1X10 = 0x300a
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 143
try:
    MEDIA_BUS_FMT_SRGGB10_1X10 = 0x300f
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 144
try:
    MEDIA_BUS_FMT_SBGGR12_1X12 = 0x3008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 145
try:
    MEDIA_BUS_FMT_SGBRG12_1X12 = 0x3010
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 146
try:
    MEDIA_BUS_FMT_SGRBG12_1X12 = 0x3011
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 147
try:
    MEDIA_BUS_FMT_SRGGB12_1X12 = 0x3012
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 148
try:
    MEDIA_BUS_FMT_SBGGR14_1X14 = 0x3019
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 149
try:
    MEDIA_BUS_FMT_SGBRG14_1X14 = 0x301a
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 150
try:
    MEDIA_BUS_FMT_SGRBG14_1X14 = 0x301b
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 151
try:
    MEDIA_BUS_FMT_SRGGB14_1X14 = 0x301c
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 152
try:
    MEDIA_BUS_FMT_SBGGR16_1X16 = 0x301d
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 153
try:
    MEDIA_BUS_FMT_SGBRG16_1X16 = 0x301e
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 154
try:
    MEDIA_BUS_FMT_SGRBG16_1X16 = 0x301f
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 155
try:
    MEDIA_BUS_FMT_SRGGB16_1X16 = 0x3020
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 158
try:
    MEDIA_BUS_FMT_JPEG_1X8 = 0x4001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 163
try:
    MEDIA_BUS_FMT_S5C_UYVY_JPEG_1X8 = 0x5001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 166
try:
    MEDIA_BUS_FMT_AHSV8888_1X32 = 0x6001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 174
try:
    MEDIA_BUS_FMT_METADATA_FIXED = 0x7001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 177
try:
    MEDIA_BUS_FMT_META_8 = 0x8001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 178
try:
    MEDIA_BUS_FMT_META_10 = 0x8002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 179
try:
    MEDIA_BUS_FMT_META_12 = 0x8003
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 180
try:
    MEDIA_BUS_FMT_META_14 = 0x8004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 181
try:
    MEDIA_BUS_FMT_META_16 = 0x8005
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 182
try:
    MEDIA_BUS_FMT_META_20 = 0x8006
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 183
try:
    MEDIA_BUS_FMT_META_24 = 0x8007
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 186
try:
    MEDIA_BUS_FMT_CCS_EMBEDDED_8 = 0x9001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 187
try:
    MEDIA_BUS_FMT_CCS_EMBEDDED_10 = 0x9002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 188
try:
    MEDIA_BUS_FMT_CCS_EMBEDDED_12 = 0x9003
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 189
try:
    MEDIA_BUS_FMT_CCS_EMBEDDED_14 = 0x9004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 190
try:
    MEDIA_BUS_FMT_CCS_EMBEDDED_16 = 0x9005
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 191
try:
    MEDIA_BUS_FMT_CCS_EMBEDDED_20 = 0x9006
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 192
try:
    MEDIA_BUS_FMT_CCS_EMBEDDED_24 = 0x9007
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/media-bus-format.h: 194
def MEDIA_BUS_FMT_IS_META(code):
    return ((code & (0xf000 == 0x7000)) or (code & (0xf000 == 0x8000)))

# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 15
try:
    V4L2_MBUS_FRAMEFMT_SET_CSC = 0x0001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 62
try:
    V4L2_SUBDEV_MBUS_CODE_CSC_COLORSPACE = 0x00000001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 63
try:
    V4L2_SUBDEV_MBUS_CODE_CSC_XFER_FUNC = 0x00000002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 64
try:
    V4L2_SUBDEV_MBUS_CODE_CSC_YCBCR_ENC = 0x00000004
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 65
try:
    V4L2_SUBDEV_MBUS_CODE_CSC_HSV_ENC = V4L2_SUBDEV_MBUS_CODE_CSC_YCBCR_ENC
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 66
try:
    V4L2_SUBDEV_MBUS_CODE_CSC_QUANTIZATION = 0x00000008
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 191
try:
    V4L2_SUBDEV_CAP_RO_SUBDEV = 0x00000001
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 194
try:
    V4L2_SUBDEV_CAP_STREAMS = 0x00000002
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 200
try:
    V4L2_SUBDEV_ROUTE_FL_ACTIVE = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 242
try:
    V4L2_SUBDEV_CLIENT_CAP_STREAMS = (1 << 0)
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 257
try:
    VIDIOC_SUBDEV_QUERYCAP = (_IOR ('V', 0, struct_v4l2_subdev_capability))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 258
try:
    VIDIOC_SUBDEV_G_FMT = (_IOWR ('V', 4, struct_v4l2_subdev_format))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 259
try:
    VIDIOC_SUBDEV_S_FMT = (_IOWR ('V', 5, struct_v4l2_subdev_format))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 260
try:
    VIDIOC_SUBDEV_G_FRAME_INTERVAL = (_IOWR ('V', 21, struct_v4l2_subdev_frame_interval))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 261
try:
    VIDIOC_SUBDEV_S_FRAME_INTERVAL = (_IOWR ('V', 22, struct_v4l2_subdev_frame_interval))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 262
try:
    VIDIOC_SUBDEV_ENUM_MBUS_CODE = (_IOWR ('V', 2, struct_v4l2_subdev_mbus_code_enum))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 263
try:
    VIDIOC_SUBDEV_ENUM_FRAME_SIZE = (_IOWR ('V', 74, struct_v4l2_subdev_frame_size_enum))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 264
try:
    VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL = (_IOWR ('V', 75, struct_v4l2_subdev_frame_interval_enum))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 265
try:
    VIDIOC_SUBDEV_G_CROP = (_IOWR ('V', 59, struct_v4l2_subdev_crop))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 266
try:
    VIDIOC_SUBDEV_S_CROP = (_IOWR ('V', 60, struct_v4l2_subdev_crop))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 267
try:
    VIDIOC_SUBDEV_G_SELECTION = (_IOWR ('V', 61, struct_v4l2_subdev_selection))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 268
try:
    VIDIOC_SUBDEV_S_SELECTION = (_IOWR ('V', 62, struct_v4l2_subdev_selection))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 269
try:
    VIDIOC_SUBDEV_G_ROUTING = (_IOWR ('V', 38, struct_v4l2_subdev_routing))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 270
try:
    VIDIOC_SUBDEV_S_ROUTING = (_IOWR ('V', 39, struct_v4l2_subdev_routing))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 271
try:
    VIDIOC_SUBDEV_G_CLIENT_CAP = (_IOR ('V', 101, struct_v4l2_subdev_client_capability))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 272
try:
    VIDIOC_SUBDEV_S_CLIENT_CAP = (_IOWR ('V', 102, struct_v4l2_subdev_client_capability))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 275
try:
    VIDIOC_SUBDEV_G_STD = (_IOR ('V', 23, v4l2_std_id))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 276
try:
    VIDIOC_SUBDEV_S_STD = (_IOW ('V', 24, v4l2_std_id))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 277
try:
    VIDIOC_SUBDEV_ENUMSTD = (_IOWR ('V', 25, struct_v4l2_standard))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 278
try:
    VIDIOC_SUBDEV_G_EDID = (_IOWR ('V', 40, struct_v4l2_edid))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 279
try:
    VIDIOC_SUBDEV_S_EDID = (_IOWR ('V', 41, struct_v4l2_edid))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 280
try:
    VIDIOC_SUBDEV_QUERYSTD = (_IOR ('V', 63, v4l2_std_id))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 281
try:
    VIDIOC_SUBDEV_S_DV_TIMINGS = (_IOWR ('V', 87, struct_v4l2_dv_timings))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 282
try:
    VIDIOC_SUBDEV_G_DV_TIMINGS = (_IOWR ('V', 88, struct_v4l2_dv_timings))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 283
try:
    VIDIOC_SUBDEV_ENUM_DV_TIMINGS = (_IOWR ('V', 98, struct_v4l2_enum_dv_timings))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 284
try:
    VIDIOC_SUBDEV_QUERY_DV_TIMINGS = (_IOR ('V', 99, struct_v4l2_dv_timings))
except:
    pass

# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 285
try:
    VIDIOC_SUBDEV_DV_TIMINGS_CAP = (_IOWR ('V', 100, struct_v4l2_dv_timings_cap))
except:
    pass

v4l2_rect = struct_v4l2_rect# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 407

v4l2_fract = struct_v4l2_fract# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 414

v4l2_area = struct_v4l2_area# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 419

v4l2_capability = struct_v4l2_capability# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 435

v4l2_pix_format = struct_v4l2_pix_format# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 490

v4l2_fmtdesc = struct_v4l2_fmtdesc# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 833

v4l2_frmsize_discrete = struct_v4l2_frmsize_discrete# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 865

v4l2_frmsize_stepwise = struct_v4l2_frmsize_stepwise# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 870

v4l2_frmsizeenum = struct_v4l2_frmsizeenum# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 879

v4l2_frmival_stepwise = struct_v4l2_frmival_stepwise# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 901

v4l2_frmivalenum = struct_v4l2_frmivalenum# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 907

v4l2_timecode = struct_v4l2_timecode# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 925

v4l2_jpegcompression = struct_v4l2_jpegcompression# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 950

v4l2_requestbuffers = struct_v4l2_requestbuffers# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 984

v4l2_plane = struct_v4l2_plane# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1026

v4l2_buffer = struct_v4l2_buffer# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1073

v4l2_exportbuffer = struct_v4l2_exportbuffer# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1170

v4l2_framebuffer = struct_v4l2_framebuffer# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1182

v4l2_clip = struct_v4l2_clip# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1217

v4l2_window = struct_v4l2_window# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1222

v4l2_captureparm = struct_v4l2_captureparm# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1235

v4l2_outputparm = struct_v4l2_outputparm# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1248

v4l2_cropcap = struct_v4l2_cropcap# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1260

v4l2_crop = struct_v4l2_crop# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1267

v4l2_selection = struct_v4l2_selection# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1285

v4l2_standard = struct_v4l2_standard# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1430

v4l2_bt_timings = struct_v4l2_bt_timings# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1478

v4l2_dv_timings = struct_v4l2_dv_timings# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1602

v4l2_enum_dv_timings = struct_v4l2_enum_dv_timings# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1621

v4l2_bt_timings_cap = struct_v4l2_bt_timings_cap# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1639

v4l2_dv_timings_cap = struct_v4l2_dv_timings_cap# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1666

v4l2_input = struct_v4l2_input# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1680

v4l2_output = struct_v4l2_output# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1732

v4l2_control = struct_v4l2_control# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1756

v4l2_ext_control = struct_v4l2_ext_control# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1761

v4l2_ext_controls = struct_v4l2_ext_controls# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1801

v4l2_queryctrl = struct_v4l2_queryctrl# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1874

v4l2_query_ext_ctrl = struct_v4l2_query_ext_ctrl# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1887

v4l2_querymenu = struct_v4l2_querymenu# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1904

v4l2_tuner = struct_v4l2_tuner# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1941

v4l2_modulator = struct_v4l2_modulator# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1955

v4l2_frequency = struct_v4l2_frequency# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 1998

v4l2_frequency_band = struct_v4l2_frequency_band# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2009

v4l2_hw_freq_seek = struct_v4l2_hw_freq_seek# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2020

v4l2_rds_data = struct_v4l2_rds_data# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2035

v4l2_audio = struct_v4l2_audio# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2055

v4l2_audioout = struct_v4l2_audioout# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2070

v4l2_enc_idx_entry = struct_v4l2_enc_idx_entry# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2087

v4l2_enc_idx = struct_v4l2_enc_idx# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2096

v4l2_encoder_cmd = struct_v4l2_encoder_cmd# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2112

v4l2_decoder_cmd = struct_v4l2_decoder_cmd# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2148

v4l2_vbi_format = struct_v4l2_vbi_format# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2181

v4l2_sliced_vbi_format = struct_v4l2_sliced_vbi_format# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2209

v4l2_sliced_vbi_cap = struct_v4l2_sliced_vbi_cap# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2233

v4l2_sliced_vbi_data = struct_v4l2_sliced_vbi_data# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2244

v4l2_mpeg_vbi_itv0_line = struct_v4l2_mpeg_vbi_itv0_line# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2274

v4l2_mpeg_vbi_itv0 = struct_v4l2_mpeg_vbi_itv0# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2279

v4l2_mpeg_vbi_ITV0 = struct_v4l2_mpeg_vbi_ITV0# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2284

v4l2_mpeg_vbi_fmt_ivtv = struct_v4l2_mpeg_vbi_fmt_ivtv# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2291

v4l2_plane_pix_format = struct_v4l2_plane_pix_format# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2311

v4l2_pix_format_mplane = struct_v4l2_pix_format_mplane# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2333

v4l2_sdr_format = struct_v4l2_sdr_format# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2358

v4l2_meta_format = struct_v4l2_meta_format# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2375

v4l2_format = struct_v4l2_format# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2395

v4l2_streamparm = struct_v4l2_streamparm# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2411

v4l2_event_vsync = struct_v4l2_event_vsync# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2434

v4l2_event_ctrl = struct_v4l2_event_ctrl# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2445

v4l2_event_frame_sync = struct_v4l2_event_frame_sync# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2459

v4l2_event_src_change = struct_v4l2_event_src_change# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2465

v4l2_event_motion_det = struct_v4l2_event_motion_det# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2478

v4l2_event = struct_v4l2_event# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2484

v4l2_event_subscription = struct_v4l2_event_subscription# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2504

v4l2_dbg_match = struct_v4l2_dbg_match# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2529

v4l2_dbg_register = struct_v4l2_dbg_register# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2537

v4l2_dbg_chip_info = struct_v4l2_dbg_chip_info# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2548

v4l2_create_buffers = struct_v4l2_create_buffers# /home/tomba/tmp/khdrs/include/linux/videodev2.h: 2568

media_device_info = struct_media_device_info# /home/tomba/tmp/khdrs/include/linux/media.h: 26

media_entity_desc = struct_media_entity_desc# /home/tomba/tmp/khdrs/include/linux/media.h: 149

media_pad_desc = struct_media_pad_desc# /home/tomba/tmp/khdrs/include/linux/media.h: 211

media_link_desc = struct_media_link_desc# /home/tomba/tmp/khdrs/include/linux/media.h: 227

media_links_enum = struct_media_links_enum# /home/tomba/tmp/khdrs/include/linux/media.h: 234

media_v2_entity = struct_media_v2_entity# /home/tomba/tmp/khdrs/include/linux/media.h: 282

media_v2_intf_devnode = struct_media_v2_intf_devnode# /home/tomba/tmp/khdrs/include/linux/media.h: 291

media_v2_interface = struct_media_v2_interface# /home/tomba/tmp/khdrs/include/linux/media.h: 296

media_v2_pad = struct_media_v2_pad# /home/tomba/tmp/khdrs/include/linux/media.h: 317

media_v2_link = struct_media_v2_link# /home/tomba/tmp/khdrs/include/linux/media.h: 325

media_v2_topology = struct_media_v2_topology# /home/tomba/tmp/khdrs/include/linux/media.h: 333

v4l2_mbus_framefmt = struct_v4l2_mbus_framefmt# /home/tomba/tmp/khdrs/include/linux/v4l2-mediabus.h: 37

v4l2_subdev_format = struct_v4l2_subdev_format# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 38

v4l2_subdev_crop = struct_v4l2_subdev_crop# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 54

v4l2_subdev_mbus_code_enum = struct_v4l2_subdev_mbus_code_enum# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 78

v4l2_subdev_frame_size_enum = struct_v4l2_subdev_frame_size_enum# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 101

v4l2_subdev_frame_interval = struct_v4l2_subdev_frame_interval# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 121

v4l2_subdev_frame_interval_enum = struct_v4l2_subdev_frame_interval_enum# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 140

v4l2_subdev_selection = struct_v4l2_subdev_selection# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 168

v4l2_subdev_capability = struct_v4l2_subdev_capability# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 184

v4l2_subdev_route = struct_v4l2_subdev_route# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 212

v4l2_subdev_routing = struct_v4l2_subdev_routing# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 229

v4l2_subdev_client_capability = struct_v4l2_subdev_client_capability# /home/tomba/tmp/khdrs/include/linux/v4l2-subdev.h: 250

# No inserted files

# No prefix-stripping

