import re

from cam_helpers import gen_subdev, infer_links, merge_configs, propagate_formats

import v4l2
import v4l2.uapi

# imx219_w, imx219_h = 3280, 2464
imx219_w, imx219_h = 1920, 1080
# imx219_w, imx219_h = 640, 480

USE_RAW_10 = False

if USE_RAW_10:
    imx219_fmt = (imx219_w, imx219_h, v4l2.BusFormat.SRGGB10_1X10, v4l2.PixelFormats.SRGGB10)
else:
    imx219_fmt = (imx219_w, imx219_h, v4l2.BusFormat.SRGGB8_1X8, v4l2.PixelFormats.SRGGB8)

MEDIA_DEV = ('TI-CSI2RX', 'model')


def resolve_media_graph():
    md = v4l2.MediaDevice(*MEDIA_DEV)

    sensor = md.find_entity('imx219*')
    assert sensor

    csirx = sensor.get_remote_entity(0)
    assert csirx

    # Find csirx2 from csirx's source pads
    csirx2 = None
    for p in csirx.pads:
        if p.is_source:
            csirx2 = p.get_remote_entity()
            if csirx2:
                break
    assert csirx2

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
        'sensor': sensor,
        'csirx': csirx,
        'csirx2': csirx2,
        'contexts': contexts,
    }


def gen_imx219_pixel(mdata):
    sensor = mdata['sensor']
    csirx = mdata['csirx']
    csirx2 = mdata['csirx2']
    context = mdata['contexts'].pop(0)

    w, h, bus_fmt, pix_fmt = imx219_fmt

    return {
        'subdevs': [
            gen_subdev(
                sensor,
                pads={(0, 0): (w, h, bus_fmt)},
                controls={v4l2.uapi.V4L2_CID_ANALOGUE_GAIN: 200, 0x009F0903: 0},
            ),
            gen_subdev(csirx, routing=((0, 0), (1, 0))),
            gen_subdev(csirx2, routing=((0, 0), (1, 0))),
        ],
        'devices': [
            {'entity': context, 'fmt': (w, h, pix_fmt)},
        ],
    }


def get_configs(config_names):
    mdata = resolve_media_graph()

    if not config_names:
        config_names = ['cam0']

    cfgs = []

    for cname in config_names:
        m = re.fullmatch(r'cam(\d+)', cname)
        if not m:
            raise RuntimeError(f'Unknown config name: {cname}')
        cfgs.append(gen_imx219_pixel(mdata))

    for cfg in cfgs:
        propagate_formats(cfg)
        infer_links(mdata['md'], cfg)

    merged_config = merge_configs(cfgs)
    merged_config['media'] = MEDIA_DEV

    return merged_config
