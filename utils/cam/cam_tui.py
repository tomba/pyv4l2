from __future__ import annotations

import asyncio
import os
import selectors
import sys
import time
from collections import deque

from cam_types import Context, StreamState
from prompt_toolkit.application import Application
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import HSplit, Layout, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.output import create_output
from prompt_toolkit.widgets import TextArea

HISTORY_FILE = '~/.cam_history'
FPS_INTERVAL = 1
DRAIN_TIMEOUT = 2

COMMANDS = {
    'help': 'show this help',
    'status': 'status [id...]: show detailed stream info',
    'start': 'start [id...]: start streams',
    'stop': 'stop [id...]: stop streams',
    'quit': 'exit (also: q, ctrl-c, ctrl-d)',
}

# The log store and the stdout redirection are module level so that the
# capture can be started with init_log() before the TUI runs, to get the
# prints from the setup phase into the log view.

LOG_MAX_LINES = 1000

_log_lines: deque[str] = deque(maxlen=LOG_MAX_LINES)
_log_partial = ''  # incomplete (not newline-terminated) last line
_orig_stdout = None
_app: Application | None = None


def _log(text: str):
    global _log_partial

    text = _log_partial + text
    lines = text.split('\n')
    _log_partial = lines.pop()
    _log_lines.extend(lines)

    if _app:
        _app.invalidate()


class _LogWriter:
    def write(self, s: str):
        _log(s)
        return len(s)

    def flush(self):
        pass

    def isatty(self):
        return False


def _real_stdout():
    return _orig_stdout if _orig_stdout is not None else sys.stdout


def init_log():
    """Redirect stdout to the TUI log view.

    run_tui() does this automatically, but this can be called before the
    setup phase to capture its prints into the log view. stderr is left
    alone, so errors still reach the console."""
    global _orig_stdout

    if not isinstance(sys.stdout, _LogWriter):
        _orig_stdout = sys.stdout
        sys.stdout = _LogWriter()


def _restore_stdout():
    global _orig_stdout

    if _orig_stdout:
        sys.stdout = _orig_stdout
        _orig_stdout = None


