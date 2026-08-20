from __future__ import annotations

import v4l2

imx219_w = 640
imx219_h = 480

mbus_fmt = [imx219_w, imx219_h, v4l2.BusFormat.RBG888_1X24]
fmt_pix = [imx219_w, imx219_h, v4l2.PixelFormats.BGR888]

#mbus_fmt = [imx219_w, imx219_h, v4l2.BusFormat.VYUY8_1X16]
#fmt_pix = [imx219_w, imx219_h, v4l2.PixelFormats.YUYV]


configurations = {}

MEDIA = 'platform:vcap_tpg_input_v_tpg_1'
TPG = 'a00e0000.v_tpg'
DMA = 'vcap_tpg_input_v_tpg_1 output 0'

MEDIA = 'platform:vcap_v_tpg_0'
TPG = 'a0020000.v_tpg'
DMA = 'vcap_v_tpg_0 output 0'

MEDIA = 'platform:xilinx_video_top'
TPG = 'a0020000.v_tpg'
DMA = 'xilinx_video_top output 0'

configurations['tpg'] = {
    'media': (MEDIA, 'bus_info'),

    'subdevs': [
        {
            'entity': TPG,
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt },
            ],
        },
    ],

    'devices': [
        {
            'entity': DMA,
            'fmt': fmt_pix,
        },
    ],

    'links': [
        { 'src': (TPG, 0), 'dst': (DMA, 0) },
    ],
}

def get_configs(config_names: list[str]):
    if 'a' in config_names:
        mbus_fmt[0] = fmt_pix[0] = 1920
        mbus_fmt[1] = fmt_pix[1] = 1024
    else:
        mbus_fmt[0] = fmt_pix[0] = 640
        mbus_fmt[1] = fmt_pix[1] = 480

    return configurations['tpg']
