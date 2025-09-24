from __future__ import annotations
import v4l2

imx219_w = 640
imx219_h = 480

mbus_fmt = [imx219_w, imx219_h, v4l2.BusFormat.SRGGB10_1X10]
fmt_pix = [imx219_w, imx219_h, v4l2.PixelFormats.SRGGB10P]

configurations = {}

MEDIA = 'platform:xilinx_video_top'
IMX219 = 'imx219 2-0010'
CSI2RX = 'a0012000.mipi_csi2_rx_subsystem'
DMA = 'xilinx_video_top output 0'

configurations['tpg'] = {
    'media': (MEDIA, 'bus_info'),

    'subdevs': [
        {
            'entity': IMX219,
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt },
            ],
        },
        {
            'entity': CSI2RX,
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt },
                { 'pad': 1, 'fmt': mbus_fmt },
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
        { 'src': (IMX219, 0), 'dst': (CSI2RX, 0) },
        { 'src': (CSI2RX, 1), 'dst': (DMA, 0) },
    ],
}

def get_configs(config_names: list[str]):
    return configurations['tpg']
