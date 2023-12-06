#!/usr/bin/python3

import v4l2

configurations = {}

fmt1 = (2592, 1940, v4l2.BusFormat.SRGGB12_1X12)
fmt2 = (2592, 1940, v4l2.BusFormat.YUYV8_2X8)
fmt3 = (1920, 1080, v4l2.BusFormat.YUYV8_2X8)
vfmt = (1920, 1080, v4l2.PixelFormat.YUYV)

crop1 = (0, 0, 2592, 1940)
crop2 = (0, 0, 2592, 1940)
crop3 = (0, 0, 2592, 1940)

#2592✕1940
configurations["cam0"] = {
    "subdevs": [
        {
            "entity": "rkisp1_tpg",
            "pads": [
                { "pad": (0, 0),
                  "fmt": fmt1 },
            ],
        },

        {
            "entity": "rkisp1_isp",
            "pads": [
                {
                    "pad": (0, 0),
                    "fmt": fmt1,
                    "crop": crop1,
                },

                {
                    "pad": (2, 0),
                    "fmt": fmt2,
                    "crop": crop2,
                },
            ],
        },

        {
            "entity": "rkisp1_resizer_mainpath",
            "pads": [
                {
                   "pad": (0, 0),
                    "fmt": fmt2,
                    "crop": crop3,
                },

                { "pad": (1, 0),
                  "fmt": fmt3,
                },
            ],
        },
    ],

    "devices": [
        {
            "entity": "rkisp1_mainpath",
            "fmt": vfmt,
            "embedded": False,
            "dra-plane-hack": False,
        },
    ],

    "links": [
        { "src": ("rkisp1_tpg", 0), "dst": ("rkisp1_isp", 0) },
        { "src": ("rkisp1_isp", 2), "dst": ("rkisp1_resizer_mainpath", 0) },
        { "src": ("rkisp1_resizer_mainpath", 1), "dst": ("rkisp1_mainpath", 0) },
    ],
}

def get_configs():
    return (configurations, ["cam0"])
