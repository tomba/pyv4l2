from __future__ import annotations

import ctypes
import mmap
import os
import numpy as np
from OpenGL import GL as gl
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

class GlScene:
    def __init__(self, gl_streams: dict[int, GLStream]):
        self.gl_streams = gl_streams
        self.width = 0
        self.height = 0
        self.num_tiles = len(gl_streams)

        print(f'GL_VENDOR: {get_gl_string(gl.GL_VENDOR)}')
        print(f'GL_VERSION: {get_gl_string(gl.GL_VERSION)}')
        print(f'GL_RENDERER: {get_gl_string(gl.GL_RENDERER)}')

        # Create and bind textures before creating the program
        self.textures = self._create_test_textures()
        self.program = self._create_program()
        self.vao = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(self.vao)
        self.vbo = self._create_grid_buffer()

        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_CULL_FACE)

    def cleanup(self):
        gl.glDeleteBuffers(1, [self.vbo])
        gl.glDeleteVertexArrays(1, [self.vao])
        gl.glDeleteTextures(len(self.textures), self.textures)
        gl.glDeleteProgram(self.program)

    def _create_test_textures(self) -> list[int]:
        def create_test_texture(seq: int) -> int:
            # For testing, create a procedural checkerboard texture
            size = 256
            img_data = np.zeros((size, size, 3), dtype=np.uint8)
            for i in range(size):
                for j in range(size):
                    if (i + j) % (seq + 1) == 0:
                        img_data[i, j] = [255, 255, 255]
                    else:
                        img_data[i, j] = [128, 128, 128]

            # Create texture object
            texture = gl.glGenTextures(1)
            gl.glBindTexture(gl.GL_TEXTURE_2D, texture)

            # Set texture parameters
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

            # Upload texture data
            gl.glTexImage2D(
                gl.GL_TEXTURE_2D, 0, gl.GL_RGB, size, size, 0,
                gl.GL_RGB, gl.GL_UNSIGNED_BYTE, img_data
            )

            return texture

        textures = []
        for i in range(self.num_tiles):
            textures.append(create_test_texture(i))

        return textures

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

        # Set the black level uniform
        black_level = 0.1
        black_level_loc = gl.glGetUniformLocation(program, 'blackLevel')
        gl.glUniform1f(black_level_loc, black_level)

        # Set white balance gains
        white_balance = [1.8, 1.0, 1.5] # R, G, B
        wb_loc = gl.glGetUniformLocation(program, 'whiteBalance')
        gl.glUniform3fv(wb_loc, 1, np.array(white_balance, dtype=np.float32))
        self.wb_loc = wb_loc

        # Set up texture uniforms
        for i in range(self.num_tiles):
            location = gl.glGetUniformLocation(program, f'textures[{i}]')
            gl.glUniform1i(location, i)  # Bind texture unit i to sampler i

        return program

    def set_viewport(self, width: int, height: int):
        self.width = width
        self.height = height
        gl.glViewport(0, 0, width, height)

    def calculate_white_balance(self, bayer_data, black_level=0.1, white_level=1.0, subsample=True):
        """
        Calculate white balance multipliers from a Bayer RGGB image

        Args:
            bayer_data: NumPy array containing raw Bayer data
            black_level: The black level to subtract (normalized 0-1)
            white_level: The white level (normalized 0-1)
            subsample: Whether to subsample the image for efficiency

        Returns:
            List of [r_multiplier, g_multiplier, b_multiplier]
        """
        # Ensure we're working with a numpy array
        bayer_data = np.asarray(bayer_data)

        # Get shape and possibly subsample for efficiency
        height, width = bayer_data.shape[:2]

        if subsample and (width > 1000 or height > 1000):
            # Only process a subset of pixels for large images
            step = max(1, min(width, height) // 500)  # Aim for ~500px in smallest dimension
            bayer_data = bayer_data[::step, ::step]
            height, width = bayer_data.shape[:2]

        # Create masks for different Bayer positions
        r_mask = np.zeros((height, width), dtype=bool)
        g1_mask = np.zeros((height, width), dtype=bool)
        g2_mask = np.zeros((height, width), dtype=bool)
        b_mask = np.zeros((height, width), dtype=bool)

        # RGGB pattern:
        # R G R G ...
        # G B G B ...
        # R G R G ...
        r_mask[0::2, 0::2] = True  # R: even rows, even cols
        g1_mask[0::2, 1::2] = True  # G1: even rows, odd cols
        g2_mask[1::2, 0::2] = True  # G2: odd rows, even cols
        b_mask[1::2, 1::2] = True  # B: odd rows, odd cols

        # Extract values for each channel
        # Apply black level subtraction and normalization
        norm_factor = 1.0 / (white_level - black_level)

        # Handle potential data formats (float 0-1, uint8 0-255, uint16 0-65535)
        data = bayer_data.astype(np.float32)
        if data.max() > 1.1:  # Not in 0-1 range
            if data.max() > 300:  # Likely 10-bit, 12-bit, 14-bit, 16-bit
                data = data / 65535.0
            else:  # Likely 8-bit
                data = data / 255.0

        # Apply black level subtraction
        data = np.maximum(0.0, (data - black_level) * norm_factor)

        # Filter out extremely dark and bright pixels (optional)
        valid_range = (data > 0.05) & (data < 0.95)

        # Get average values for each channel
        r_values = data[r_mask & valid_range]
        g1_values = data[g1_mask & valid_range]
        g2_values = data[g2_mask & valid_range]
        b_values = data[b_mask & valid_range]

        # Combine G1 and G2
        g_values = np.concatenate([g1_values, g2_values])

        # Calculate averages, with safety checks
        r_avg = np.mean(r_values) if len(r_values) > 0 else 1.0
        g_avg = np.mean(g_values) if len(g_values) > 0 else 1.0
        b_avg = np.mean(b_values) if len(b_values) > 0 else 1.0

        # Calculate multipliers
        if g_avg < 0.001:  # Protect against division by zero
            return [1.8, 1.0, 1.5]  # Default values

        r_multiplier = g_avg / r_avg if r_avg > 0.001 else 1.8
        b_multiplier = g_avg / b_avg if b_avg > 0.001 else 1.5

        # Clamp to reasonable values
        r_multiplier = min(3.0, max(0.3, r_multiplier))
        b_multiplier = min(3.0, max(0.3, b_multiplier))

        print(f'WB Multipliers: R={r_multiplier:.2f}, G=1.00, B={b_multiplier:.2f}')

        return [r_multiplier, 1.0, b_multiplier]


    def calculate_simple_white_balance(self):
        gl_stream = self.gl_streams[0]
        cap = gl_stream.cap
        gl_buf = gl_stream.bufs[gl_stream.current_buf]

        with mmap.mmap(
            cap.fd,
            cap.framesize,
            mmap.MAP_SHARED,
            mmap.PROT_READ | mmap.PROT_WRITE,
            offset=gl_buf.vbuf_offset,
        ) as b:
                buf = np.frombuffer(b, dtype=np.uint8).reshape((gl_stream.height, gl_stream.width))
                ret = self.calculate_white_balance(buf)
                buf = None
                return ret

        return [1, 1, 1]

        r_values, g_values, b_values = [], [], []

        # Create a temporary framebuffer
        fbo = gl.glGenFramebuffers(1)
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, fbo)

        for i, gl_stream in enumerate(self.gl_streams.values()):
            if gl_stream.current_buf == -1:
                continue

            texture = gl_stream.bufs[gl_stream.current_buf].tex

            # Get texture size
            gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
            width = gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_2D, 0, gl.GL_TEXTURE_WIDTH)
            height = gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_2D, 0, gl.GL_TEXTURE_HEIGHT)

            # Attach texture to framebuffer
            gl.glFramebufferTexture2D(
                gl.GL_FRAMEBUFFER, gl.GL_COLOR_ATTACHMENT0, gl.GL_TEXTURE_2D, texture, 0
            )

            # Check framebuffer status
            status = gl.glCheckFramebufferStatus(gl.GL_FRAMEBUFFER)
            if status != gl.GL_FRAMEBUFFER_COMPLETE:
                print(f'Framebuffer incomplete: {status}')
                continue

            # Read a downsampled version by striding through the pixels
            # (For large textures, you might want to actually downsample)
            sample_step = max(1, min(width, height) // 64)  # Aim for ~64 samples in smallest dimension

            for y_sample in range(0, height, sample_step):
                for x_sample in range(0, width, sample_step):
                    # Read a single pixel
                    pixel_data = np.zeros((1, 1, 4), dtype=np.float32)
                    gl.glReadPixels(x_sample, y_sample, 1, 1, gl.GL_RGBA, gl.GL_FLOAT, pixel_data)

                    value = pixel_data[0, 0, 0]  # Assuming R channel contains the raw value

                    # Apply black level subtraction
                    value = max(0.0, (value - 0.1) / 0.9)  # Use your black/white levels

                    # Determine Bayer pixel type based on coordinates
                    if y_sample % 2 == 0:
                        if x_sample % 2 == 0:
                            r_values.append(value)  # Red
                        else:
                            g_values.append(value)  # Green in red row
                    else:
                        if x_sample % 2 == 0:
                            g_values.append(value)  # Green in blue row
                        else:
                            b_values.append(value)  # Blue

        # Clean up
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, 0)
        gl.glDeleteFramebuffers(1, [fbo])

        # Calculate averages
        r_avg = np.mean(r_values) if r_values else 1.0
        g_avg = np.mean(g_values) if g_values else 1.0
        b_avg = np.mean(b_values) if b_values else 1.0

        # Calculate multipliers (with safety checks)
        r_multiplier = min(2.5, max(0.5, g_avg / r_avg)) if r_avg > 0.01 else 1.8
        b_multiplier = min(2.5, max(0.5, g_avg / b_avg)) if b_avg > 0.01 else 1.5

        print(f'WB Multipliers: R={r_multiplier:.2f}, G=1.00, B={b_multiplier:.2f}')

        return [r_multiplier, 1.0, b_multiplier]

    def draw(self, frame_num: int):
        gl.glClearColor(0.2, 0.3, 0.3, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # type: ignore

        # Bind textures to their respective texture units
        for i, gl_stream in enumerate(self.gl_streams.values()):
            gl.glActiveTexture(gl.GL_TEXTURE0 + i)

            if len(gl_stream.in_queue) > 0:
                if gl_stream.current_buf != -1:
                    gl_stream.out_queue.append(gl_stream.current_buf)
                new_buf = gl_stream.in_queue.popleft()
                gl_stream.current_buf = new_buf

                gl_stream.bufs[new_buf].update()

            cur_idx = gl_stream.current_buf
            texture = gl_stream.bufs[cur_idx].tex

            gl.glBindTexture(gl.GL_TEXTURE_2D, texture)

        white_balance = self.calculate_simple_white_balance()
        gl.glUniform3fv(self.wb_loc, 1, np.array(white_balance, dtype=np.float32))

        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3 * 2 * self.num_tiles)
