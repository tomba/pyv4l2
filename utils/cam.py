#!/usr/bin/python3

from collections import deque
import argparse
import importlib
import mmap
import os
import pprint
import pykms
import selectors
import struct
import sys
import time
import v4l2

# ctx-idx, width, height, bytesperline, format, num-planes, plane1, plane2, plane3, plane4
struct_fmt = struct.Struct("<IIII16pI4I")

CONNECTOR = ""

parser = argparse.ArgumentParser()
parser.add_argument("config_name", help="Configuration name")
parser.add_argument("-c", "--config", action="store_true", default=False, help="configure only")
parser.add_argument("-s", "--save", action="store_true", default=False, help="save frames to files")
parser.add_argument("-d", "--display", action="store_true", default=False, help="show frames on screen")
parser.add_argument("-x", "--tx", nargs='?', type=str, default=None, const='all', help="send frames to a server")
parser.add_argument("-t", "--type", type=str, default="drm", help="buffer type (drm/v4l2)")
parser.add_argument("-p", "--print", action="store_true", default=False, help="print config dict")
args = parser.parse_args()

if args.tx:
    args.tx = args.tx.split(',')

if not args.type in ["drm", "v4l2"]:
    print("Bad buffer type", args.type)
    exit(-1)

def merge_configs(configs):
    d = { "subdevs": [], "devices": [], "links": [] }

    for config in configs:
        # links can be appended directly
        # xxx there may be (harmless) duplicates
        d["links"] += config["links"]

        # devices can be appended directly
        d["devices"] += config["devices"]

        # subdevs need to be merged based on entity
        for subdev in config["subdevs"]:
            ent = subdev["entity"]

            dst = next((s for s in d["subdevs"] if s["entity"] == ent), None)
            if dst:
                if "pads" in subdev:
                    dst["pads"] += subdev["pads"]
                if "routing" in subdev:
                    dst["routing"] += subdev["routing"]
            else:
                d["subdevs"].append(subdev)

    return d

parts = args.config_name.split(":")

if len(parts) > 2:
    sys.exit(-1)

config_file = parts[0]

if len(parts) == 2:
    config_names = parts[1].split(",")
else:
    config_names = []

config_names = [c for c in config_names if len(c) > 0]

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/cam-configs")
configurations, default_configurations = importlib.import_module(config_file).get_configs()

if len(config_names) == 0:
    config_names = default_configurations

for cfg in config_names:
    if cfg not in configurations:
        print("Cannot find config '{}'".format(cfg))
        sys.exit(-1)

config = merge_configs([configurations[x] for x in config_names])

# Disable all possible links
def disable_all_links(md):
    for ent in md.entities:
        for l in ent.pad_links:
            if l.is_immutable:
                continue
            #print((l.sink, l.sink_pad), (l.source, l.source_pad))
            l.enabled = False
            md.link_setup(l.source, l.sink, 0)
            #ent.setup_link(l)


# Enable link between (src_ent, src_pad) -> (sink_ent, sink_pad)
def link(source, sink):
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


print("Configure media entities")

md = v4l2.MediaDevice("/dev/media0")

disable_all_links(md)

# Setup links
for l in config.get("links", []):
    source_ent, source_pad = l["src"]
    sink_ent, sink_pad = l["dst"]

    try:
        source_ent = md.find_entity(source_ent)
        if source_ent == None:
            print("Failed to find entity", l["src"])
            exit(-1)

        sink_ent = md.find_entity(sink_ent)
        if sink_ent == None:
            print("Failed to find entity", l["dst"])
            exit(-1)

        link((source_ent, source_pad), (sink_ent, sink_pad))
    except Exception as e:
        print("Failed to link {} -> {}".format((source_ent, source_pad), (sink_ent, sink_pad)))
        raise e

