from __future__ import annotations

import v4l2

tpg_w = 640
tpg_h = 480

mbus_fmt = [tpg_w, tpg_h, v4l2.BusFormat.RBG888_1X24]
fmt_pix = [tpg_w, tpg_h, v4l2.PixelFormats.BGR888]

configurations = {}

#driver          xilinx-video
#model           Xilinx Video Composite Device
#serial
#bus info        platform:xilinx_tpg_top
#hw revision     0x0
#driver version  6.16.0
#
#Device topology
#- entity 1: xilinx_tpg_top output 0 (1 pad, 1 link)
#            type Node subtype V4L flags 0
#            device node name /dev/video0
#	pad0: SINK
#		<- "a0050000.v_tpg":0 [ENABLED]
#
#- entity 5: a0050000.v_tpg (1 pad, 1 link, 0 routes)
#            type V4L2 subdev subtype Unknown flags 0
#            device node name /dev/v4l-subdev0
#	pad0: SOURCE
#		[stream:0 fmt:RBG888_1X24/0x0 field:none colorspace:srgb]
#		-> "xilinx_tpg_top output 0":0 [ENABLED]

MEDIA = 'platform:xilinx_tpg_top'
TPG = 'a0050000.v_tpg'
DMA = 'xilinx_tpg_top output 0'

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
