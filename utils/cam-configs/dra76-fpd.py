import v4l2

ov10635_w = 1280
ov10635_h = 720
ov10635_bus_fmt_1 = v4l2.BusFormat.UYVY8_2X8
ov10635_bus_fmt_2 = v4l2.BusFormat.UYVY8_1X16
ov10635_pix_fmt = v4l2.PixelFormats.UYVY
ov10635_meta_h = 1

imx390_w = 1936
imx390_h = 1100
imx390_bus_fmt = v4l2.BusFormat.SRGGB12_1X12
imx390_pix_fmt = v4l2.PixelFormats.SRGGB12
imx390_meta_h = 1

mbus_fmt_ov10635_1 = (ov10635_w, ov10635_h, ov10635_bus_fmt_1)
mbus_fmt_ov10635_2 = (ov10635_w, ov10635_h, ov10635_bus_fmt_2)
fmt_pix_ov10635 = (ov10635_w, ov10635_h, ov10635_pix_fmt)

mbus_fmt_ov10635_meta = (ov10635_w, ov10635_meta_h, v4l2.BusFormat.META_8)
fmt_pix_ov10635_meta = (ov10635_w, ov10635_meta_h, v4l2.MetaFormats.GENERIC_8)

mbus_fmt_imx390 = (imx390_w, imx390_h, imx390_bus_fmt)
fmt_pix_imx390 = (imx390_w, imx390_h, imx390_pix_fmt)

mbus_fmt_imx390_meta = (imx390_w, imx390_meta_h, v4l2.BusFormat.META_12)
fmt_pix_imx390_meta = (imx390_w, imx390_meta_h, v4l2.MetaFormats.GENERIC_CSI2_12)

# IMX219

imx219_w = 640
imx219_h = 480
#imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
#imx219_pix_fmt = v4l2.PixelFormat.SRGGB10P
imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
imx219_pix_fmt = v4l2.PixelFormats.SRGGB8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)
fmt_pix_imx219 = (imx219_w, imx219_h, imx219_pix_fmt)

mbus_fmt_imx219_meta = (imx219_w, 2, v4l2.BusFormat.META_8)
fmt_pix_imx219_meta = (imx219_w, 2, v4l2.MetaFormats.GENERIC_8)

# TPG

mbus_fmt_tpg = (1920, 1024, v4l2.BusFormat.UYVY8_1X16)
fmt_tpg = (1920, 1024, v4l2.PixelFormats.UYVY)

configurations = {}

OVNAME='ov10635'
#OVNAME="ov1063x"

def gen_imx390_pixel(port):
    sensor_ent = f'imx390 {port + 5}-0021'
    ser_ent = f'ds90ub953 4-004{4 + port}'

    return {
        'media': ('CAL', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (1, 0), 'fmt': mbus_fmt_imx390 },
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx390 },
                ],
                'routing': [
                   { 'src': (1, 0), 'dst': (0, 0) },
                ],
            },
            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (0, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx390 },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_imx390 },
                ],
            },
            # Deserializer
            {
                'entity': 'ds90ub960 4-003d',
                'routing': [
                    { 'src': (port, 0), 'dst': (4, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_imx390 },
                    { 'pad': (4, port), 'fmt': mbus_fmt_imx390 },
                ],
            },
            # CSI-2 RX
            {
                'entity': 'CAMERARX0',
                'routing': [
                    { 'src': (0, port), 'dst': (1 + port, 0) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_imx390 },
                    { 'pad': (1 + port, 0), 'fmt': mbus_fmt_imx390 },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'CAL output {port}',
                'fmt': fmt_pix_imx390,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 4-003d', port) },
            { 'src': ('ds90ub960 4-003d', 4), 'dst': ('CAMERARX0', 0) },
            { 'src': ('CAMERARX0', 1 + port), 'dst': (f'CAL output {port}', 0) },
        ],
    }

def gen_imx390_meta(port):
    sensor_ent = f'imx390 {port + 5}-0021'
    ser_ent = f'ds90ub953 4-004{4 + port}'

    return {
        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (2, 0), 'fmt': mbus_fmt_imx390_meta },
                    { 'pad': (0, 1), 'fmt': mbus_fmt_imx390_meta },
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
                    { 'pad': (0, 1), 'fmt': mbus_fmt_imx390_meta },
                    { 'pad': (1, 1), 'fmt': mbus_fmt_imx390_meta },
                ],
            },
            # Deserializer
            {
                'entity': 'ds90ub960 4-003d',
                'routing': [
                    { 'src': (port, 1), 'dst': (4, port + 4) },
                ],
                'pads': [
                    { 'pad': (port, 1), 'fmt': mbus_fmt_imx390_meta },
                    { 'pad': (4, port + 4), 'fmt': mbus_fmt_imx390_meta },
                ],
            },
            # CSI-2 RX
            {
                'entity': 'CAMERARX0',
                'routing': [
                    { 'src': (0, port + 4), 'dst': (1 + port + 4, 0) },
                ],
                'pads': [
                    { 'pad': (0, port + 4), 'fmt': mbus_fmt_imx390_meta },
                    { 'pad': (1 + port + 4, 0), 'fmt': mbus_fmt_imx390_meta },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'CAL output {port + 4}',
                'fmt': fmt_pix_imx390_meta,
                'embedded': True,
                'display': False,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 4-003d', port) },
            { 'src': ('ds90ub960 4-003d', 4), 'dst': ('CAMERARX0', 0) },
            { 'src': ('CAMERARX0', 1 + port + 4), 'dst': (f'CAL output {port + 4}', 0) },
        ],
    }


