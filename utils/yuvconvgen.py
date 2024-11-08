#!/usr/bin/env python3

import ctypes
import pprint
import numpy as np

# libcamera utils/rkisp1/gen-csc-table.py

# ./utils/rkisp1/gen-csc-table.py -i --precision Q15.16 rec601

matrices = {
    'rec601_limited': [
        0x00012a15, 0x00000000, 0x00019895,
        0x00012a15, 0xffff9bb5, 0xffff2fe1,
        0x00012a15, 0x00020469, 0x00000000,
    ],

    'rec601_full': [
        0x00010000, 0x00000000, 0x000166e9,
        0x00010000, 0xffffa7e7, 0xffff492e,
        0x00010000, 0x0001c5a2, 0x00000000,
    ],

    'rec709_full': [
        0x00010000, 0x00000000, 0x00019326,
        0x00010000, 0xffffd00c, 0xffff8829,
        0x00010000, 0x0001db09, 0x00000000,
    ],

    'rec709_limited': [
        0x00012a15, 0x00000000, 0x0001caf1,
        0x00012a15, 0xffffc969, 0xffff7793,
        0x00012a15, 0x00021cc6, 0x00000000,
    ],
}

def conv_value(v):
    v = ctypes.c_int32(v).value

    sign = v < 0

    v = abs(v)

    int_part = v >> 16
    decimal_part = (v & 0xffff) / 0xffff

    v = int_part + decimal_part

    if sign:
        v = -v

    #v = round(v, 3)

    return v

def conv_matrix(m):
    m = [conv_value(v) for v in m]

    m = np.matrix(m)

    m = m.reshape((3,3))

    m = m.transpose()

    return m.tolist()

matrices = { name:conv_matrix(m) for (name, m) in matrices.items() }

pprint.pprint(matrices)
