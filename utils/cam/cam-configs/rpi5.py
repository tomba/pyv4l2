import v4l2

imx219_w = 640
imx219_h = 480
#imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
#imx219_pix_fmt = v4l2.PixelFormat.SRGGB10P
imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
imx219_pix_fmt = v4l2.PixelFormats.SRGGB8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)
fmt_pix_imx219 = (imx219_w, imx219_h, imx219_pix_fmt)

imx219_meta_w = imx219_w
imx219_meta_h = 2
imx219_meta_bus_fmt = v4l2.BusFormat.META_8
imx219_meta_pix_fmt = v4l2.MetaFormats.GENERIC_8
#imx219_meta_bus_fmt = v4l2.BusFormat.META_10
#imx219_meta_pix_fmt = v4l2.MetaFormat.GENERIC_CSI2_10

meta_mbus_fmt_imx219 = (imx219_meta_w, imx219_meta_h, imx219_meta_bus_fmt)
meta_fmt_pix_imx219 = (imx219_meta_w, imx219_meta_h, imx219_meta_pix_fmt)

configurations = {}

sensor_ent = 'imx219 6-0010'

configurations['cam0'] = {
    'media': ('rp1-cfe', 'model'),

    'subdevs': [
        # Camera
        {
            'entity': sensor_ent,
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
            ],
#            "routing": [
#               { "src": (1, 0), "dst": (0, 0) },
#            ],
        },
        # CSI-2 RX
        {
            'entity': 'csi2',
            'routing': [
                { 'src': (0, 0), 'dst': (1, 0) },
            ],
            'pads': [
                { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                { 'pad': (1, 0), 'fmt': mbus_fmt_imx219 },
            ],
        },
    ],

    'devices': [
        {
            'entity': 'rp1-cfe-csi2-ch0',
            'fmt': fmt_pix_imx219,
        },
    ],

    'links': [
        { 'src': (sensor_ent, 0), 'dst': ('csi2', 0) },
        { 'src': ('csi2', 1), 'dst': ('rp1-cfe-csi2-ch0', 0) },
    ],
}

configurations['cam0-meta'] = {
    'subdevs': [
        # Camera
        {
            'entity': sensor_ent,
            'pads': [
                { 'pad': (0, 1), 'fmt': meta_mbus_fmt_imx219 },
            ],
#            "routing": [
#               { "src": (1, 0), "dst": (0, 0) },
#            ],
        },
        # CSI-2 RX
        {
            'entity': 'csi2',
            'routing': [
                { 'src': (0, 1), 'dst': (2, 0) },
            ],
            'pads': [
                { 'pad': (0, 1), 'fmt': meta_mbus_fmt_imx219 },
                { 'pad': (2, 0), 'fmt': meta_mbus_fmt_imx219 },
            ],
        },
    ],

    'devices': [
        {
            'entity': 'rp1-cfe-csi2-ch1',
            'fmt': meta_fmt_pix_imx219,
            'embedded': True,
        },
    ],

    'links': [
        { 'src': (sensor_ent, 0), 'dst': ('csi2', 0) },
        { 'src': ('csi2', 2), 'dst': ('rp1-cfe-csi2-ch1', 0) },
    ],
}

def get_configs():
    return (configurations, ['cam0'])
