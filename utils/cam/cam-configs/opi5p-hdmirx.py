import v4l2

w, h = 640, 480
w, h = 1920, 1080
fmt = v4l2.PixelFormats.RGB888

fmt_pix = (w, h, fmt)

configurations = {}

configurations['hdmirx'] = {
    'devices': [
        {
            'device': ('bus_info', 'platform:fdee0000.hdmi_receiver'),
            'num_bufs': 5,
            'fmt': fmt_pix,
        },
    ],
}


def get_configs():
    return (configurations, ['hdmirx'])
