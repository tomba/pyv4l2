from __future__ import annotations

from collections import deque
import mmap
import os
import time
import sys
import selectors
import typing

import numpy as np

import kms
from cam_types import Context, Consumer
from v4l2.videodev import VideoCaptureStreamer

# It's hard to import from the current dir... So add the current directory to PYTHONPATH
sys.path.append(os.path.dirname(__file__))

os.environ['PYOPENGL_PLATFORM'] = 'egl'

from gbm import GbmDevice, GBM_FORMAT_XRGB8888, GBM_BO_USE_SCANOUT, GBM_BO_USE_RENDERING

from grid_egl import EglState, EglSurface
from grid_gl import GlScene

import dmabuf_egl_img
from cam_gl_types import GLBuffer, GLStream

class GbmEglSurface:
    # Class-level cache of buffer objects to framebuffers
    _fb_cache = {}

    def __init__(self, card, gbm_dev: GbmDevice, egl_state: EglState, width: int, height: int):
        self.card = card
        self.egl = egl_state
        self.width = width
        self.height = height

        self.gbm_surface = gbm_dev.create_surface(
            width,
            height,
            GBM_FORMAT_XRGB8888,
            GBM_BO_USE_SCANOUT | GBM_BO_USE_RENDERING
        )

        self.egl_surface = EglSurface(self.egl, self.gbm_surface.handle)

        self.bo_prev = None
        self.bo_next = None

    def make_current(self):
        if not self.gbm_surface.has_free_buffers:
            raise RuntimeError('No free buffers')
        self.egl_surface.make_current()

    def swap_buffers(self):
        self.egl_surface.swap_buffers()

    def _create_framebuffer(self, bo):
        return kms.ExtFramebuffer(
            self.card,
            bo.width,
            bo.height,
            kms.PixelFormats.XRGB8888,
            [bo.handle],
            [bo.stride],
            [0]
        )

    def _get_fb_for_bo(self, bo):
        if bo not in self._fb_cache:
            self._fb_cache[bo] = self._create_framebuffer(bo)
        return self._fb_cache[bo]

    def lock_next(self):
        self.bo_prev = self.bo_next
        self.bo_next = self.gbm_surface.lock_front_buffer()
        if not self.bo_next:
            raise RuntimeError('Could not lock GBM buffer')

        return self._get_fb_for_bo(self.bo_next)

    def free_prev(self):
        if self.bo_prev:
            if self.bo_prev in self._fb_cache:
                del self._fb_cache[self.bo_prev]
            self.gbm_surface.release_buffer(self.bo_prev)
            self.bo_prev = None

    def __del__(self):
        if self.bo_next:
            if self.bo_next in self._fb_cache:
                del self._fb_cache[self.bo_next]
            self.gbm_surface.release_buffer(self.bo_next)


class OutputHandler:
    def __init__(self, card, gbm_dev, egl_state, connector, crtc, mode, modeb,
                 plane, gl_streams):
        self.frame_num = 0
        self.connector = connector
        self.crtc = crtc
        self.plane = plane
        self.modeb = modeb
        self.start_time = time.time()
        self.fps_frame_count = 0
        self.flip_pending = False
        self.card = crtc.card

        self.surface1 = GbmEglSurface(card, gbm_dev, egl_state, mode.hdisplay, mode.vdisplay)
        self.scene1 = GlScene(gl_streams)
        self.scene1.set_viewport(self.surface1.width, self.surface1.height)

    def setup(self):
        # Initial buffer setup
        self.surface1.make_current()
        self.surface1.swap_buffers()
        fb = self.surface1.lock_next()

        req = kms.AtomicReq(self.card)
        req.add_connector(self.connector, self.crtc)
        req.add_crtc(self.crtc, self.modeb)
        req.add_plane(self.plane, fb, self.crtc, dst=(0, 0, fb.width, fb.height))
        req.commit_sync(allow_modeset = True)

    def handle_page_flip(self, frame, cur_time):
        self.frame_num += 1
        self.fps_frame_count += 1

        #print(f'Frame {self.frame_num}')

        if self.fps_frame_count == 100:
            end_time = time.time()
            duration = end_time - self.start_time
            fps = self.fps_frame_count / duration
            print(f'FPS: {fps:.2f}')

            self.fps_frame_count = 0
            self.start_time = end_time

        self.surface1.free_prev()

        self.flip_pending = False

        self.queue_next()

    def queue_next(self):
        self.surface1.make_current()
        self.scene1.draw(self.frame_num)
        self.surface1.swap_buffers()
        fb = self.surface1.lock_next()

        req = kms.AtomicReq(self.crtc.card)
        req.add(self.plane, 'FB_ID', fb.id)
        req.commit()

        self.flip_pending = True

