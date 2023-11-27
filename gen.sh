#!/bin/sh

includes="/home/tomba/tmp/khdrs/include"
files="$includes/linux/videodev2.h $includes/linux/media.h $includes/linux/v4l2-subdev.h $includes/linux/media-bus-format.h $includes/linux/v4l2-mediabus.h"

mkdir -p v4l2
ctypesgen -D__signed__=  --allow-gnu-c -o v4l2/v4l2_kernel.py --no-embed-preamble $files

# Fix _IOC by using ord(type)
sed --in-place s#"return ((((dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))"#"return ((((dir << _IOC_DIRSHIFT) | (ord(type) << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))"# v4l2/v4l2_kernel.py