def gen_imx219_pixel(port):
    sensor_ent = f'imx219 {port + 5}-0010'
    ser_ent = f'ds90ub953 4-004{4 + port}'

    return {
        'media': ('CAL', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (1, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                ],
                'routing': [
                   { 'src': (1, 0), 'dst': (0, 0) },
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
                'entity': 'ds90ub960 4-003d',
                'routing': [
                    { 'src': (port, 0), 'dst': (4, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (4, port), 'fmt': mbus_fmt_imx219 },
                ],
            },
            # CSI-2 RX
            {
                'entity': 'CAMERARX0',
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
                'entity': f'CAL output {port}',
                'fmt': fmt_pix_imx219,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 4-003d', port) },
            { 'src': ('ds90ub960 4-003d', 4), 'dst': ('CAMERARX0', 0) },
            { 'src': ('CAMERARX0', 1 + port), 'dst': (f'CAL output {port}', 0) },
        ],
    }

def gen_imx219_meta(port):
    sensor_ent = f'imx219 {port + 5}-0010'
    ser_ent = f'ds90ub953 4-004{4 + port}'

    return {
        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (2, 0), 'fmt': mbus_fmt_imx219_meta },
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
                'entity': 'ds90ub960 4-003d',
                'routing': [
                    { 'src': (port, 1), 'dst': (4, port + 4) },
                ],
                'pads': [
                    { 'pad': (port, 1), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (4, port + 4), 'fmt': mbus_fmt_imx219_meta },
                ],
            },
            # CSI-2 RX
            {
                'entity': 'CAMERARX0',
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
                'entity': f'CAL output {port + 4}',
                'fmt': fmt_pix_imx219_meta,
                'embedded': True,
                'display': False,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 4-003d', port) },
            { 'src': ('ds90ub960 4-003d', 4), 'dst': ('CAMERARX0', 0) },
            { 'src': ('CAMERARX0', 1 + port + 4), 'dst': (f'CAL output {port + 4}', 0) },
        ],
    }


