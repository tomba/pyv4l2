import v4l2
import pisp
import mmap

def fill_fe_config(stream, vbuf: v4l2.VideoBuffer, cfg: pisp.pisp_fe_config):
    cfg.input.streaming = 1
    cfg.global_.enables |= pisp.PISP_FE_ENABLE_INPUT
    cfg.input.format.width = stream['w']
    cfg.input.format.height = stream['h']
    cfg.input.format.stride = stream['w'] * 1  # 8 bits per pixel??
    cfg.input.format.format = pisp.PISP_IMAGE_FORMAT_BPS_8; # | pisp.PISP_IMAGE_FORMAT_SHIFT_8

    ch = 0
    cfg.global_.enables |= pisp.PISP_FE_ENABLE_OUTPUT(ch)
    cfg.ch[ch].output.format.width = stream['w']
    cfg.ch[ch].output.format.height = stream['h']
    cfg.ch[ch].output.format.stride = stream['w'] * 2
    cfg.ch[ch].output.format.format = pisp.PISP_IMAGE_FORMAT_BPS_16

    #ch = 1
    #cfg.global_.enables |= pisp.PISP_FE_ENABLE_OUTPUT(ch)
    #cfg.ch[ch].output.format.width = stream['w']
    #cfg.ch[ch].output.format.height = stream['h']
    #cfg.ch[ch].output.format.stride = stream['w'] * 2
    #cfg.ch[ch].output.format.format = pisp.PISP_IMAGE_FORMAT_BPS_16


def pisp_create_config(stream, cap, vbuf: v4l2.VideoBuffer):
    #print(f"CREATE, cap.fd:{cap.fd}, offset:{vbuf.offset}, size:{vbuf.buffer_size}, fd:{vbuf.fd}")

    if vbuf.fd >= 0: # XXX is drm buffer?
        with mmap.mmap(vbuf.fd, vbuf.buffer_size, mmap.MAP_SHARED,
                       mmap.PROT_READ | mmap.PROT_WRITE) as b:
            cfg = pisp.pisp_fe_config.from_buffer(b)

            fill_fe_config(stream, vbuf, cfg)

            # XXX need to destroy cfg before mmap can be closed
            cfg = None
    else:
        with mmap.mmap(cap.fd, vbuf.buffer_size, mmap.MAP_SHARED,
                       mmap.PROT_READ | mmap.PROT_WRITE,
                       offset=vbuf.offset) as b:
            cfg = pisp.pisp_fe_config.from_buffer(b)

            fill_fe_config(stream, vbuf, cfg)

            # XXX need to destroy cfg before mmap can be closed
            cfg = None
