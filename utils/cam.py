#!/usr/bin/env python3

from __future__ import annotations

import argparse
import pprint
import selectors
import sys
import time

import v4l2
from v4l2.videodev import VideoCaptureStreamer

from cam_helpers import read_config, save_fb_to_file, disable_all_links, configure_subdevs, setup_links
from cam_types import Stream, Context

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
    parser.add_argument('config_name', help='<config name>[:<stream name>[,<stream name>...]]')
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
        ctx.net_host=args.host
        ctx.net_port=args.port
        print(f'Network transfer on {args.host}:{args.port}')
    else:
        ctx.tx = None

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
        if ctx.consumer:
            ctx.consumer.setup_stream(ctx, stream)

        if ctx.buf_type == 'drm':
            fds = [fb.fd(0) for fb in stream['fbs']]
            cap.reserve_buffers_dmabuf(fds)
        else:
            cap.reserve_buffers(stream['num_bufs'])

        first_buf = 1 if stream['display'] else 0

        # Queue the rest to the camera
        for i in range(first_buf, stream['num_bufs']):
            cap.queue(cap.vbuffers[i])

    if ctx.consumer:
        ctx.consumer.setup_streams_done(ctx)

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

    if ctx.user_script:
        ctx.updater = ctx.user_script.Updater(ctx.subdevices)
    else:
        ctx.updater = None


def queue_buf(stream: Stream, vbuf: v4l2.VideoBuffer):
    cap = stream['cap']
    cap.queue(vbuf)


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

    if ctx.consumer:
        ctx.consumer.handle_frame(ctx, stream, vbuf)
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

    # Register stdin only if we are not in IPython mode
    if not ctx.use_ipython:
        sel.register(sys.stdin, selectors.EVENT_READ, lambda: readkey(ctx))

    if ctx.consumer:
        ctx.consumer.register_selector(sel)

    for stream in ctx.streams:
        sel.register(stream['cap'].fd,
                     selectors.EVENT_READ | selectors.EVENT_WRITE,
                     lambda data=stream: readvid(ctx, data))

    if not ctx.use_ipython:
        while not ctx.exit:
            events = sel.select()

            if ctx.consumer:
                ctx.consumer.handle_tick(ctx)

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

    ctx.consumer = None

    if ctx.use_display or ctx.buf_type == 'drm':
        from cam_kms import DisplayConsumer
        ctx.consumer = DisplayConsumer(ctx)

    if ctx.tx:
        from cam_net import NetConsumer
        ctx.consumer = NetConsumer(host=ctx.net_host, port=ctx.net_port)

    if ctx.print_config:
        for stream in ctx.streams:
            pprint.pprint(stream)

    if ctx.config_only:
        sys.exit(0)

    setup(ctx)

    run(ctx)

    if ctx.consumer:
        ctx.consumer.cleanup(ctx)

    return 0

if __name__ == '__main__':
    sys.exit(main())
