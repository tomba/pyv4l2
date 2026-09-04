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

tpg_fmt = (1920, 1080, v4l2.BusFormat.RGB888_1X24, v4l2.PixelFormats.XRGB8888)

MEDIA_DEV = ('TI-CSI2RX', 'model')

# GMSL2 deserializers supported by the Maxim serdes driver
DESER_REGEX = r'(max9296a|max96714|max96716a|max96724|max96726a) [0-9]+-[0-9a-f]+'

# Stream ID used on the deser source pad and csirx sink pad for the deser TPG.
# Pixel streams use 0-3 and embedded data streams 4-7.
DES_TPG_STREAM = 8


def find_internal_pad(ent):
    """Return the index of the internal (TPG) sink pad of a serdes entity, or None."""
    return next((p.index for p in ent.pads if p.is_internal), None)


def get_context(mdata, ctx_idx):
    """Return the DMA context entity for the given context index. The contexts
    are interchangeable, so use context N for stream N.
    """
    contexts = mdata['contexts']
    assert ctx_idx < len(contexts), f'No DMA context {ctx_idx}'
    return contexts[ctx_idx]


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

    # csirx source pad 1 is wired to the ticsi2rx
    csirx2 = csirx.get_remote_entity(1)
    assert csirx2

    # The ticsi2rx has one source pad per DMA context
    contexts = [p.get_remote_entity() for p in csirx2.source_pads]
    assert all(contexts)

    # Find the serializers and cameras from the deser sink pads. A serializer
    # without a sensor is kept so that its TPG can be used.
    cams = []

    for p in des.sink_pads:
        if p.is_internal:
            continue

        ser = p.get_remote_entity()
        if not ser:
            continue

        cams.append(
            {
                'des_pad': p.index,
                'ser': ser,
                'ser_tpg_pad': find_internal_pad(ser),
                'sensor': ser.get_remote_entity(0),
            }
        )

    return {
        'md': md,
        'des': des,
        'des_src_pad': des_src_pad.index,
        'des_tpg_pad': find_internal_pad(des),
        'csirx': csirx,
        'csirx2': csirx2,
        'contexts': contexts,
        'cams': cams,
    }


def gen_imx219_pixel(mdata, idx):
    cam = mdata['cams'][idx]
    des = mdata['des']
    des_src_pad = mdata['des_src_pad']
    csirx = mdata['csirx']
    csirx2 = mdata['csirx2']

    ser = cam['ser']
    sensor = cam['sensor']
    assert sensor, f'No sensor for cam{idx}'

    w, h, bus_fmt, pix_fmt = imx219_fmt
    stream_id = idx
    ctx_idx = stream_id
    context = get_context(mdata, ctx_idx)

    return {
        'subdevs': [
            gen_subdev(
                sensor,
                pads={(0, 0): (w, h, bus_fmt)},
                controls={
                    v4l2.uapi.V4L2_CID_ANALOGUE_GAIN: 200,
                    v4l2.uapi.V4L2_CID_TEST_PATTERN: 0,
                },
            ),
            gen_subdev(ser, routing=((0, 0), (1, 0))),
            gen_subdev(des, routing=((cam['des_pad'], 0), (des_src_pad, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(csirx2, routing=((0, stream_id), (1 + ctx_idx, 0))),
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
    csirx2 = mdata['csirx2']

    ser = cam['ser']
    sensor = cam['sensor']
    assert sensor, f'No sensor for cam{idx}'

    w, h, bus_fmt, pix_fmt = imx219_meta_fmt
    stream_id = idx + 4
    ctx_idx = stream_id
    context = get_context(mdata, ctx_idx)

    return {
        'subdevs': [
            gen_subdev(sensor, fmt=(w, h, bus_fmt), routing=((2, 0), (0, 1))),
            gen_subdev(ser, routing=((0, 1), (1, 1))),
            gen_subdev(des, routing=((cam['des_pad'], 1), (des_src_pad, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(csirx2, routing=((0, stream_id), (1 + ctx_idx, 0))),
        ],
        'devices': [
            {
                'entity': context,
                'fmt': (w, h, pix_fmt),
                'embedded': True,
            },
        ],
    }


def gen_ser_tpg(mdata, idx):
    cam = mdata['cams'][idx]
    des = mdata['des']
    des_src_pad = mdata['des_src_pad']
    csirx = mdata['csirx']
    csirx2 = mdata['csirx2']

    ser = cam['ser']
    tpg_pad = cam['ser_tpg_pad']
    assert tpg_pad is not None, f'No TPG pad on {ser.name}'

    w, h, bus_fmt, pix_fmt = tpg_fmt
    stream_id = idx
    ctx_idx = stream_id
    context = get_context(mdata, ctx_idx)

    return {
        'subdevs': [
            gen_subdev(ser, fmt=(w, h, bus_fmt), routing=((tpg_pad, 0), (1, 0))),
            gen_subdev(des, routing=((cam['des_pad'], 0), (des_src_pad, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(csirx2, routing=((0, stream_id), (1 + ctx_idx, 0))),
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
    csirx2 = mdata['csirx2']
    assert tpg_pad is not None, f'No TPG pad on {des.name}'

    # The deser TPG is not tied to any camera. Use DMA context 0, so this
    # conflicts with cam0 and cam0-tpg.
    w, h, bus_fmt, pix_fmt = tpg_fmt
    stream_id = DES_TPG_STREAM
    ctx_idx = 0
    context = get_context(mdata, ctx_idx)

    return {
        'subdevs': [
            gen_subdev(des, fmt=(w, h, bus_fmt), routing=((tpg_pad, 0), (des_src_pad, stream_id))),
            gen_subdev(csirx, routing=((0, stream_id), (1, stream_id))),
            gen_subdev(csirx2, routing=((0, stream_id), (1 + ctx_idx, 0))),
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