def gen_ov10635_pixel(port):
    sensor_ent = OVNAME + f' {port + 5}-0030'
    ser_ent = f'ds90ub913a 4-004{4 + port}'

    return {
        'media': ('CAL', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': 1, 'fmt': mbus_fmt_ov10635_1 },
                    { 'pad': 0, 'fmt': mbus_fmt_ov10635_1 },
                ],
                'routing': [
                    { 'src': (1, 0), 'dst': (0, 0) },
                ],
            },
            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (0, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_ov10635_1 },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_ov10635_2 },
                ],
            },
            # Deserializer
            {
                'entity': 'ds90ub960 4-003d',
                'routing': [
                    { 'src': (port, 0), 'dst': (4, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_ov10635_2 },
                    { 'pad': (4, port), 'fmt': mbus_fmt_ov10635_2 },
                ],
            },
            # CSI-2 RX
            {
                'entity': 'CAMERARX0',
                'routing': [
                    { 'src': (0, port), 'dst': (1 + port, 0) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_ov10635_2 },
                    { 'pad': (1 + port, 0), 'fmt': mbus_fmt_ov10635_2 },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'CAL output {port}',
                'fmt': fmt_pix_ov10635,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 4-003d', port) },
            { 'src': ('ds90ub960 4-003d', 4), 'dst': ('CAMERARX0', 0) },
            { 'src': ('CAMERARX0', 1 + port), 'dst': (f'CAL output {port}', 0) },
        ],
    }


def gen_ov10635_meta(port):
    sensor_ent = OVNAME + f' {port + 5}-0030'
    ser_ent = f'ds90ub913a 4-004{4 + port}'

    return {
        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
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
                    { 'pad': (0, 1), 'fmt': mbus_fmt_ov10635_meta },
                    { 'pad': (1, 1), 'fmt': mbus_fmt_ov10635_meta },
                ],
            },
            # Deserializer
            {
                'entity': 'ds90ub960 4-003d',
                'routing': [
                    { 'src': (port, 1), 'dst': (4, port + 4) },
                ],
                'pads': [
                    { 'pad': (port, 1), 'fmt': mbus_fmt_ov10635_meta },
                    { 'pad': (4, port + 4), 'fmt': mbus_fmt_ov10635_meta },
                ],
            },
            # CSI-2 RX
            {
                'entity': 'CAMERARX0',
                'routing': [
                    { 'src': (0, port + 4), 'dst': (1 + port + 4, 0) },
                ],
                'pads': [
                    { 'pad': (0, port + 4), 'fmt': mbus_fmt_ov10635_meta },
                    { 'pad': (1 + port + 4, 0), 'fmt': mbus_fmt_ov10635_meta },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'CAL output {port + 4}',
                'fmt': fmt_pix_ov10635_meta,
                'embedded': True,
                'display': False,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 4-003d', port) },
            { 'src': ('ds90ub960 4-003d', 4), 'dst': ('CAMERARX0', 0) },
            { 'src': ('CAMERARX0', 1 + port + 4), 'dst': (f'CAL output {port + 4}', 0) },
        ],
    }

def gen_ub953_tpg(port):
    ser_ent = f'ds90ub953 4-004{4 + port}'

    return {
        'media': ('CAL', 'model'),

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
                'entity': 'ds90ub960 4-003d',
                'routing': [
                    { 'src': (port, 0), 'dst': (4, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (4, port), 'fmt': mbus_fmt_tpg },
                ],
            },
            # CSI-2 RX
            {
                'entity': 'CAMERARX0',
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
                'entity': f'CAL output {port}',
                'fmt': fmt_tpg,
            },
        ],

        'links': [
            { 'src': (ser_ent, 1), 'dst': ('ds90ub960 4-003d', port) },
            { 'src': ('ds90ub960 4-003d', 4), 'dst': ('CAMERARX0', 0) },
            { 'src': ('CAMERARX0', 1 + port), 'dst': (f'CAL output {port}', 0) },
        ],
    }

configurations['cam0-tpg'] = gen_ub953_tpg(0)
configurations['cam1-tpg'] = gen_ub953_tpg(1)
configurations['cam3-tpg'] = gen_ub953_tpg(3)

configurations['cam0'] = gen_imx390_pixel(0)
configurations['cam1'] = gen_imx390_pixel(1)
configurations['cam2'] = gen_ov10635_pixel(2)
configurations['cam3'] = gen_imx219_pixel(3)

configurations['cam0-meta'] = gen_imx390_meta(0)
configurations['cam1-meta'] = gen_imx390_meta(1)
configurations['cam2-meta'] = gen_ov10635_meta(2)
configurations['cam3-meta'] = gen_imx219_meta(3)

def get_configs():
    return (configurations, ['cam0', 'cam1', 'cam2'])
