#!/usr/bin/python3

from collections import deque
import argparse
import pprint
import selectors
import sys
import time
import types

from cam_helpers import *
from cam_pisp import *
import v4l2


class Context(object):
    config: dict
    use_ipython: bool
    user_script: types.ModuleType | None
    subdevices: dict
    streams: list
    md: v4l2.MediaDevice
    buf_type: str
    use_display: bool
    kms_committed: bool
    print_config: bool
    config_only: bool
    delay: int
    save: bool
    tx: list[str]
    run_ipython: types.LambdaType

    kms_alloc_fbs: types.LambdaType
    kms_init: types.LambdaType
    kms_setup_stream: types.LambdaType
    kms_init_modeset: types.LambdaType
    kms_readdrm: types.LambdaType


def parse_args(ctx: Context):
    parser = argparse.ArgumentParser()
    parser.add_argument('config_name', help='Configuration name')
    parser.add_argument('-c', '--config-only', action='store_true', default=False, help='configure only')
    parser.add_argument('-s', '--save', action='store_true', default=False, help='save frames to files')
    parser.add_argument('-d', '--display', action='store_true', default=False, help='show frames on screen')
    parser.add_argument('-x', '--tx', nargs='?', type=str, default=None, const='all', help='send frames to a server')
    parser.add_argument('-t', '--type', type=str, help='buffer type (drm/v4l2)')
    parser.add_argument('-p', '--print', action='store_true', default=False, help='print config dict')
    parser.add_argument('-i', '--ipython', action='store_true', default=False, help='IPython mode')
    parser.add_argument('-S', '--script', help='User script')
    parser.add_argument('-D', '--delay', type=int, help='Delay in secs after the initial KMS modeset')
    args = parser.parse_args()

    ctx.print_config = args.print
    ctx.config_only = args.config_only
    ctx.delay = args.delay
    ctx.save = args.save

    ctx.use_ipython = args.ipython

    if ctx.use_ipython:
        from cam_ipython import run_ipython
        ctx.run_ipython = run_ipython

    if args.script:
        import importlib.util
        spec = importlib.util.spec_from_file_location('userscript', args.script)
        assert(spec)
        user_mod = importlib.util.module_from_spec(spec)
        assert(spec.loader)
        spec.loader.exec_module(user_mod)
        ctx.user_script = user_mod
    else:
        ctx.user_script = None

    if args.tx:
        ctx.tx = args.tx.split(',')
        ctx.net_tx = NetTX()
    else:
        ctx.tx = None
        ctx.net_tx = None

    if args.type and args.type not in ['drm', 'v4l2']:
        print('Bad buffer type', args.type)
        sys.exit(-1)

    ctx.use_display = args.display

    if args.type:
        ctx.buf_type = args.type
    else:
        if args.display:
            ctx.buf_type = 'drm'
        else:
            ctx.buf_type = 'v4l2'

    if ctx.use_display or ctx.buf_type == 'drm':
        from cam_kms import alloc_fbs, init_kms
        ctx.kms_alloc_fbs = alloc_fbs
        ctx.kms_init = init_kms

    ctx.config = read_config(args.config_name)


def init_mdev(ctx: Context):
    if ctx.config['media']:
        ctx.md = v4l2.MediaDevice(*ctx.config['media'])
    else:
        ctx.md = None


def init_links(ctx: Context):
    if not ctx.md:
        return

    disable_all_links(ctx.md)

    setup_links(ctx.md, ctx.config)


def init_subdevs(ctx: Context):
    if not ctx.md:
        ctx.subdevices = None
        return

    ctx.subdevices = configure_subdevs(ctx.md, ctx.config)


def init_viddevs(ctx: Context):
    ctx.streams = ctx.config['devices']

    streams = ctx.streams

    for i, stream in enumerate(streams):
        stream['id'] = i

    for stream in streams:
        stream['num_bufs'] = stream.get('num_bufs', 5)
        stream['display'] = ctx.use_display and stream.get('display', True)
        stream['embedded'] = stream.get('embedded', False)

        stream['w'] = stream['fmt'][0]
        stream['h'] = stream['fmt'][1]
        stream['fourcc'] = stream['fmt'][2]

        if ctx.md:
            vid_ent = ctx.md.find_entity(stream['entity'])
            assert(vid_ent)

            if not 'dev_path' in stream:
                stream['dev_path'] = vid_ent.interface.dev_path

            vd = v4l2.VideoDevice(vid_ent.interface.dev_path)
        else:
            dev_path = v4l2.VideoDevice.find_video_device(*stream['entity'])
            stream['dev_path'] = dev_path

            vd = v4l2.VideoDevice(dev_path)

        stream['dev'] = vd


def init_streamer(ctx: Context):
    streams = ctx.streams

    for stream in streams:
        vd = stream['dev']

        mem_type = v4l2.MemType.DMABUF if ctx.buf_type == 'drm' else v4l2.MemType.MMAP

        if not stream.get('embedded', False):
            cap = vd.get_capture_streamer(mem_type, stream['w'], stream['h'], stream['fourcc'])
        else:
            bpp = embedded_fourcc_to_bytes_per_pixel(stream['fourcc'])
            size = stream['w'] * stream['h'] * bpp // 8
            cap = vd.get_meta_capture_streamer(mem_type, size, stream['fourcc'])

        stream['cap'] = cap


