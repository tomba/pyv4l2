#!/usr/bin/python3

from __future__ import annotations

import argparse
import pprint
import selectors
import sys
import time
import types
import queue
import threading

from typing import TYPE_CHECKING

from cam_helpers import read_config, save_fb_to_file, disable_all_links, configure_subdevs, setup_links
from cam_net import NetTX

from cam_types import Stream

import v4l2
from v4l2.videodev import VideoCaptureStreamer

if TYPE_CHECKING:
    from .cam_kms import KmsContext

class Context:
    verbose: bool
    config: dict
    use_ipython: bool
    user_script: types.ModuleType | None
    subdevices: dict[str, v4l2.SubDevice] | None
    streams: list[Stream]
    md: v4l2.MediaDevice | None
    buf_type: str
    use_display: bool
    kms_committed: bool
    print_config: bool
    config_only: bool
    delay: int
    save: bool
    tx: None | list[str]
    run_ipython: types.LambdaType
    exit: bool
    exit_num_frames: int

    kms_ctx: KmsContext

    net_tx: None | NetTX
    net_tx_queue: queue.Queue
    net_done_queue: queue.Queue

    updater: object


def parse_args(ctx: Context):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config-only', action='store_true', default=False, help='configure only')
    parser.add_argument('-s', '--save', action='store_true', default=False, help='save frames to files')
    parser.add_argument('-d', '--display', action='store_true', default=False, help='show frames on screen')
    parser.add_argument('-x', '--tx', nargs='?', type=str, default=None, const='all', help='send frames to a server')
    parser.add_argument('-t', '--type', type=str, help='buffer type (drm/v4l2)')
    parser.add_argument('-p', '--print', action='store_true', default=False, help='print config dict')
    parser.add_argument('-i', '--ipython', action='store_true', default=False, help='IPython mode')
    parser.add_argument('-S', '--script', help='User script')
    parser.add_argument('-D', '--delay', type=int, help='Delay in secs after the initial KMS modeset')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose output')
    parser.add_argument('-H', '--host', default='192.168.88.20', type=str)
    parser.add_argument('-P', '--port', default=43242, type=int)
    parser.add_argument('-n', '--numframes', default=0, type=int, help='Number of frames to capture')
    parser.add_argument('config_name', help='Configuration name')
    parser.add_argument('params', nargs='*', help='Parameters to the configuration')
    args = parser.parse_args()

    ctx.verbose = args.verbose
    ctx.print_config = args.print
    ctx.config_only = args.config_only
    ctx.delay = args.delay
    ctx.save = args.save
    ctx.exit_num_frames = args.numframes

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
        ctx.net_tx = NetTX(host=args.host, port=args.port)
        print(f'Network transfer on {args.host}:{args.port}')
    else:
        ctx.tx = None
        ctx.net_tx = None

    if not args.type:
        if args.display:
            args.type = 'drm'
        else:
            args.type = 'v4l2'

    if args.type not in ['drm', 'v4l2']:
        print('Bad buffer type', args.type)
        sys.exit(-1)

    ctx.use_display = args.display
    ctx.buf_type = args.type

    ctx.config = read_config(args.config_name, args.params)


def init_mdev(ctx: Context):
    if ctx.config['media']:
        ctx.md = v4l2.MediaDevice(*ctx.config['media'])
    else:
        ctx.md = None


def init_links(ctx: Context):
    if not ctx.md:
        return

    disable_all_links(ctx.md)

    setup_links(ctx, ctx.config)


def init_subdevs(ctx: Context):
    if not ctx.md:
        ctx.subdevices = None
        return

    ctx.subdevices = configure_subdevs(ctx, ctx.config)


