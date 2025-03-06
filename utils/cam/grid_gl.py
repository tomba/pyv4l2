from __future__ import annotations

import ctypes
import os
import numpy as np

from OpenGL import GL as gl
from OpenGL.GLES2.OES.EGL_image_external import GL_TEXTURE_EXTERNAL_OES

from cam_gl_types import GLStream

MAX_TILES = 6

def check_shader_compile(shader, shader_type):
    if gl.glGetShaderiv(shader, gl.GL_COMPILE_STATUS) != gl.GL_TRUE:
        error_log = gl.glGetShaderInfoLog(shader).decode()
        raise RuntimeError(f'{shader_type} shader compilation failed:\n{error_log}')

def check_program_link(program):
    if gl.glGetProgramiv(program, gl.GL_LINK_STATUS) != gl.GL_TRUE:
        error_log = gl.glGetProgramInfoLog(program).decode()
        raise RuntimeError(f'Shader program linking failed:\n{error_log}')

def get_gl_string(name):
    s = gl.glGetString(name)
    if not s:
        return ''
    return s.decode()

def gl_dbg_callback(source, msg_type, msg_id, severity, length, raw, user):
    #print(source, msg_type, msg_id, severity, length, raw, user)
    print(f'{raw.decode().strip()}')

class GlScene:
    def __init__(self, gl_streams: dict[int, GLStream]):
        self.gl_streams = gl_streams
        self.width = 0
        self.height = 0
        self.num_tiles = len(gl_streams)

        print(f'GL_VENDOR: {get_gl_string(gl.GL_VENDOR)}')
        print(f'GL_VERSION: {get_gl_string(gl.GL_VERSION)}')
        print(f'GL_RENDERER: {get_gl_string(gl.GL_RENDERER)}')

        self.program = self._create_program()
        self.vao = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(self.vao)
        self.vbo = self._create_grid_buffer()

        if False:
            # We need to store the callback object to prevent it from being garbage collected
            self.dbg_callback_proc = gl.GLDEBUGPROC(gl_dbg_callback)
            gl.glDebugMessageCallback(self.dbg_callback_proc, None)
            gl.glEnable(gl.GL_DEBUG_OUTPUT)
            gl.glEnable(gl.GL_DEBUG_OUTPUT_SYNCHRONOUS)

        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_CULL_FACE)

    def cleanup(self):
        gl.glDeleteBuffers(1, [self.vbo])
        gl.glDeleteVertexArrays(1, [self.vao])
        gl.glDeleteProgram(self.program)

    def _create_grid_buffer(self) -> int:
        vertices = []

        # Calculate grid dimensions based on the number of tiles
        grid_width = int(np.ceil(np.sqrt(self.num_tiles)))
        grid_height = int(np.ceil(self.num_tiles / grid_width))
        cell_width = 2.0 / grid_width
        cell_height = 2.0 / grid_height

        # Generate vertices for each cell in the grid
        for row in range(grid_height):
            for col in range(grid_width):
                if row * grid_width + col >= self.num_tiles:
                    break  # Stop if we have generated all the required tiles

                x0 = -1 + col * cell_width
                y0 = -1 + row * cell_height
                x1 = x0 + cell_width
                y1 = y0 + cell_height
                tile_idx = row * grid_width + col

                # First triangle of cell
                vertices.extend([x0, y0, 0, 0, 0, tile_idx])  # v0 pos + uv + tile_idx
                vertices.extend([x1, y0, 0, 1, 0, tile_idx])  # v1 pos + uv + tile_idx
                vertices.extend([x0, y1, 0, 0, 1, tile_idx])  # v2 pos + uv + tile_idx

                # Second triangle of cell
                vertices.extend([x1, y0, 0, 1, 0, tile_idx])  # v1 pos + uv + tile_idx
                vertices.extend([x1, y1, 0, 1, 1, tile_idx])  # v3 pos + uv + tile_idx
                vertices.extend([x0, y1, 0, 0, 1, tile_idx])  # v2 pos + uv + tile_idx

        vertices = np.array(vertices, dtype=np.float32)

        vbo = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)

        # Position attribute
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 6 * 4, None)
        gl.glEnableVertexAttribArray(0)

        # Texture coordinates and tile index
        gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 6 * 4, ctypes.c_void_p(3 * 4))
        gl.glEnableVertexAttribArray(1)

        return vbo

    def _create_program(self) -> int:
        current_dir = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(current_dir, 'grid.vert')) as f:
            vertex_shader = f.read()

        with open(os.path.join(current_dir, 'grid.frag')) as f:
            fragment_shader_standard = f.read()

        with open(os.path.join(current_dir, 'grid-srggb8.frag')) as f:
            fragment_shader_srggb8 = f.read()

        RAW_MODE = True
        if RAW_MODE:
            fragment_shader = fragment_shader_srggb8
        else:
            fragment_shader = fragment_shader_standard

        # Compile vertex shader
        vs = gl.glCreateShader(gl.GL_VERTEX_SHADER)
        gl.glShaderSource(vs, vertex_shader)
        gl.glCompileShader(vs)
        check_shader_compile(vs, 'Vertex')

        # Compile fragment shader
        fs = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
        gl.glShaderSource(fs, fragment_shader)
        gl.glCompileShader(fs)
        check_shader_compile(fs, 'Fragment')

        # Create and link program
        program = gl.glCreateProgram()
        assert program
        gl.glAttachShader(program, vs)
        gl.glAttachShader(program, fs)
        gl.glLinkProgram(program)
        check_program_link(program)

        gl.glDeleteShader(vs)
        gl.glDeleteShader(fs)
        gl.glUseProgram(program)

        black_level = 16 / 255
        white_level = 1.0
        white_balance = [1.8, 1.0, 1.5]  # R, G, B (default)
        gamma = 2.2

        # Set the black level uniform
        black_level_loc = gl.glGetUniformLocation(program, 'blackLevel')
        gl.glUniform1f(black_level_loc, black_level)

        # Set the white level uniform
        white_level_loc = gl.glGetUniformLocation(program, 'whiteLevel')
        gl.glUniform1f(white_level_loc, white_level)

        # Set white balance gains
        wb_loc = gl.glGetUniformLocation(program, 'whiteBalance')
        gl.glUniform3fv(wb_loc, 1, np.array(white_balance, dtype=np.float32))
        self.wb_loc = wb_loc

        # Set the gamma uniform
        gamma_loc = gl.glGetUniformLocation(program, 'gamma')
        gl.glUniform1f(gamma_loc, gamma)

        # Set the color correction matrix uniform
        ccm_loc = gl.glGetUniformLocation(program, 'colorCorrectionMatrix')
        ccm = [
            2.18644, -0.66148, -0.52496,
            -0.77828, 2.69474, -0.91645,
            -0.25239, -0.83059, 2.08298
        ]
        gl.glUniformMatrix3fv(ccm_loc, 1, False, ccm)

        # Set up texture uniforms
        for i in range(self.num_tiles):
            location = gl.glGetUniformLocation(program, f'textures[{i}]')
            gl.glUniform1i(location, i)  # Bind texture unit i to sampler i

        return program

    def set_viewport(self, width: int, height: int):
        self.width = width
        self.height = height
        gl.glViewport(0, 0, width, height)

    def draw(self, frame_num: int):
        gl.glClearColor(0.2, 0.3, 0.3, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # type: ignore

        # Bind textures to their respective texture units
        for i, gl_stream in enumerate(self.gl_streams.values()):
            gl.glActiveTexture(int(gl.GL_TEXTURE0) + i)

            if len(gl_stream.in_queue) > 0:
                if gl_stream.current_buf != -1:
                    gl_stream.out_queue.append(gl_stream.current_buf)
                new_buf = gl_stream.in_queue.popleft()
                gl_stream.current_buf = new_buf

            cur_idx = gl_stream.current_buf
            texture = gl_stream.bufs[cur_idx].tex

            gl.glBindTexture(GL_TEXTURE_EXTERNAL_OES, texture)

        # Use wb coefficients from the first stream for all streams
        if hasattr(self.gl_streams[0], 'coefs'):
            coefs = self.gl_streams[0].coefs
            gl.glUniform3fv(self.wb_loc, 1, coefs)

        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3 * 2 * self.num_tiles)
