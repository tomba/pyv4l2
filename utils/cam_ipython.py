import IPython
from traitlets.config import Config
import time
import selectors

import v4l2
import v4l2.uapi

def run_ipython(ctx, sel):
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

    import IPython
    from traitlets.config import Config

    IPython.terminal.pt_inputhooks.register('mygui', inputhook)

    from pygments.token import Token

    class MyPrompt(IPython.terminal.prompts.Prompts):
        def in_prompt_tokens(self, cli=None):
            # TODO: handle all streams

            stream = ctx.streams[0]

            ts = time.perf_counter()

            diff = ts - stream['last_timestamp']
            num_frames = stream['total_num_frames'] - stream['last_framenum']

            fps = num_frames / diff

            fps_str = '[frames:{:8} fps:{:5.2f}]\n'.format(ctx.streams[0]['total_num_frames'], fps)

            stream['last_timestamp'] = ts
            stream['last_framenum'] = stream['total_num_frames']

            return [
                (Token, fps_str),
                (Token.Prompt, '> '),
            ]

    print('Starting IPython')

    def set_crop(x, y, w, h):
        import v4l2.uapi # XXX
        ctx.subdevices['rkisp1_resizer_mainpath'].set_selection(v4l2.uapi.V4L2_SEL_TGT_CROP, (x, y, w, h), pad=0)

    if True:
        c = Config()
        c.InteractiveShellApp.exec_lines = [
            '%gui mygui',
        ]
        c.TerminalInteractiveShell.confirm_exit = False
        c.TerminalInteractiveShell.banner1 = ''
        c.TerminalInteractiveShell.prompts_class = MyPrompt

        scope = {
            'v4l2': v4l2,
            'streams': ctx.streams,
            'subdevices': ctx.subdevices,
            'set_crop': set_crop,
        }

        IPython.start_ipython(config=c, argv=[], user_ns=scope)
    else:
        c = Config()
        c.InteractiveShellEmbed.confirm_exit = False
        c.InteractiveShellEmbed.banner1 = ''
        IPython.embed(config=c)