def init_viddevs(ctx: Context):
    ctx.streams = ctx.config['devices']

    streams = ctx.streams

    for i, stream in enumerate(streams):
        stream['id'] = i

    for stream in streams:
        stream['num_bufs'] = stream.get('num_bufs', 5)
        stream['display'] = ctx.use_display and stream.get('display', True)
        stream['embedded'] = stream.get('embedded', False)

        fmt = stream['fmt']
        if len(fmt) == 3:
            stream['w'] = fmt[0]
            stream['h'] = fmt[1]
            stream['size'] = (stream['w'], stream['h'])
            stream['format'] = fmt[2]
        elif len(fmt) == 2:
            stream['size'] = fmt[0]
            stream['format'] = fmt[1]
        else:
            raise RuntimeError()

        if ctx.md:
            vid_ent = ctx.md.find_entity(stream['entity'])
            assert(vid_ent)

            if 'dev_path' not in stream:
                stream['dev_path'] = vid_ent.interface.dev_path

            if ctx.verbose:
                print(f'Configuring {vid_ent.name} ({stream["dev_path"]})')

            vd = v4l2.VideoDevice(vid_ent.interface.dev_path)
        else:
            dev_path = v4l2.VideoDevice.find_video_device(*stream['device'])
            stream['dev_path'] = dev_path

            if ctx.verbose:
                print(f'Configuring {dev_path}')

            vd = v4l2.VideoDevice(dev_path)

        stream['dev'] = vd


def init_streamer(ctx: Context):
    streams = ctx.streams

    for stream in streams:
        vd = stream['dev']

        if ctx.verbose:
            print(f'Configuring streamer {vd.dev_path}')

        mem_type = v4l2.MemType.DMABUF if ctx.buf_type == 'drm' else v4l2.MemType.MMAP

        if not stream.get('embedded', False):
            assert isinstance(stream['format'], v4l2.PixelFormat)
            cap = vd.get_capture_streamer(mem_type, stream['w'], stream['h'], stream['format'])
        else:
            assert isinstance(stream['format'], v4l2.MetaFormat)
            cap = vd.get_meta_capture_streamer(mem_type, stream['size'], stream['format'])

        stream['cap'] = cap


def setup(ctx: Context):
    streams = ctx.streams

    for stream in streams:
        cap = stream['cap']

        if ctx.buf_type == 'drm':
            ctx.kms_ctx.alloc_fbs(stream)

        if stream['display']:
            ctx.kms_ctx.setup_stream(stream)

        if ctx.buf_type == 'drm':
            fds = [fb.fd(0) for fb in stream['fbs']]
            cap.reserve_buffers_dmabuf(fds)
        else:
            cap.reserve_buffers(stream['num_bufs'])

        first_buf = 1 if stream['display'] else 0

        # Queue the rest to the camera
        for i in range(first_buf, stream['num_bufs']):
            cap.queue(cap.vbuffers[i])

    if ctx.use_display:
        ctx.kms_ctx.init_modeset()

    for stream in streams:
        if 'size' in stream:
            print(f'{stream["dev_path"]}: stream on {stream["size"]}-{stream["format"].name}')
        else:
            streamer: VideoCaptureStreamer = stream['cap']
            strides = '/'.join(map(str, streamer.strides))
            bufsizes = '/'.join(map(str, streamer.buffersizes))
            print(f'{stream["dev_path"]}: stream on {stream["w"]}x{stream["h"]}-{stream["format"].name} framesize={streamer.framesize} bufsizes={bufsizes} strides={strides}')
        stream['cap'].stream_on()

    for stream in streams:
        stream['total_num_frames'] = 0
        stream['last_framenum'] = 0
        stream['last_timestamp'] = time.perf_counter()

    ctx.kms_committed = False

    if ctx.user_script:
        ctx.updater = ctx.user_script.Updater(ctx.subdevices)
    else:
        ctx.updater = None


def queue_buf(stream: Stream, vbuf: v4l2.VideoBuffer):
    cap = stream['cap']
    cap.queue(vbuf)


def net_main(ctx):
    while True:
        data = ctx.net_tx_queue.get()

        if not data:
            break

        stream, vbuf, is_drm = data

        ctx.net_tx.tx(stream, vbuf, is_drm)

        ctx.net_done_queue.put((stream, vbuf))


def handle_sent_buffers(ctx: Context):
    while not ctx.net_done_queue.empty():
        stream, vbuf = ctx.net_done_queue.get()

        stream['tx_buf'] = None

        queue_buf(stream, vbuf)


