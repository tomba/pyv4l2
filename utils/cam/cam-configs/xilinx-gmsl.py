import re

from cam_helpers import gen_subdev, infer_links, merge_configs, propagate_formats

import v4l2
import v4l2.uapi

# imx219_w, imx219_h = 3280, 2464
# imx219_w, imx219_h = 1920, 1080
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

# GMSL2 deserializers supported by the Maxim serdes driver
DESER_REGEX = r'(max9296a|max96714|max96716a|max96724|max96726a) [0-9]+-[0-9a-f]+'

# Stream ID used on the deser source pad and csirx sink pad for the deser TPG.
# Pixel streams use 0-3 and embedded data streams 4-7.
DES_TPG_STREAM = 8


def find_internal_pad(ent):
    """Return the index of the internal (TPG) sink pad of a serdes entity, or None."""
    return next((p.index for p in ent.pads if p.is_internal), None)


def resolve_pipeline(pix_switch, emb_switch, slot):
    """Traverse the graph downstream from the switches to find the IPs
    dedicated to the given slot. Switch pad 0 is the sink, source pads follow,
    so slot N uses switch source pad 1 + N. Everything after the switch is
    fixed hardware wiring.
    """
    switch_pad = 1 + slot

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

    return {
        'switch_pad': switch_pad,
        'demosaic': demosaic,
        'gamma': gamma,
        'pix_dma': pix_dma,
        'emb_dma': emb_dma,
    }


def resolve_media_graph():
    md = v4l2.MediaDevice(*MEDIA_DEV)

    des = md.find_entity(regex=DESER_REGEX)
    assert des

    # The deser has one sink pad per GMSL link, one source pad per CSI-2
    # output port, and an internal sink pad for the TPG. Find the source pad
    # that is wired to the csirx.
    des_src_pad = next((p for p in des.source_pads if p.links), None)
    assert des_src_pad, f'No linked source pad on {des.name}'

    csirx = des_src_pad.get_remote_entity()
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

    # Find the serializers and cameras from the deser sink pads. A serializer
    # without a sensor is kept so that its TPG can be used. Camera N uses
    # switch slot N.
    cams = []

    for p in des.sink_pads:
        if p.is_internal:
            continue

        ser = p.get_remote_entity()
        if not ser:
            continue

        cam = {
            'des_pad': p.index,
            'ser': ser,
            'ser_tpg_pad': find_internal_pad(ser),
            'sensor': ser.get_remote_entity(0),
        }
        cam.update(resolve_pipeline(pix_switch, emb_switch, len(cams)))
        cams.append(cam)

    return {
        'md': md,
        'des': des,
        'des_src_pad': des_src_pad.index,
        'des_tpg_pad': find_internal_pad(des),
        'csirx': csirx,
        'pix_switch': pix_switch,
        'emb_switch': emb_switch,
        'cams': cams,
    }


