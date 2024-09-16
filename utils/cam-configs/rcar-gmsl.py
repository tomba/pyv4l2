#!/usr/bin/python3

import v4l2

# TPG

mbus_fmt_tpg = (1920, 1080, v4l2.BusFormat.SRGGB8_1X8)
mbus_fmt_fixed = (1920, 1080, v4l2.BusFormat.FIXED)
#mbus_fmt_des = (1920, 1080, v4l2.BusFormat.SRGGB8_1X8)
mbus_fmt_des = (1920, 1080, v4l2.BusFormat.RGB888_1X24)

#fmt_tpg = (1920, 1080, v4l2.PixelFormats.SRGGB8)
#fmt_tpg = (1920, 1080, v4l2.PixelFormats.YUYV)
fmt_tpg = (1920, 1080, v4l2.PixelFormats.XRGB8888)

configurations = {}

def gen_des_tpg():
    cam_ent = 'imx219 7-005d'
    ser_ent = 'max96717 6-0040:0' # AR
    #ser_ent = 'max96717 6-0062:0' # IMX
    des_ent = 'max96724 1-0049:0'
    csi_ent = 'rcar_csi2 fe500000.csi2'
    isp_ent = 'rcar_isp fed00000.isp'
    vin_port = 0

    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

        "subdevs": [
            # Camera
            {
                "entity": cam_ent,
                #"routing": [
                #    { "src": (port, 0), "dst": (4, port) },
                #],
                "pads": [
                #    { "pad": (port, 0), "fmt": mbus_fmt_tpg },
                    { "pad": (0, 0), "fmt": mbus_fmt_tpg },
                ],
            },
            # Serializer
            {
                "entity": ser_ent,
                #"routing": [
                #    { "src": (port, 0), "dst": (4, port) },
                #],
                "pads": [
                    { "pad": (1, 0), "fmt": mbus_fmt_tpg },
                    #{ "pad": (0, 0), }, # "fmt": mbus_fmt_fixed },
                ],
            },
            # Deserializer
            {
                "entity": des_ent,
                #"routing": [
                #    { "src": (port, 0), "dst": (4, port) },
                #],
                "pads": [
                    #{ "pad": (1, 0), }, # "fmt": mbus_fmt_fixed },
                    { "pad": (0, 0), "fmt": mbus_fmt_des },
                ],
            },
            # CSI-2 RX
            {
                "entity": csi_ent,
                #"routing": [
                #    { "src": (0, port), "dst": (1 + port, 0) },
                #],
                "pads": [
                    { "pad": (0, 0), "fmt": mbus_fmt_des },
                    { "pad": (1, 0), "fmt": mbus_fmt_des },
                ],
            },
            # ISP
            {
                "entity": isp_ent,
                #"routing": [
                #    { "src": (0, port), "dst": (1 + port, 0) },
                #],
                "pads": [
                    { "pad": (0, 0), "fmt": mbus_fmt_des },
                    { "pad": (1, 0), "fmt": mbus_fmt_des },
                ],
            },
        ],

        "devices": [
            {
                "entity": f"VIN{vin_port} output",
                "fmt": fmt_tpg,
            },
        ],

        "links": [
            { "src": (cam_ent, 0), "dst": (ser_ent, 1) },
            { "src": (ser_ent, 0), "dst": (des_ent, 1) },
            { "src": (des_ent, 0), "dst": (csi_ent, 0) },
            { "src": (csi_ent, 1), "dst": (isp_ent, 0) },
            { "src": (isp_ent, 1), "dst": (f"VIN{vin_port} output", 0) },
        ],
    }

configurations["des0"] = gen_des_tpg()

def get_configs():
    return (configurations, ["des0"])
