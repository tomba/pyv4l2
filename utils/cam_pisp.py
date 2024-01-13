import v4l2
import pisp
import mmap
import ctypes

def pisp_create_config(cap, vbuf: v4l2.VideoBuffer):
    print(f"CREATE, offset {vbuf.offset}, {vbuf.buffer_size}")

    with mmap.mmap(cap.fd, vbuf.buffer_size, mmap.MAP_SHARED,
                   mmap.PROT_READ | mmap.PROT_WRITE,
                   offset=vbuf.offset) as b:
        cfg = pisp.pisp_fe_config.from_buffer(b)

        cfg.input.streaming = 1
        cfg.global_.enables |= pisp.PISP_FE_ENABLE_INPUT
        cfg.input.format.width = 640
        cfg.input.format.height = 480
        cfg.input.format.stride = 640 * 1
        cfg.input.format.format = pisp.PISP_IMAGE_FORMAT_BPS_8; # | pisp.PISP_IMAGE_FORMAT_SHIFT_8

        ch = 0
        cfg.global_.enables |= pisp.PISP_FE_ENABLE_OUTPUT(ch)
        cfg.ch[ch].output.format.width = 640
        cfg.ch[ch].output.format.height = 480
        cfg.ch[ch].output.format.stride = 640 * 2
        cfg.ch[ch].output.format.format = pisp.PISP_IMAGE_FORMAT_BPS_16
