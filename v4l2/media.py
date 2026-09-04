"""Media controller device and graph.

The graph structure (entities, interfaces, pads and links) is read once when
the MediaDevice is opened and kept as a snapshot. Link flags can change at any
time, so they are read from the kernel on every access. refresh() re-reads the
graph; objects from the old snapshot are not updated.
"""

from __future__ import annotations

import ctypes
import fcntl
import fnmatch
import glob
import os
import re

import v4l2.uapi

from .device import Device
from .enums import MediaEntityFunction, MediaInterfaceType, MediaLinkFlag, MediaPadFlag
from .helpers import filepath_for_major_minor

__all__ = [
    'MediaDevice',
    'MediaEntity',
    'MediaInterface',
    'MediaLink',
    'MediaObject',
    'MediaPad',
]


class MediaTopology:
    def __init__(self, topology, entities, interfaces, pads, links) -> None:
        self.topology = topology
        self.entities = entities
        self.interfaces = interfaces
        self.pads = pads
        self.links = links


class MediaObject:
    links: list[MediaLink]

    def __init__(self, md: MediaDevice, id: int) -> None:
        self.md = md
        self.id = id

    def _finalize(self):
        self.links = self.md._links_by_object_id.get(self.id, [])


class MediaEntity(MediaObject):
    def __init__(self, md, media_entity: v4l2.uapi.media_v2_entity) -> None:
        super().__init__(md, media_entity.id)
        self.media_entity = media_entity
        self.name = media_entity.name.decode('ascii')
        self.function = MediaEntityFunction(media_entity.function)
        self.flags = media_entity.flags
        self.pads: list[MediaPad] = None  # type: ignore
        self.interface: MediaInterface = None  # type: ignore

    def _finalize(self):
        super()._finalize()
        self.pads = self.md._pads_by_entity_id.get(self.id, [])

        ifaces = []

        for ids in [(l.media_link.source_id, l.media_link.sink_id) for l in self.links]:
            for id in ids:
                ob = self.md.find_id(id)

                if not isinstance(ob, MediaInterface):
                    continue

                ifaces.append(ob)

        if len(ifaces) > 1:
            raise RuntimeError('Multiple interfaces for entity')

        if len(ifaces) > 0:
            self.interface = ifaces[0]

    def __repr__(self) -> str:
        return f"MediaEntity({self.id}, '{self.name}')"

    @property
    def pad_links(self) -> list[MediaLink]:
        return [l for p in self.pads for l in p.links]

    @property
    def source_pads(self) -> list[MediaPad]:
        return [p for p in self.pads if p.is_source]

    @property
    def sink_pads(self) -> list[MediaPad]:
        return [p for p in self.pads if p.is_sink]

    def get_remote_pad(self, pad_idx: int) -> None | MediaPad:
        pad = self.pads[pad_idx]
        return pad.get_remote_pad()

    def get_remote_entity(self, pad_idx: int) -> None | MediaEntity:
        pad = self.pads[pad_idx]
        return pad.get_remote_entity()


class MediaInterface(MediaObject):
    def __init__(self, md, media_iface: v4l2.uapi.media_v2_interface) -> None:
        super().__init__(md, media_iface.id)
        self.media_iface = media_iface
        self.majorminor = (
            self.media_iface.unnamed_1.devnode.major,
            self.media_iface.unnamed_1.devnode.minor,
        )
        self.dev_path = filepath_for_major_minor(*self.majorminor)
        self.intf_type = MediaInterfaceType(self.media_iface.intf_type)

    def _finalize(self):
        super()._finalize()

    def __repr__(self) -> str:
        return f'MediaInterface({self.id})'

    @property
    def is_subdev(self):
        return self.media_iface.intf_type == v4l2.uapi.MEDIA_INTF_T_V4L_SUBDEV

    @property
    def is_video(self):
        return self.media_iface.intf_type == v4l2.uapi.MEDIA_INTF_T_V4L_VIDEO


