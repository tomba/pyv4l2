from __future__ import annotations
from collections import deque

import kms
from cam_types import Stream

import sys
import os

# It's hard to import from the current dir... So add the current directory to PYTHONPATH
sys.path.append(os.path.dirname(__file__))

os.environ['PYOPENGL_PLATFORM'] = 'egl'

from OpenGL import EGL as egl

import dmabuf_egl_img

class GLBuffer:
    display: egl.EGLDisplay
    fd: int
    tex: int
    img: egl.EGLImageKHR
    vbuf_offset: int

    def update(self):
        dmabuf_egl_img.update_texture_from_dmabuf(self.display, self.tex, self.img)

class GLStream:
    id: int
    stream: Stream
    format: kms.PixelFormat
    width: int
    height: int
    stride: int
    bufs: list[GLBuffer]
    current_buf: int
    in_queue: deque[int]
    out_queue: deque[int]
    cap: VideoCaptureStreamer
