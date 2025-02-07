import v4l2
import v4l2.uapi

USE_RAW_10=True
MEDIA_DEVICE_NAME = ('rp1-cfe', 'model')
DESER_REGEX = '(max96724|max96726a|max9296a) [0-9]+-[a-f0-9]+'

# Pixel

imx219_w = 640
imx219_h = 480
if USE_RAW_10:
    imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
    imx219_pix_fmt = v4l2.PixelFormats.SRGGB10P
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

mbus_fmt_tpg = (640, 480, v4l2.BusFormat.RGB888_1X24)
fmt_tpg = (640, 480, v4l2.PixelFormats.BGR888)


def gen_imx219_pixel(des_ent, cameras, port):
    sensor_ent = cameras[port][1]
    ser_ent = cameras[port][0]

    return {
        'media': MEDIA_DEVICE_NAME,

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
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
                    { 'src': (port, 0), 'dst': (6, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (6, port), 'fmt': mbus_fmt_imx219 },
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
                    { 'pad': (1 + port, 0), 'fmt': mbus_fmt_imx219 },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'rp1-cfe-csi2-ch{port}',
                'fmt': fmt_pix,
                'kms-format': v4l2.PixelFormats.RGB565,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 6), 'dst': ('csi2', 0) },
            { 'src': ('csi2', 1 + port), 'dst': (f'rp1-cfe-csi2-ch{port}', 0) },
        ],
    }

def gen_imx219_meta(des_ent, cameras, port):
    sensor_ent = cameras[port][1]
    ser_ent = cameras[port][0]

    return {
        'media': MEDIA_DEVICE_NAME,

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
                    { 'src': (port, 1), 'dst': (6, port + 4) },
                ],
                'pads': [
                    { 'pad': (port, 1), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (6, port + 4), 'fmt': mbus_fmt_imx219_meta },
                ],
            },

            # CSI-2 RX
            {
                'entity': 'csi2',
                'routing': [
                    { 'src': (0, port + 4), 'dst': (1 + port + 2, 0) },
                ],
                'pads': [
                    { 'pad': (0, port + 4), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (1 + port + 2, 0), 'fmt': mbus_fmt_imx219_meta },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'rp1-cfe-csi2-ch{port + 2}',
                'fmt': fmt_pix_imx219_meta,
                'embedded': True,
                'display': False,
                'kms-format': v4l2.PixelFormats.RGB565,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 6), 'dst': ('csi2', 0) },
            { 'src': ('csi2', 1 + port + 2), 'dst': (f'rp1-cfe-csi2-ch{port + 2}', 0) },
        ],
    }

def gen_des_tpg(des_ent):
    return {
        'media': MEDIA_DEVICE_NAME,

        'subdevs': [
            # Deserializer
            {
                'entity': des_ent,
                'routing': [
                    { 'src': (8, 0), 'dst': (6, 0) },
                ],
                'pads': [
                    { 'pad': (8, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (6, 0), 'fmt': mbus_fmt_tpg },
                ],
            },

            # CSI-2 RX
            {
                'entity': 'csi2',
                'routing': [
                    { 'src': (0, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
        ],

        'devices': [
            {
                'entity': 'rp1-cfe-csi2-ch0',
                'fmt': fmt_tpg,
            },
        ],

        'links': [
            { 'src': (des_ent, 6), 'dst': ('csi2', 0) },
            { 'src': ('csi2', 1), 'dst': ('rp1-cfe-csi2-ch0', 0) },
        ],
    }

def gen_ser_tpg(des_ent, cameras, port):
    ser_ent = cameras[port][0]

    return {
        'media': MEDIA_DEVICE_NAME,

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
                    { 'src': (port, 0), 'dst': (6, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (6, port), 'fmt': mbus_fmt_tpg },
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
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 6), 'dst': ('csi2', 0) },
            { 'src': ('csi2', 1 + port), 'dst': (f'rp1-cfe-csi2-ch{port}', 0) },
        ],
    }

# Find serializers and sensors connected to the deserializer
def find_devices(mdev_name, deser_regex):
    md = v4l2.MediaDevice(*mdev_name)
    assert md
    deser = md.find_entity(regex=deser_regex)
    assert deser

    cameras = {}

    for p in deser.pads:
        if not p.is_sink:
            continue

        if len(p.links) == 0:
            continue

        assert len(p.links) == 1

        ser = p.links[0].source.entity
        sensor = ser.pads[0].links[0].source.entity

        cameras[p.index] = (ser.name, sensor.name)

    return deser.name, cameras

def get_configs():
    des_name, cameras = find_devices(MEDIA_DEVICE_NAME, DESER_REGEX)

    num_cameras = len(cameras)

    configurations = {}
    for i in range(num_cameras):
        configurations[f'cam{i}'] = gen_imx219_pixel(des_name, cameras, i)
        configurations[f'cam{i}-meta'] = gen_imx219_meta(des_name, cameras, i)
        configurations[f'ser{i}-tpg'] = gen_ser_tpg(des_name, cameras, i)

    configurations['des-tpg'] = gen_des_tpg(des_name)

    return (configurations, ['cam0'])