class MediaPad(MediaObject):
    def __init__(self, md, media_pad: v4l2.uapi.media_v2_pad) -> None:
        super().__init__(md, media_pad.id)
        self.media_pad = media_pad
        self.index = media_pad.index
        self.entity: MediaEntity = None  # type: ignore

    def _finalize(self):
        super()._finalize()
        entity = self.md.find_id(self.media_pad.entity_id)
        assert isinstance(entity, MediaEntity)
        self.entity = entity

    def __repr__(self) -> str:
        return f"MediaPad({self.id}, '{self.entity.name}':{self.index})"

    @property
    def is_source(self):
        return (self.media_pad.flags & v4l2.uapi.MEDIA_PAD_FL_SOURCE) != 0

    @property
    def is_sink(self):
        return (self.media_pad.flags & v4l2.uapi.MEDIA_PAD_FL_SINK) != 0

    @property
    def is_internal(self):
        return (self.media_pad.flags & v4l2.uapi.MEDIA_PAD_FL_INTERNAL) != 0

    @property
    def flags(self) -> MediaPadFlag:
        return MediaPadFlag(self.media_pad.flags)

    def get_remote_pad(self) -> None | MediaPad:
        if len(self.links) == 0:
            return None

        assert len(self.links) == 1

        if self.is_sink:
            pad = self.links[0].source_pad
        elif self.is_source:
            pad = self.links[0].sink_pad
        else:
            raise RuntimeError('Pad is not source or sink')

        assert pad
        return pad

    def get_remote_entity(self) -> None | MediaEntity:
        rpad = self.get_remote_pad()
        if not rpad:
            return None

        assert rpad.entity
        return rpad.entity

    def get_remote_entities(self) -> list[MediaEntity]:
        l = []
        for link in self.links:
            if self.is_sink:
                ent = link.source_pad.entity
            elif self.is_source:
                ent = link.sink_pad.entity
            else:
                raise RuntimeError('Pad is not source or sink')

            assert ent
            l.append(ent)

        return l


class MediaLink(MediaObject):
    def __init__(self, md, media_link: v4l2.uapi.media_v2_link) -> None:
        super().__init__(md, media_link.id)
        self.media_link = media_link
        self.source: MediaObject = None  # type: ignore
        self.sink: MediaObject = None  # type: ignore

    def _finalize(self):
        super()._finalize()
        source = self.md.find_id(self.media_link.source_id)
        sink = self.md.find_id(self.media_link.sink_id)
        assert source and sink
        self.source = source
        self.sink = sink

    def __repr__(self) -> str:
        return f'MediaLink({self.id}, {self.source}->{self.sink})'

    @property
    def flags(self) -> MediaLinkFlag:
        # Link flags can change, read them from the kernel
        return self.md._get_link_flags(self.id)

    @property
    def is_enabled(self):
        return (self.flags & v4l2.uapi.MEDIA_LNK_FL_ENABLED) != 0

    @property
    def is_immutable(self):
        return (self.flags & v4l2.uapi.MEDIA_LNK_FL_IMMUTABLE) != 0

    @property
    def source_pad(self) -> MediaPad:
        if isinstance(self.source, MediaPad):
            return self.source
        raise RuntimeError('Source is not a MediaPad')

    @property
    def sink_pad(self) -> MediaPad:
        if isinstance(self.sink, MediaPad):
            return self.sink
        raise RuntimeError('Sink is not a MediaPad')

    def enable(self):
        self._setup(v4l2.uapi.MEDIA_LNK_FL_ENABLED)

    def disable(self):
        self._setup(0)

    def _setup(self, flags):
        desc = v4l2.uapi.media_link_desc()
        desc.source.entity = self.source_pad.entity.id
        desc.source.index = self.source_pad.index
        desc.sink.entity = self.sink_pad.entity.id
        desc.sink.index = self.sink_pad.index
        desc.flags = flags

        fcntl.ioctl(self.md.fd, v4l2.uapi.MEDIA_IOC_SETUP_LINK, desc, False)


