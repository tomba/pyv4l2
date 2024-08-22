#!/usr/bin/python3

import v4l2

sensor_1_w = 1280
sensor_1_h = 720

PIX_BUS_FMT = v4l2.BusFormat.UYVY8_1X16
PIX_FMT = v4l2.PixelFormats.UYVY

mbus_fmt_pix_1 = (sensor_1_w, sensor_1_h, PIX_BUS_FMT)
fmt_pix_1 = (sensor_1_w, sensor_1_h, PIX_FMT)

configurations = {}

configurations["ov5640"] = {
    "subdevs": [
        {
            "entity": "ov5640 4-003c",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_pix_1 },
            ],
        },
        {
            "entity": "cdns_csi2rx.4504000.csi-bridge",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_pix_1 },
                { "pad": (1, 0), "fmt": mbus_fmt_pix_1 },
            ],
        },
    ],

    "devices": [
        {
            "entity": "j721e-csi2rx",
            "fmt": fmt_pix_1,
            "dev": "/dev/video0",
        },
    ],

    "links": [
        { "src": ("ov5640 4-003c", 0), "dst": ("cdns_csi2rx.4504000.csi-bridge", 0) },
        { "src": ("cdns_csi2rx.4504000.csi-bridge", 1), "dst": ("j721e-csi2rx", 0) },
    ],
}

def get_configs():
    return (configurations, ["ov5640"])