# Configure entities
for e in config.get("subdevs", []):
    ent = md.find_entity(e["entity"])
    assert ent
    subdev = v4l2.SubDevice(ent)
    assert subdev, "no subdev for entity %s" % ent

    # Configure routes
    if "routing" in e:
        routes = []
        for r in e["routing"]:
            sink_pad, sink_stream = r["src"]
            source_pad, source_stream = r["dst"]

            route = v4l2.Route()
            route.sink_pad = sink_pad
            route.sink_stream = sink_stream
            route.source_pad = source_pad
            route.source_stream = source_stream
            route.flags = v4l2.V4L2_SUBDEV_ROUTE_FL_ACTIVE

            routes.append(route)

        if len(routes) > 0:
            try:
                subdev.set_routes(routes)
            except Exception as e:
                print("Failed to set routes for {}".format(ent))
                raise e

    # Configure streams
    for p in e.get("pads", []):
        if type(p["pad"]) == tuple:
            pad, stream = p["pad"]
        else:
            pad = p["pad"]
            stream = 0
        w, h, fmt = p["fmt"]
        try:
            subdev.set_format(pad, stream, w, h, fmt)
        except Exception as e:
            print("Failed to set format for {}".format(ent))
            raise e

        if "ival" in p:
            numerator, denominator = p["ival"]
            subdev.set_frame_interval(pad, stream, numerator, denominator)


card = None

if args.type == "drm":
    card = pykms.Card()

if args.display:
    if card == None:
        card = pykms.Card()
    res = pykms.ResourceManager(card)
    conn = res.reserve_connector(CONNECTOR)
    crtc = res.reserve_crtc(conn)

    card.disable_planes()

    mode = conn.get_default_mode()
    modeb = mode.to_blob(card)

    req = pykms.AtomicReq(card)
    req.add(conn, "CRTC_ID", crtc.id)
    req.add(crtc, {"ACTIVE": 1,
            "MODE_ID": modeb.id})
    req.commit_sync(allow_modeset = True)

if args.tx:
    import socket

    HOST, PORT = "192.168.88.20", 43242

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

NUM_BUFS = 5

streams = config["devices"]

num_planes = sum(1 for stream in streams if args.display and stream.get("display", True))

display_idx = 0

for i, stream in enumerate(streams):
    stream["display"] = args.display and stream.get("display", True)

    stream["id"] = i

    stream["w"] = stream["fmt"][0]
    stream["h"] = stream["fmt"][1]
    stream["fourcc"] = stream["fmt"][2]

    stream["kms-buf-w"] = stream["w"]
    stream["kms-buf-h"] = stream["h"]

    if stream.get("dra-plane-hack", False):
        # Hack to reserve the unscaleable GFX plane
        res.reserve_generic_plane(crtc, pykms.PixelFormat.RGB565)

    if not "kms-fourcc" in stream:
        if stream["fourcc"] == v4l2.V4L2_META_FMT_GENERIC_8:
            stream["kms-fourcc"] = pykms.PixelFormat.RGB565
        elif stream["fourcc"] == v4l2.V4L2_META_FMT_GENERIC_CSI2_12:
            stream["kms-fourcc"] = pykms.PixelFormat.RGB565
        else:
            #kms_fourcc = v4l2.pixelformat_to_drm_fourcc(stream["fourcc"])
            #stream["kms-fourcc"] = pykms.fourcc_to_pixelformat(kms_fourcc)
            # XXX
            stream["kms-fourcc"] = pykms.PixelFormat(stream["fourcc"])

    if args.type == "drm" and "embedded" in stream and stream["embedded"]:
        divs = [16, 8, 4, 2, 1]
        for div in divs:
            w = stream["kms-buf-w"] // div
            if w % 2 == 0:
                break

        h = stream["kms-buf-h"] * div

        stream["kms-buf-w"] = w
        stream["kms-buf-h"] = h

    if stream["display"]:
        max_w = mode.hdisplay // (1 if num_planes == 1 else 2)
        max_h = mode.vdisplay // (1 if num_planes <= 2 else 2)

        stream["kms-src-w"] = min(stream["kms-buf-w"], max_w)
        stream["kms-src-h"] = min(stream["kms-buf-h"], max_h)
        stream["kms-src-x"] = (stream["kms-buf-w"] - stream["kms-src-w"]) // 2
        stream["kms-src-y"] = (stream["kms-buf-h"] - stream["kms-src-h"]) // 2

        stream["kms-dst-w"]  =stream["kms-src-w"]
        stream["kms-dst-h"] = stream["kms-src-h"]

        if display_idx % 2 == 0:
            stream["kms-dst-x"] = 0
        else:
            stream["kms-dst-x"] = mode.hdisplay - stream["kms-dst-w"]

        if display_idx // 2 == 0:
            stream["kms-dst-y"] = 0
        else:
            stream["kms-dst-y"] = mode.vdisplay - stream["kms-dst-h"]

        display_idx += 1

        plane = res.reserve_generic_plane(crtc, stream["kms-fourcc"])
        assert(plane)
        stream["plane"] = plane

