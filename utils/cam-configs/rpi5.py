#!/usr/bin/python3

import v4l2
import kms
import pisp
import ctypes

imx219_w = 640
imx219_h = 480
#imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
#imx219_pix_fmt = v4l2.PixelFormat.SRGGB10P
imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
imx219_pix_fmt = v4l2.PixelFormat.SRGGB8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)
fmt_pix_imx219 = (imx219_w, imx219_h, imx219_pix_fmt)

mbus_fmt_imx219_fe = (imx219_w, imx219_h, v4l2.BusFormat.SRGGB16_1X16)
fmt_pix_imx219_fe = (imx219_w, imx219_h, v4l2.PixelFormat.SRGGB16)

imx219_meta_w = imx219_w
imx219_meta_h = 2
imx219_meta_bus_fmt = v4l2.BusFormat.META_8
imx219_meta_pix_fmt = v4l2.MetaFormat.GENERIC_8

meta_mbus_fmt_imx219 = (imx219_meta_w, imx219_meta_h, imx219_meta_bus_fmt)
meta_fmt_pix_imx219 = (imx219_meta_w, imx219_meta_h, imx219_meta_pix_fmt)

meta_fmt_fe_config = (ctypes.sizeof(pisp.pisp_fe_config), 1, v4l2.MetaFormat.RPI_FE_CFG)

meta_mbus_fmt_imx219_legacy = (16384, 1, v4l2.BusFormat.SENSOR_DATA)
meta_fmt_pix_imx219_legacy = (16384, 1, v4l2.MetaFormat.SENSOR_DATA)

configurations = {}

sensor_ent = "imx219 6-0010"

configurations["cam0"] = {
    'media': ('rp1-cfe', 'model'),

    "subdevs": [
        # Camera
        {
            "entity": sensor_ent,
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
            ],
#            "routing": [
#               { "src": (1, 0), "dst": (0, 0) },
#            ],
        },
        # CSI-2 RX
        {
            "entity": "csi2",
            "routing": [
                { "src": (0, 0), "dst": (1, 0) },
            ],
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
                { "pad": (1, 0), "fmt": mbus_fmt_imx219 },
            ],
        },
    ],

    "devices": [
        {
            "entity": "rp1-cfe-csi2_ch0",
            "fmt": fmt_pix_imx219,
            "embedded": False,
            "kms-fourcc": kms.PixelFormat.RGB565,
        },
    ],

    "links": [
        { "src": (sensor_ent, 0), "dst": ("csi2", 0) },
        { "src": ("csi2", 1), "dst": ("rp1-cfe-csi2_ch0", 0) },
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
            "entity": "csi2",
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
            "entity": "rp1-cfe-csi2_ch1",
            "fmt": meta_fmt_pix_imx219,
            "embedded": True,
            "display": True,
            "kms-fourcc": kms.PixelFormat.RGB565,
        },
    ],

    "links": [
        { "src": (sensor_ent, 0), "dst": ("csi2", 0) },
        { "src": ("csi2", 2), "dst": ("rp1-cfe-csi2_ch1", 0) },
    ],
}

configurations["cam0-fe0"] = {
    'media': ('rp1-cfe', 'model'),

    "subdevs": [
        # Camera
        {
            "entity": sensor_ent,
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
            ],
#            "routing": [
#               { "src": (1, 0), "dst": (0, 0) },
#            ],
        },
        # CSI-2 RX
        {
            "entity": "csi2",
            "routing": [
                { "src": (0, 0), "dst": (1, 0) },
            ],
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
                { "pad": (1, 0), "fmt": mbus_fmt_imx219_fe },
            ],
        },
        # FE
        {
            "entity": "pisp-fe",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219_fe },
                { "pad": (2, 0), "fmt": mbus_fmt_imx219_fe },
            ],
        },
    ],

    "devices": [
        {
            "entity": "rp1-cfe-fe_image0",
            "fmt": fmt_pix_imx219_fe,
            "embedded": False,
            "kms-fourcc": kms.PixelFormat.RGB565,
        },
    ],

    "links": [
        { "src": (sensor_ent, 0), "dst": ("csi2", 0) },
        { "src": ("csi2", 1), "dst": ("pisp-fe", 0) },
        { "src": ("pisp-fe", 2), "dst": ("rp1-cfe-fe_image0", 0) },
    ],
}

