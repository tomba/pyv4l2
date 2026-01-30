import v4l2
import v4l2.uapi

USE_RAW_10=False

#imx219_w, imx219_h = 3280, 2464
#imx219_w, imx219_h = 1920, 1080
imx219_w, imx219_h = 640, 480

if USE_RAW_10:
    imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
    imx219_pix_fmt = v4l2.PixelFormats.SRGGB10
else:
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

def gen_imx219_pixel(port):
    sensor_ent = f'imx219 {port + 5}-0010'
    ser_ent = f'ds90ub953 4-004{4 + port}'
    des_ent = 'ds90ub960 4-0030'
    csirx_ent = 'cdns_csi2rx.30101000.csi-bridge'
    csirx2_ent = '30102000.ticsi2rx'
    dma_ent = '30102000.ticsi2rx context'

    return {
        'media': ('TI-CSI2RX', 'model'),

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
#                    { 'pad': (1, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                ],
#                'routing': [
#                   { 'src': (1, 0), 'dst': (0, 0) },
#                ],
                'controls': [
                    (v4l2.uapi.V4L2_CID_ANALOGUE_GAIN, 200),
                    (0x009f0903, 0),
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
                    { 'src': (port, 0), 'dst': (4, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (4, port), 'fmt': mbus_fmt_imx219 },
                ],
            },
            # CSI-2 RX
            {
                'entity': csirx_ent,
                'routing': [
                    { 'src': (0, port), 'dst': (1, port) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (1, port), 'fmt': mbus_fmt_imx219 },
                ],
            },
            # CSI-2 RX 2
            {
                'entity': csirx2_ent,
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
                'entity': f'{dma_ent} {port}',
                'fmt': fmt_pix_imx219,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 4), 'dst': (csirx_ent, 0) },
            { 'src': (csirx_ent, 1), 'dst': (csirx2_ent, 0) },
            { 'src': (csirx2_ent, 1 + port), 'dst': (f'{dma_ent} {port}', 0) },
        ],
    }

def gen_imx219_meta(port):
    sensor_ent = f'imx219 {port + 5}-0010'
    ser_ent = f'ds90ub953 4-004{4 + port}'
    des_ent = 'ds90ub960 4-0030'
    csirx_ent = 'cdns_csi2rx.30101000.csi-bridge'
    csirx2_ent = '30102000.ticsi2rx'
    dma_ent = '30102000.ticsi2rx context'

    meta_stream_offset = 4
    meta_port_offset = 1

    return {
        'media': ('TI-CSI2RX', 'model'),

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
                'entity': des_ent,
                'routing': [
                    { 'src': (port, 1), 'dst': (4, port + meta_stream_offset) },
                ],
                'pads': [
                    { 'pad': (port, 1), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (4, port + meta_stream_offset), 'fmt': mbus_fmt_imx219_meta },
                ],
            },
            # CSI-2 RX
            {
                'entity': csirx_ent,
                'routing': [
                    { 'src': (0, port + meta_stream_offset), 'dst': (1, port + meta_stream_offset) },
                ],
                'pads': [
                    { 'pad': (0, port + meta_stream_offset), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (1, port + meta_stream_offset), 'fmt': mbus_fmt_imx219_meta },
                ],
            },
            # CSI-2 RX 2
            {
                'entity': csirx2_ent,
                'routing': [
                    { 'src': (0, port + meta_stream_offset), 'dst': (1 + port + meta_port_offset, 0) },
                ],
                'pads': [
                    { 'pad': (0, port + meta_stream_offset), 'fmt': mbus_fmt_imx219_meta },
                    { 'pad': (1 + port + meta_port_offset, 0), 'fmt': mbus_fmt_imx219_meta },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'{dma_ent} {port + meta_port_offset}',
                'fmt': fmt_pix_imx219_meta,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 4), 'dst': (csirx_ent, 0) },
            { 'src': (csirx_ent, 1), 'dst': (csirx2_ent, 0) },
            { 'src': (csirx2_ent, 1 + port + meta_port_offset), 'dst': (f'{dma_ent} {port + meta_port_offset}', 0) },
        ],
    }

def gen_ub953_tpg(port):
    ser_ent = f'ds90ub953 4-004{4 + port}'
    des_ent = 'ds90ub960 4-0030'
    csirx_ent = 'cdns_csi2rx.30101000.csi-bridge'
    csirx2_ent = '30102000.ticsi2rx'
    dma_ent = '30102000.ticsi2rx context'

    return {
        'media': ('TI-CSI2RX', 'model'),

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
                'entity': csirx_ent,
                'routing': [
                    { 'src': (0, port), 'dst': (1, port) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_tpg },
                    { 'pad': (1, port), 'fmt': mbus_fmt_tpg },
                ],
            },
            # CSI-2 RX 2
            {
                'entity': csirx2_ent,
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
                'entity': f'{dma_ent} {port}',
                'fmt': fmt_tpg,
            },
        ],

        'links': [
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 4), 'dst': (csirx_ent, 0) },
            { 'src': (csirx_ent, 1), 'dst': (csirx2_ent, 0) },
            { 'src': (csirx2_ent, 1 + port), 'dst': (f'{dma_ent} {port}', 0) },
        ],
    }

configurations['cam0-tpg'] = gen_ub953_tpg(0)
configurations['cam1-tpg'] = gen_ub953_tpg(1)
configurations['cam3-tpg'] = gen_ub953_tpg(3)
configurations['cam3-tpg'] = gen_ub953_tpg(4)

configurations['cam0'] = gen_imx219_pixel(0)
configurations['cam1'] = gen_imx219_pixel(1)
configurations['cam2'] = gen_imx219_pixel(2)
configurations['cam3'] = gen_imx219_pixel(3)

configurations['cam0-meta'] = gen_imx219_meta(0)
configurations['cam1-meta'] = gen_imx219_meta(1)
configurations['cam2-meta'] = gen_imx219_meta(2)
configurations['cam3-meta'] = gen_imx219_meta(3)

def get_configs():
    return (configurations, ['cam0', 'cam1', 'cam2', 'cam3'])