def setup(ctx: Context):
    streams = ctx.streams

    for stream in streams:
        cap = stream['cap']

        if ctx.buf_type == 'drm':
            ctx.kms_alloc_fbs(ctx, stream)

        if stream['display']:
            ctx.kms_setup_stream(ctx, stream)

        if ctx.buf_type == 'drm':
            fds = [fb.fd(0) for fb in stream['fbs']]
            cap.reserve_buffers_dmabuf(fds)
        else:
            cap.reserve_buffers(stream['num_bufs'])

        first_buf = 1 if stream['display'] else 0

        # Queue the rest to the camera
        for i in range(first_buf, stream['num_bufs']):
            if stream['fourcc'] == v4l2.MetaFormat.RPI_FE_CFG:
                pisp_create_config(cap, cap.buffers[i])

            cap.queue(cap.buffers[i])

    if ctx.use_display:
        ctx.kms_init_modeset(ctx)

    for stream in streams:
        print(f'{stream["dev_path"]}: stream on')
        stream['cap'].stream_on()

    for stream in streams:
        stream['total_num_frames'] = 0
        stream['last_framenum'] = 0
        stream['last_timestamp'] = time.perf_counter()

    ctx.kms_committed = False

    if ctx.user_script:
        ctx.updater = ctx.user_script.Updater(subdevices)
    else:
        ctx.updater = None



def readvid(ctx: Context, stream):
    if ctx.updater:
        ctx.updater.update()

    stream['total_num_frames'] += 1

    # With IPython we have separate fps tracking
    if not ctx.use_ipython:
        ts = time.perf_counter()

        diff = ts - stream['last_timestamp']
        num_frames = stream['total_num_frames'] - stream['last_framenum']

        if stream['total_num_frames'] == 1:
            print('{}: first frame in {:.2f} s'
                  .format(stream['dev_path'], diff))

        if diff >= 5:
            print('{}: {} frames in {:.2f} s, {:.2f} fps'
                  .format(stream['dev_path'], num_frames, diff, num_frames / diff))

            stream['last_timestamp'] = ts
            stream['last_framenum'] = stream['total_num_frames']

    cap = stream['cap']
    vbuf = cap.dequeue()

    if ctx.buf_type == 'drm':
        fb = next((fb for fb in stream['fbs'] if fb.fd(0) == vbuf.fd), None)
        assert(fb != None)

    if ctx.save:
        save_fb_to_file(stream, ctx.buf_type == 'drm', fb if ctx.buf_type == 'drm' else vbuf)

    if stream['display']:
        stream['kms_fb_queue'].append(fb)

        if len(stream['kms_fb_queue']) >= stream['num_bufs'] - 1:
            print('WARNING fb_queue {}'.format(len(stream['kms_fb_queue'])))

        #print(f'Buf from {stream['dev_path']}: kms_fb_queue {len(stream['kms_fb_queue'])}, commit ongoing {kms_committed}')

        # XXX with a small delay we might get more planes to the commit
        if ctx.kms_committed == False:
            handle_pageflip(ctx)
    else:
        if ctx.tx and (ctx.tx == ['all'] or str(stream['id']) in ctx.tx):
            ctx.net_tx.tx(stream, vbuf, ctx.buf_type == 'drm')

        cap.queue(vbuf)


def readkey(ctx):
    streams = ctx.streams

    for stream in reversed(streams):
        print(f'{stream["dev_path"]}: stream off')
        stream['cap'].stream_off()
        #time.sleep(0.5)
        #print('DISABLED CAP')
        #time.sleep(1)

    print('Done')
    sys.stdin.readline()
    exit(0)


def run(ctx: Context):
    sel = selectors.DefaultSelector()

    if not ctx.use_ipython:
        sel.register(sys.stdin, selectors.EVENT_READ, lambda: readkey(ctx))
    if ctx.use_display:
        sel.register(card.fd, selectors.EVENT_READ, lambda: ctx.kms_readdrm(ctx))
    for stream in ctx.streams:
        sel.register(stream['cap'].fd, selectors.EVENT_READ, lambda data=stream: readvid(ctx, data))

    if not ctx.use_ipython:
        while True:
            events = sel.select()
            for key, _ in events:
                callback = key.data
                callback()
        sys.exit(0)
    else:
        ctx.run_ipython(ctx, sel)


if __name__ == "__main__":
    ctx = Context()

    parse_args(ctx)
    init_mdev(ctx)
    init_links(ctx)
    init_subdevs(ctx)
    init_viddevs(ctx)
    init_streamer(ctx)

    if ctx.use_display or ctx.buf_type == 'drm':
        ctx.kms_init(ctx)

    if ctx.print_config:
        for stream in ctx.streams:
            pprint.pprint(stream)

    if ctx.config_only:
        sys.exit(0)

    setup(ctx)
    run(ctx)
