#!/usr/bin/python3

import typing

import v4l2

imx219_w = 1920
imx219_h = 1080

mbus_fmt_cam = (imx219_w, imx219_h, v4l2.BusFormat.SGRBG12_1X12)
mbus_fmt_switch = (imx219_w, imx219_h, v4l2.BusFormat.SGRBG8_1X8)
mbus_fmt_demos = (imx219_w, imx219_h, v4l2.BusFormat.RBG888_1X24)
mbus_fmt_csc = (imx219_w, imx219_h, v4l2.BusFormat.UYVY8_1X16)

fmt_pix = (imx219_w, imx219_h, v4l2.PixelFormats.YUYV)

def expand_link_path(arr):
    links = []

    current_source = None

    for ent, sink_pad, source_pad in arr:
        if current_source:
            links.append({ 'src': current_source,
                           'dst': (ent, sink_pad) })

        current_source = (ent, source_pad)

    return links

configurations = {}

configurations['cam0'] = {
    'media': ('platform:amba_pl@0:vcap_csi_p0_', 'bus_info'),

    'subdevs': [
        {
            'entity': 'mars 31-0041',
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt_cam },
            ],
        },
        {
            'entity': 'max9286 23-0048',
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt_cam },
                { 'pad': (4, 0), 'fmt': mbus_fmt_cam, "ival": (1, 30) },
            ],
            "routing": [
                { "src": (0, 0), "dst": (4, 0) },
            ],
        },
        {
            'entity': 'a0000000.mipi_csi2_rx_subsystem',
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt_cam },
                { 'pad': (1, 0), 'fmt': mbus_fmt_cam },
            ],
            "routing": [
                { "src": (0, 0), "dst": (1, 0) },
            ],
        },
        {
            'entity': 'amba_pl@0:axis_switch_csi_axis_switch_0@0',
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt_switch },
                { 'pad': 1, 'fmt': mbus_fmt_switch },
            ],
            "routing": [
                { "src": (0, 0), "dst": (1, 0) },
            ],
        },
        {
            'entity': 'a0190000.v_demosaic',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_switch },
                { 'pad': 1, 'fmt': mbus_fmt_demos },
            ],
        },
        {
            'entity': 'a0180000.v_gamma_lut',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_demos },
                { 'pad': 1, 'fmt': mbus_fmt_demos },
            ],
        },
        {
            'entity': 'a0010000.v_proc_ss',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_demos },
                { 'pad': 1, 'fmt': mbus_fmt_csc },
            ],
        },
        {
            'entity': 'a0040000.v_proc_ss',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_csc },
                { 'pad': 1, 'fmt': mbus_fmt_csc },
            ],
        },
    ],

    'devices': [
        {
            'entity': 'vcap_csi_p0_scalar_0 output 0',
            'fmt': fmt_pix,
        },
    ],

    'links': expand_link_path([
                              ('mars 31-0041', None, 0),
                              ('max9286 23-0048', 0, 4),
                              ('a0000000.mipi_csi2_rx_subsystem', 0, 1),
                              ('amba_pl@0:axis_switch_csi_axis_switch_0@0', 0, 1),
                              ('a0190000.v_demosaic', 0, 1),
                              ('a0180000.v_gamma_lut', 0, 1),
                              ('a0010000.v_proc_ss', 0, 1),
                              ('a0040000.v_proc_ss', 0, 1),
                              ('vcap_csi_p0_scalar_0 output 0', 0, None),
                              ]),
}

configurations['cam1'] = {
    'media': ('platform:amba_pl@0:vcap_csi_p0_', 'bus_info'),

    'subdevs': [
        {
            'entity': 'mars 32-0042',
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt_cam },
            ],
        },
        {
            'entity': 'max9286 23-0048',
            'pads': [
                { 'pad': (1, 0), 'fmt': mbus_fmt_cam },
                { 'pad': (4, 1), 'fmt': mbus_fmt_cam, "ival": (1, 30) },
            ],
            "routing": [
                { "src": (1, 0), "dst": (4, 1) },
            ],
        },
        {
            'entity': 'a0000000.mipi_csi2_rx_subsystem',
            'pads': [
                { 'pad': (0, 1), 'fmt': mbus_fmt_cam },
                { 'pad': (1, 1), 'fmt': mbus_fmt_cam },
            ],
            "routing": [
                { "src": (0, 1), "dst": (1, 1) },
            ],
        },
        {
            'entity': 'amba_pl@0:axis_switch_csi_axis_switch_0@0',
            'pads': [
                { 'pad': (0, 1), 'fmt': mbus_fmt_switch },
                { 'pad': 2, 'fmt': mbus_fmt_switch },
            ],
            "routing": [
                { "src": (0, 1), "dst": (2, 0) },
            ],
        },
        {
            'entity': 'a01c0000.v_demosaic',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_switch },
                { 'pad': 1, 'fmt': mbus_fmt_demos },
            ],
        },
        {
            'entity': 'a01b0000.v_gamma_lut',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_demos },
                { 'pad': 1, 'fmt': mbus_fmt_demos },
            ],
        },
        {
            'entity': 'a0020000.v_proc_ss',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_demos },
                { 'pad': 1, 'fmt': mbus_fmt_csc },
            ],
        },
        {
            'entity': 'a0080000.v_proc_ss',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_csc },
                { 'pad': 1, 'fmt': mbus_fmt_csc },
            ],
        },
    ],

    'devices': [
        {
            'entity': 'vcap_csi_p0_scalar_0 output 1',
            'fmt': fmt_pix,
        },
    ],

    'links': expand_link_path([
                              ('mars 32-0042', None, 0),
                              ('max9286 23-0048', 1, 4),
                              ('a0000000.mipi_csi2_rx_subsystem', 0, 1),
                              ('amba_pl@0:axis_switch_csi_axis_switch_0@0', 0, 2),
                              ('a01c0000.v_demosaic', 0, 1),
                              ('a01b0000.v_gamma_lut', 0, 1),
                              ('a0020000.v_proc_ss', 0, 1),
                              ('a0080000.v_proc_ss', 0, 1),
                              ('vcap_csi_p0_scalar_0 output 1', 0, None),
                              ]),
}

def get_configs():
    return (configurations, ['cam0', 'cam1'])
