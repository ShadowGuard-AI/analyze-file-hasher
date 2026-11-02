#!/usr/bin/env python3
"""analyze-file-hasher logo: one finished cocoon on a broad lobed mulberry leaf, close and alone.
Strand work built from many fine overlapping arcs, teal lit side, rust shadow where the leaf curls,
one loose thread lifting off the tip and ending open. Name in Average below, field guide heading plain."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont
random.seed(87)
V1 = "--v1" in sys.argv
W, H = 880, 660
TEALD = (13, 62, 59); REED = (95, 127, 62); RUST = (154, 74, 38); WHITE = (247, 244, 234)
img = Image.new("RGB", (W, H), WHITE); d = ImageDraw.Draw(img, "RGBA")
HERE = __file__.rsplit("/", 1)[0]
font = ImageFont.truetype(HERE + "/fonts/Average.ttf", 44)
# broad lobed leaf, stem leaving frame at lower left
cx, cy = 440, 268
pts = []
for k in range(73):
    a = k / 72 * 6.283; r = 268 * (0.60 + 0.40 * abs(math.sin(a * 2.5 + 0.4)))
    pts.append((cx + math.cos(a) * r, cy + math.sin(a) * r * 0.74))
d.polygon(pts, fill=(116, 148, 74))
pts2 = [(cx + (x - cx) * 0.9, cy + (y - cy) * 0.88) for x, y in pts]
d.polygon(pts2, fill=REED)
for a in (-0.5, 0.1, 0.8, 2.4, 3.6, 4.6):  # veins in reed green dark
    d.line([(cx, cy), (cx + math.cos(a) * 178, cy + math.sin(a) * 124)], fill=(74, 104, 48), width=5)
d.line([(cx - 40, cy + 120), (30, 620)], fill=(90, 70, 40), width=13)  # stem out lower left
d.line([(cx + 90, cy + 130), (cx + 240, cy + 176)], fill=(70, 96, 42), width=6)  # leaf curl shadow edge
# cocoon: oval of wound silk, fine overlapping strands, never smooth
ex, ey, ew, eh = cx - 128, cy - 92, 256, 168
if V1:  # smooth oval: reads as an egg, the flaw draft 2 must fix
    d.ellipse([ex, ey, ex + ew, ey + eh], fill=(240, 236, 220), outline=(200, 194, 172), width=3)
else:
    d.ellipse([ex, ey + 8, ex + ew, ey + eh + 8], fill=(238, 234, 216), outline=(198, 192, 168), width=3)
    import PIL.Image as _I
    mask = _I.new("L", (W, H), 0)
    from PIL import ImageDraw as _D
    _D.Draw(mask).ellipse([ex + 4, ey + 12, ex + ew - 4, ey + eh + 4], fill=255)
    layer = _I.new("RGB", (W, H), (238, 234, 216)); ld = _D.Draw(layer)
    for i in range(90):  # wound strands running around the oval, clipped to its body
        y0 = ey + 14 + i * 1.9; wob = math.sin(i * 1.35) * 7
        col = (18, 110, 104) if i % 9 == 0 else (206, 200, 176) if i % 3 else (224, 220, 200)
        ld.line([(ex + 8, y0), (ex + ew - 8, y0 + wob)], fill=col, width=2)
    for r in range(6):  # concentric winding at the lit left edge, teal where light catches
        ld.ellipse([ex + 6 + r * 5, ey + 14 + r * 4, ex + 92 - r * 3, ey + eh - r * 4], outline=(18, 110, 104), width=2)
    img.paste(layer, (0, 0), mask); d = ImageDraw.Draw(img, "RGBA")
    d.polygon([(ex + 30, ey + eh - 26), (ex + ew - 20, ey + eh - 6), (ex + ew - 60, ey + eh + 22), (ex + 60, ey + eh + 10)], fill=(154, 74, 38, 70))  # rust shadow where leaf curls
# one loose thread lifting off the tip, the only line that does not close
tip = (ex + ew - 8, ey + 30)
d.line([tip, (tip[0] + 58, tip[1] - 26), (tip[0] + 118, tip[1] - 12), (tip[0] + 168, tip[1] - 34)], fill=(18, 110, 104), width=3)
name = "analyze-file-hasher"
tw = d.textlength(name, font=font); d.text(((W - tw) / 2, 520), name, font=font, fill=TEALD)
out = "scratch/logo-v1.png" if V1 else "logo.png"
img.save(HERE + "/" + out)
if not V1:
    img.resize((64, 48)).save(HERE + "/scratch/logo64-ship.png")
print("saved", out)
