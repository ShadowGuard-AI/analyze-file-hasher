#!/usr/bin/env python3
"""analyze-file-hasher banner: silk farmhouse workroom before the evening feed, from the doorway.
Racks of trays along both walls, pale worms at mixed instars, long table at centre with the ledger
open: dates column left page, cocoon counts right page, handwriting as brown strokes that form no
readable word apart from the one heading, analyze-file-hasher in Average across the right page top.
Baskets of cocoons under the table, plain clock with hands only, alternate teal shade and rust warmth."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(233)
V1 = "--v1" in sys.argv
W, H = 1200, 520
TEAL = (18, 79, 76); REED = (95, 127, 62); RUST = (154, 74, 38); WHITE = (244, 241, 230); BROWN = (110, 76, 44)
img = Image.new("RGB", (W, H), (20, 62, 58)); d = ImageDraw.Draw(img, "RGBA")
HERE = __file__.rsplit("/", 1)[0]
# papered window far wall and a plain clock, hands only, no numerals
d.rectangle([500, 26, 700, 168], fill=(236, 228, 192)); d.rectangle([500, 26, 700, 168], outline=(88, 64, 38), width=7)
d.ellipse([556, 178, 644, 266], fill=WHITE, outline=BROWN, width=5)
d.line([(600, 222), (600, 192)], fill=BROWN, width=5); d.line([(600, 222), (626, 234)], fill=BROWN, width=5)  # feeding hour approaching
# rows of racks along both walls receding
def rack(x, y, w, flip):
    for r in range(3):
        ty = y + r * 44
        d.polygon([(x, ty), (x + w, ty + (10 if flip else -4)), (x + w - 10, ty + 24), (x + 10, ty + 24)], fill=(140, 100, 58))
        d.rectangle([x + 8, ty - 8, x + w - 8, ty + 3], fill=REED)
        for i in range(int(w / 26)):  # worms at mixed instars, largest near front handled by row scale
            wx = x + 16 + i * 24; s = 5 + r * 2
            for sg in range(4):
                d.ellipse([wx + sg * (s - 1), ty - 5 + (sg % 2), wx + sg * (s - 1) + s + 2, ty + 2], fill=(232, 226, 204))
    d.rectangle([x + 4, y - 12, x + 12, y + 150], fill=(110, 76, 44)); d.rectangle([x + w - 12, y - 12, x + w - 4, y + 150], fill=(110, 76, 44))
for i, (x, y, w) in enumerate([(26, 90, 330), (26, 268, 380)]):
    rack(x, y, w, False)
    d.polygon([(x, y - 14), (x + w, y - 14), (x + w, y + 160), (x, y + 160)], fill=(18, 110, 104, 26))  # teal shade band
for i, (x, y, w) in enumerate([(844, 90, 330), (794, 268, 380)]):
    rack(x, y, w, True)
    d.polygon([(x, y - 14), (x + w, y - 14), (x + w, y + 160), (x, y + 160)], fill=(214, 120, 60, 26))  # rust warmth band
# long table at centre
d.polygon([(392, 300), (808, 300), (852, 402), (348, 402)], fill=(128, 88, 50))
d.rectangle([372, 402, 396, 486], fill=(100, 66, 36)); d.rectangle([804, 402, 828, 486], fill=(100, 66, 36))
# woven baskets under the table, cocoons heaped above the rims
for bx in (440, 640):
    d.polygon([(bx, 428), (bx + 120, 428), (bx + 104, 478), (bx + 16, 478)], fill=(150, 108, 60))
    for i in range(11):
        cx = bx + 12 + (i % 5) * 22; cy = 414 - (i // 5) * 11
        d.ellipse([cx, cy, cx + 21, cy + 14], fill=WHITE, outline=(206, 200, 178))
# the ledger open on the table: two ruled pages
d.polygon([(408, 306), (596, 296), (596, 388), (408, 396)], fill=(248, 245, 234))
d.polygon([(604, 296), (792, 306), (792, 396), (604, 388)], fill=(244, 241, 228))
d.line([(600, 296), (600, 392)], fill=(180, 168, 140), width=3)
for p, (x0, x1) in enumerate([(420, 584), (616, 780)]):
    for r in range(6):
        y = 330 + r * 11
        d.line([(x0, y + 8), (x1, y + 8)], fill=(168, 178, 188), width=1)  # ruled account line
        # brown hand: strokes with rhythm, forming no readable word
        xx = x0 + 4
        while xx < x1 - 26:
            ln = random.uniform(9, 22); d.arc([xx, y - 3, xx + ln, y + 7], 190, 350, fill=BROWN, width=2); xx += ln + 7
if V1:  # flaw: heading put on the wall as signage instead of in the book
    f = ImageFont.truetype(HERE + "/fonts/Average.ttf", 40)
    t = "analyze-file-hasher"; tw = d.textlength(t, font=f); d.text(((W - tw) / 2, 8), t, font=f, fill=WHITE)
else:  # heading is the ledger heading itself, right page top, same brown ink
    f = ImageFont.truetype(HERE + "/fonts/Average.ttf", 20)
    d.text((616, 302), "analyze-file-hasher", font=f, fill=BROWN)
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/banner-v1.png" if V1 else "banner.png"
img.save(HERE + "/" + out); print("saved", out)
