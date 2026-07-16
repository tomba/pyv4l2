from __future__ import annotations

import asyncio
import os
import selectors
import sys
import time

from prompt_toolkit.application import Application
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.document import Document
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import HSplit, Layout, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import TextArea

from cam_types import Context

HISTORY_FILE = '~/.cam_history'
FPS_INTERVAL = 0.5

COMMANDS = {
    'help': 'show this help',
    'quit': 'exit (also: q, ctrl-c, ctrl-d)',
}


def run_tui(ctx: Context, sel: selectors.BaseSelector):
    streams = [stream for sctx in ctx.subcontexts for stream in sctx.streams]

    # Status pane

    fps_cache: dict[int, float] = {}

    def get_status():
        ts = time.perf_counter()

        lines = []
        for stream in streams:
            diff = ts - stream.last_timestamp
            if diff >= FPS_INTERVAL:
                num_frames = stream.total_num_frames - stream.last_framenum
                fps_cache[stream.id] = num_frames / diff
                stream.last_timestamp = ts
                stream.last_framenum = stream.total_num_frames

            lines.append('{}: {} frames:{:8} fps:{:6.2f}'
                         .format(stream.id, stream.dev_path,
                                 stream.total_num_frames,
                                 fps_cache.get(stream.id, 0)))

        return '\n'.join(lines)

    status_win = Window(FormattedTextControl(get_status),
                        height=len(streams), style='reverse')

    # Log area

    log_area = TextArea(read_only=True, scrollbar=True, wrap_lines=True)

    def log(text: str):
        doc = Document(log_area.text + text,
                       cursor_position=len(log_area.text) + len(text))
        log_area.buffer.set_document(doc, bypass_readonly=True)

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
                          completer=WordCompleter(list(COMMANDS)))
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
        log_area,
        input_area,
    ])

    app: Application = Application(layout=Layout(root, focused_element=input_area),
                                   key_bindings=kb,
                                   full_screen=True,
                                   refresh_interval=FPS_INTERVAL)

    # Event handling

    def wrap_callback(callback):
        def cb():
            if ctx.consumer:
                ctx.consumer.handle_tick(ctx)

            callback()

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
