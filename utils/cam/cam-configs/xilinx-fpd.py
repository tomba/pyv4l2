import re

import v4l2
import v4l2.uapi

from cam_helpers import merge_configs, gen_subdev, infer_links, propagate_formats

#imx219_w, imx219_h = 3280, 2464
#imx219_w, imx219_h = 1920, 1080
imx219_w, imx219_h = 640, 480

USE_RAW_10 = False

if USE_RAW_10:
    imx219_fmt = (imx219_w, imx219_h, v4l2.BusFormat.SRGGB10_1X10, v4l2.PixelFormats.SRGGB10)
    imx219_meta_fmt = (imx219_w, 2, v4l2.BusFormat.META_10, v4l2.MetaFormats.GENERIC_CSI2_10)
else:
    imx219_fmt = (imx219_w, imx219_h, v4l2.BusFormat.SRGGB8_1X8, v4l2.PixelFormats.SRGGB8)
    imx219_meta_fmt = (imx219_w, 2, v4l2.BusFormat.META_8, v4l2.MetaFormats.GENERIC_8)

tpg_fmt = (1920, 1024, v4l2.BusFormat.RGB888_1X24, v4l2.PixelFormats.XRGB8888)

MEDIA_DEV = ('platform:xilinx_video_top', 'bus_info')

def resolve_media_graph():
    md = v4l2.MediaDevice(*MEDIA_DEV)

    des = md.find_entity('ds90ub960*')
    assert des

    csirx = des.get_remote_entity(4)
    assert csirx

    # The csirx has a single sink pad and one source pad per output port. A
    # second source pad means the embedded data path is available.
    num_src_pads = len(csirx.source_pads)
    assert num_src_pads in (1, 2), f'Unexpected number of csirx source pads: {num_src_pads}'
    has_emb = num_src_pads == 2

    # Find switches from csirx source pads
    pix_switch = csirx.get_remote_entity(1)
    assert pix_switch

    if has_emb:
        emb_switch = csirx.get_remote_entity(2)
        assert emb_switch
    else:
        emb_switch = None

    # Find the cameras from the deser sink pads, and traverse the graph
    # downstream from the switches to find the IPs dedicated to each camera's
    # pipeline. The switch source pad used for a camera is 1 + camera index,
    # and everything after the switch is fixed hardware wiring.
    cams = []

    for p in des.sink_pads:
        ser = p.get_remote_entity()
        if not ser:
            continue

        sensor = ser.get_remote_entity(0)
        if not sensor:
            continue

        # Switch pad 0 is the sink, source pads follow
        switch_pad = 1 + len(cams)

        # pix path: switch -> demosaic -> gamma -> dma
        demosaic = gamma = pix_dma = None

        if switch_pad < len(pix_switch.pads):
            demosaic = pix_switch.get_remote_entity(switch_pad)
        if demosaic:
            gamma = demosaic.get_remote_entity(1)
        if gamma:
            pix_dma = gamma.get_remote_entity(1)

        # emb path: switch -> dma
        emb_dma = None

        if emb_switch and switch_pad < len(emb_switch.pads):
            emb_dma = emb_switch.get_remote_entity(switch_pad)

        cams.append({
            'des_pad': p.index,
            'ser': ser,
            'sensor': sensor,
            'switch_pad': switch_pad,
            'demosaic': demosaic,
            'gamma': gamma,
            'pix_dma': pix_dma,
            'emb_dma': emb_dma,
        })

    return {
        'md': md,
        'des': des,
        'csirx': csirx,
        'pix_switch': pix_switch,
        'emb_switch': emb_switch,
        'cams': cams,
    }

def gen_imx219_pixel(mdata, idx):
    cam = mdata['cams'][idx]
    des = mdata['des']
    csirx = mdata['csirx']
    switch = mdata['pix_switch']

    ser = cam['ser']
    sensor = cam['sensor']
    demosaic = cam['demosaic']
    gamma = cam['gamma']
    context = cam['pix_dma']
    assert demosaic and gamma and context, f'No pixel pipeline for cam{idx}'

    w, h, bus_fmt, pix_fmt = imx219_fmt
    stream_id = idx
    bus_fmt_demosaic = v4l2.BusFormat.RBG888_1X24
    pix_fmt = v4l2.PixelFormats.RGB888

    return {
        'subdevs': [
            gen_subdev(sensor,
                       pads={(0, 0): (w, h, bus_fmt)},
                       controls={v4l2.uapi.V4L2_CID_ANALOGUE_GAIN: 300,
                                 0x009f0903: 0}),
            gen_subdev(ser, routing=((0, 0), (1, 0))),
            gen_subdev(des, routing=((cam['des_pad'], 0), (4, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(switch, routing=((0, stream_id), (cam['switch_pad'], 0))),
            gen_subdev(demosaic,
                       pads={0: (w, h, bus_fmt),
                             1: (w, h, bus_fmt_demosaic)}),
            gen_subdev(gamma,
                       pads={0: (w, h, bus_fmt_demosaic),
                             1: (w, h, bus_fmt_demosaic)}),
        ],

        'devices': [
            { 'entity': context, 'fmt': (w, h, pix_fmt) },
        ],
    }

def gen_imx219_meta(mdata, idx):
    cam = mdata['cams'][idx]
    des = mdata['des']
    csirx = mdata['csirx']
    switch = mdata['emb_switch']

    ser = cam['ser']
    sensor = cam['sensor']
    context = cam['emb_dma']
    assert context, f'No embedded data pipeline for cam{idx}'

    w, h, bus_fmt, pix_fmt = imx219_meta_fmt
    stream_id = idx + 4

    return {
        'subdevs': [
            gen_subdev(sensor, fmt=(w, h, bus_fmt),
                       routing=((2, 0), (0, 1))),
            gen_subdev(ser, routing=((0, 1), (1, 1))),
            gen_subdev(des, routing=((cam['des_pad'], 1), (4, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (2, idx))),
            gen_subdev(switch, routing=((0, idx), (cam['switch_pad'], 0))),
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
    cam = mdata['cams'][idx]
    des = mdata['des']
    csirx = mdata['csirx']
    csirx2 = mdata['csirx2']

    ser = cam['ser']
    context = cam['pix_dma']
    assert context, f'No pixel pipeline for cam{idx}'

    w, h, bus_fmt, pix_fmt = tpg_fmt
    stream_id = idx

    return {
        'subdevs': [
            gen_subdev(ser, fmt=(w, h, bus_fmt),
                       routing=((2, 0), (1, 0))),
            gen_subdev(des, routing=((cam['des_pad'], 0), (4, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(csirx2, routing=((0, stream_id), (cam['switch_pad'], 0))),
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