if args.print:
    for stream in streams:
        pprint.pprint(stream)

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

for stream in streams:
    vid_ent = md.find_entity(stream["entity"])

    if not "dev" in stream:
        stream["dev"] = vid_ent.dev_path

    vd = v4l2.VideoDevice(vid_ent)

    if not stream.get("embedded", False):
        cap = vd.get_capture_streamer(v4l2.V4L2_MEMORY_MMAP if args.type == "v4l2" else v4l2.V4L2_MEMORY_DMABUF,
                                      v4l2.V4L2_BUF_TYPE_VIDEO_CAPTURE)
        cap.set_port(0)
        cap.set_format(stream["fourcc"], stream["w"], stream["h"])
    else:
        cap = vd.meta_capture_streamer
        bpp = embedded_fourcc_to_bytes_per_pixel(stream["fourcc"])

        cap.set_format(stream["fourcc"], stream["w"] * stream["h"] * bpp // 8)

    stream["vd"] = vd
    stream["cap"] = cap

if args.config:
    exit(0)

for stream in streams:
    cap = stream["cap"]

    mem_type = v4l2.V4L2_MEMORY_DMABUF if args.type == "drm" else v4l2.V4L2_MEMORY_MMAP
    cap.set_queue_size(NUM_BUFS)

    if args.type == "drm":
        # Allocate FBs
        fbs = []
        for i in range(NUM_BUFS):
            fb = pykms.DumbFramebuffer(card, stream["kms-buf-w"], stream["kms-buf-h"], stream["kms-fourcc"])
            fbs.append(fb)
        stream["fbs"] = fbs

    if stream["display"]:
        assert(args.type == "drm")

        # Set fb0 to screen
        fb = stream["fbs"][0]
        plane = stream["plane"]

        plane.set_props({
            "FB_ID": fb.id,
            "CRTC_ID": crtc.id,
            "SRC_X": stream["kms-src-x"] << 16,
            "SRC_Y": stream["kms-src-y"] << 16,
            "SRC_W": stream["kms-src-w"] << 16,
            "SRC_H": stream["kms-src-h"] << 16,
            "CRTC_X": stream["kms-dst-x"],
            "CRTC_Y": stream["kms-dst-y"],
            "CRTC_W": stream["kms-dst-w"],
            "CRTC_H": stream["kms-dst-h"],
        })

        stream["kms_old_fb"] = None
        stream["kms_fb"] = fb
        stream["kms_fb_queue"] = deque()

    first_buf = 1 if stream["display"] else 0

    # Queue the rest to the camera
    for i in range(first_buf, NUM_BUFS):
        if args.type == "drm":
            vbuf = v4l2.create_dmabuffer(fbs[i].fd(0))
        else:
            vbuf = v4l2.create_mmapbuffer()
        cap.queue(vbuf)

for stream in streams:
    print(f'{stream["dev"]}: stream on')
    stream["cap"].stream_on()

for stream in streams:
    stream["num_frames"] = 0
    stream["total_num_frames"] = 0
    stream["time"] = time.perf_counter()

kms_committed = False

def net_tx(stream, vbuf):
    cap = stream["cap"]

    if args.type == "drm":
        fb = next((fb for fb in stream["fbs"] if fb.fd(0) == vbuf.fd), None)
        assert(fb != None)
        plane_sizes = [fb.size(0), 0, 0, 0]
    else:
        plane_sizes = [vbuf.length, 0, 0, 0]

    fmt = stream["fourcc"]

    if stream["embedded"]:
        # XXX we dont' really have "lines" with embedded data
        bytesperline = stream["w"]
        bpp = embedded_fourcc_to_bytes_per_pixel(stream["fourcc"])
        bytesperline = bytesperline * bpp // 8
    else:
        bytesperline = stream["cap"].bytesperline

    hdr = struct_fmt.pack(stream["id"],
                          stream["w"], stream["h"],
                          bytesperline,
                          bytes(str(fmt.name), "ascii"),
                          1, *plane_sizes)

    sock.sendall(hdr)

    if args.type == "drm":
        with mmap.mmap(fb.fd(0), fb.size(0), mmap.MAP_SHARED, mmap.PROT_READ) as b:
            sock.sendall(b)
    else:
        with mmap.mmap(cap.fd, vbuf.length, mmap.MAP_SHARED, mmap.PROT_READ,
                       offset=vbuf.offset) as b:
            sock.sendall(b)


def readvid(stream):
    stream["num_frames"] += 1
    stream["total_num_frames"] += 1

    t = time.perf_counter()
    diff = time.perf_counter() - stream["time"]

    if stream["total_num_frames"] == 1:
        print("{}: first frame in {:.2f} s"
              .format(stream["dev"], diff))

    if diff >= 5:
        print("{}: {} frames in {:.2f} s, {:.2f} fps"
              .format(stream["dev"],stream["num_frames"], diff, stream["num_frames"] / diff))

        stream["num_frames"] = 0
        stream["time"] = t

    cap = stream["cap"]
    vbuf = cap.dequeue()

    if args.type == "drm":
        fb = next((fb for fb in stream["fbs"] if fb.fd(0) == vbuf.fd), None)
        assert(fb != None)

    if args.save:
        filename = "frame-{}-{}.data".format(stream["id"], stream["total_num_frames"])
        print("save to " + filename)

        if args.type == "drm":
            with mmap.mmap(fb.fd(0), fb.size(0), mmap.MAP_SHARED, mmap.PROT_READ) as b:
                with open(filename, "wb") as f:
                    f.write(b)
        else:
            with mmap.mmap(cap.fd, vbuf.length, mmap.MAP_SHARED, mmap.PROT_READ,
                           offset=vbuf.offset) as b:
                with open(filename, "wb") as f:
                    f.write(b)

    if stream["display"]:
        stream["kms_fb_queue"].append(fb)

        if len(stream["kms_fb_queue"]) >= NUM_BUFS - 1:
            print("WARNING fb_queue {}".format(len(stream["kms_fb_queue"])))

        #print(f'Buf from {stream["dev"]}: kms_fb_queue {len(stream["kms_fb_queue"])}, commit ongoing {kms_committed}')

        # XXX with a small delay we might get more planes to the commit
        if kms_committed == False:
            handle_pageflip()
    else:
        if args.tx and (args.tx == ["all"] or str(stream["id"]) in args.tx):
            net_tx(stream, vbuf)

        cap.queue(vbuf)


def readkey(conn, mask):
    for stream in reversed(streams):
        print(f'{stream["dev"]}: stream off')
        stream["cap"].stream_off()
        #time.sleep(0.5)
        #print("DISABLED CAP")
        #time.sleep(1)

    print("Done")
    sys.stdin.readline()
    exit(0)

def handle_pageflip():
    global kms_committed

    kms_committed = False

    req = pykms.AtomicReq(card)

    do_commit = False

    for stream in streams:
        if not stream["display"]:
            continue

        #print(f'Page flip {stream["dev"]}: kms_fb_queue {len(stream["kms_fb_queue"])}, new_fb {stream["kms_fb"]}, old_fb {stream["kms_old_fb"]}')

        cap = stream["cap"]

        if stream["kms_old_fb"]:
            assert(args.type == "drm")

            fb = stream["kms_old_fb"]
            vbuf = v4l2.create_dmabuffer(fb.fd(0))
            cap.queue(vbuf)
            stream["kms_old_fb"] = None

        if len(stream["kms_fb_queue"]) == 0:
            continue

        stream["kms_old_fb"] = stream["kms_fb"]

        fb = stream["kms_fb_queue"].popleft()
        stream["kms_fb"] = fb

        plane = stream["plane"]

        req.add(plane, "FB_ID", fb.id)

        do_commit = True

    if do_commit:
        req.commit(allow_modeset = False)
        kms_committed = True


def readdrm(fileobj, mask):
    #print("EVENT");
    for ev in card.read_events():
        if ev.type == pykms.DrmEventType.FLIP_COMPLETE:
            handle_pageflip()

sel = selectors.DefaultSelector()
sel.register(sys.stdin, selectors.EVENT_READ, readkey)
if args.display:
    sel.register(card.fd, selectors.EVENT_READ, readdrm)
for stream in streams:
    sel.register(stream["cap"].fd, selectors.EVENT_READ, lambda c,m,d=stream: readvid(d))

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
