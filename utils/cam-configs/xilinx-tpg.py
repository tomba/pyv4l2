#!/usr/bin/python3

import v4l2

imx219_w = 640
imx219_h = 480

mbus_fmt = (imx219_w, imx219_h, v4l2.BusFormat.RBG888_1X24)
fmt_pix = (imx219_w, imx219_h, v4l2.PixelFormat.BGR888)

configurations = {}

configurations['tpg'] = {
    #'media': ('platform:amba_pl@0:vcap_tpg_inp', 'bus_info'),
    'media': ('platform:axi:vcap_tpg_input_v_t', 'bus_info'),

    'subdevs': [
        {
            'entity': 'a00e0000.v_tpg',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt },
            ],
        },
    ],

    'devices': [
        {
            'entity': 'vcap_tpg_input_v_tpg_1 output 0',
            'fmt': fmt_pix,
        },
    ],

    'links': [
        { 'src': ('a00e0000.v_tpg', 0), 'dst': ('vcap_tpg_input_v_tpg_1 output 0', 0) },
    ],
}

def get_configs():
    return (configurations, ['tpg'])
