from __future__ import annotations

import v4l2
import v4l2.uapi

from cam_helpers import merge_configs

USE_RAW_10=False

#imx219_width, imx219_height = 3280, 2464
#imx219_width, imx219_height = 1920, 1080
imx219_width, imx219_height = 640, 480

if USE_RAW_10:
    imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
    imx219_pix_fmt = v4l2.PixelFormats.SRGGB10
else:
    imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
    imx219_pix_fmt = v4l2.PixelFormats.SRGGB8

imx219_fmt = (
    ( imx219_width, imx219_height, imx219_bus_fmt ),
    ( imx219_width, imx219_height, imx219_bus_fmt ),
    ( imx219_width, imx219_height, imx219_pix_fmt ),
)

imx219_meta_fmt = ( imx219_width, 2, v4l2.BusFormat.META_8, v4l2.MetaFormats.GENERIC_8 )

tpg_fmt = ( 1920, 1024, v4l2.BusFormat.RGB888_1X24, v4l2.PixelFormats.XRGB8888 )

def gen_cam_pixel(mdata: dict, idx):
    ser_ent = mdata['cams'][idx][0]
    sensor_ent = mdata['cams'][idx][1]
    des_ent = mdata['deser']
    csi2_ent = mdata['csi2']
    isp_ent = mdata['isp']
    vnode = mdata['vnodes'].pop(0) # Consume the vnode
    isp_out_port = mdata['isp_ports'].pop(0)

    des_in_port = ser_ent.get_remote_pad(1).index
    des_out_port = csi2_ent.get_remote_pad(0).index
    des_csi2_stream = idx

    if sensor_ent.name.startswith('imx219'):
        fmt = imx219_fmt
        kms_format = v4l2.PixelFormats.RGB565
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
#                    { 'pad': (1, 0), 'fmt': cam_mbus_fmt },
                    { 'pad': (0, 0), 'fmt': cam_mbus_fmt },
                ],
#                'routing': [
#                   { 'src': (1, 0), 'dst': (0, 0) },
#                ],
                'controls': [
                    (v4l2.uapi.V4L2_CID_ANALOGUE_GAIN, 200),
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
                    { 'src': (0, des_csi2_stream), 'dst': (1, des_csi2_stream) },
                ],
                'pads': [
                    { 'pad': (0, des_csi2_stream), 'fmt': mbus_fmt },
                    { 'pad': (1, des_csi2_stream), 'fmt': mbus_fmt },
                ],
            },
            # ISP/CS
            {
                'entity': isp_ent,
                'routing': [
                    { 'src': (0, des_csi2_stream), 'dst': (isp_out_port, 0) },
                ],
                'pads': [
                    { 'pad': (0, des_csi2_stream), 'fmt': mbus_fmt },
                    { 'pad': (isp_out_port, 0), 'fmt': mbus_fmt },
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
            { 'src': (csi2_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, isp_out_port), 'dst': (vnode, 0) },
        ],
    }

def gen_cam_meta(mdata: dict, idx):
    ser_ent = mdata['cams'][idx][0]
    sensor_ent = mdata['cams'][idx][1]
    des_ent = mdata['deser']
    csi2_ent = mdata['csi2']
    isp_ent = mdata['isp']
    vnode = mdata['vnodes'].pop(0) # Consume the vnode
    isp_out_port = mdata['isp_ports'].pop(0)

    des_in_port = ser_ent.get_remote_pad(1).index
    des_out_port = csi2_ent.get_remote_pad(0).index
    des_csi2_stream = idx + 10

    if sensor_ent.name.startswith('imx219'):
        fmt = imx219_meta_fmt
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
                    { 'src': (0, des_csi2_stream), 'dst': (1, des_csi2_stream) },
                ],
                'pads': [
                    { 'pad': (0, des_csi2_stream), 'fmt': mbus_fmt },
                    { 'pad': (1, des_csi2_stream), 'fmt': mbus_fmt },
                ],
            },
            # ISP/CS
            {
                'entity': isp_ent,
                'routing': [
                    { 'src': (0, des_csi2_stream), 'dst': (isp_out_port, 0) },
                ],
                'pads': [
                    { 'pad': (0, des_csi2_stream), 'fmt': mbus_fmt },
                    { 'pad': (isp_out_port, 0), 'fmt': mbus_fmt },
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
            { 'src': (csi2_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, isp_out_port), 'dst': (vnode, 0) },
        ],
    }

def gen_ub953_tpg(mdata: dict, idx):
    ser_ent = mdata['cams'][idx][0]
    des_ent = mdata['deser']
    csi2_ent = mdata['csi2']
    isp_ent = mdata['isp']
    vnode = mdata['vnodes'].pop(0) # Consume the vnode
    isp_out_port = mdata['isp_ports'].pop(0)

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
                    { 'src': (0, des_csi2_stream), 'dst': (1, des_csi2_stream) },
                ],
                'pads': [
                    { 'pad': (0, des_csi2_stream), 'fmt': mbus_fmt },
                    { 'pad': (1, des_csi2_stream), 'fmt': mbus_fmt },
                ],
            },
            # ISP/CS
            {
                'entity': isp_ent,
                'routing': [
                    { 'src': (0, des_csi2_stream), 'dst': (isp_out_port, 0) },
                ],
                'pads': [
                    { 'pad': (0, des_csi2_stream), 'fmt': mbus_fmt },
                    { 'pad': (isp_out_port, 0), 'fmt': mbus_fmt },
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
            { 'src': (csi2_ent, 1), 'dst': (isp_ent, 0) },
            { 'src': (isp_ent, isp_out_port), 'dst': (vnode, 0) },        ],
    }


def resolve_media_graph():
    mdev_name = ('platform:e6ef0000.video', 'bus_info')
    md = v4l2.MediaDevice(*mdev_name)
    assert md

    csi2rx = md.find_entity(regex='rcar_csi2')
    assert csi2rx

    deser = csi2rx.get_remote_entity(0)
    assert deser

    isp = md.find_entity(regex='rcar_isp')
    assert isp

    vnodes = [e for e in md.entities if e.name.startswith('VIN')]

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
        'isp': isp,
        'deser': deser,
        'cams': cams,
        'isp_ports': [p.index for p in isp.pads if p.is_source],
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
