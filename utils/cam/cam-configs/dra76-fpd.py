import v4l2
from cam_helpers import merge_configs

ov10635_fmt = (
    ( 1280, 720, v4l2.BusFormat.UYVY8_2X8 ),
    ( 1280, 720, v4l2.BusFormat.UYVY8_1X16 ),
    ( 1280, 720, v4l2.PixelFormats.UYVY ),
)

ov10635_meta_fmt = ( 1280, 1, v4l2.BusFormat.META_8, v4l2.MetaFormats.GENERIC_8 )

imx390_fmt = (
    ( 1936, 1100, v4l2.BusFormat.SRGGB12_1X12 ),
    ( 1936, 1100, v4l2.BusFormat.SRGGB12_1X12 ),
    ( 1936, 1100, v4l2.PixelFormats.SRGGB12 ),
)

imx390_meta_fmt = ( 1936, 1, v4l2.BusFormat.META_12, v4l2.MetaFormats.GENERIC_CSI2_12 )

tpg_fmt = ( 1920, 1024, v4l2.BusFormat.RGB888_1X24, v4l2.PixelFormats.RGB888 )

def gen_cam_pixel(mdata: dict, idx):
    ser_ent = mdata['cams'][idx][0]
    sensor_ent = mdata['cams'][idx][1]
    des_ent = mdata['deser']
    csi2_ent = mdata['csi2']
    vnode = mdata['vnodes'].pop(0) # Consume the vnode
    csi2_out_port = mdata['cal_ports'].pop(0)

    des_in_port = ser_ent.get_remote_pad(1).index
    des_out_port = csi2_ent.get_remote_pad(0).index
    des_csi2_stream = idx

    if sensor_ent.name.startswith('imx390'):
        fmt = imx390_fmt
        kms_format = v4l2.PixelFormats.RGB565
    elif sensor_ent.name.startswith('ov1063'):
        fmt = ov10635_fmt
        kms_format = fmt[2][2]
    else:
        raise RuntimeError('Unknown sensor type')

    cam_mbus_fmt = fmt[0]
    mbus_fmt = fmt[1]
    pix_fmt = fmt[2]

    return {
        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (1, 0), 'fmt': cam_mbus_fmt },
                    { 'pad': (0, 0), 'fmt': cam_mbus_fmt },
                ],
                'routing': [
                   { 'src': (1, 0), 'dst': (0, 0) },
                ],
            },
            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (0, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (0, 0), 'fmt': cam_mbus_fmt },
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
                'kms-format': kms_format,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, des_in_port) },
            { 'src': (des_ent, des_out_port), 'dst': (csi2_ent, 0) },
            { 'src': (csi2_ent, csi2_out_port), 'dst': (vnode, 0) },
        ],
    }

def gen_cam_meta(mdata: dict, idx):
    ser_ent = mdata['cams'][idx][0]
    sensor_ent = mdata['cams'][idx][1]
    des_ent = mdata['deser']
    csi2_ent = mdata['csi2']
    vnode = mdata['vnodes'].pop(0) # Consume the vnode
    csi2_out_port = mdata['cal_ports'].pop(0)

    des_in_port = ser_ent.get_remote_pad(1).index
    des_out_port = csi2_ent.get_remote_pad(0).index
    des_csi2_stream = idx + 10

    if sensor_ent.name.startswith('imx390'):
        fmt = imx390_meta_fmt
    elif sensor_ent.name.startswith('ov1063'):
        fmt = ov10635_meta_fmt
    else:
        raise RuntimeError('Unknown sensor type')

    w = fmt[0]
    h = fmt[1]
    mbus_fmt = (w, h, fmt[2])
    pix_fmt = (w, h, fmt[3])

    return {
        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (2, 0), 'fmt': mbus_fmt },
                    { 'pad': (0, 1), 'fmt': mbus_fmt },
                ],
                'routing': [
                   { 'src': (2, 0), 'dst': (0, 1) },
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
                'display': False,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, des_in_port) },
            { 'src': (des_ent, des_out_port), 'dst': (csi2_ent, 0) },
            { 'src': (csi2_ent, csi2_out_port), 'dst': (vnode, 0) },
        ],
    }

def gen_ub953_tpg(mdata: dict, idx):
    ser_ent = mdata['cams'][idx][0]
    des_ent = mdata['deser']
    csi2_ent = mdata['csi2']
    vnode = mdata['vnodes'].pop(0) # Consume the vnode
    csi2_out_port = mdata['cal_ports'].pop(0)

    des_in_port = ser_ent.get_remote_pad(1).index
    des_out_port = csi2_ent.get_remote_pad(0).index
    des_csi2_stream = idx

    w = tpg_fmt[0]
    h = tpg_fmt[1]
    mbus_fmt = (w, h, tpg_fmt[2])
    pix_fmt = (w, h, tpg_fmt[3])

    return {
        'subdevs': [
            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (2, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (2, 0), 'fmt': mbus_fmt },
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
            { 'src': (ser_ent, 1), 'dst': (des_ent, des_in_port) },
            { 'src': (des_ent, des_out_port), 'dst': (csi2_ent, 0) },
            { 'src': (csi2_ent, csi2_out_port), 'dst': (vnode, 0) },
        ],
    }


def resolve_media_graph():
    mdev_name = ('CAL', 'model')
    md = v4l2.MediaDevice(*mdev_name)
    assert md

    csi2rx = md.find_entity('CAMERARX0')
    assert csi2rx

    vnodes = [e for e in md.entities if e.name.startswith('CAL output')]

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
        'cal_ports': [p.index for p in csi2rx.pads if p.is_source],
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
            cfgs.append(gen_cam_pixel(mdata, num))
        elif cname == 'meta':
            cfgs.append(gen_cam_meta(mdata, num))
        elif cname == 'tpg':
            cfgs.append(gen_ub953_tpg(mdata, num))
        else:
            raise RuntimeError(f'Unknown config name: {cname}')

    merged_config = merge_configs(cfgs)

    merged_config['media'] = mdata['mdev']

    return merged_config
