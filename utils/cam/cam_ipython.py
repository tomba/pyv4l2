import selectors
import time

import IPython
from traitlets.config import Config
from pygments.token import Token

import v4l2

from cam_types import Context


def run_ipython(ctx: Context, sel: selectors.BaseSelector):
    streams = [stream for sctx in ctx.subcontexts for stream in sctx.streams]

    subdevices = {}
    for sctx in ctx.subcontexts:
        if sctx.subdevices:
            subdevices.update(sctx.subdevices)

    def inputhook(context):
        fd = context.fileno()

        ipy_key = sel.register(fd, selectors.EVENT_READ)

        loop = True
        while loop:
            events = sel.select()
            for key, _ in events:
                if key == ipy_key:
                    loop = False
                    continue

                callback = key.data
                callback()

        sel.unregister(fd)

    IPython.terminal.pt_inputhooks.register('mygui', inputhook)

    class MyPrompt(IPython.terminal.prompts.Prompts):
        def in_prompt_tokens(self, cli=None):
            ts = time.perf_counter()

            lines = []
            for stream in streams:
                diff = ts - stream.last_timestamp
                num_frames = stream.total_num_frames - stream.last_framenum

                fps = num_frames / diff if diff > 0 else 0

                stream.last_timestamp = ts
                stream.last_framenum = stream.total_num_frames

                lines.append('[{}: {} frames:{:8} fps:{:5.2f}]'
                             .format(stream.id, stream.dev_path,
                                     stream.total_num_frames, fps))

            return [
                (Token, '\n'.join(lines) + '\n'),
                (Token.Prompt, '> '),
            ]

    banner = (
        'cam IPython mode\n'
        'Scope: ctx, streams, subdevices, v4l2\n'
    )

    c = Config()
    c.InteractiveShellApp.exec_lines = [
        '%gui mygui',
    ]
    c.TerminalInteractiveShell.confirm_exit = False
    c.TerminalInteractiveShell.banner1 = banner
    c.TerminalInteractiveShell.prompts_class = MyPrompt

    scope = {
        'v4l2': v4l2,
        'ctx': ctx,
        'streams': streams,
        'subdevices': subdevices,
    }

    IPython.start_ipython(config=c, argv=[], user_ns=scope)