def gen_imx219_pixel(mdata, idx):
    cam = mdata['cams'][idx]
    des = mdata['des']
    des_src_pad = mdata['des_src_pad']
    csirx = mdata['csirx']
    switch = mdata['pix_switch']

    ser = cam['ser']
    sensor = cam['sensor']
    demosaic = cam['demosaic']
    gamma = cam['gamma']
    context = cam['pix_dma']
    assert sensor, f'No sensor for cam{idx}'
    assert demosaic and gamma and context, f'No pixel pipeline for cam{idx}'

    w, h, bus_fmt, pix_fmt = imx219_fmt
    stream_id = idx
    bus_fmt_demosaic = v4l2.BusFormat.RBG888_1X24
    pix_fmt = v4l2.PixelFormats.RGB888

    return {
        'subdevs': [
            gen_subdev(
                sensor,
                pads={(0, 0): (w, h, bus_fmt)},
                controls={
                    v4l2.uapi.V4L2_CID_ANALOGUE_GAIN: 300,
                    v4l2.uapi.V4L2_CID_TEST_PATTERN: 0,
                },
            ),
            gen_subdev(ser, routing=((0, 0), (1, 0))),
            gen_subdev(des, routing=((cam['des_pad'], 0), (des_src_pad, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(switch, routing=((0, stream_id), (cam['switch_pad'], 0))),
            gen_subdev(demosaic, pads={0: (w, h, bus_fmt), 1: (w, h, bus_fmt_demosaic)}),
            gen_subdev(gamma, pads={0: (w, h, bus_fmt_demosaic), 1: (w, h, bus_fmt_demosaic)}),
        ],
        'devices': [
            {'entity': context, 'fmt': (w, h, pix_fmt)},
        ],
    }


def gen_imx219_meta(mdata, idx):
    cam = mdata['cams'][idx]
    des = mdata['des']
    des_src_pad = mdata['des_src_pad']
    csirx = mdata['csirx']
    switch = mdata['emb_switch']

    ser = cam['ser']
    sensor = cam['sensor']
    context = cam['emb_dma']
    assert sensor, f'No sensor for cam{idx}'
    assert switch and context, f'No embedded data pipeline for cam{idx}'

    w, h, bus_fmt, pix_fmt = imx219_meta_fmt
    stream_id = idx + 4

    return {
        'subdevs': [
            gen_subdev(sensor, fmt=(w, h, bus_fmt), routing=((2, 0), (0, 1))),
            gen_subdev(ser, routing=((0, 1), (1, 1))),
            gen_subdev(des, routing=((cam['des_pad'], 1), (des_src_pad, stream_id))),
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


# The serdes TPGs output RGB888, which cannot go through the demosaic in the
# pixel path, so the TPG configs use the embedded data path (csirx pad 2 ->
# switch -> dma) which has no processing IPs in between.


def gen_ser_tpg(mdata, idx):
    cam = mdata['cams'][idx]
    des = mdata['des']
    des_src_pad = mdata['des_src_pad']
    csirx = mdata['csirx']
    switch = mdata['emb_switch']

    ser = cam['ser']
    tpg_pad = cam['ser_tpg_pad']
    context = cam['emb_dma']
    assert tpg_pad is not None, f'No TPG pad on {ser.name}'
    assert switch and context, f'No embedded data pipeline for cam{idx}'

    w, h, bus_fmt, pix_fmt = tpg_fmt
    stream_id = idx

    return {
        'subdevs': [
            gen_subdev(ser, fmt=(w, h, bus_fmt), routing=((tpg_pad, 0), (1, 0))),
            gen_subdev(des, routing=((cam['des_pad'], 0), (des_src_pad, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (2, idx))),
            gen_subdev(switch, routing=((0, idx), (cam['switch_pad'], 0))),
        ],
        'devices': [
            {'entity': context, 'fmt': (w, h, pix_fmt)},
        ],
    }


def gen_des_tpg(mdata):
    des = mdata['des']
    des_src_pad = mdata['des_src_pad']
    tpg_pad = mdata['des_tpg_pad']
    csirx = mdata['csirx']
    switch = mdata['emb_switch']
    assert tpg_pad is not None, f'No TPG pad on {des.name}'

    # The deser TPG is not tied to any camera. Use slot 0's embedded data
    # pipeline, so this conflicts with cam0-meta and cam0-tpg.
    slot = 0
    pipe = resolve_pipeline(mdata['pix_switch'], switch, slot)
    context = pipe['emb_dma']
    assert switch and context, f'No embedded data pipeline for slot {slot}'

    w, h, bus_fmt, pix_fmt = tpg_fmt
    stream_id = DES_TPG_STREAM

    return {
        'subdevs': [
            gen_subdev(des, fmt=(w, h, bus_fmt), routing=((tpg_pad, 0), (des_src_pad, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (2, slot))),
            gen_subdev(switch, routing=((0, slot), (pipe['switch_pad'], 0))),
        ],
        'devices': [
            {'entity': context, 'fmt': (w, h, pix_fmt)},
        ],
    }


def get_configs(config_names):
    mdata = resolve_media_graph()

    if not config_names:
        config_names = [f'cam{i}' for i, cam in enumerate(mdata['cams']) if cam['sensor']]

    cfgs = []

    for cname in config_names:
        if cname == 'des-tpg':
            cfgs.append(gen_des_tpg(mdata))
            continue

        m = re.fullmatch(r'cam(\d+)(?:-(\w+))?', cname)
        if not m:
            raise RuntimeError(f'Unknown config name: {cname}')
        num = int(m.group(1))
        suffix = m.group(2)
        if num >= len(mdata['cams']):
            raise RuntimeError(f'No cam{num}: {len(mdata["cams"])} serializer(s) found')
        if suffix is None:
            cfgs.append(gen_imx219_pixel(mdata, num))
        elif suffix == 'tpg':
            cfgs.append(gen_ser_tpg(mdata, num))
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
