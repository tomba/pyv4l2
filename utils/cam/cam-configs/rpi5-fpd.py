import v4l2
import v4l2.uapi
from cam_helpers import merge_configs

# Pixel

cam_fmts = [
    ( 640, 480, v4l2.BusFormat.SRGGB8_1X8, v4l2.PixelFormats.SRGGB8 ),
    ( 640, 480, v4l2.BusFormat.SRGGB8_1X8, v4l2.PixelFormats.SRGGB8 ),
    ( 640, 480, v4l2.BusFormat.SRGGB8_1X8, v4l2.PixelFormats.SRGGB8 ),
    ( 640, 480, v4l2.BusFormat.SRGGB8_1X8, v4l2.PixelFormats.SRGGB8 ),
]

meta_fmts = [
    ( 640, 2, v4l2.BusFormat.META_8, v4l2.MetaFormats.GENERIC_8 ),
    ( 640, 2, v4l2.BusFormat.META_8, v4l2.MetaFormats.GENERIC_8 ),
    ( 640, 2, v4l2.BusFormat.META_8, v4l2.MetaFormats.GENERIC_8 ),
    ( 640, 2, v4l2.BusFormat.META_8, v4l2.MetaFormats.GENERIC_8 ),
]

tpg_fmts = [
    ( 640, 480, v4l2.BusFormat.UYVY8_1X16, v4l2.PixelFormats.UYVY, (1, 15) ),
    ( 640, 480, v4l2.BusFormat.UYVY8_1X16, v4l2.PixelFormats.UYVY, (1, 15) ),
    ( 640, 480, v4l2.BusFormat.UYVY8_1X16, v4l2.PixelFormats.UYVY, (1, 15) ),
    ( 640, 480, v4l2.BusFormat.UYVY8_1X16, v4l2.PixelFormats.UYVY, (1, 15) ),
]

def gen_imx219_pixel(mdata: dict, idx: int):
    ser_ent = mdata['cams'][idx][0]
    sensor_ent = mdata['cams'][idx][1]
    des_ent = mdata['deser']
    csi2_ent = mdata['csi2']
    vnode = mdata['vnodes'].pop(0) # Consume the vnode

    des_in_port = ser_ent.get_remote_pad(1).index
    des_out_port = csi2_ent.get_remote_pad(0).index
    des_csi2_stream = idx

    csi2_out_port = vnode.get_remote_pad(0).index

    w = cam_fmts[idx][0]
    h = cam_fmts[idx][1]
    mbus_fmt = (w, h, cam_fmts[idx][2])
    pix_fmt = (w, h, cam_fmts[idx][3])

    return {
        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt },
                ],
                'controls': [
                    (v4l2.uapi.V4L2_CID_ANALOGUE_GAIN, 200),
                    (v4l2.uapi.V4L2_CID_DIGITAL_GAIN, 512),
                ],
            },

            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (0, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt },
                    { 'pad': (1, 0), 'fmt': mbus_fmt },
                ],
            },

            # Deserializer
            {
                'entity': des_ent,
                'routing': [
                    { 'src': (des_in_port, 0), 'dst': (des_out_port, des_csi2_stream) },
                ],
                'pads': [
                    { 'pad': (des_in_port, 0), 'fmt': mbus_fmt },
                    { 'pad': (des_out_port, des_csi2_stream), 'fmt': mbus_fmt },
                ],
            },

            # CSI-2 RX
            {
                'entity': csi2_ent,
                'routing': [
                    { 'src': (0, des_csi2_stream), 'dst': (csi2_out_port, 0) },
                ],
                'pads': [
                    { 'pad': (0, des_csi2_stream), 'fmt': mbus_fmt },
                    { 'pad': (csi2_out_port, 0), 'fmt': mbus_fmt },
                ],
            },
        ],

        'devices': [
            {
                'entity': vnode,
                'fmt': pix_fmt,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, des_in_port) },
            { 'src': (des_ent, des_out_port), 'dst': (csi2_ent, 0) },
            { 'src': (csi2_ent, csi2_out_port), 'dst': (vnode, 0) },
        ],
    }

