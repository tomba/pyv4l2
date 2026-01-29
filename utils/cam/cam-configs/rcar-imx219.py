from __future__ import annotations

import v4l2
import v4l2.uapi

USE_RAW_10=False

# Pixel

imx219_w, imx219_h = 3280, 2464
#imx219_w, imx219_h = 1920, 1080
#imx219_w, imx219_h = 640, 480

if USE_RAW_10:
    imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
    imx219_pix_fmt = v4l2.PixelFormats.SRGGB10
else:
    imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
    imx219_pix_fmt = v4l2.PixelFormats.SRGGB8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)
fmt_pix = (imx219_w, imx219_h, imx219_pix_fmt)

# Embedded

if USE_RAW_10:
    imx219_bus_fmt_meta = v4l2.BusFormat.META_10
    imx219_pix_fmt_meta = v4l2.MetaFormats.GENERIC_CSI2_10
else:
    imx219_bus_fmt_meta = v4l2.BusFormat.META_8
    imx219_pix_fmt_meta = v4l2.MetaFormats.GENERIC_8

mbus_fmt_imx219_meta = (imx219_w, 2, imx219_bus_fmt_meta)
fmt_pix_imx219_meta = (imx219_w, 2, imx219_pix_fmt_meta)

csi_ent = 'rcar_csi2 fe500000.csi2'
isp_ent = 'rcar_isp fed00000.isp'
vin_port_vid = 0
vin_port_emb = 1
first_imx_i2c_port = 1

def gen_imx219_pixel(port):
    sensor_ent = f'imx219 {port * 2 + first_imx_i2c_port}-0010'

    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                ],
#                'routing': [
#                   { 'src': (1, 0), 'dst': (0, 0) },
#                ],
                'controls': [
                    (v4l2.uapi.V4L2_CID_ANALOGUE_GAIN, 200),
                    (0x009f0903, 1),
                ],
            },

            # CSI-2 RX
            {
                'entity': csi_ent,
#                'routing': [
#                    { 'src': (0, 0), 'dst': (1, 0) },
#                ],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_imx219 },
                ],
            },

            # ISP
            {
                'entity': isp_ent,
#                'routing': [
#                    { 'src': (0, 0), 'dst': (1 + vin_port_vid, 0) },
#                ],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (1 + vin_port_vid, 0), 'fmt': mbus_fmt_imx219 },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'VIN{vin_port_vid} output',
                'fmt': fmt_pix,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (csi_ent, 0) },
            { 'src': (csi_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, 1 + vin_port_vid), 'dst': (f'VIN{vin_port_vid} output', 0) },
        ],
    }

def gen_imx219_meta(port):
    sensor_ent = f'imx219 {port * 2 + first_imx_i2c_port}-0010'

    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
#                    { 'pad': (0, 1), 'fmt': mbus_fmt_imx219_meta },
                ],
                'routing': [
                   { 'src': (2, 0), 'dst': (0, 1) },
                ],
            },

            # CSI-2 RX
            {
                'entity': csi_ent,
                'routing': [
                    { 'src': (0, 1), 'dst': (1, 1) },
                ],
                'pads': [
                    { 'pad': (0, 1), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (1, 1), 'fmt': mbus_fmt_imx219_meta },
                ],
            },

            # ISP
            {
                'entity': isp_ent,
                'routing': [
                    { 'src': (0, 1), 'dst': (1 + vin_port_emb, 0) },
                ],
                'pads': [
                    { 'pad': (0, 1), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (1 + vin_port_emb, 0), 'fmt': mbus_fmt_imx219_meta },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'VIN{vin_port_emb} output',
                'fmt': fmt_pix_imx219_meta,
                'embedded': True,
                'display': False,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (csi_ent, 0) },
            { 'src': (csi_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, 1 + vin_port_emb), 'dst': (f'VIN{vin_port_emb} output', 0) },
        ],
    }

def get_configs():
    configurations = {}

    for i in range(1):
        configurations[f'cam{i}'] = gen_imx219_pixel(i)
        configurations[f'cam{i}-meta'] = gen_imx219_meta(i)

    return (configurations, ['cam0'])
