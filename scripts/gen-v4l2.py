#!/usr/bin/env python3

import sys
import re

CTYPESGEN_PATH = '/home/tomba/work/ctypesgen/'

INCLUDE_PATH = '/home/tomba/tmp/khdrs/include'

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
    '--no-embed-preamble',
    '--no-macro-try-except',
    '--no-source-comments',
    '-D__volatile__=',
    '-D__signed__=',
    '-U__SIZEOF_INT128__',
)

sys.path.insert(0, CTYPESGEN_PATH)
from ctypesgen.__main__ import main  # pylint: disable=E,C # type: ignore # noqa: E402

sys.argv = ['ctypesgen', *CTYPESGEN_OPTS, f'-I{INCLUDE_PATH}', f'-o{OUT}', *INCLUDES]

main()

def replace(filename, replaces):
    for r in replaces:
        pat = r[0]
        repl = r[1]

        with open(filename, encoding='utf-8') as f:
            content = f.read()

        content = re.sub(pat, repl, content, count=1, flags=re.MULTILINE)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

def find_packed_structs(headers):
    """
    Find packed structs in the given header files.

    :param headers: List of header file paths.
    :return: List of packed struct names.
    """
    packed_structs = []
    pattern = re.compile(r'struct (\w+) {[^{}]*(?:{[^{}]*}[^{}]*)*} __attribute__ \(\(packed\)\);', re.DOTALL)

    for header_file in headers:
        with open(header_file, encoding='utf-8') as f:
            content = f.read()
            matches = pattern.findall(content)
            packed_structs.extend(matches)

    return packed_structs

def add_pack_to_structs(filename, struct_names):
    """
    Add _pack_ = 1 to the specified structs in the v4l2 python binding

    :param filename: The name of the Python file to modify.
    :param struct_names: List of struct names to update.
    """
    replaces = []
    for name in struct_names:
        pattern = rf'^struct_{name}._fields_ = \['
        replacement = f'struct_{name}._pack_ = 1\nstruct_{name}._fields_ = ['
        replaces.append((pattern, replacement))

    replace(filename, replaces)

# Fix _IOC by using ord(type)

replace(OUT, [
        (re.escape('return ((((dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))'),
         'return ((((dir << _IOC_DIRSHIFT) | (ord(type) << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))'),
        ])

# Fix missing _pack_ attribute

structs = find_packed_structs(INCLUDES)
add_pack_to_structs(OUT, structs)

# Add pylint ignore comment

replace('v4l2/uapi/ctypes_preamble.py', [
        (r'^def POINTER\(obj\):$',
         'def POINTER(obj): # pylint: disable=function-redefined:')
        ])
