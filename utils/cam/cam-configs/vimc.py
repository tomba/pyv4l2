import v4l2

imx219_w = 640
imx219_h = 480
imx219_bus_fmt = v4l2.BusFormat.SBGGR8_1X8
imx219_pix_fmt = v4l2.PixelFormats.SBGGR8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)
fmt_pix_imx219 = (imx219_w, imx219_h, imx219_pix_fmt)

mbus_fmt = (imx219_w, imx219_h, v4l2.BusFormat.RGB888_1X24)
fmt_pix = (imx219_w, imx219_h, v4l2.PixelFormats.BGR888)

configurations = {}

configurations['cam0'] = {
    'media': ('VIMC MDEV', 'model'),

    'subdevs': [
        {
            'entity': 'Sensor A',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_imx219 },
            ],
        },
        {
            'entity': 'Debayer A',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt_imx219 },
                { 'pad': 1, 'fmt': mbus_fmt },
            ],
        },
        {
            'entity': 'Scaler',
            'pads': [
                { 'pad': 0, 'fmt': mbus_fmt },
                { 'pad': 1, 'fmt': mbus_fmt },
            ],
        },
    ],

    'devices': [
        {
            'entity': 'RGB/YUV Capture',
            'fmt': fmt_pix,
        },
    ],

    'links': [
        { 'src': ('Sensor A', 0), 'dst': ('Debayer A', 0) },
        { 'src': ('Debayer A', 1), 'dst': ('Scaler', 0) },
        { 'src': ('Scaler', 1), 'dst': ('RGB/YUV Capture', 0) },
    ],
}

def get_configs():
    return (configurations, ['cam0'])
