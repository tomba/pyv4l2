from __future__ import annotations

from collections import deque
from selectors import BaseSelector, EVENT_READ
import time

import kms
import v4l2

from cam_types import Stream, Context, Consumer

class KmsStream:
    stream: Stream
    kms_buf_w: int
    kms_buf_h: int
    kms_format: kms.PixelFormat
    kms_src_w: int
    kms_src_h: int
    kms_src_x: int
    kms_src_y: int
    kms_dst_w: int
    kms_dst_h: int
    kms_dst_x: int
    kms_dst_y: int
    kms_old_fb: kms.DumbFramebuffer | None
    kms_fb: kms.DumbFramebuffer
    kms_fb_queue: deque
    plane: kms.Plane

class KmsContext:
    def __init__(self, ctx: Context) -> None:
        self.ctx = ctx
        self.kms_committed = False

        self.kms_streams: dict[int, KmsStream] = {}

        for sctx in ctx.subcontexts:
            for stream in sctx.streams:
                if not stream.display:
                    continue

                kms_stream = KmsStream()
                kms_stream.stream = stream
                self.kms_streams[stream.id] = kms_stream

        card = kms.Card()

        self.card = card

        res = None
        crtc = None
        mode = None
        if ctx.use_display:
            res = kms.ResourceManager(card)
            conn = res.reserve_connector()
            crtc = res.reserve_crtc(conn)
            mode = conn.get_default_mode()
            modeb = mode.to_blob(card)

            self.crtc = crtc
            self.conn = conn
            self.modeb = modeb

        num_planes = len(self.kms_streams) if ctx.use_display else 0

        display_idx = 0

        for kms_stream in self.kms_streams.values():
            stream = kms_stream.stream

            if isinstance(stream.size, int):
                kms_stream.kms_buf_w = stream.size
                kms_stream.kms_buf_h = 1
            else:
                kms_stream.kms_buf_w = stream.w
                kms_stream.kms_buf_h = stream.h

            if not hasattr(stream, 'kms_format'):
                if isinstance(stream.format, v4l2.MetaFormat):
                    raise RuntimeError('No KMS format specified')

                kms_stream.kms_format = stream.format
            else:
                kms_stream.kms_format = stream.kms_format

            if not kms_stream.kms_format.drm_fourcc:
                raise RuntimeError('No KMS format available or specified')

            if stream.format != kms_stream.kms_format:
                if (isinstance(stream.format, v4l2.PixelFormat) and
                    len(stream.format.planes) > 1):
                    raise RuntimeError('Unable to adjust formats with more than one plane')

                print(f'Aligning V4L2 and KMS formats: {stream.format}, {kms_stream.kms_format}')

                kms_w = kms_stream.kms_buf_w

                if isinstance(stream.format, v4l2.MetaFormat):
                    v4l2_stride = stream.format.stride(kms_w)
                else:
                    v4l2_stride = stream.format.stride(kms_w, plane=0)

                kms_stride = kms_stream.kms_format.stride(kms_w, plane=0)

                if kms_stride % v4l2_stride == 0:
                    kms_stream.kms_buf_w //= kms_stride // v4l2_stride
                else:
                    raise RuntimeError('Unable to adjust formats')

                if kms_w != kms_stream.kms_buf_w:
                    print(f'Adjusted kms width from {kms_w} to {kms_stream.kms_buf_w}')

            if ctx.buf_type == 'drm' and stream.embedded:
                divs = [16, 8, 4, 2, 1]
                div = None
                w = None
                for div in divs:
                    w = kms_stream.kms_buf_w // div
                    if w % 2 == 0:
                        break

                assert div is not None
                assert w is not None

                h = kms_stream.kms_buf_h * div

                kms_stream.kms_buf_w = w
                kms_stream.kms_buf_h = h

            if stream.display:
                assert mode is not None
                max_w = mode.hdisplay // (1 if num_planes == 1 else 2)
                max_h = mode.vdisplay // (1 if num_planes <= 2 else 2)

                kms_stream.kms_src_w = min(kms_stream.kms_buf_w, max_w)
                kms_stream.kms_src_h = min(kms_stream.kms_buf_h, max_h)
                kms_stream.kms_src_x = (kms_stream.kms_buf_w - kms_stream.kms_src_w) // 2
                kms_stream.kms_src_y = (kms_stream.kms_buf_h - kms_stream.kms_src_h) // 2

                kms_stream.kms_dst_w  =kms_stream.kms_src_w
                kms_stream.kms_dst_h = kms_stream.kms_src_h

                if display_idx % 2 == 0:
                    kms_stream.kms_dst_x = 0
                else:
                    kms_stream.kms_dst_x = mode.hdisplay - kms_stream.kms_dst_w

                if display_idx // 2 == 0:
                    kms_stream.kms_dst_y = 0
                else:
                    kms_stream.kms_dst_y = mode.vdisplay - kms_stream.kms_dst_h

                display_idx += 1

                assert res is not None
                assert crtc is not None
                plane = res.reserve_generic_plane(crtc, kms_stream.kms_format)
                assert(plane)
                kms_stream.plane = plane

    def alloc_fbs(self, stream: Stream):
        # XXX I don't think alloc works for drm buffers that are not displayed (e.g. embedded)
        kms_stream = self.kms_streams[stream.id]

        fbs = []
        cap = stream.cap
        for i in range(stream.num_bufs):
            fb = kms.DumbFramebuffer(self.card, kms_stream.kms_buf_w, kms_stream.kms_buf_h, kms_stream.kms_format)
            fbs.append(fb)

            if isinstance(cap.format, v4l2.PixelFormat):
                for pi in range(len(cap.format.planes)):
                    assert cap.strides[pi] == fb.planes[pi].pitch, f'{cap.strides[pi]}, {fb.planes[pi].pitch}'
                    assert cap.buffersizes[pi] == fb.planes[pi].size
            else:
                pass

        stream.fbs = fbs

    def setup_stream(self, stream: Stream):
        kms_stream = self.kms_streams[stream.id]

        ctx = self.ctx

        assert(ctx.buf_type == 'drm')

        # Set fb0 to screen
        fb = stream.fbs[0]
        plane = kms_stream.plane

        plane.set_props({
            'FB_ID': fb.id,
            'CRTC_ID': self.crtc.id,
            'SRC_X': kms_stream.kms_src_x << 16,
            'SRC_Y': kms_stream.kms_src_y << 16,
            'SRC_W': kms_stream.kms_src_w << 16,
            'SRC_H': kms_stream.kms_src_h << 16,
            'CRTC_X': kms_stream.kms_dst_x,
            'CRTC_Y': kms_stream.kms_dst_y,
            'CRTC_W': kms_stream.kms_dst_w,
            'CRTC_H': kms_stream.kms_dst_h,
        })

        kms_stream.kms_old_fb = None
        kms_stream.kms_fb = fb
        kms_stream.kms_fb_queue = deque()


    def init_modeset(self):
        ctx = self.ctx

        # Do the initial modeset
        req = kms.AtomicReq(self.card)
        req.add(self.conn, 'CRTC_ID', self.crtc.id)
        req.add(self.crtc, {'ACTIVE': 1,
                'MODE_ID': self.modeb.id})

        for kms_stream in self.kms_streams.values():
            req.add(kms_stream.plane, 'FB_ID', kms_stream.kms_fb.id)

        req.commit_sync(allow_modeset = True)

        if ctx.delay:
            print(f'Waiting for {ctx.delay} seconds')
            time.sleep(ctx.delay)


    def handle_pageflip(self):
        ctx = self.ctx

        assert ctx.buf_type == 'drm'

        self.kms_committed = False

        req = kms.AtomicReq(self.card)

        do_commit = False

        for kms_stream in self.kms_streams.values():
            stream = kms_stream.stream

            #print(f'Page flip {stream.dev_path}: kms_fb_queue {len(stream.kms_fb_queue)}, new_fb {stream.kms_fb}, old_fb {stream.kms_old_fb}')

            cap = stream.cap

            if kms_stream.kms_old_fb:
                fb = kms_stream.kms_old_fb

                # XXX we should just track the vbufs in streams, instead of looking
                # for the vbuf based on the drm fb
                vbuf = next(vbuf for vbuf in cap.vbuffers if vbuf.fd == fb.fd(0))

                cap.queue(vbuf)
                kms_stream.kms_old_fb = None

            if len(kms_stream.kms_fb_queue) == 0:
                continue

            kms_stream.kms_old_fb = kms_stream.kms_fb

            fb = kms_stream.kms_fb_queue.popleft()
            kms_stream.kms_fb = fb

            plane = kms_stream.plane

            req.add(plane, 'FB_ID', fb.id)

            do_commit = True

        if do_commit:
            req.commit(allow_modeset = False)
            self.kms_committed = True

    def readdrm(self):
        #print('EVENT')
        for ev in self.card.read_events():
            if ev.type == kms.DrmEventType.FLIP_COMPLETE:
                self.handle_pageflip()

    def register_selector(self, sel: BaseSelector):
        sel.register(self.card.fd, EVENT_READ, lambda: self.readdrm())

