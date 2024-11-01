import v4l2

sensor_fmt = (2592, 1940, v4l2.BusFormat.SRGGB12_1X12)
isp_out_fmt = (2592, 1940, v4l2.BusFormat.YUYV8_2X8)
resizer_out_fmt = (1920, 1080, v4l2.BusFormat.YUYV8_2X8)
vid_fmt = (1920, 1080, v4l2.PixelFormats.YUYV)

isp_crop = (0, 0, 2592, 1940)
resizer_crop = (0, 0, 2592, 1940)

configurations = {}

configurations['cam0'] = {
    # TODO: add 'media' entry
    'subdevs': [
        # Camera
        {
            'entity': 'imx335 1-001a',
            'pads': [
                { 'pad': (0, 0), 'fmt': sensor_fmt },
            ],
        },
        # CSI-2 RX
        {
            'entity': 'csis-32e40000.csi',
            'pads': [
                { 'pad': (0, 0), 'fmt': sensor_fmt },
                { 'pad': (1, 0), 'fmt': sensor_fmt },
            ],
        },

        {
            'entity': 'rkisp1_isp',
            'pads': [
                { 'pad': (0, 0), 'fmt': sensor_fmt,
                    'crop': isp_crop,
                },
                { 'pad': (2, 0), 'fmt': isp_out_fmt,
                    'crop': isp_crop,
                },
            ],
        },

        {
            'entity': 'rkisp1_resizer_mainpath',
            'pads': [
                { 'pad': (0, 0), 'fmt': isp_out_fmt,
                    'crop': resizer_crop,
                },
                { 'pad': (1, 0), 'fmt': resizer_out_fmt },
            ],
        },

    ],

    'devices': [
        {
            'entity': 'rkisp1_mainpath',
            'fmt': vid_fmt,
        },
    ],

    'links': [
        { 'src': ('imx335 1-001a', 0), 'dst': ('csis-32e40000.csi', 0) },
        { 'src': ('csis-32e40000.csi', 1), 'dst': ('rkisp1_isp', 0) },
        { 'src': ('rkisp1_isp', 2), 'dst': ('rkisp1_resizer_mainpath', 0) },
        { 'src': ('rkisp1_resizer_mainpath', 1), 'dst': ('rkisp1_mainpath', 0) },
    ],
}

def get_configs():
    return (configurations, ['cam0'])
