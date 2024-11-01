#!/usr/bin/python3

import v4l2

sensor_1_w = 1280
sensor_1_h = 720

PIX_BUS_FMT = v4l2.BusFormat.UYVY8_1X16
PIX_FMT = v4l2.PixelFormats.UYVY

mbus_fmt_pix_1 = (sensor_1_w, sensor_1_h, PIX_BUS_FMT)
fmt_pix_1 = (sensor_1_w, sensor_1_h, PIX_FMT)

configurations = {}

#
# Non-MC OV5640
#
configurations["legacy-ov5640"] = {
    "devices": [
        {
            # TODO: add 'device' entry
            "fmt": fmt_pix_1,
        },
    ],
}

#
# DRA76 EVM: OV5640
#
configurations["ov5640"] = {
    # TODO: add 'media' entry
    "subdevs": [
        {
            "entity": "ov5640 4-003c",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_pix_1 },
            ],
        },
        {
            "entity": "CAMERARX0",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_pix_1 },
                { "pad": (1, 0), "fmt": mbus_fmt_pix_1 },
            ],
        },
    ],

    "devices": [
        {
            "entity": "CAL output 0",
            "fmt": fmt_pix_1,
        },
    ],

    "links": [
        { "src": ("ov5640 4-003c", 0), "dst": ("CAMERARX0", 0) },
        { "src": ("CAMERARX0", 1), "dst": ("CAL output 0", 0) },
    ],
}

def get_configs():
    return (configurations, ["ov5640"])
