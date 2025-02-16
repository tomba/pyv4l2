import v4l2
import v4l2.uapi

# Pixel

imx219_w = 640
imx219_h = 480
#imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
#imx219_pix_fmt = v4l2.PixelFormats.SRGGB10P
imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
# To remap to 16-bit, csi2_bus_fmt must be set to a 16-bit format
csi2_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
imx219_pix_fmt = v4l2.PixelFormats.SRGGB8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)
mbus_fmt_csi2 = (imx219_w, imx219_h, csi2_bus_fmt)
fmt_pix_imx219 = (imx219_w, imx219_h, imx219_pix_fmt)

# Meta

imx219_meta_w = imx219_w
imx219_meta_h = 2
imx219_meta_bus_fmt = v4l2.BusFormat.META_8
imx219_meta_pix_fmt = v4l2.MetaFormats.GENERIC_8

meta_mbus_fmt_imx219 = (imx219_meta_w, imx219_meta_h, imx219_meta_bus_fmt)
meta_fmt_pix_imx219 = (imx219_meta_w, imx219_meta_h, imx219_meta_pix_fmt)

tpg_fmts = [
    (640, 480, v4l2.BusFormat.UYVY8_1X16, v4l2.PixelFormats.UYVY, (1, 15)),
    (640, 480, v4l2.BusFormat.UYVY8_1X16, v4l2.PixelFormats.UYVY, (1, 15)),
]

#tpg_w = 640//2
#tpg_h = 480//2
#mbus_fmt_tpg = (tpg_w, tpg_h, v4l2.BusFormat.UYVY8_1X16)
#fmt_tpg = (tpg_w, tpg_h, v4l2.PixelFormat.UYVY)

configurations = {}

first_imx_i2c_bus = 13

def gen_imx219_pixel(port):
    sensor_ent = f'imx219 {port + first_imx_i2c_bus}-0010'
    ser_ent = f'ds90ub953 6-004{4 + port}'

    return {
        'media': ('rp1-cfe', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
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
                'entity': 'ds90ub960 6-0030',
                'routing': [
                    { 'src': (port, 0), 'dst': (2, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (2, port), 'fmt': mbus_fmt_imx219 },
                ],
            },

            # CSI-2 RX
            {
                'entity': 'csi2',
                'routing': [
                    { 'src': (0, port), 'dst': (1 + port, 0) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (1 + port, 0), 'fmt': mbus_fmt_csi2 },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'rp1-cfe-csi2-ch{port}',
                'fmt': fmt_pix_imx219,
                'kms-format': v4l2.PixelFormats.RGB565,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 6-0030', port) },
            { 'src': ('ds90ub960 6-0030', 2), 'dst': ('csi2', 0) },
            { 'src': ('csi2', 1 + port), 'dst': (f'rp1-cfe-csi2-ch{port}', 0) },
        ],
    }

def gen_imx219_meta(port):
    sensor_ent = f'imx219 {port + first_imx_i2c_bus}-0010'
    ser_ent = f'ds90ub953 6-004{4 + port}'

    return {
        'media': ('rp1-cfe', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (0, 1), 'fmt': meta_mbus_fmt_imx219 },
                ],
            },

            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (0, 1), 'dst': (1, 1) },
                ],
                'pads': [
                    { 'pad': (0, 1), 'fmt': meta_mbus_fmt_imx219 },
                    { 'pad': (1, 1), 'fmt': meta_mbus_fmt_imx219 },
                ],
            },
            # Deserializer
            {
                'entity': 'ds90ub960 6-0030',
                'routing': [
                    { 'src': (port, 1), 'dst': (2, port + 2) },
                ],
                'pads': [
                    { 'pad': (port, 1), 'fmt': meta_mbus_fmt_imx219 },
                    { 'pad': (2, port + 2), 'fmt': meta_mbus_fmt_imx219 },
                ],
            },

            # CSI-2 RX
            {
                'entity': 'csi2',
                'routing': [
                    { 'src': (0, port + 2), 'dst': (1 + port + 2, 0) },
                ],
                'pads': [
                    { 'pad': (0, port + 2), 'fmt': meta_mbus_fmt_imx219 },
                    { 'pad': (1 + port + 2, 0), 'fmt': meta_mbus_fmt_imx219 },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'rp1-cfe-csi2-ch{port+2}',
                'fmt': meta_fmt_pix_imx219,
                'embedded': True,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 6-0030', port) },
            { 'src': ('ds90ub960 6-0030', 2), 'dst': ('csi2', 0) },
            { 'src': ('csi2', 1 + port + 2), 'dst': (f'rp1-cfe-csi2-ch{port + 2}', 0) },
        ],
    }

def gen_ub953_tpg(port):
    ser_ent = f'ds90ub953 6-004{4 + port}'

    tpg_w = tpg_fmts[port][0]
    tpg_h = tpg_fmts[port][1]
    mbus_fmt_tpg = (tpg_w, tpg_h, tpg_fmts[port][2])
    fmt_tpg = (tpg_w, tpg_h, tpg_fmts[port][3])
    ival = tpg_fmts[port][4]

    return {
        'media': ('rp1-cfe', 'model'),

        'subdevs': [
            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (2, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (2, 0), 'fmt': mbus_fmt_tpg, 'ival': ival },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
            # Deserializer
            {
                'entity': 'ds90ub960 6-0030',
                'routing': [
                    { 'src': (port, 0), 'dst': (2, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (2, port), 'fmt': mbus_fmt_tpg },
                ],
            },

            # CSI-2 RX
            {
                'entity': 'csi2',
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
                'entity': f'rp1-cfe-csi2-ch{port}',
                'fmt': fmt_tpg,
            },
        ],

        'links': [
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 6-0030', port) },
            { 'src': ('ds90ub960 6-0030', 2), 'dst': ('csi2', 0) },
            { 'src': ('csi2', 1 + port), 'dst': (f'rp1-cfe-csi2-ch{port}', 0) },
        ],
    }


configurations['cam0'] = gen_imx219_pixel(0)
configurations['cam1'] = gen_imx219_pixel(1)

configurations['cam0-meta'] = gen_imx219_meta(0)
configurations['cam1-meta'] = gen_imx219_meta(1)

configurations['cam0-tpg'] = gen_ub953_tpg(0)
configurations['cam1-tpg'] = gen_ub953_tpg(1)

def get_configs():
    return (configurations, ['cam0'])
