from __future__ import annotations

# pyright: reportInvalidTypeForm=false

import ctypes

from OpenGL import GL as gl
from OpenGL import EGL as egl
from OpenGL.platform import PLATFORM # type: ignore
from OpenGL.EGL.KHR.image import EGLImageKHR, eglCreateImageKHR, eglDestroyImageKHR
from OpenGL.EGL.EXT import image_dma_buf_import as ext_dmabuf
from OpenGL.raw.GLES2 import _types as _cs

glEGLImageTargetTexture2DOES = ctypes.CFUNCTYPE(
    None,  # return type
    _cs.GLenum,  # target
    _cs.GLeglImageOES,  # image
)(PLATFORM.getExtensionProcedure(b'glEGLImageTargetTexture2DOES'))


def create_dmabuf_image(
    egl_display, fd: int, width: int, height: int, format: int, stride: int
) -> EGLImageKHR:
    """Create an EGLImage from a DMA-buf file descriptor."""
    attribs = (egl.EGLint * 13)(
        egl.EGL_WIDTH,
        width,
        egl.EGL_HEIGHT,
        height,
        ext_dmabuf.EGL_LINUX_DRM_FOURCC_EXT,
        format,
        ext_dmabuf.EGL_DMA_BUF_PLANE0_FD_EXT,
        fd,
        ext_dmabuf.EGL_DMA_BUF_PLANE0_OFFSET_EXT,
        0,
        ext_dmabuf.EGL_DMA_BUF_PLANE0_PITCH_EXT,
        stride,
        egl.EGL_NONE,
    )

    image = eglCreateImageKHR(
        egl_display, egl.EGL_NO_CONTEXT, ext_dmabuf.EGL_LINUX_DMA_BUF_EXT, None, attribs
    )

    if not image:
        egl_error = egl.eglGetError()
        raise RuntimeError(f'Failed to create EGLImage: error {egl_error}')

    return image

def destroy_dmabuf_image(egl_display: egl.EGLDisplay, egl_image: EGLImageKHR):
    eglDestroyImageKHR(egl_display, egl_image)

def create_texture_from_dmabuf(
    egl_display: egl.EGLDisplay, fd: int, width: int, height: int, format: int, stride: int
) -> tuple[int, EGLImageKHR]:
    """Create an OpenGL texture from a DMA-buf file descriptor."""
    # Create EGLImage from DMA-buf
    egl_image = create_dmabuf_image(egl_display, fd, width, height, format, stride)

    # Create and bind OpenGL texture
    texture = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)

    # Import EGLImage as texture
    glEGLImageTargetTexture2DOES(gl.GL_TEXTURE_2D, egl_image)

    # Set texture parameters (GL_NEAREST for RAW immage data)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)

    return texture, egl_image


def update_texture_from_dmabuf(
    egl_display: egl.EGLDisplay, texture: int, egl_image: EGLImageKHR
) -> None:
    """Update an existing OpenGL texture from a DMA-buf file descriptor."""
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
    glEGLImageTargetTexture2DOES(gl.GL_TEXTURE_2D, egl_image)
