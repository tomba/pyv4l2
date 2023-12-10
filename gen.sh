#!/bin/sh

INCLUDE_PATH="/home/tomba/tmp/khdrs/include"
INCLUDES="
	${INCLUDE_PATH}/linux/videodev2.h
	${INCLUDE_PATH}/linux/media.h
	${INCLUDE_PATH}/linux/v4l2-subdev.h
	${INCLUDE_PATH}/linux/media-bus-format.h
	${INCLUDE_PATH}/linux/v4l2-mediabus.h
"

# For some reason ctypesgen refuses to use the media-bus-format.h from the above
# include dir, but rather takes it from the host include dir...

OUT=v4l2/uapi/v4l2.py

#CTYPESGEN=ctypesgen
CTYPESGEN=/home/tomba/work/ctypesgen/run.py

CTYPESGEN_OPTS="--no-embed-preamble --no-macro-try-except --no-source-comments -D__volatile__= -D__signed__= -U__SIZEOF_INT128__"

${CTYPESGEN} ${CTYPESGEN_OPTS} -I${INCLUDE_PATH} -o ${OUT} ${INCLUDES}

# Fix _IOC by using ord(type)
sed --in-place s#"return ((((dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))"#"return ((((dir << _IOC_DIRSHIFT) | (ord(type) << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))"# ${OUT}

# Add pylint ignore comment
sed --in-place s/"^def POINTER(obj):"/"def POINTER(obj): # pylint: disable=function-redefined:"/ v4l2/uapi/ctypes_preamble.py
