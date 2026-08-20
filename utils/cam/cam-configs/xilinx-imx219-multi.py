from __future__ import annotations
import v4l2
import v4l2.uapi

USE_RAW_10=False

imx219_w = 640
imx219_h = 480

if USE_RAW_10:
    imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
    imx219_pix_fmt = v4l2.PixelFormats.SRGGB10P
else:
    imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
    imx219_pix_fmt = v4l2.PixelFormats.SRGGB8

mbus_fmt = [imx219_w, imx219_h, imx219_bus_fmt]
fmt_pix = [imx219_w, imx219_h, imx219_pix_fmt]

configurations = {}

MEDIA = 'platform:xilinx_video_top'
IMX219 = 'imx219 5-0010'
CSI2RX = 'a0012000.mipi_csi2_rx_subsystem'
DMA0 = 'xilinx_video_top output 0'
DMA1 = 'xilinx_video_top output 1'
SWITCH0 = 'pl-bus:axis_switch_0'

configurations['cam0'] = {
    'media': (MEDIA, 'bus_info'),

    'subdevs': [
        {
            'entity': IMX219,
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt },
            ],
            'controls': [
                (v4l2.uapi.V4L2_CID_ANALOGUE_GAIN, 200),
            ],
        },
        {
            'entity': SWITCH0,
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt },
                { 'pad': (1, 0), 'fmt': mbus_fmt },
            ],
        },
        {
            'entity': CSI2RX,
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt },
                { 'pad': (1, 0), 'fmt': mbus_fmt },
            ],
        },
    ],

    'devices': [
        {
            'entity': DMA0,
            'fmt': fmt_pix,
        },
    ],

    'links': [
        { 'src': (IMX219, 0), 'dst': (CSI2RX, 0) },
        { 'src': (CSI2RX, 1), 'dst': (SWITCH0, 0) },
        { 'src': (SWITCH0, 1), 'dst': (DMA0, 0) },
    ],
}

def get_configs():
    return (configurations, ['cam0'])
