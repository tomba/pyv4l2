#!/usr/bin/python3

import v4l2

# Pixel

imx219_w = 640
imx219_h = 480
#imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
#imx219_pix_fmt = v4l2.PixelFormats.SRGGB10P
imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
imx219_pix_fmt = v4l2.PixelFormats.SRGGB8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)

mbus_fmt_des = mbus_fmt_imx219

fmt_pix = (imx219_w, imx219_h, imx219_pix_fmt)

# TPG
mbus_fmt_des_tpg = (1920, 1080, v4l2.BusFormat.RGB888_1X24)
fmt_pix_tpg = (1920, 1080, v4l2.PixelFormats.YUYV)


configurations = {}

first_imx_i2c_port = 7

def gen_imx219_pixel(port):
    sensor_ent = f'imx219 {port + first_imx_i2c_port}-0010'
    ser_ent = 'max96717 6-0040'
    des_ent = 'max96724 1-0049'
    csi_ent = 'rcar_csi2 fe500000.csi2'
    isp_ent = 'rcar_isp fed00000.isp'
    vin_port = 0

    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

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
                    { 'src': (port, 0), 'dst': (5, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (5, 0), 'fmt': mbus_fmt_des },
                ],
            },

            # CSI-2 RX
            {
                "entity": csi_ent,
                #"routing": [
                #    { "src": (0, port), "dst": (1 + port, 0) },
                #],
                "pads": [
                    { "pad": (0, 0), "fmt": mbus_fmt_des },
                    { "pad": (1, 0), "fmt": mbus_fmt_des },
                ],
            },

            # ISP
            {
                "entity": isp_ent,
                #"routing": [
                #    { "src": (0, port), "dst": (1 + port, 0) },
                #],
                "pads": [
                    { "pad": (0, 0), "fmt": mbus_fmt_des },
                    { "pad": (1, 0), "fmt": mbus_fmt_des },
                ],
            },
        ],

        "devices": [
            {
                "entity": f"VIN{vin_port} output",
                "fmt": fmt_pix,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, 0) },
            { 'src': (des_ent, 5), 'dst': (csi_ent, 0) },
            { "src": (csi_ent, 1), "dst": (isp_ent, 0) },
            { "src": (isp_ent, 1), "dst": (f"VIN{vin_port} output", 0) },
        ],
    }

def gen_des_tpg(port):
    sensor_ent = f'imx219 {port + first_imx_i2c_port}-0010'
    ser_ent = 'max96717 6-0040'
    des_ent = 'max96724 1-0049'
    csi_ent = 'rcar_csi2 fe500000.csi2'
    isp_ent = 'rcar_isp fed00000.isp'
    vin_port = 0

    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

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
                    { 'src': (port, 0), 'dst': (5, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_des_tpg },
                    { 'pad': (5, 0), 'fmt': mbus_fmt_des_tpg },
                ],
            },

            # CSI-2 RX
            {
                "entity": csi_ent,
                #"routing": [
                #    { "src": (0, port), "dst": (1 + port, 0) },
                #],
                "pads": [
                    { "pad": (0, 0), "fmt": mbus_fmt_des_tpg },
                    { "pad": (1, 0), "fmt": mbus_fmt_des_tpg },
                ],
            },

            # ISP
            {
                "entity": isp_ent,
                #"routing": [
                #    { "src": (0, port), "dst": (1 + port, 0) },
                #],
                "pads": [
                    { "pad": (0, 0), "fmt": mbus_fmt_des_tpg },
                    { "pad": (1, 0), "fmt": mbus_fmt_des_tpg },
                ],
            },
        ],

        "devices": [
            {
                "entity": f"VIN{vin_port} output",
                "fmt": fmt_pix_tpg,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, 0) },
            { 'src': (des_ent, 5), 'dst': (csi_ent, 0) },
            { "src": (csi_ent, 1), "dst": (isp_ent, 0) },
            { "src": (isp_ent, 1), "dst": (f"VIN{vin_port} output", 0) },
        ],
    }


configurations['cam0'] = gen_imx219_pixel(0)
configurations['tpg'] = gen_des_tpg(0)

def get_configs():
    return (configurations, ['cam0'])
