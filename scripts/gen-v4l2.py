#!/usr/bin/python3

import sys
import re

CTYPESGEN_PATH = '/home/tomba/work/ctypesgen/'

INCLUDE_PATH = "/home/tomba/tmp/khdrs/include"

INCLUDES = (
    f'{INCLUDE_PATH}/linux/videodev2.h',
    f'{INCLUDE_PATH}/linux/media.h',
    f'{INCLUDE_PATH}/linux/v4l2-subdev.h',
    f'{INCLUDE_PATH}/linux/media-bus-format.h',
    f'{INCLUDE_PATH}/linux/v4l2-mediabus.h',
    f'{INCLUDE_PATH}/linux/v4l2-controls.h',
)

# For some reason ctypesgen refuses to use the media-bus-format.h from the above
# include dir, but rather takes it from the host include dir...

OUT = 'v4l2/uapi/v4l2.py'

CTYPESGEN_OPTS = (
    "--no-embed-preamble",
    '--no-macro-try-except',
    '--no-source-comments',
    '-D__volatile__=',
    '-D__signed__=',
    '-U__SIZEOF_INT128__',
)

sys.path.insert(0, CTYPESGEN_PATH)
from ctypesgen.__main__ import main  # pylint: disable=E,C # type: ignore

sys.argv = ['ctypesgen', *CTYPESGEN_OPTS, f'-I{INCLUDE_PATH}', f'-o{OUT}', *INCLUDES]

main()

def replace(filename, replaces):
    for r in replaces:
        pat = r[0]
        repl = r[1]

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(pat, repl, content, count=1, flags=re.MULTILINE)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

# Fix _IOC by using ord(type)

replace(OUT, [
        (re.escape('return ((((dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))'),
         'return ((((dir << _IOC_DIRSHIFT) | (ord(type) << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))'),
        ])

# Add pylint ignore comment

replace('v4l2/uapi/ctypes_preamble.py', [
        (r"^def POINTER\(obj\):$",
         "def POINTER(obj): # pylint: disable=function-redefined:")
        ])