def gen_imx219_meta(mdata: dict, idx: int):
    ser_ent = mdata['cams'][idx][0]
    sensor_ent = mdata['cams'][idx][1]
    des_ent = mdata['deser']
    csi2_ent = mdata['csi2']
    vnode = mdata['vnodes'].pop(0) # Consume the vnode

    des_in_port = ser_ent.get_remote_pad(1).index
    des_out_port = csi2_ent.get_remote_pad(0).index
    des_csi2_stream = idx + 10

    csi2_out_port = vnode.get_remote_pad(0).index

    w = meta_fmts[idx][0]
    h = meta_fmts[idx][1]
    mbus_fmt = (w, h, meta_fmts[idx][2])
    pix_fmt = (w, h, meta_fmts[idx][3])

    return {
        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (0, 1), 'fmt': mbus_fmt },
                ],
            },

            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (0, 1), 'dst': (1, 1) },
                ],
                'pads': [
                    { 'pad': (0, 1), 'fmt': mbus_fmt },
                    { 'pad': (1, 1), 'fmt': mbus_fmt },
                ],
            },
            # Deserializer
            {
                'entity': des_ent,
                'routing': [
                    { 'src': (des_in_port, 1), 'dst': (des_out_port, des_csi2_stream) },
                ],
                'pads': [
                    { 'pad': (des_in_port, 1), 'fmt': mbus_fmt },
                    { 'pad': (des_out_port, des_csi2_stream), 'fmt': mbus_fmt },
                ],
            },

            # CSI-2 RX
            {
                'entity': csi2_ent,
                'routing': [
                    { 'src': (0, des_csi2_stream), 'dst': (csi2_out_port, 0) },
                ],
                'pads': [
                    { 'pad': (0, des_csi2_stream), 'fmt': mbus_fmt },
                    { 'pad': (csi2_out_port, 0), 'fmt': mbus_fmt },
                ],
            },
        ],

        'devices': [
            {
                'entity': vnode,
                'fmt': pix_fmt,
                'embedded': True,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, des_in_port) },
            { 'src': (des_ent, des_out_port), 'dst': (csi2_ent, 0) },
            { 'src': (csi2_ent, csi2_out_port), 'dst': (vnode, 0) },
        ],
    }

def gen_ub953_tpg(mdata: dict, idx: int):
    ser_ent = mdata['cams'][idx][0]
    des_ent = mdata['deser']
    csi2_ent = mdata['csi2']
    vnode = mdata['vnodes'].pop(0) # Consume the vnode

    des_in_port = ser_ent.get_remote_pad(1).index
    des_out_port = csi2_ent.get_remote_pad(0).index
    des_csi2_stream = idx

    csi2_out_port = vnode.get_remote_pad(0).index

    tpg_w = tpg_fmts[idx][0]
    tpg_h = tpg_fmts[idx][1]
    mbus_fmt_tpg = (tpg_w, tpg_h, tpg_fmts[idx][2])
    fmt_tpg = (tpg_w, tpg_h, tpg_fmts[idx][3])
    ival = tpg_fmts[idx][4]

    return {
        'subdevs': [
            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (2, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (2, 0), 'fmt': mbus_fmt_tpg, 'ival': ival },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
            # Deserializer
            {
                'entity': des_ent,
                'routing': [
                    { 'src': (des_in_port, 0), 'dst': (des_out_port, des_csi2_stream) },
                ],
                'pads': [
                    { 'pad': (des_in_port, 0), 'fmt': mbus_fmt_tpg },
                    { 'pad': (des_out_port, des_csi2_stream), 'fmt': mbus_fmt_tpg },
                ],
            },

            # CSI-2 RX
            {
                'entity': 'csi2',
                'routing': [
                    { 'src': (0, des_csi2_stream), 'dst': (csi2_out_port, 0) },
                ],
                'pads': [
                    { 'pad': (0, des_csi2_stream), 'fmt': mbus_fmt_tpg },
                    { 'pad': (csi2_out_port, 0), 'fmt': mbus_fmt_tpg },
                ],
            },
        ],

        'devices': [
            {
                'entity': vnode,
                'fmt': fmt_tpg,
            },
        ],

        'links': [
            { 'src': (ser_ent, 1), 'dst': (des_ent, des_in_port) },
            { 'src': (des_ent, des_out_port), 'dst': (csi2_ent, 0) },
            { 'src': (csi2_ent, csi2_out_port), 'dst': (vnode, 0) },
        ],
    }

def resolve_media_graph():
    #mdev_name = ('rp1-cfe', 'model')
    mdev_name = ('platform:1f00110000.csi', 'bus_info')
    md = v4l2.MediaDevice(*mdev_name)
    assert md

    csi2rx = md.find_entity('csi2')
    assert csi2rx

    vnodes = []
    for p in csi2rx.pads:
        if not p.is_source:
            continue
        # Get the csi2 node, not the fe node
        vnode = next(e for e in p.get_remote_entities() if 'csi2' in e.name)
        assert vnode
        vnodes.append(vnode)

    deser = csi2rx.get_remote_entity(0)
    assert deser

    cams = []
    for p in deser.pads:
        if not p.is_sink:
            continue

        ser = p.get_remote_entity()
        if not ser:
            continue

        cam = ser.get_remote_entity(0)
        assert cam

        cams.append((ser, cam))

    return {
        'mdev': mdev_name,
        'vnodes': vnodes,
        'csi2': csi2rx,
        'deser': deser,
        'cams': cams,
    }

def get_configs(config_names):
    mdata = resolve_media_graph()

    if not config_names:
        config_names = [f'cam{i}' for i in range(len(mdata['cams']))]

    cfgs = []

    for cname in config_names:
        num = int(cname[-1])
        cname = cname[:-1]

        if cname == 'cam':
            cfgs.append(gen_imx219_pixel(mdata, num))
        elif cname == 'meta':
            cfgs.append(gen_imx219_meta(mdata, num))
        elif cname == 'tpg':
            cfgs.append(gen_ub953_tpg(mdata, num))

    merged_config = merge_configs(cfgs)

    merged_config['media'] = mdata['mdev']

    return merged_config
