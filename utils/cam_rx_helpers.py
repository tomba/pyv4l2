# SPDX-License-Identifier: BSD-3-Clause
# Copyright (C) 2023, Tomi Valkeinen <tomi.valkeinen@ideasonboard.com>
#
# Debayering code from PiCamera documentation

from numpy.lib.stride_tricks import as_strided
from PyQt5 import QtGui
import numpy as np


def demosaic(data, r0, g0, g1, b0):
    # Separate the components from the Bayer data to RGB planes

    rgb = np.zeros(data.shape + (3,), dtype=data.dtype)
    rgb[1::2, 0::2, 0] = data[r0[1]::2, r0[0]::2]  # Red
    rgb[0::2, 0::2, 1] = data[g0[1]::2, g0[0]::2]  # Green
    rgb[1::2, 1::2, 1] = data[g1[1]::2, g1[0]::2]  # Green
    rgb[0::2, 1::2, 2] = data[b0[1]::2, b0[0]::2]  # Blue

    # Below we present a fairly naive de-mosaic method that simply
    # calculates the weighted average of a pixel based on the pixels
    # surrounding it. The weighting is provided by a byte representation of
    # the Bayer filter which we construct first:

    bayer = np.zeros(rgb.shape, dtype=np.uint8)
    bayer[1::2, 0::2, 0] = 1  # Red
    bayer[0::2, 0::2, 1] = 1  # Green
    bayer[1::2, 1::2, 1] = 1  # Green
    bayer[0::2, 1::2, 2] = 1  # Blue

    # Allocate an array to hold our output with the same shape as the input
    # data. After this we define the size of window that will be used to
    # calculate each weighted average (3x3). Then we pad out the rgb and
    # bayer arrays, adding blank pixels at their edges to compensate for the
    # size of the window when calculating averages for edge pixels.

    output = np.empty(rgb.shape, dtype=rgb.dtype)
    window = (3, 3)
    borders = (window[0] - 1, window[1] - 1)
    border = (borders[0] // 2, borders[1] // 2)

    rgb = np.pad(rgb, [
        (border[0], border[0]),
        (border[1], border[1]),
        (0, 0),
    ], 'constant')
    bayer = np.pad(bayer, [
        (border[0], border[0]),
        (border[1], border[1]),
        (0, 0),
    ], 'constant')

    # For each plane in the RGB data, we use a nifty numpy trick
    # (as_strided) to construct a view over the plane of 3x3 matrices. We do
    # the same for the bayer array, then use Einstein summation on each
    # (np.sum is simpler, but copies the data so it's slower), and divide
    # the results to get our weighted average:

    for plane in range(3):
        p = rgb[..., plane]
        b = bayer[..., plane]

        pview = as_strided(p, shape=(
            p.shape[0] - borders[0],
            p.shape[1] - borders[1]) + window, strides=p.strides * 2)
        bview = as_strided(b, shape=(
            b.shape[0] - borders[0],
            b.shape[1] - borders[1]) + window, strides=b.strides * 2)
        psum = np.einsum('ijkl->ij', pview)
        bsum = np.einsum('ijkl->ij', bview)
        output[..., plane] = psum // bsum

    return output


def convert_raw_packed(data, w, h, bytesperline, fmt):
    bayer_pattern = fmt[1:5]

    packed = fmt.endswith("P")

    if packed:
        bitspp = int(fmt[5:-1])
    else:
        bitspp = int(fmt[5:])

    if bytesperline:
        data = data.reshape((len(data) // bytesperline, bytesperline))
    else:
        data = data.reshape((h, len(data) // h))

    # cut the extra padding on the right
    extra = bytesperline - w * bitspp // 8
    if extra:
        data = np.delete(data, np.s_[-extra:], 1)

    data = data.astype(np.uint16) << 2
    for byte in range(4):
        asd = ((data[:, 4::5] >> ((4 - byte) * 2)) & 0b11)
        data[:, byte::5] |= asd
    data = np.delete(data, np.s_[4::5], 1)

    idx = bayer_pattern.find('R')
    assert(idx != -1)
    r0 = (idx % 2, idx // 2)

    idx = bayer_pattern.find('G')
    assert(idx != -1)
    g0 = (idx % 2, idx // 2)

    idx = bayer_pattern.find('G', idx + 1)
    assert(idx != -1)
    g1 = (idx % 2, idx // 2)

    idx = bayer_pattern.find('B')
    assert(idx != -1)
    b0 = (idx % 2, idx // 2)

    rgb = demosaic(data, r0, g0, g1, b0)
    rgb = (rgb >> (bitspp - 8)).astype(np.uint8)

    return rgb

def convert_raw(data, w, h, bytesperline, fmt):
    bayer_pattern = fmt[1:5]

    packed = fmt.endswith("P")

    if packed:
        bitspp = int(fmt[5:-1])
    else:
        bitspp = int(fmt[5:])

    if packed:
        return convert_raw_packed(data, w, h, bytesperline, fmt)

    if bitspp == 8:
        data = data.reshape((h, w))
        data = data.astype(np.uint16)
    elif bitspp in [10, 12, 16]:
        data = data.view(np.uint16)
        data = data.reshape((h, w))
    else:
        raise Exception('Bad bitspp:' + str(bitspp))

    idx = bayer_pattern.find('R')
    assert(idx != -1)
    r0 = (idx % 2, idx // 2)

    idx = bayer_pattern.find('G')
    assert(idx != -1)
    g0 = (idx % 2, idx // 2)

    idx = bayer_pattern.find('G', idx + 1)
    assert(idx != -1)
    g1 = (idx % 2, idx // 2)

    idx = bayer_pattern.find('B')
    assert(idx != -1)
    b0 = (idx % 2, idx // 2)

    rgb = demosaic(data, r0, g0, g1, b0)
    rgb = (rgb >> (bitspp - 8)).astype(np.uint8)

    return rgb


def convert_yuv444_to_rgb(yuv):
    m = np.array([
        [1.0, 1.0, 1.0],
        [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
        [1.4019975662231445, -0.7141380310058594, 0.00001542569043522235]
    ])

    rgb = np.dot(yuv, m)
    rgb[:, :, 0] -= 179.45477266423404
    rgb[:, :, 1] += 135.45870971679688
    rgb[:, :, 2] -= 226.8183044444304
    rgb = rgb.astype(np.uint8)

    return rgb


def convert_yuyv(data, w, h):
    # YUV422
    yuyv = data.reshape((h, w // 2 * 4))

    # YUV444
    yuv = np.empty((h, w, 3), dtype=np.uint8)
    yuv[:, :, 0] = yuyv[:, 0::2]                    # Y
    yuv[:, :, 1] = yuyv[:, 1::4].repeat(2, axis=1)  # U
    yuv[:, :, 2] = yuyv[:, 3::4].repeat(2, axis=1)  # V

    return convert_yuv444_to_rgb(yuv)


def convert_uyvy(data, w, h):
    # YUV422
    yuyv = data.reshape((h, w // 2 * 4))

    # YUV444
    yuv = np.empty((h, w, 3), dtype=np.uint8)
    yuv[:, :, 0] = yuyv[:, 1::2]                    # Y
    yuv[:, :, 1] = yuyv[:, 0::4].repeat(2, axis=1)  # U
    yuv[:, :, 2] = yuyv[:, 2::4].repeat(2, axis=1)  # V

    return convert_yuv444_to_rgb(yuv)


def convert_nv12(data, w, h):
    plane1 = data[:w * h]
    plane2 = data[w * h:]

    y = plane1.reshape((h, w))
    uv = plane2.reshape((h // 2, w // 2, 2))

    # YUV444
    yuv = np.empty((h, w, 3), dtype=np.uint8)
    yuv[:, :, 0] = y[:, :]                    # Y
    yuv[:, :, 1] = uv[:, :, 0].repeat(2, axis=0).repeat(2, axis=1)  # U
    yuv[:, :, 2] = uv[:, :, 1].repeat(2, axis=0).repeat(2, axis=1)  # V

    return convert_yuv444_to_rgb(yuv)


def convert_y8(data, w, h):
    y = data.reshape((h, w))

    # YUV444
    yuv = np.zeros((h, w, 3), dtype=np.uint8)
    yuv[:, :, 0] = y #yuyv[:, 0::2]                    # Y
    yuv[:, :, 1] = y  # U
    yuv[:, :, 2] = y  # V

    return yuv

    #return convert_yuv444_to_rgb(yuv)


def to_rgb(fmt, w, h, bytesperline, data):
    if fmt == 'Y8':
        return convert_y8(data, w, h)

    if fmt == 'YUYV':
        return convert_yuyv(data, w, h)

    if fmt == 'UYVY':
        return convert_uyvy(data, w, h)

    elif fmt == 'NV12':
        return convert_nv12(data, w, h)

    elif fmt == 'RGB888':
        rgb = data.reshape((h, w, 3))
        rgb[:, :, [0, 1, 2]] = rgb[:, :, [2, 1, 0]]

    elif fmt == 'BGR888':
        rgb = data.reshape((h, w, 3))

    elif fmt in ['ARGB8888', 'XRGB8888']:
        rgb = data.reshape((h, w, 4))
        rgb = np.flip(rgb, axis=2)
        # drop alpha component
        rgb = np.delete(rgb, np.s_[0::4], axis=2)

    elif fmt.startswith('S'):
        return convert_raw(data, w, h, bytesperline, fmt)

    else:
        raise Exception('Unsupported format ' + fmt)

    return rgb


def data_to_rgb(fmt, w, h, bytesperline, data):
    data = np.frombuffer(data, dtype=np.uint8)
    rgb = to_rgb(fmt, w, h, bytesperline, data)
    return rgb


def rgb_to_pix(rgb):
    w = rgb.shape[1]
    h = rgb.shape[0]
    qim = QtGui.QImage(rgb, w, h, QtGui.QImage.Format.Format_RGB888) # pylint: disable=no-member
    pix = QtGui.QPixmap.fromImage(qim)
    return pix


def data_to_pix(fmt, w, h, bytesperline, data):
    if fmt == 'MJPEG':
        pix = QtGui.QPixmap(w, h)
        pix.loadFromData(data)
    else:
        rgb = data_to_rgb(fmt, w, h, bytesperline, data)
        pix = rgb_to_pix(rgb)

    return pix
