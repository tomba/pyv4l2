#!/usr/bin/python3

import v4l2

# Pixel

imx219_w = 1920
imx219_h = 1080
imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
imx219_pix_fmt = v4l2.PixelFormats.SRGGB10P
#imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
#imx219_pix_fmt = v4l2.PixelFormats.SRGGB8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)

mbus_fmt_des = mbus_fmt_imx219

fmt_pix = (imx219_w, imx219_h, imx219_pix_fmt)

configurations = {}

first_imx_i2c_port = 14

def gen_imx219_pixel(port):
    sensor_ent = f'imx219 {port + first_imx_i2c_port}-0010'
    ser_ent = 'max96717 13-0040'
    des_ent = 'max96724 6-0027'

    return {
        'media': ('rp1-cfe', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                ],
            },

            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (0, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_imx219 },
                ],
            },
            # Deserializer
            {
                'entity': des_ent,
                'routing': [
                    { 'src': (port, 0), 'dst': (6, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (6, 0), 'fmt': mbus_fmt_des },
                ],
            },

            # CSI-2 RX
            {
                'entity': 'csi2',
                'routing': [
                    { 'src': (0, port), 'dst': (1 + port, 0) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_des },
                    { 'pad': (1 + port, 0), 'fmt': mbus_fmt_des },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'rp1-cfe-csi2-ch{port}',
                'fmt': fmt_pix,
                'embedded': False,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, 0) },
            { 'src': (des_ent, 6), 'dst': ('csi2', 0) },
            { 'src': ('csi2', 1 + port), 'dst': (f'rp1-cfe-csi2-ch{port}', 0) },
        ],
    }

configurations['cam0'] = gen_imx219_pixel(0)

def get_configs():
    return (configurations, ['cam0'])
