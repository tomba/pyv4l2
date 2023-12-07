import v4l2

# Disable all possible links
def disable_all_links(md: v4l2.MediaDevice):
    for ent in md.entities:
        for l in ent.pad_links:
            if l.is_immutable:
                continue
            #print((l.sink, l.sink_pad), (l.source, l.source_pad))
            l.enabled = False
            md.link_setup(l.source, l.sink, 0)
            #ent.setup_link(l)


# Enable link between (src_ent, src_pad) -> (sink_ent, sink_pad)
def link(md: v4l2.MediaDevice, source, sink):
    src_ent = source[0]
    sink_ent = sink[0]

    source_pad = src_ent.pads[source[1]]

    #links = src_ent.get_links(source[1])
    links = source_pad.links

    link = None

    for l in links:
        if l.sink_pad.entity == sink_ent and l.sink_pad.index == sink[1]:
            link = l
            break

    if link == None:
        raise Exception("Failed to find link between", source, sink)

    #if link.is_enabled:
    #    return

    #print("CONF")

    if link.is_immutable:
        return

    link.enabled = True
    #src_ent.setup_link(link)

    md.link_setup(link.source, link.sink, v4l2.MEDIA_LNK_FL_ENABLED)

def embedded_fourcc_to_bytes_per_pixel(fmt):
    if fmt == v4l2.PixelFormat.META_CSI2_12:
        return 12
    elif fmt == v4l2.PixelFormat.META_CSI2_10:
        return 10
    elif fmt == v4l2.PixelFormat.META_8:
        return 8
    elif fmt == v4l2.PixelFormat.SENSOR_DATA:
        return 8
    else:
        assert(False)