def readvid(ctx: Context, stream: Stream):
    if ctx.verbose:
        print('{}: event'.format(stream['dev_path']))

    if ctx.updater:
        ctx.updater.update()

    stream['total_num_frames'] += 1

    if stream['total_num_frames'] == ctx.exit_num_frames:
        ctx.exit = True

    # With IPython we have separate fps tracking
    if not ctx.use_ipython:
        ts = time.perf_counter()

        diff = ts - stream['last_timestamp']
        num_frames = stream['total_num_frames'] - stream['last_framenum']

        if stream['total_num_frames'] == 1:
            print('{}: first frame in {:.2f} s'
                  .format(stream['dev_path'], diff))

        if diff >= 1:
            print('{}: {} frames in {:.2f} s, {:.2f} fps'
                  .format(stream['dev_path'], num_frames, diff, num_frames / diff))

            stream['last_timestamp'] = ts
            stream['last_framenum'] = stream['total_num_frames']

    cap = stream['cap']
    vbuf = cap.dequeue()

    fb = None

    if ctx.buf_type == 'drm':
        fb = next((fb for fb in stream['fbs'] if fb.fd(0) == vbuf.fd), None)
        assert fb is not None

    if ctx.save:
        save_fb_to_file(stream, ctx.buf_type == 'drm', fb if ctx.buf_type == 'drm' else vbuf)

    if stream['display']:
        assert fb is not None
        stream['kms_fb_queue'].append(fb)

        if len(stream['kms_fb_queue']) >= stream['num_bufs'] - 1:
            print('WARNING fb_queue {}'.format(len(stream['kms_fb_queue'])))

        #print(f'Buf from {stream['dev_path']}: kms_fb_queue {len(stream['kms_fb_queue'])}, commit ongoing {kms_committed}')

        # XXX with a small delay we might get more planes to the commit
        if not ctx.kms_committed:
            ctx.kms_ctx.handle_pageflip()
    elif ctx.tx and (ctx.tx == ['all'] or str(stream['id']) in ctx.tx) and not stream['tx_buf']:
        stream['tx_buf'] = vbuf
        ctx.net_tx_queue.put((stream, vbuf, ctx.buf_type == 'drm'))
    else:
        queue_buf(stream, vbuf)


def readkey(ctx):
    streams = ctx.streams

    for stream in reversed(streams):
        print(f'{stream["dev_path"]}: stream off')
        stream['cap'].stream_off()

    print('Done')
    sys.stdin.readline()
    ctx.exit = True


def run(ctx: Context):
    ctx.exit = False

    sel = selectors.DefaultSelector()

    if not ctx.use_ipython:
        sel.register(sys.stdin, selectors.EVENT_READ, lambda: readkey(ctx))
    if ctx.use_display:
        ctx.kms_ctx.register_selector(sel)
    for stream in ctx.streams:
        sel.register(stream['cap'].fd,
                     selectors.EVENT_READ | selectors.EVENT_WRITE,
                     lambda data=stream: readvid(ctx, data))

    if not ctx.use_ipython:
        while not ctx.exit:
            events = sel.select()

            if ctx.tx:
                handle_sent_buffers(ctx)

            for key, _ in events:
                callback = key.data
                callback()
    else:
        ctx.run_ipython(ctx, sel)


def main():
    ctx = Context()

    parse_args(ctx)
    init_mdev(ctx)
    init_links(ctx)
    init_subdevs(ctx)
    init_viddevs(ctx)
    init_streamer(ctx)

    if ctx.use_display or ctx.buf_type == 'drm':
        from cam_kms import KmsContext
        ctx.kms_ctx = KmsContext(ctx)

    if ctx.print_config:
        for stream in ctx.streams:
            pprint.pprint(stream)

    if ctx.config_only:
        sys.exit(0)

    setup(ctx)

    net_thread = None
    if ctx.tx:
        for stream in ctx.streams:
            stream['tx_buf'] = None

        ctx.net_tx_queue = queue.Queue()
        ctx.net_done_queue = queue.Queue()

        net_thread = threading.Thread(target=net_main, args=(ctx,))
        net_thread.start()

    run(ctx)

    if ctx.tx:
        assert net_thread is not None
        ctx.net_tx_queue.put(None)
        net_thread.join()

    return 0

if __name__ == '__main__':
    sys.exit(main())
