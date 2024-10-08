from collections import deque
import selectors
import time

import kms
import v4l2

class KmsContext:
    def __init__(self, ctx) -> None:
        self.ctx = ctx

        streams = ctx.streams

        card = kms.Card()

        self.card = card

        if ctx.use_display:
            res = kms.ResourceManager(card)
            conn = res.reserve_connector()
            crtc = res.reserve_crtc(conn)
            card.disable_planes()
            mode = conn.get_default_mode()
            modeb = kms.Blob(card, mode)

            self.crtc = crtc
            self.conn = conn
            self.modeb = modeb

        num_planes = sum(1 for stream in streams if ctx.use_display and stream.get('display', True))

        display_idx = 0

        for stream in streams:
            if 'size' in stream:
                # It's metadata, we use RGB565 for it, so divide by 2
                stream['kms-buf-w'] = stream['size'] // 2
                stream['kms-buf-h'] = 1
            else:
                stream['kms-buf-w'] = stream['w']
                stream['kms-buf-h'] = stream['h']

            if stream.get('dra-plane-hack', False):
                # Hack to reserve the unscaleable GFX plane
                res.reserve_generic_plane(crtc, v4l2.PixelFormats.RGB565)

            # If we don't have a DRM fmt, just fall back to RGB565
            if isinstance(stream['format'], v4l2.MetaFormat) or not stream['format'].drm_fourcc:
                stream['kms-format'] = v4l2.PixelFormats.RGB565
            else:
                stream['kms-format'] = stream['format']

            if ctx.buf_type == 'drm' and stream.get('embedded', False):
                divs = [16, 8, 4, 2, 1]
                for div in divs:
                    w = stream['kms-buf-w'] // div
                    if w % 2 == 0:
                        break

                h = stream['kms-buf-h'] * div

                stream['kms-buf-w'] = w
                stream['kms-buf-h'] = h

            if stream['display']:
                max_w = mode.hdisplay // (1 if num_planes == 1 else 2)
                max_h = mode.vdisplay // (1 if num_planes <= 2 else 2)

                stream['kms-src-w'] = min(stream['kms-buf-w'], max_w)
                stream['kms-src-h'] = min(stream['kms-buf-h'], max_h)
                stream['kms-src-x'] = (stream['kms-buf-w'] - stream['kms-src-w']) // 2
                stream['kms-src-y'] = (stream['kms-buf-h'] - stream['kms-src-h']) // 2

                stream['kms-dst-w']  =stream['kms-src-w']
                stream['kms-dst-h'] = stream['kms-src-h']

                if display_idx % 2 == 0:
                    stream['kms-dst-x'] = 0
                else:
                    stream['kms-dst-x'] = mode.hdisplay - stream['kms-dst-w']

                if display_idx // 2 == 0:
                    stream['kms-dst-y'] = 0
                else:
                    stream['kms-dst-y'] = mode.vdisplay - stream['kms-dst-h']

                display_idx += 1

                plane = res.reserve_generic_plane(crtc, stream['kms-format'])
                assert(plane)
                stream['plane'] = plane

    def alloc_fbs(self, stream):
        fbs = []
        cap = stream['cap']
        for i in range(stream['num_bufs']):
            fb = kms.DumbFramebuffer(self.card, stream['kms-buf-w'], stream['kms-buf-h'], stream['kms-format'])
            fbs.append(fb)

            for i in range(len(cap.format.planes)):
                assert cap.strides[i] == fb.planes[i].pitch
                assert cap.buffersizes[i] == fb.planes[i].size

        stream['fbs'] = fbs

    def setup_stream(self, stream):
        ctx = self.ctx

        assert(ctx.buf_type == 'drm')

        # Set fb0 to screen
        fb = stream['fbs'][0]
        plane = stream['plane']

        plane.set_props({
            'FB_ID': fb.id,
            'CRTC_ID': self.crtc.id,
            'SRC_X': stream['kms-src-x'] << 16,
            'SRC_Y': stream['kms-src-y'] << 16,
            'SRC_W': stream['kms-src-w'] << 16,
            'SRC_H': stream['kms-src-h'] << 16,
            'CRTC_X': stream['kms-dst-x'],
            'CRTC_Y': stream['kms-dst-y'],
            'CRTC_W': stream['kms-dst-w'],
            'CRTC_H': stream['kms-dst-h'],
        })

        stream['kms_old_fb'] = None
        stream['kms_fb'] = fb
        stream['kms_fb_queue'] = deque()


    def init_modeset(self):
        ctx = self.ctx

        streams = ctx.streams

        # Do the initial modeset
        req = kms.AtomicReq(self.card)
        req.add(self.conn, 'CRTC_ID', self.crtc.id)
        req.add(self.crtc, {'ACTIVE': 1,
                'MODE_ID': self.modeb.id})

        for stream in streams:
            if 'plane' in stream:
                req.add(stream['plane'], 'FB_ID', stream['kms_fb'].id)

        req.commit_sync(allow_modeset = True)

        if ctx.delay:
            print(f'Waiting for {ctx.delay} seconds')
            time.sleep(ctx.delay)


    def handle_pageflip(self):
        ctx = self.ctx

        streams = ctx.streams

        ctx.kms_committed = False

        req = kms.AtomicReq(self.card)

        do_commit = False

        for stream in streams:
            if not stream['display']:
                continue

            #print(f'Page flip {stream['dev_path']}: kms_fb_queue {len(stream['kms_fb_queue'])}, new_fb {stream['kms_fb']}, old_fb {stream['kms_old_fb']}')

            cap = stream['cap']

            if stream['kms_old_fb']:
                assert(ctx.buf_type == 'drm')

                fb = stream['kms_old_fb']

                # XXX we should just track the vbufs in streams, instead of looking
                # for the vbuf based on the drm fb
                vbuf = next(vbuf for vbuf in cap.vbuffers if vbuf.fd == fb.fd(0))

                cap.queue(vbuf)
                stream['kms_old_fb'] = None

            if len(stream['kms_fb_queue']) == 0:
                continue

            stream['kms_old_fb'] = stream['kms_fb']

            fb = stream['kms_fb_queue'].popleft()
            stream['kms_fb'] = fb

            plane = stream['plane']

            req.add(plane, 'FB_ID', fb.id)

            do_commit = True

        if do_commit:
            req.commit(allow_modeset = False)
            ctx.kms_committed = True

    def readdrm(self):
        #print('EVENT')
        for ev in self.card.read_events():
            if ev.type == kms.DrmEventType.FLIP_COMPLETE:
                self.handle_pageflip()

    def register_selector(self, sel):
        sel.register(self.card.fd, selectors.EVENT_READ, lambda: self.readdrm())