class DisplayConsumer(Consumer):
    def __init__(self, ctx: Context):
        self.kms_ctx = KmsContext(ctx)

    def alloc_buffers(self, ctx: Context, stream: Stream):
        if ctx.buf_type == 'drm':
            self.kms_ctx.alloc_fbs(stream)

    def setup_stream(self, ctx: Context, stream: Stream):
        if stream.display:
            self.kms_ctx.setup_stream(stream)

    def setup_streams_done(self, ctx: Context):

        if ctx.use_display:
            self.kms_ctx.init_modeset()

    def handle_frame(self, ctx: Context, stream: Stream, vbuf):
        if stream.id not in self.kms_ctx.kms_streams:
            return

        kms_stream = self.kms_ctx.kms_streams[stream.id]

        fb = None

        if ctx.buf_type == 'drm':
            fb = next((fb for fb in stream.fbs if fb.fd(0) == vbuf.fd), None)
            assert fb is not None

        assert fb is not None
        kms_stream.kms_fb_queue.append(fb)

        if len(kms_stream.kms_fb_queue) >= stream.num_bufs - 1:
            print('WARNING fb_queue {}'.format(len(kms_stream.kms_fb_queue)))

        if not self.kms_ctx.kms_committed:
            self.kms_ctx.handle_pageflip()

    def cleanup(self, ctx: Context):
        pass

    def register_selector(self, sel: BaseSelector):
        self.kms_ctx.register_selector(sel)
