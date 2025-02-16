import v4l2
import v4l2.uapi

USE_RAW_10=False

# Pixel

imx219_w = 640
imx219_h = 480
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

# TPG

mbus_fmt_tpg = (1920, 1080, v4l2.BusFormat.RGB888_1X24)
fmt_tpg = (1920, 1080, v4l2.PixelFormats.XRGB8888)


first_ser_i2c_port = 6
first_imx_i2c_port = 7

if False:
    # The deser 0 is unstable due to unstable vpoc
    des_ent = 'max96724 1-0049'
    csi_ent = 'rcar_csi2 fe500000.csi2'
    isp_ent = 'rcar_isp fed00000.isp'
    vin_port = 0
else:
    des_ent = 'max96724 1-004b'
    csi_ent = 'rcar_csi2 fe540000.csi2'
    isp_ent = 'rcar_isp fed20000.isp'
    vin_port = 8

def gen_imx219_pixel(port):
    sensor_ent = f'imx219 {port * 2 + first_imx_i2c_port}-0010'
    ser_ent = f'max96717 {port * 2 + first_ser_i2c_port}-0040'

    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    #{ 'pad': (1, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                ],
                'routing': [
                   { 'src': (1, 0), 'dst': (0, 0) },
                ],
                'controls': [
                    (v4l2.uapi.V4L2_CID_ANALOGUE_GAIN, 200),
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
                    { 'pad': (5, port), 'fmt': mbus_fmt_imx219 },
                ],
            },

            # CSI-2 RX
            {
                'entity': csi_ent,
                'routing': [
                    { 'src': (0, port), 'dst': (1, port) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (1, port), 'fmt': mbus_fmt_imx219 },
                ],
            },

            # ISP
            {
                'entity': isp_ent,
                'routing': [
                    { 'src': (0, port), 'dst': (1 + port, 0) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (1 + port, 0), 'fmt': mbus_fmt_imx219 },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'VIN{vin_port + port} output',
                'fmt': fmt_pix,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 5), 'dst': (csi_ent, 0) },
            { 'src': (csi_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, 1 + port), 'dst': (f'VIN{vin_port + port} output', 0) },
        ],
    }

def gen_imx219_meta(port):
    sensor_ent = f'imx219 {port * 2 + first_imx_i2c_port}-0010'
    ser_ent = f'max96717 {port * 2 + first_ser_i2c_port}-0040'

    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (0, 1), 'fmt': mbus_fmt_imx219_meta },
                ],
                'routing': [
                   { 'src': (2, 0), 'dst': (0, 1) },
                ],
            },

            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (0, 1), 'dst': (1, 1) },
                ],
                'pads': [
                    { 'pad': (0, 1), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (1, 1), 'fmt': mbus_fmt_imx219_meta },
                ],
            },
            # Deserializer
            {
                'entity': des_ent,
                'routing': [
                    { 'src': (port, 1), 'dst': (5, port + 4) },
                ],
                'pads': [
                    { 'pad': (port, 1), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (5, port + 4), 'fmt': mbus_fmt_imx219_meta },
                ],
            },

            # CSI-2 RX
            {
                'entity': csi_ent,
                'routing': [
                    { 'src': (0, port + 4), 'dst': (1, port + 4) },
                ],
                'pads': [
                    { 'pad': (0, port + 4), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (1, port + 4), 'fmt': mbus_fmt_imx219_meta },
                ],
            },

            # ISP
            {
                'entity': isp_ent,
                'routing': [
                    { 'src': (0, port + 4), 'dst': (1 + port + 4, 0) },
                ],
                'pads': [
                    { 'pad': (0, port + 4), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (1 + port + 4, 0), 'fmt': mbus_fmt_imx219_meta },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'VIN{vin_port + port + 4} output',
                'fmt': fmt_pix_imx219_meta,
                'embedded': True,
                'display': False,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 5), 'dst': (csi_ent, 0) },
            { 'src': (csi_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, 1 + port + 4), 'dst': (f'VIN{vin_port + port + 4} output', 0) },
        ],
    }

def gen_des_tpg():
    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

        'subdevs': [
            # Deserializer
            {
                'entity': des_ent,
                'routing': [
                    { 'src': (8, 0), 'dst': (5, 0) },
                ],
                'pads': [
                    { 'pad': (8, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (5, 0), 'fmt': mbus_fmt_tpg },
                ],
            },

            # CSI-2 RX
            {
                'entity': csi_ent,
                #'routing': [
                #    { 'src': (0, port), 'dst': (1 + port, 0) },
                #],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_tpg },
                ],
            },

            # ISP
            {
                'entity': isp_ent,
                #'routing': [
                #    { 'src': (0, port), 'dst': (1 + port, 0) },
                #],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'VIN{vin_port} output',
                'fmt': fmt_tpg,
            },
        ],

        'links': [
            { 'src': (des_ent, 5), 'dst': (csi_ent, 0) },
            { 'src': (csi_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, 1), 'dst': (f'VIN{vin_port} output', 0) },
        ],
    }

def gen_ser_tpg(port):
    ser_ent = f'max96717 {port * 2 + first_ser_i2c_port}-0040'

    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

        'subdevs': [
            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (2, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (2, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
            # Deserializer
            {
                'entity': des_ent,
                'routing': [
                    { 'src': (port, 0), 'dst': (5, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (5, port), 'fmt': mbus_fmt_tpg },
                ],
            },

            # CSI-2 RX
            {
                'entity': csi_ent,
                'routing': [
                    { 'src': (0, port), 'dst': (1, port) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_tpg },
                    { 'pad': (1, port), 'fmt': mbus_fmt_tpg },
                ],
            },

            # ISP
            {
                'entity': isp_ent,
                'routing': [
                    { 'src': (0, port), 'dst': (1 + port, 0) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_tpg },
                    { 'pad': (1 + port, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'VIN{vin_port + port} output',
                'fmt': fmt_tpg,
            },
        ],

        'links': [
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 5), 'dst': (csi_ent, 0) },
            { 'src': (csi_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, 1 + port), 'dst': (f'VIN{vin_port + port} output', 0) },
        ],
    }

def get_configs():
    configurations = {}

    for i in range(2):
        configurations[f'cam{i}'] = gen_imx219_pixel(i)
        configurations[f'cam{i}-meta'] = gen_imx219_meta(i)
        configurations[f'ser{i}-tpg'] = gen_ser_tpg(i)

    configurations['des-tpg'] = gen_des_tpg()

    return (configurations, ['cam0'])
