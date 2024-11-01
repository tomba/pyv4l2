import v4l2

sensor_1_w = 1280
sensor_1_h = 720

PIX_FMT = v4l2.PixelFormats.YUYV

fmt_pix_1 = (sensor_1_w, sensor_1_h, PIX_FMT)

configurations = {}

configurations['lappy'] = {
    # TODO: add 'media' entry
    'subdevs': [
    ],

    'devices': [
        {
            'entity': 'Integrated Camera: Integrated C',
            'fmt': fmt_pix_1,
        },
    ],

    'links': [
    ],
}

def get_configs():
    return (configurations, ['lappy'])
