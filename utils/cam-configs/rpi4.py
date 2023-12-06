#!/usr/bin/python3

import v4l2
import kms

imx219_w = 1920
imx219_h = 1080
imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
imx219_pix_fmt = v4l2.PixelFormat.SRGGB8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)
fmt_pix_imx219 = (imx219_w, imx219_h, imx219_pix_fmt)


imx219_meta_w = 1024
imx219_meta_h = 2
imx219_meta_bus_fmt = v4l2.BusFormat.META_8
imx219_meta_pix_fmt = v4l2.PixelFormat.META_8

meta_mbus_fmt_imx219 = (imx219_meta_w, imx219_meta_h, imx219_meta_bus_fmt)
imx219_meta_h = 16

meta_fmt_pix_imx219 = (imx219_meta_w, imx219_meta_h, imx219_meta_pix_fmt)


configurations = {}

sensor_ent = "imx219 5-0010"

configurations["cam0"] = {
    "subdevs": [
        # Camera
        {
            "entity": sensor_ent,
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
            ],
#            "routing": [
#               { "src": (1, 0), "dst": (0, 0) },
#               { "src": (2, 0), "dst": (0, 1) },
#            ],
        },
        # CSI-2 RX
        {
            "entity": "unicam",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
                { "pad": (1, 0), "fmt": mbus_fmt_imx219 },
            ],
            "routing": [
                { "src": (0, 0), "dst": (1, 0) },
            ],
        },
    ],

    "devices": [
        {
            "entity": "unicam-image",
            "fmt": fmt_pix_imx219,
            "embedded": False,
            "dra-plane-hack": False,
            "kms-fourcc": kms.PixelFormat.RGB565,
        },
    ],

    "links": [
        { "src": (sensor_ent, 0), "dst": ("unicam", 0) },
        { "src": ("unicam", 1), "dst": ("unicam-image", 0) },
    ],
}

configurations["cam0-meta"] = {
    "subdevs": [
        # Camera
        {
            "entity": sensor_ent,
            "pads": [
                { "pad": (0, 1), "fmt": meta_mbus_fmt_imx219 },
            ],
#            "routing": [
#               { "src": (1, 0), "dst": (0, 0) },
#            ],
        },
        # CSI-2 RX
        {
            "entity": "unicam",
            "routing": [
                { "src": (0, 1), "dst": (2, 0) },
            ],
            "pads": [
                { "pad": (0, 1), "fmt": meta_mbus_fmt_imx219 },
                { "pad": (2, 0), "fmt": meta_mbus_fmt_imx219 },
            ],
        },
    ],

    "devices": [
        {
            "entity": "unicam-embedded",
            "fmt": meta_fmt_pix_imx219,
            "embedded": True,
            "display": False,
        },
    ],

    "links": [
        { "src": (sensor_ent, 0), "dst": ("unicam", 0) },
        { "src": ("unicam", 2), "dst": ("unicam-embedded", 0) },
    ],
}

def get_configs():
    return (configurations, ["cam0"])
