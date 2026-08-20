from __future__ import annotations

from cam_helpers import merge_configs

import v4l2

imx219_w = 640
imx219_h = 480

mbus_fmt = [imx219_w, imx219_h, v4l2.BusFormat.SRGGB8_1X8]
fmt_pix = [imx219_w, imx219_h, v4l2.PixelFormats.SRGGB8]

tpg_w = 640
tpg_h = 480

tpg_mbus_fmt = [tpg_w, tpg_h, v4l2.BusFormat.RBG888_1X24]
tpg_fmt_pix = [tpg_w, tpg_h, v4l2.PixelFormats.BGR888]


configurations = {}

MEDIA = 'platform:xilinx_video_top'
IMX219 = 'imx219 6-0010'
CSI2RX = 'a0012000.mipi_csi2_rx_subsystem'
DMA = 'xilinx_video_top output 0'

configurations['cam'] = {
    'media': (MEDIA, 'bus_info'),
    'subdevs': [
        {
            'entity': IMX219,
            'pads': [
                {'pad': 0, 'fmt': mbus_fmt},
            ],
        },
        {
            'entity': CSI2RX,
            'pads': [
                {'pad': 0, 'fmt': mbus_fmt},
                {'pad': 1, 'fmt': mbus_fmt},
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
        {'src': (IMX219, 0), 'dst': (CSI2RX, 0)},
        {'src': (CSI2RX, 1), 'dst': (DMA, 0)},
    ],
}

TPG = 'a0050000.v_tpg'
TPG_DMA = 'xilinx_video_top output 1'

configurations['tpg'] = {
    'media': (MEDIA, 'bus_info'),
    'subdevs': [
        {
            'entity': TPG,
            'pads': [
                {'pad': 0, 'fmt': tpg_mbus_fmt},
            ],
        },
    ],
    'devices': [
        {
            'entity': TPG_DMA,
            'fmt': tpg_fmt_pix,
        },
    ],
    'links': [
        {'src': (TPG, 0), 'dst': (TPG_DMA, 0)},
    ],
}


def get_configs(config_names: list[str]):
    # return configurations['cam']

    if not config_names:
        config_names = ['cam']

    cfgs = []
    for name in config_names:
        if name in configurations:
            cfgs.append(configurations[name])
        else:
            raise ValueError(f'Unknown configuration: {name}')

    merged_config = merge_configs(cfgs)
    return merged_config
