#!/usr/bin/python3

from typing import List
import v4l2

# Pixel

imx219_w = 640
imx219_h = 480
imx219_bus_fmt = v4l2.BusFormat.SRGGB10_1X10
imx219_pix_fmt = v4l2.PixelFormats.SRGGB10P
#imx219_bus_fmt = v4l2.BusFormat.SRGGB8_1X8
#imx219_pix_fmt = v4l2.PixelFormats.SRGGB8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)

mbus_fmt_des = mbus_fmt_imx219

fmt_pix = (imx219_w, imx219_h, imx219_pix_fmt)

configurations = {}

media_device_name = ('rp1-cfe', 'model')
des_ent = 'max96724 6-0027'

def find_devices():
    md = v4l2.MediaDevice(*media_device_name)
    assert md
    deser = md.find_entity(des_ent)
    assert deser

    cameras = {}

    for p in [p for p in deser.pads if p.index < 4]:
        if len(p.links) == 0:
            continue

        assert len(p.links) == 1

        ser = p.links[0].source.entity
        sensor = ser.pads[0].links[0].source.entity

        cameras[p.index] = (ser.name, sensor.name)

    return cameras

cameras = find_devices()


def gen_imx219_pixel(port, num_cameras):
    first_ser_i2c_port = 13
    first_imx_i2c_port = first_ser_i2c_port + num_cameras

    sensor_ent = cameras[port][1]
    ser_ent = cameras[port][0]

    return {
        'media': media_device_name,

        'subdevs': [
            # Camera
            {
                'entity': sensor_ent,
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                ],
            },

            # Serializer
            {
                'entity': ser_ent,
                'routing': [
                    { 'src': (0, 0), 'dst': (1, 0) },
                ],
                'pads': [
                    { 'pad': (0, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (1, 0), 'fmt': mbus_fmt_imx219 },
                ],
            },
            # Deserializer
            {
                'entity': des_ent,
                'routing': [
                    { 'src': (port, 0), 'dst': (6, port) },
                ],
                'pads': [
                    { 'pad': (port, 0), 'fmt': mbus_fmt_imx219 },
                    { 'pad': (6, 0), 'fmt': mbus_fmt_des },
                ],
            },

            # CSI-2 RX
            {
                'entity': 'csi2',
                'routing': [
                    { 'src': (0, port), 'dst': (1 + port, 0) },
                ],
                'pads': [
                    { 'pad': (0, port), 'fmt': mbus_fmt_des },
                    { 'pad': (1 + port, 0), 'fmt': mbus_fmt_des },
                ],
            },
        ],

        'devices': [
            {
                'entity': f'rp1-cfe-csi2-ch{port}',
                'fmt': fmt_pix,
                'embedded': False,
            },
        ],

        'links': [
            { 'src': (sensor_ent, 0), 'dst': (ser_ent, 0) },
            { 'src': (ser_ent, 1), 'dst': (des_ent, port) },
            { 'src': (des_ent, 6), 'dst': ('csi2', 0) },
            { 'src': ('csi2', 1 + port), 'dst': (f'rp1-cfe-csi2-ch{port}', 0) },
        ],
    }

def get_configs():
    num_cameras = len(cameras)

    for i in range(num_cameras):
        configurations[f'cam{i}'] = gen_imx219_pixel(i, num_cameras)

    return (configurations, ['cam0'])