class GLDRMConsumer(Consumer):
    def __init__(self, ctx: Context):
        self.ctx = ctx

        # Black level and white level scaling LUT

        bl = 16 # Black level
        wl = 255 # White level
        self.lut = (np.clip((np.arange(256) - bl), 0, 255) * (255 / (wl - bl))).astype(np.uint8)

    def setup_stream(self, ctx, stream):
        # First buffer is taken by the consumer
        return True

    def setup_streams_done(self, ctx: Context):
        self.gl_streams: dict[int, GLStream] = {}

        card = kms.Card()
        res = kms.ResourceManager(card)
        conn = res.reserve_connector()
        crtc = res.reserve_crtc(conn)
        plane = res.reserve_generic_plane(crtc)
        mode = conn.get_default_mode()
        modeb = mode.to_blob(card)

        gbm_dev = GbmDevice(card.fd)
        egl_state = EglState(gbm_dev.handle)

        for sctx in ctx.subcontexts:
            for stream in sctx.streams:
                #if not stream.display:
                #    continue

                cap = typing.cast(VideoCaptureStreamer, stream.cap)
                cap.export_dmabuf_fds()

                gl_stream = GLStream()
                gl_stream.id = stream.id
                gl_stream.width = stream.w
                gl_stream.height = stream.h
                gl_stream.stride = cap.strides[0]
                gl_stream.stream = stream
                gl_stream.in_queue = deque()
                gl_stream.out_queue = deque()

                # Add initial buffer
                gl_stream.in_queue.append(0)
                gl_stream.current_buf = -1

                fmt = typing.cast(kms.PixelFormat, stream.format)
                if not fmt.drm_fourcc:
                    fmt = kms.PixelFormats.R8

                fourcc = fmt.drm_fourcc
                assert fourcc

                gl_stream.format = fmt

                gl_stream.bufs = []
                for vbuf in cap.vbuffers:
                    gl_buf = GLBuffer()
                    gl_buf.display = egl_state.display
                    gl_buf.fd = vbuf.fd
                    gl_buf.tex, gl_buf.img = dmabuf_egl_img.create_texture_from_dmabuf(egl_state.display,
                                                                                       vbuf.fd,
                                                                                       gl_stream.width, gl_stream.height,
                                                                                       fourcc,
                                                                                       gl_stream.stride)
                    gl_stream.bufs.append(gl_buf)

                self.gl_streams[stream.id] = gl_stream

        self.card = card

        out = OutputHandler(card, gbm_dev, egl_state, conn, crtc, mode, modeb,
                            plane, self.gl_streams)

        out.setup()
        out.start_time = time.time()
        out.queue_next()

        self.out = out


    def calculate_wb_coefficients(self, raw_image):
        # Black level and white level scaling with LUT
        raw_image = self.lut[raw_image]

        # Extract channels based on RGGB pattern
        R = raw_image[0::2, 0::2]
        G1 = raw_image[0::2, 1::2]
        G2 = raw_image[1::2, 0::2]
        B = raw_image[1::2, 1::2]

        # Calculate channel averages with implicit conversion to float
        R_avg = np.mean(R)
        G_avg = (np.mean(G1) + np.mean(G2)) / 2
        B_avg = np.mean(B)

        # Gray world assumption - normalize to green
        r_gain = G_avg / R_avg
        g_gain = 1.0
        b_gain = G_avg / B_avg

        #print(
        #    f'avgs: {R_avg:6.2f}, {G_avg:6.2f}, {B_avg:6.2f} coefs: {r_gain:4.2f}, {g_gain:4.2f}, {b_gain:4.2f}'
        #)

        return [r_gain, g_gain, b_gain]

    def handle_frame(self, ctx, stream, vbuf):
        gl_stream = self.gl_streams[stream.id]
        gl_stream.in_queue.append(vbuf.index)

        # Calculate white balance coefficients only for first stream
        if stream.id == 0:
            cap = typing.cast(VideoCaptureStreamer, stream.cap)
            with mmap.mmap(
                cap.fd,
                cap.framesize,
                mmap.MAP_SHARED,
                mmap.PROT_READ | mmap.PROT_WRITE,
                offset=vbuf.offset,
            ) as b:
                buf = np.frombuffer(b, dtype=np.uint8).reshape((stream.h, stream.w))
                coefs = self.calculate_wb_coefficients(buf)
                buf = None

            gl_stream.coefs = coefs

    def readdrm(self):
        for ev in self.card.read_events():
            if ev.type == kms.DrmEventType.FLIP_COMPLETE:
                if self.out.flip_pending:
                    self.out.handle_page_flip(ev.seq, ev.time)

                # return processed buffers
                for gl_stream in self.gl_streams.values():
                    while len(gl_stream.out_queue) > 0:
                        idx = gl_stream.out_queue.popleft()
                        stream = gl_stream.stream
                        cap = stream.cap
                        cap.queue(cap.vbuffers[idx])

    def register_selector(self, sel: selectors.BaseSelector):
        sel.register(self.card.fd, selectors.EVENT_READ, lambda: self.readdrm())
