import re

import v4l2
import v4l2.uapi

from cam_helpers import merge_configs, gen_subdev, infer_links, propagate_formats

#imx219_w, imx219_h = 3280, 2464
imx219_w, imx219_h = 1920, 1080
#imx219_w, imx219_h = 640, 480

USE_RAW_10 = False

if USE_RAW_10:
    imx219_fmt = (imx219_w, imx219_h, v4l2.BusFormat.SRGGB10_1X10, v4l2.PixelFormats.SRGGB10)
    imx219_meta_fmt = (imx219_w, 2, v4l2.BusFormat.META_10, v4l2.MetaFormats.GENERIC_CSI2_10)
else:
    imx219_fmt = (imx219_w, imx219_h, v4l2.BusFormat.SRGGB8_1X8, v4l2.PixelFormats.SRGGB8)
    imx219_meta_fmt = (imx219_w, 2, v4l2.BusFormat.META_8, v4l2.MetaFormats.GENERIC_8)

tpg_fmt = (1920, 1024, v4l2.BusFormat.RGB888_1X24, v4l2.PixelFormats.XRGB8888)

MEDIA_DEV = ('TI-CSI2RX', 'model')

def resolve_media_graph():
    md = v4l2.MediaDevice(*MEDIA_DEV)

    des = md.find_entity('ds90ub960*')
    assert des

    csirx = des.get_remote_entity(4)
    assert csirx

    # Find csirx2 from csirx's source pads
    csirx2 = None
    for p in csirx.pads:
        if p.is_source:
            csirx2 = p.get_remote_entity()
            if csirx2:
                break
    assert csirx2

    # Find (serializer, sensor) pairs from deser sink pads
    cams = []
    for p in des.pads:
        if not p.is_sink:
            continue
        ser = p.get_remote_entity()
        if not ser:
            continue
        sensor = ser.get_remote_entity(0)
        if not sensor:
            continue
        cams.append((ser, sensor))

    # Find DMA context entities from csirx2 source pads
    contexts = []
    for p in csirx2.pads:
        if not p.is_source:
            continue
        ctx_ent = p.get_remote_entity()
        if ctx_ent:
            contexts.append(ctx_ent)
    contexts.sort(key=lambda e: e.name)

    return {
        'md': md,
        'des': des,
        'csirx': csirx,
        'csirx2': csirx2,
        'cams': cams,
        'contexts': contexts,
    }

def gen_imx219_pixel(mdata, idx):
    ser, sensor = mdata['cams'][idx]
    des = mdata['des']
    csirx = mdata['csirx']
    csirx2 = mdata['csirx2']
    context = mdata['contexts'].pop(0)

    w, h, bus_fmt, pix_fmt = imx219_fmt
    stream_id = idx

    return {
        'subdevs': [
            gen_subdev(sensor,
                       pads={(0, 0): (w, h, bus_fmt)},
                       controls={v4l2.uapi.V4L2_CID_ANALOGUE_GAIN: 200,
                                 0x009f0903: 0}),
            gen_subdev(ser, routing=((0, 0), (1, 0))),
            gen_subdev(des, routing=((idx, 0), (4, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(csirx2, routing=((0, stream_id), (1 + idx, 0))),
        ],

        'devices': [
            { 'entity': context, 'fmt': (w, h, pix_fmt) },
        ],
    }

def gen_imx219_meta(mdata, idx):
    ser, sensor = mdata['cams'][idx]
    des = mdata['des']
    csirx = mdata['csirx']
    csirx2 = mdata['csirx2']
    context = mdata['contexts'].pop(0)

    w, h, bus_fmt, pix_fmt = imx219_meta_fmt
    stream_id = idx + 4

    return {
        'subdevs': [
            gen_subdev(sensor, fmt=(w, h, bus_fmt),
                       routing=((2, 0), (0, 1))),
            gen_subdev(ser, routing=((0, 1), (1, 1))),
            gen_subdev(des, routing=((idx, 1), (4, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(csirx2, routing=((0, stream_id), (1 + idx + 1, 0))),
        ],

        'devices': [
            {
                'entity': context,
                'fmt': (w, h, pix_fmt),
                'embedded': True,
            },
        ],
    }

def gen_ub953_tpg(mdata, idx):
    ser, _sensor = mdata['cams'][idx]
    des = mdata['des']
    csirx = mdata['csirx']
    csirx2 = mdata['csirx2']
    context = mdata['contexts'].pop(0)

    w, h, bus_fmt, pix_fmt = tpg_fmt
    stream_id = idx

    return {
        'subdevs': [
            gen_subdev(ser, fmt=(w, h, bus_fmt),
                       routing=((2, 0), (1, 0))),
            gen_subdev(des, routing=((idx, 0), (4, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(csirx2, routing=((0, stream_id), (1 + idx, 0))),
        ],

        'devices': [
            { 'entity': context, 'fmt': (w, h, pix_fmt) },
        ],
    }

def get_configs(config_names):
    mdata = resolve_media_graph()

    if not config_names:
        config_names = [f'cam{i}' for i in range(len(mdata['cams']))]

    cfgs = []

    for cname in config_names:
        m = re.fullmatch(r'cam(\d+)(?:-(\w+))?', cname)
        if not m:
            raise RuntimeError(f'Unknown config name: {cname}')
        num = int(m.group(1))
        suffix = m.group(2)
        if suffix is None:
            cfgs.append(gen_imx219_pixel(mdata, num))
        elif suffix == 'tpg':
            cfgs.append(gen_ub953_tpg(mdata, num))
        elif suffix == 'meta':
            cfgs.append(gen_imx219_meta(mdata, num))
        else:
            raise RuntimeError(f'Unknown config name: {cname}')

    for cfg in cfgs:
        propagate_formats(cfg)
        infer_links(mdata['md'], cfg)

    merged_config = merge_configs(cfgs)
    merged_config['media'] = MEDIA_DEV

    return merged_config
