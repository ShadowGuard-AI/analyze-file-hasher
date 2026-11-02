#!/usr/bin/env python3
"""analyze-file-hasher intro: silkworm rearing room, nobody in it, nothing written anywhere.
Nearest tray close in front with feeding worms and frass, racks of trays receding, baskets of
river white cocoons catching window light, papered window bright and featureless, open doorway
with a half stripped mulberry branch top right. No ledger, no numerals, no labels."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter
random.seed(410)
V1 = "--v1" in sys.argv
W, H = 1200, 520
TEAL = (18, 79, 76); INK = (9, 42, 40); REED = (95, 127, 62); RUST = (154, 74, 38)
WHITE = (244, 241, 230); WOOD = (122, 84, 52)
img = Image.new("RGB", (W, H), INK); d = ImageDraw.Draw(img, "RGBA")
# room walls in deep teal shade, late sideways light
d.rectangle([0, 0, W, H], fill=(16, 58, 55))
# papered window, bright and featureless, back wall
d.rectangle([430, 36, 700, 250], fill=(238, 230, 196))
d.rectangle([430, 36, 700, 250], outline=(90, 66, 40), width=8)
d.line([(565, 36), (565, 250)], fill=(150, 132, 96), width=5)
for i in range(40):  # glow, no pattern that could be read
    x, y = random.uniform(440, 690), random.uniform(46, 240)
    d.point((x, y), fill=(246, 240, 210))
# open doorway right with yard light and mulberry tree filling upper right
d.rectangle([950, 30, 1180, 330], fill=(196, 205, 150))
d.rectangle([950, 30, 1180, 330], outline=(80, 58, 34), width=9)
d.line([(1130, 330), (1010, 120)], fill=(96, 66, 38), width=16)  # trunk slant
def leaf(x, y, s, col):
    pts = []
    for k in range(13):
        a = k / 12 * 6.283; r = s * (0.62 + 0.38 * abs(math.sin(a * 2.5)))
        pts.append((x + math.cos(a) * r, y + math.sin(a) * r * 0.8))
    d.polygon(pts, fill=col)
for i in range(16):
    leaf(random.uniform(980, 1180), random.uniform(36, 170), random.uniform(22, 44),
         random.choice([REED, (120, 150, 74), (76, 108, 50)]))
# one low branch half stripped from picking, entering from upper right
d.line([(1195, 60), (1010, 130)], fill=(96, 66, 38), width=9)
for i in range(4):
    leaf(1060 + i * 32, 118 + (i % 2) * 22, 26, REED)
# racks of trays receding in soft order, leaf green repeating and paling with distance
def tray(x, y, w, pale, worms):
    h = w * 0.20
    d.polygon([(x, y), (x + w, y), (x + w - 14, y + h), (x + 14, y + h)], fill=(146, 106, 62))
    d.rectangle([x + 8, y - 10, x + w - 8, y + 4], fill=(int(120 * pale + 60), int(150 * pale + 40), 60))
    for _ in range(int(w / 7)):  # chopped mulberry leaf heaped and uneven
        lx, ly = random.uniform(x + 14, x + w - 14), random.uniform(y - 9, y + 1)
        d.ellipse([lx, ly, lx + 11, ly + 5], fill=random.choice([REED, (130, 158, 80), (84, 116, 54)]))
    for i in range(worms):  # pale segmented feeders, heads down
        wx, wy = x + 22 + i * (w - 44) / max(worms, 1), y - 6
        for s in range(5):
            d.ellipse([wx + s * 7, wy - 3 + (s % 2), wx + s * 7 + 9, wy + 5], fill=(232, 226, 204), outline=(196, 188, 160))
for row, (y, w, pale) in enumerate([(150, 300, 0.55), (205, 360, 0.7), (268, 430, 0.85)]):
    tray(40, y, w, pale, 3 + row); tray(760 - row * 30, y, w, pale, 3 + row)
    d.rectangle([52, y + 26, 64, y + 66], fill=WOOD); d.rectangle([40 + w - 24, y + 26, 40 + w - 12, y + 66], fill=WOOD)
# baskets of harvested cocoons on the floor between racks, white heaps catching light first
def basket(x, y, s, n):
    d.polygon([(x, y), (x + s, y), (x + s - 14, y + s * 0.52), (x + 14, y + s * 0.52)], fill=(150, 108, 60))
    for ly in range(3):
        d.line([(x + 6, y + 12 + ly * 14), (x + s - 6, y + 12 + ly * 14)], fill=(116, 80, 42), width=3)
    for i in range(n):
        cx, cy = x + 14 + (i % 5) * s / 5.4, y - 8 - (i // 5) * 11
        d.ellipse([cx, cy, cx + 20, cy + 13], fill=WHITE, outline=(206, 200, 178))
basket(520, 300, 120, 13 if not V1 else 5); basket(690, 322, 96, 10 if not V1 else 4)
# floor in rust warmth where the low sun lands
d.polygon([(0, 400), (W, 372), (W, H), (0, H)], fill=(110, 66, 38))
for i in range(26):
    d.line([(i * 48, 402), (i * 48 - 60, H)], fill=(88, 50, 28), width=3)
# FOREGROUND: nearest tray edge at close range, leaf litter, frass, three feeding worms, one reared apart
d.polygon([(0, 408), (880, 386), (920, H), (0, H)], fill=(158, 116, 66))
d.rectangle([0, 392, 890, 416], fill=(104, 132, 58))
for _ in range(210):
    x, y = random.uniform(8, 870), random.uniform(396, 500)
    d.ellipse([x, y, x + 15, y + 7], fill=random.choice([REED, (134, 164, 82), (80, 110, 50)]))
for _ in range(46):  # frass pellets dark among the green
    x, y = random.uniform(20, 850), random.uniform(410, 505)
    d.ellipse([x, y, x + 4, y + 3], fill=(42, 36, 24))
def big_worm(x, y, reared):
    if reared:
        for s in range(6):
            d.ellipse([x + s * 5, y - s * 13, x + s * 5 + 24, y - s * 13 + 16], fill=(238, 232, 212), outline=(198, 190, 162))
    else:
        for s in range(7):
            d.ellipse([x + s * 19, y + (s % 2) * 4, x + s * 19 + 26, y + 18], fill=(238, 232, 212), outline=(198, 190, 162))
big_worm(150, 440, False); big_worm(430, 466, False); big_worm(610, 428, False)
big_worm(330, 486, True)  # the one apart, reared up and still, testing the air
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/intro-v1.png" if V1 else "intro-banner.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
