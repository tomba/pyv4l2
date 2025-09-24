import v4l2

sensor_1_w = 1920
sensor_1_h = 1080

PIX_FMT = v4l2.PixelFormats.RGB888

fmt_pix_1 = (sensor_1_w, sensor_1_h, PIX_FMT)

configurations = {}

configurations['desky'] = {
    'media': ('USB Capture HDMI 4K+*', 'model'),

    'subdevs': [
    ],

    'devices': [
        {
            'entity': 'USB Capture HDMI 4K+: USB Captu',
            'fmt': fmt_pix_1,
        },
    ],

    'links': [
    ],
}

def get_configs():
    return (configurations, ['desky'])
