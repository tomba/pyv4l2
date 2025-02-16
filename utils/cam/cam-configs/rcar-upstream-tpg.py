#!/usr/bin/python3

import v4l2

# TPG

mbus_fmt_tpg = (1920, 1080, v4l2.BusFormat.RGB888_1X24)
fmt_tpg = (1920, 1080, v4l2.PixelFormats.XRGB8888)

configurations = {}

def gen_des_tpg(port):
    if port == 0:
        des_ent = 'max96712 1-0049'
        csi_ent = 'rcar_csi2 fe500000.csi2'
        isp_ent = 'rcar_isp fed00000.isp'
        vin_port = 0
    elif port == 1:
        des_ent = 'max96712 1-004b'
        csi_ent = 'rcar_csi2 fe540000.csi2'
        isp_ent = 'rcar_isp fed20000.isp'
        vin_port = 8
    else:
        raise RuntimeError()

    return {
        'media': ('renesas,vin-r8a779g0', 'model'),

        'subdevs': [
            # Deserializer
            {
                'entity': des_ent,
                #"routing": [
                #    { "src": (port, 0), "dst": (4, port) },
                #],
                'pads': [
                #    { "pad": (port, 0), "fmt": mbus_fmt_tpg },
                    { 'pad': (0, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
            # CSI-2 RX
            {
                'entity': csi_ent,
                #"routing": [
                #    { "src": (0, port), "dst": (1 + port, 0) },
                #],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
            # ISP
            {
                'entity': isp_ent,
                #"routing": [
                #    { "src": (0, port), "dst": (1 + port, 0) },
                #],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'VIN{vin_port} output',
                'fmt': fmt_tpg,
            },
        ],

        'links': [
            { 'src': (des_ent, 0), 'dst': (csi_ent, 0) },
            { 'src': (csi_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, 1), 'dst': (f'VIN{vin_port} output', 0) },
        ],
    }

configurations['des0-tpg'] = gen_des_tpg(0)
configurations['des1-tpg'] = gen_des_tpg(1)

def get_configs():
    return (configurations, ['des0-tpg'])
