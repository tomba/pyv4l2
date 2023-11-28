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

ctypesgen -I${INCLUDE_PATH} -D__signed__= -U__SIZEOF_INT128__ -o v4l2/v4l2_kernel.py --no-embed-preamble $INCLUDES

# Fix _IOC by using ord(type)
sed --in-place s#"return ((((dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))"#"return ((((dir << _IOC_DIRSHIFT) | (ord(type) << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))"# v4l2/v4l2_kernel.py