class MediaDevice(Device):
    def __init__(self, name: str, key: str = 'path') -> None:
        if key != 'path':
            name = MediaDevice.__find_media_device_by_value(key, name)
            key = 'path'

        super().__init__(name)
        self.__read_device_info()
        self.__read_topology()

    @staticmethod
    def __find_media_device_by_value(key: str, value: str) -> str:
        for path in glob.glob('/dev/media*'):
            try:
                fd = os.open(path, os.O_RDWR | os.O_NONBLOCK)
            except OSError:
                continue

            try:
                mdi = v4l2.uapi.media_device_info()
                fcntl.ioctl(fd, v4l2.uapi.MEDIA_IOC_DEVICE_INFO, mdi, True)

                device_val = getattr(mdi, key).decode()

                if fnmatch.fnmatch(device_val, value):
                    return path
            finally:
                os.close(fd)

        raise FileNotFoundError(f'No media device "{key}" = "{value}" found')

    def get_device_info(self):
        mdi = v4l2.uapi.media_device_info()
        fcntl.ioctl(self.fd, v4l2.uapi.MEDIA_IOC_DEVICE_INFO, mdi, True)
        return mdi

    @staticmethod
    def __decode_kernel_version(v: int):
        a = (v >> 16) & 0xFF
        b = (v >> 8) & 0xFF
        c = v & 0xFF
        return (a, b, c)

    def __read_device_info(self):
        mdi = v4l2.uapi.media_device_info()
        fcntl.ioctl(self.fd, v4l2.uapi.MEDIA_IOC_DEVICE_INFO, mdi, True)

        self.driver = mdi.driver.decode()
        self.model = mdi.model.decode()
        self.serial = mdi.serial.decode()
        self.bus_info = mdi.bus_info.decode()
        self.media_version = MediaDevice.__decode_kernel_version(mdi.media_version)
        self.hw_revision = mdi.hw_revision
        self.driver_version = MediaDevice.__decode_kernel_version(mdi.driver_version)

    def __read_topology(self):
        topology = v4l2.uapi.media_v2_topology()

        fcntl.ioctl(self.fd, v4l2.uapi.MEDIA_IOC_G_TOPOLOGY, topology, True)

        entities = (v4l2.uapi.media_v2_entity * topology.num_entities)()
        interfaces = (v4l2.uapi.media_v2_interface * topology.num_interfaces)()
        pads = (v4l2.uapi.media_v2_pad * topology.num_pads)()
        links = (v4l2.uapi.media_v2_link * topology.num_links)()

        topology.ptr_entities = ctypes.addressof(entities)
        topology.ptr_interfaces = ctypes.addressof(interfaces)
        topology.ptr_pads = ctypes.addressof(pads)
        topology.ptr_links = ctypes.addressof(links)

        fcntl.ioctl(self.fd, v4l2.uapi.MEDIA_IOC_G_TOPOLOGY, topology, True)

        self.topology_version = topology.topology_version
        self.topology = MediaTopology(topology, entities, interfaces, pads, links)

        self.entities = [MediaEntity(self, e) for e in entities]
        self.interfaces = [MediaInterface(self, i) for i in interfaces]
        self.pads = [MediaPad(self, p) for p in pads]
        self.links = [MediaLink(self, l) for l in links]
        self.objects: list[MediaObject] = [
            *self.entities,
            *self.interfaces,
            *self.pads,
            *self.links,
        ]

        self._objects_by_id = {o.id: o for o in self.objects}

        self._pads_by_entity_id: dict[int, list[MediaPad]] = {}
        for p in self.pads:
            self._pads_by_entity_id.setdefault(p.media_pad.entity_id, []).append(p)

        self._links_by_object_id: dict[int, list[MediaLink]] = {}
        for l in self.links:
            for id in (l.media_link.source_id, l.media_link.sink_id):
                self._links_by_object_id.setdefault(id, []).append(l)

        for o in self.objects:
            o._finalize()

    def refresh(self):
        """Re-read the graph. Objects from the old graph are not updated."""
        self.__read_topology()

    def _read_links(self):
        topology = v4l2.uapi.media_v2_topology()
        fcntl.ioctl(self.fd, v4l2.uapi.MEDIA_IOC_G_TOPOLOGY, topology, True)

        if topology.topology_version != self.topology_version:
            raise RuntimeError('Media topology has changed')

        links = (v4l2.uapi.media_v2_link * topology.num_links)()
        topology.ptr_links = ctypes.addressof(links)
        fcntl.ioctl(self.fd, v4l2.uapi.MEDIA_IOC_G_TOPOLOGY, topology, True)

        return links

    def _get_link_flags(self, link_id: int) -> MediaLinkFlag:
        for l in self._read_links():
            if l.id == link_id:
                return MediaLinkFlag(l.flags)

        raise RuntimeError(f'Link {link_id} not found')

    def find_id(self, id) -> MediaObject | None:
        return self._objects_by_id.get(id)

    def find_entity(self, name=None, regex=None):
        for e in self.entities:
            if name is not None and not fnmatch.fnmatch(e.name, name):
                continue

            if regex is not None and re.match(regex, e.name) is None:
                continue

            return e

        return None