configurations["cam0-fe1"] = {
    "subdevs": [
        # Camera
        {
            "entity": sensor_ent,
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
            ],
#            "routing": [
#               { "src": (1, 0), "dst": (0, 0) },
#            ],
        },
        # CSI-2 RX
        {
            "entity": "csi2",
            # XXX identical to fe0, so set_routing fails with two same routes
            #"routing": [
            #    { "src": (0, 0), "dst": (1, 0) },
            #],
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
                { "pad": (1, 0), "fmt": mbus_fmt_imx219_fe },
            ],
        },
        # FE
        {
            "entity": "pisp-fe",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219_fe },
                { "pad": (3, 0), "fmt": mbus_fmt_imx219_fe },
            ],
        },
    ],

    "devices": [
        {
            "entity": "rp1-cfe-fe_image1",
            "fmt": fmt_pix_imx219_fe,
            "embedded": False,
            "kms-fourcc": kms.PixelFormat.RGB565,
        },
    ],

    "links": [
        { "src": (sensor_ent, 0), "dst": ("csi2", 0) },
        { "src": ("csi2", 1), "dst": ("pisp-fe", 0) },
        { "src": ("pisp-fe", 3), "dst": ("rp1-cfe-fe_image1", 0) },
    ],
}

configurations["cam0-fe-config"] = {
    "devices": [
        {
            "entity": "rp1-cfe-fe_config",
            "fmt": meta_fmt_fe_config,
            "embedded": True,
            "display": False,
        },
    ],

    "links": [
        { "src": ("rp1-cfe-fe_config", 0), "dst": ("pisp-fe", 1) },
    ],
}


configurations["cam0-legacy"] = {
    'media': ('rp1-cfe', 'model'),

    "subdevs": [
        # Camera
        {
            "entity": sensor_ent,
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
            ],
        },
        # CSI-2 RX
        {
            "entity": "csi2",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
                { "pad": (4, 0), "fmt": mbus_fmt_imx219 },
            ],
        },
    ],

    "devices": [
        {
            "entity": "rp1-cfe-csi2_ch0",
            "fmt": fmt_pix_imx219,
            "embedded": False,
            "kms-fourcc": kms.PixelFormat.RGB565,
        },
    ],

    "links": [
        { "src": (sensor_ent, 0), "dst": ("csi2", 0) },
        { "src": ("csi2", 4), "dst": ("rp1-cfe-csi2_ch0", 0) },
    ],
}

configurations["cam0-meta-legacy"] = {
    "subdevs": [
        # Camera
        {
            "entity": sensor_ent,
            "pads": [
                { "pad": (1, 0), "fmt": meta_mbus_fmt_imx219_legacy },
            ],
        },
        # CSI-2 RX
        {
            "entity": "csi2",
            "pads": [
                { "pad": (1, 0), "fmt": meta_mbus_fmt_imx219_legacy },
                { "pad": (5, 0), "fmt": meta_mbus_fmt_imx219_legacy },
            ],
        },
    ],

    "devices": [
        {
            "entity": "rp1-cfe-embedded",
            "fmt": meta_fmt_pix_imx219_legacy,
            "embedded": True,
            "kms-fourcc": kms.PixelFormat.RGB565,
        },
    ],

    "links": [
        { "src": (sensor_ent, 1), "dst": ("csi2", 1) },
        { "src": ("csi2", 5), "dst": ("rp1-cfe-embedded", 0) },
    ],
}

configurations["cam0-fe0-legacy"] = {
    "subdevs": [
        # Camera
        {
            "entity": sensor_ent,
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
            ],
        },
        # CSI-2 RX
        {
            "entity": "csi2",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219 },
                { "pad": (4, 0), "fmt": mbus_fmt_imx219_fe },
            ],
        },
        # FE
        {
            "entity": "pisp-fe",
            "pads": [
                { "pad": (0, 0), "fmt": mbus_fmt_imx219_fe },
                { "pad": (2, 0), "fmt": mbus_fmt_imx219_fe },
            ],
        },
    ],

    "devices": [
        {
            "entity": "rp1-cfe-fe_image0",
            "fmt": fmt_pix_imx219_fe,
            "embedded": False,
            "kms-fourcc": kms.PixelFormat.RGB565,
        },
    ],

    "links": [
        { "src": (sensor_ent, 0), "dst": ("csi2", 0) },
        { "src": ("csi2", 4), "dst": ("pisp-fe", 0) },
        { "src": ("pisp-fe", 2), "dst": ("rp1-cfe-fe_image0", 0) },
    ],
}

def get_configs():
    return (configurations, ["cam0"])
