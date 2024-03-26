#!/usr/bin/python3

import v4l2
import errno

dot = []

dot += [
    'digraph "media-graph" {',
    '    compound=true',
    '    graph [rankdir=LR]',
    '    node [shape=Mrecord]',
]

def add_entity(entity_id: int, entity_label: str,
               sink_pads, source_pads,
               routes):
    dot.append(f'    subgraph cluster_e{entity_id} {{')
    dot.append(f'        label="{entity_label}"')

    if sink_pads:
        dot.append(f'        subgraph cluster_e{entity_id}_sinks {{')
        dot.append('            label=""')

        for p, streams in sink_pads.items():
            if len(streams) == 0:
                streams = [0]
            stream_str = str.join(' | ', [f'<p{p}s{s}> {s}' for s in streams])
            dot.append(f'            e{entity_id}p{p} [ label="Pad{p} | {stream_str}" ]')

        dot.append('        }')

    if source_pads:
        dot.append(f'        subgraph cluster_e{entity_id}_sources {{')
        dot.append('            label=""')

        for p, streams in source_pads.items():
            if len(streams) == 0:
                streams = [0]
            stream_str = str.join(' | ', [f'<p{p}s{s}> {s}' for s in streams])
            dot.append(f'            e{entity_id}p{p} [ label="Pad{p} | {stream_str}" ]')

        dot.append('        }')

    for r in routes:
        dot.append(f'        e{entity_id}p{r.sink_pad}:p{r.sink_pad}s{r.sink_stream} -> e{entity_id}p{r.source_pad}:p{r.source_pad}s{r.source_stream}')

    dot.append('    }')

def add_link(source_entity, source_pad, source_stream,
             sink_entity, sink_pad, sink_stream,
             tooltip, is_enabled):
    attrs = []
    attrs.append(f'tooltip="{tooltip}"')
    if not is_enabled:
        attrs.append('style=dashed')
    attrs = '[' + str.join(' ', attrs) + ']'
    dot.append(f'        e{source_entity}p{source_pad}:p{source_pad}s{source_stream} -> e{sink_entity}p{sink_pad}:p{sink_pad}s{sink_stream} {attrs}')

def mc_work():
    md = v4l2.MediaDevice('/dev/media0')

    entities = list(md.entities)

    for entity in entities:
        if entity.interface and entity.interface.is_subdev:
            subdev = v4l2.SubDevice(entity.interface.dev_path)
        else:
            subdev = None

        sink_pads = {}
        source_pads = {}

        for pad in entity.pads:
            if pad.is_sink:
                sink_pads[pad.index] = []
            else:
                source_pads[pad.index] = []

        if subdev:
            routes = [r for r in subdev.get_routes() if r.is_active]
            if len(routes) > 0:
                for r in routes:
                    sink_pads[r.sink_pad].append(r.sink_stream)
                    source_pads[r.source_pad].append(r.source_stream)
        else:
            routes = []

        add_entity(entity.id, entity.name,
                   sink_pads,
                   source_pads,
                   routes)

    for entity in entities:
        src_name = f'entity{entity.id}'

        for pad in [p for p in entity.pads if p.is_source]:
            for l in pad.links:
                remote_pad = l.sink_pad
                remote_entity = remote_pad.entity

                sink_name = f'entity{remote_entity.id}'

                if entity.interface and entity.interface.is_subdev:
                    subdev = v4l2.SubDevice(entity.interface.dev_path)
                else:
                    subdev = None

                if subdev:
                    routes = [r for r in subdev.get_routes() if r.is_active]
                else:
                    routes = []

                streams = set([r.source_stream for r in routes if r.source_pad == pad.index] + [r.sink_stream for r in routes if r.sink_pad == pad.index])

                if len(streams) == 0:
                    streams = [ 0 ]

                if remote_entity.interface and remote_entity.interface.is_subdev:
                    remote_subdev = v4l2.SubDevice(remote_entity.interface.dev_path)
                    routes = [r for r in remote_subdev.get_routes() if r.is_active]

                    remote_streams = set()

                    for r in routes:
                        if r.sink_pad == remote_pad.index:
                            remote_streams.add(r.sink_stream)

                    if len(remote_streams) == 0:
                        remote_streams = set([0])

                else:
                    remote_streams = set([0])

                for stream in streams:
                    if subdev:
                        try:
                            fmt = subdev.get_format(pad.index, stream)
                            f = fmt.format

                            try:
                                bfmt = v4l2.BusFormat(f.code).name
                            except ValueError:
                                bfmt = f'0x{f.code:x}'

                            fmt = f'Stream{stream}\n{f.width}x{f.height}/{bfmt}\nfield:{f.field}\ncolorspace:{f.colorspace}\nquantization:{f.quantization}\nxfer:{f.xfer_func}\nflags:{f.flags}'
                        except OSError as e:
                            if e.errno != errno.ENOTTY:
                                fmt = f'Stream{stream}\n{e}'
                            else:
                                fmt = ''
                    else:
                        fmt = ''

                    if stream not in remote_streams:
                        continue

                    add_link(entity.id, pad.index, stream,
                             remote_entity.id, remote_pad.index, stream,
                             fmt, l.is_enabled)


mc_work()


dot.append('}')

#for l in dot:
#    print(l)

with open('media.dot', 'w', encoding='ascii') as f:
    f.writelines([l + '\n' for l in dot])
