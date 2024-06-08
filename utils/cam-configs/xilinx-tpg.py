#!/usr/bin/python3

import v4l2

def get_tpg_config(w, h, busfmt, pixfmt):
    mbus_fmt = (w, h, busfmt)
    fmt_pix = (w, h, pixfmt)

    return {
        'media': ('platform:amba_pl@0:vcap_tpg_inp', 'bus_info'),
        #'media': ('platform:axi:vcap_tpg_input_v_t', 'bus_info'),

        'subdevs': [
            {
                'entity': 'a00e0000.v_tpg',
                'pads': [
                    { 'pad': 0, 'fmt': mbus_fmt },
                ],
            },
        ],

        'devices': [
            {
                'entity': 'vcap_tpg_input_v_tpg_1 output 0',
                'fmt': fmt_pix,
            },
        ],

        'links': [
            { 'src': ('a00e0000.v_tpg', 0), 'dst': ('vcap_tpg_input_v_tpg_1 output 0', 0) },
        ],
    }

mbus_formats = {
    v4l2.PixelFormats.RGB888: v4l2.BusFormat.RBG888_1X24,
    v4l2.PixelFormats.BGR888: v4l2.BusFormat.RBG888_1X24,
    v4l2.PixelFormats.XRGB8888: v4l2.BusFormat.RBG888_1X24,
    v4l2.PixelFormats.XBGR8888: v4l2.BusFormat.RBG888_1X24,

    v4l2.PixelFormats.VUY888: v4l2.BusFormat.VUY8_1X24,
    v4l2.PixelFormats.XVUY8888: v4l2.BusFormat.VUY8_1X24,

    v4l2.PixelFormats.Y8: v4l2.BusFormat.VUY8_1X24,

    v4l2.PixelFormats.YUYV: v4l2.BusFormat.VYUY8_1X16,
    v4l2.PixelFormats.UYVY: v4l2.BusFormat.VYUY8_1X16,

    v4l2.PixelFormats.XBGR2101010: v4l2.BusFormat.RBG101010_1X30,
}

def get_configs(params):
    print(params)

    if len(params) > 1:
        raise RuntimeError("Bad number of params")

    if len(params) == 1:
        pixfmt = v4l2.PixelFormats.find_by_name(params[0].upper())
    else:
        pixfmt = v4l2.PixelFormats.RGB888

    if not pixfmt:
        raise RuntimeError("no pix format")

    print(pixfmt)

    busfmt = mbus_formats[pixfmt]

    configurations = {}
    configurations['tpg'] = get_tpg_config(640, 480, busfmt, pixfmt)

    return (configurations, ['tpg'])