def run_tui(ctx: Context, sel: selectors.BaseSelector, stream_callbacks: dict):
    streams = [stream for sctx in ctx.subcontexts for stream in sctx.streams]

    def make_stream_descs():
        def dim_str(stream):
            if isinstance(stream.size, tuple):
                return f'{stream.size[0]}x{stream.size[1]}'
            return str(stream.size)

        fmts = {s.id: f'{dim_str(s)}-{s.format.name}' for s in streams}

        path_w = max((len(s.dev_path) for s in streams), default=0)
        fmt_w = max((len(f) for f in fmts.values()), default=0)

        return {s.id: f'{s.id}: {s.dev_path:<{path_w}} {fmts[s.id]:<{fmt_w}}'
                for s in streams}

    stream_descs = make_stream_descs()

    # Status pane

    # Time spent in the frame callbacks, to see how much of the event loop
    # they eat ("load")
    cb_time = 0.0

    status = ''
    status_ts = 0.0
    prev_cb_time = 0.0

    def get_status():
        nonlocal status, status_ts, prev_cb_time

        ts = time.perf_counter()
        diff = ts - status_ts

        # The whole layout is rendered on every keypress. Update the status
        # text only every FPS_INTERVAL so that those renders don't change the
        # pane content (and don't reset the fps tracking).
        if status and diff < FPS_INTERVAL:
            return status

        load = (cb_time - prev_cb_time) / diff if status_ts else 0
        prev_cb_time = cb_time
        status_ts = ts

        lines = [f'load:{load:6.1%}']

        for stream in streams:
            sdiff = ts - stream.last_timestamp
            num_frames = stream.total_num_frames - stream.last_framenum

            fps = num_frames / sdiff if sdiff > 0 else 0

            stream.last_timestamp = ts
            stream.last_framenum = stream.total_num_frames

            if stream.state == StreamState.RUNNING:
                state_str = f'fps:{fps:6.2f}'
            else:
                state_str = f'[{stream.state.name.lower()}]'

            lines.append('{} frames:{:8} {}'
                         .format(stream_descs[stream.id],
                                 stream.total_num_frames, state_str))

        status = '\n'.join(lines)
        return status

    status_win = Window(FormattedTextControl(get_status),
                        height=len(streams) + 1, style='reverse')

    # Log area
    #
    # A TextArea is far too heavy to render on slow devices, so use a plain
    # FormattedTextControl over a deque of lines, scrolled to the tail.

    def get_log():
        return '\n'.join(_log_lines) + '\n' + _log_partial

    def log_vscroll(window):
        info = window.render_info
        if info is None:
            return 0
        return max(0, len(_log_lines) + 1 - info.window_height)

    log_win = Window(FormattedTextControl(get_log), wrap_lines=False,
                     get_vertical_scroll=log_vscroll)

    # Command input

    def cmd_help(_args: list[str]):
        for name, desc in COMMANDS.items():
            _log(f'{name:12} {desc}\n')

    def parse_streams(args: list[str]):
        """Args to a list of streams; no args means all streams"""
        try:
            ids = [int(a) for a in args]
        except ValueError:
            _log('Bad stream id\n')
            return None

        if not ids:
            return streams

        for i in ids:
            if not any(s.id == i for s in streams):
                _log(f'No stream {i}\n')

        return [s for s in streams if s.id in ids]

    def cmd_status(args: list[str]):
        sel_streams = parse_streams(args)
        if sel_streams is None:
            return

        for stream in sel_streams:
            cap = stream.cap
            info = stream.dev.get_format_info(cap.buf_type)

            def name(v):
                return v.name if hasattr(v, 'name') else str(v)

            entity = getattr(stream, 'entity', None)

            _log(f'{stream.id}: {stream.dev_path}' +
                 (f' ({entity})' if isinstance(entity, str) else '') +
                 f' [{stream.state.name.lower()}]\n')
            _log(f'   {name(info.format)} {info.width}x{info.height}'
                 f' sizeimage:{info.sizeimage}'
                 f' strides:{cap.strides} bufsizes:{cap.buffersizes}\n')
            _log(f'   bufs:{stream.num_bufs} mem:{cap.mem_type.name}'
                 f' buftype:{cap.buf_type.name}\n')

            if info.colorspace is not None:
                _log(f'   field:{name(info.field)}'
                     f' colorspace:{name(info.colorspace)}'
                     f' ycbcr_enc:{name(info.ycbcr_enc)}'
                     f' quantization:{name(info.quantization)}'
                     f' xfer_func:{name(info.xfer_func)}\n')

    async def do_stop(stream):
        loop = asyncio.get_running_loop()

        t0 = loop.time()

        # Wait until the consumer has returned the buffers it can
        while ctx.consumer and not ctx.consumer.drain_done(ctx, stream):
            if loop.time() - t0 > DRAIN_TIMEOUT:
                _log(f'{stream.dev_path}: timeout waiting for the consumer '
                     'to return buffers, not stopping\n')
                stream.state = StreamState.RUNNING
                return

            await asyncio.sleep(0.05)

        loop.remove_reader(stream.cap.fd)
        stream.cap.stream_off()
        stream.state = StreamState.STOPPED
        _log(f'{stream.dev_path}: stream off\n')

    def cmd_stop(args: list[str]):
        sel_streams = parse_streams(args)
        if sel_streams is None:
            return

        for stream in sel_streams:
            if stream.state != StreamState.RUNNING:
                _log(f'{stream.id}: not running\n')
                continue

            # readvid() bypasses the consumer for a draining stream
            stream.state = StreamState.DRAINING

            asyncio.get_running_loop().create_task(do_stop(stream))

    def cmd_start(args: list[str]):
        sel_streams = parse_streams(args)
        if sel_streams is None:
            return

        loop = asyncio.get_running_loop()

        for stream in sel_streams:
            if stream.state != StreamState.STOPPED:
                _log(f'{stream.id}: not stopped\n')
                continue

            cap = stream.cap

            held = ctx.consumer.held_vbuffers(ctx, stream) if ctx.consumer else []

            for vbuf in cap.vbuffers:
                if vbuf not in held:
                    cap.queue(vbuf)

            cap.stream_on()

            loop.add_reader(cap.fd, wrapped_callbacks[stream.id])

            stream.state = StreamState.RUNNING
            _log(f'{stream.dev_path}: stream on\n')

    def on_command(buf):
        argv = buf.text.split()
        if not argv:
            return

        cmd = argv[0]

        if cmd in ('quit', 'q'):
            app.exit()
        elif cmd == 'help':
            cmd_help(argv[1:])
        elif cmd == 'status':
            cmd_status(argv[1:])
        elif cmd == 'start':
            cmd_start(argv[1:])
        elif cmd == 'stop':
            cmd_stop(argv[1:])
        else:
            _log(f'Unknown command: {cmd}\n')

    input_area = TextArea(height=1, prompt='> ', multiline=False,
                          history=FileHistory(os.path.expanduser(HISTORY_FILE)),
                          completer=WordCompleter(list(COMMANDS)),
                          complete_while_typing=False)
    input_area.accept_handler = on_command

    # Application

    kb = KeyBindings()

    @kb.add('c-c')
    @kb.add('c-d')
    def _exit(event):
        event.app.exit()

    root = HSplit([
        status_win,
        Window(height=1, char='─'),
        log_win,
        input_area,
    ])

    # stdout may already be redirected to the log view, so give
    # prompt_toolkit the real stdout to render to
    app: Application = Application(layout=Layout(root, focused_element=input_area),
                                   key_bindings=kb,
                                   full_screen=True,
                                   refresh_interval=FPS_INTERVAL,
                                   output=create_output(stdout=_real_stdout()))

    # Event handling

    def wrap_callback(callback):
        def cb():
            nonlocal cb_time

            t0 = time.perf_counter()

            if ctx.consumer:
                ctx.consumer.handle_tick(ctx)

            callback()

            cb_time += time.perf_counter() - t0

            if ctx.exit:
                app.exit()
        return cb

    # Stream id -> wrapped event callback, for (re-)adding the reader when
    # starting a stream
    wrapped_callbacks = {stream.id: wrap_callback(stream_callbacks[stream.id])
                         for stream in streams}

    async def amain():
        loop = asyncio.get_running_loop()

        stream_fds = {stream.cap.fd for stream in streams}

        # Non-stream selector entries (e.g. the DRM fd) stay registered for
        # the whole run
        for key in sel.get_map().values():
            if key.fd in stream_fds:
                continue
            loop.add_reader(key.fd, wrap_callback(key.data))

        for stream in streams:
            if stream.state == StreamState.RUNNING:
                loop.add_reader(stream.cap.fd, wrapped_callbacks[stream.id])

        try:
            await app.run_async()
        finally:
            # remove_reader is a no-op for fds that are not registered
            # (e.g. stopped streams)
            for key in sel.get_map().values():
                loop.remove_reader(key.fd)
            for stream in streams:
                loop.remove_reader(stream.cap.fd)

    global _app

    init_log()
    _app = app
    try:
        asyncio.run(amain())
    finally:
        _app = None
        _restore_stdout()
