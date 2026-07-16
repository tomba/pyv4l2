from __future__ import annotations

import asyncio
import os
import selectors
import sys
import time
from collections import deque

from prompt_toolkit.application import Application
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import HSplit, Layout, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import TextArea

from cam_types import Context

HISTORY_FILE = '~/.cam_history'
FPS_INTERVAL = 1

COMMANDS = {
    'help': 'show this help',
    'quit': 'exit (also: q, ctrl-c, ctrl-d)',
}


def run_tui(ctx: Context, sel: selectors.BaseSelector):
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

            lines.append('{} frames:{:8} fps:{:6.2f}'
                         .format(stream_descs[stream.id],
                                 stream.total_num_frames, fps))

        status = '\n'.join(lines)
        return status

    status_win = Window(FormattedTextControl(get_status),
                        height=len(streams) + 1, style='reverse')

    # Log area
    #
    # A TextArea is far too heavy to render on slow devices, so use a plain
    # FormattedTextControl over a deque of lines, scrolled to the tail.

    log_lines: deque[str] = deque(maxlen=1000)
    log_partial = ''  # incomplete (not newline-terminated) last line

    def get_log():
        return '\n'.join(log_lines) + '\n' + log_partial

    def log_vscroll(window):
        info = window.render_info
        if info is None:
            return 0
        return max(0, len(log_lines) + 1 - info.window_height)

    log_win = Window(FormattedTextControl(get_log), wrap_lines=False,
                     get_vertical_scroll=log_vscroll)

    def log(text: str):
        nonlocal log_partial

        text = log_partial + text
        lines = text.split('\n')
        log_partial = lines.pop()
        log_lines.extend(lines)

        app.invalidate()

    # In full-screen mode stray prints would be lost (alternate screen), so
    # redirect stdout to the log area while the TUI runs.
    class LogWriter:
        def write(self, s: str):
            log(s)
            return len(s)

        def flush(self):
            pass

    # Command input

    def cmd_help(_args: list[str]):
        for name, desc in COMMANDS.items():
            log(f'{name:12} {desc}\n')

    def on_command(buf):
        argv = buf.text.split()
        if not argv:
            return

        cmd = argv[0]

        if cmd in ('quit', 'q'):
            app.exit()
        elif cmd == 'help':
            cmd_help(argv[1:])
        else:
            log(f'Unknown command: {cmd}\n')

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

    app: Application = Application(layout=Layout(root, focused_element=input_area),
                                   key_bindings=kb,
                                   full_screen=True,
                                   refresh_interval=FPS_INTERVAL)

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

    async def amain():
        loop = asyncio.get_running_loop()

        fds = []
        for key in sel.get_map().values():
            loop.add_reader(key.fd, wrap_callback(key.data))
            fds.append(key.fd)

        try:
            await app.run_async()
        finally:
            for fd in fds:
                loop.remove_reader(fd)

    old_stdout = sys.stdout
    sys.stdout = LogWriter()
    try:
        asyncio.run(amain())
    finally:
        sys.stdout = old_stdout
