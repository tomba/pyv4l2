from __future__ import annotations

import ctypes

from OpenGL import EGL as egl

def _print_egl_config(egl_display, config):
    attributes = {
        egl.EGL_CONFIG_ID: 'CONFIG_ID',
        egl.EGL_BUFFER_SIZE: 'BUFFER_SIZE',
        egl.EGL_RED_SIZE: 'RED_SIZE',
        egl.EGL_GREEN_SIZE: 'GREEN_SIZE',
        egl.EGL_BLUE_SIZE: 'BLUE_SIZE',
        egl.EGL_ALPHA_SIZE: 'ALPHA_SIZE',
        egl.EGL_DEPTH_SIZE: 'DEPTH_SIZE',
        egl.EGL_STENCIL_SIZE: 'STENCIL_SIZE',
        egl.EGL_SURFACE_TYPE: 'SURFACE_TYPE',
        egl.EGL_RENDERABLE_TYPE: 'RENDERABLE_TYPE'
    }

    values = {}
    for attr, name in attributes.items():
        value = ctypes.c_long()
        egl.eglGetConfigAttrib(egl_display, config, attr, value)
        values[name] = value.value

    print('EGL Config:', values)


def get_egl_string(dpy, name):
    s = egl.eglQueryString(dpy, name)
    if not s:
        return ''
    return s.decode()

class EglState:
    def __init__(self, native_display, native_visual_id=0):
        self.native_visual_id = native_visual_id

        # Initialize EGL
        self.display = egl.eglGetDisplay(native_display)
        if not self.display:
            raise RuntimeError('Failed to get EGL display')

        if not egl.eglInitialize(self.display, None, None):
            raise RuntimeError('Failed to initialize EGL')

        # Print useful debug info
        print(f'EGL_VENDOR: {get_egl_string(self.display, egl.EGL_VENDOR)}')
        print(f'EGL_VERSION: {get_egl_string(self.display, egl.EGL_VERSION)}')
        print(f'EGL_CLIENT_APIS: {get_egl_string(self.display, egl.EGL_CLIENT_APIS)}')

        # Configure attributes
        config_attribs = [
            egl.EGL_SURFACE_TYPE, egl.EGL_WINDOW_BIT,
            egl.EGL_RED_SIZE, 8,
            egl.EGL_GREEN_SIZE, 8,
            egl.EGL_BLUE_SIZE, 8,
            egl.EGL_ALPHA_SIZE, 8,
            egl.EGL_RENDERABLE_TYPE, egl.EGL_OPENGL_ES3_BIT,
            egl.EGL_NONE
        ]

        # Get all matching configs
        num_configs = ctypes.c_int()
        if not egl.eglGetConfigs(self.display, None, 0, num_configs):
            raise RuntimeError('Failed to get number of configs')

        configs = (egl.EGLConfig * num_configs.value)()
        num_matched = ctypes.c_int()
        if not egl.eglChooseConfig(self.display, config_attribs, configs, num_configs.value, num_matched):
            raise RuntimeError('Failed to choose EGL config')

        if num_matched.value < 1:
            raise RuntimeError('No matching EGL configs found')

        # Find config matching native_visual_id if specified
        self.config = None
        for cfg in configs[:num_matched.value]:
            vid = ctypes.c_long()
            if egl.eglGetConfigAttrib(self.display, cfg, egl.EGL_NATIVE_VISUAL_ID, vid):
                if vid.value == native_visual_id or not native_visual_id:
                    self.config = cfg
                    break

        if not self.config:
            raise RuntimeError('Failed to find matching EGL config')

        # Create OpenGL ES 3.0 context
        context_attribs = [
            egl.EGL_CONTEXT_CLIENT_VERSION, 3,
            egl.EGL_NONE
        ]

        if not egl.eglBindAPI(egl.EGL_OPENGL_ES_API):
            raise RuntimeError('Failed to bind OpenGL ES API')

        self.context = egl.eglCreateContext(self.display, self.config, egl.EGL_NO_CONTEXT, context_attribs)
        if not self.context:
            raise RuntimeError('Failed to create EGL context')

        # Initial make current without a surface
        if not egl.eglMakeCurrent(self.display, egl.EGL_NO_SURFACE, egl.EGL_NO_SURFACE, self.context):
            raise RuntimeError('Failed to make EGL context current')


class EglSurface:
    def __init__(self, egl_state: EglState, native_window):
        self.egl = egl_state
        self.surface = egl.eglCreateWindowSurface(self.egl.display, self.egl.config, native_window, None)
        if not self.surface:
            raise RuntimeError('Failed to create EGL surface')

    def make_current(self):
        if not egl.eglMakeCurrent(self.egl.display, self.surface, self.surface, self.egl.context):
            raise RuntimeError('Failed to make EGL context current')

    def swap_buffers(self):
        egl.eglSwapBuffers(self.egl.display, self.surface)

    def __del__(self):
        if hasattr(self, 'surface') and self.surface:
            egl.eglDestroySurface(self.egl.display, self.surface)
