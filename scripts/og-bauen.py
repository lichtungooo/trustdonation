"""Baut das Vorschaubild og.png fuer trustdonation.

1200x630, Farben aus dem Logo: Tannengruen #1B5E40 (Vertrauen), Orange #EA580C (Geben).
Schriften kommen aus landing/fonts/, die woff2-Dateien werden dafuer nach ttf gewandelt.
"""
import os, math, tempfile
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

os.chdir(r"D:/Workspace/20-repos/trustdonation")
TMP = tempfile.mkdtemp()

def ttf(name):
    """woff2 nach ttf wandeln, damit PIL sie lesen kann."""
    ziel = os.path.join(TMP, name + ".ttf")
    f = TTFont("landing/fonts/%s.woff2" % name)
    f.flavor = None
    f.save(ziel)
    return ziel

BRI = ttf("bricolage")   # Ueberschriften
HAN = ttf("hanken")      # Fliesstext

W, H = 1200, 630
GRUEN = (27, 94, 64)
ORANGE = (234, 88, 12)
BG = (255, 255, 255)
SOFT = (255, 248, 241)
LINE = (239, 224, 210)
INK = (27, 94, 64)
BODY = (60, 95, 78)
MUTED = (107, 133, 120)

im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)

# --- Hintergrund: weiche Orange-Flaeche unten rechts, wie die Sektionen der Seite
d.rectangle([0, 0, W, H], fill=BG)
d.pieslice([W - 560, H - 460, W + 320, H + 420], 180, 360, fill=SOFT)
d.rectangle([0, H - 14, W, H], fill=GRUEN)
d.rectangle([0, H - 14, 360, H], fill=ORANGE)

# --- Kartenmotiv rechts: Wege und Pins, wie im Hero
def pin(cx, cy, r, farbe):
    """Ein Kartenstift: Tropfenform mit heller Mitte."""
    d.polygon([(cx, cy), (cx - r * 0.72, cy - r * 1.55), (cx + r * 0.72, cy - r * 1.55)], fill=farbe)
    d.ellipse([cx - r, cy - r * 2.55, cx + r, cy - r * 0.55], fill=farbe)
    d.ellipse([cx - r * 0.38, cy - r * 1.93, cx + r * 0.38, cy - r * 1.17], fill=BG)

def weg(p0, c, p2, farbe=(255, 217, 184), breite=7):
    """Ein weicher Bogen als Kurve, damit das Motiv wie eine Karte liest."""
    punkte = []
    for i in range(41):
        t = i / 40
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t ** 2 * p2[1]
        punkte.append((x, y))
    d.line(punkte, fill=farbe, width=breite, joint="curve")

weg((700, 520), (930, 330), (1200, 330))
weg((690, 250), (900, 360), (1200, 250))
weg((780, 600), (1000, 520), (1200, 560), farbe=(255, 228, 204), breite=6)
for (x, y, r, c) in [(830, 300, 17, GRUEN), (960, 250, 17, ORANGE), (1080, 360, 17, GRUEN),
                     (900, 430, 17, ORANGE), (1040, 490, 17, GRUEN)]:
    pin(x, y, r, c)

# --- Wortmarke: trustd(signet)nation, das Signet ersetzt das o
f_marke = ImageFont.truetype(BRI, 54)
x, y = 86, 82
d.text((x, y), "trustd", font=f_marke, fill=INK)
b = d.textbbox((x, y), "trustd", font=f_marke)
sx = b[2] + 6
sy = y + 16
r = 21
# Signet: zwei Halbkreise, gruen und orange, mit Kern
d.pieslice([sx, sy, sx + 2 * r, sy + 2 * r], 90, 270, fill=GRUEN)
d.pieslice([sx, sy, sx + 2 * r, sy + 2 * r], 270, 90, fill=ORANGE)
d.ellipse([sx + r * 0.42, sy + r * 0.42, sx + r * 1.58, sy + r * 1.58], fill=BG)
d.ellipse([sx + r * 0.68, sy + r * 0.68, sx + r * 1.32, sy + r * 1.32], fill=ORANGE)
d.text((sx + 2 * r + 6, y), "nation", font=f_marke, fill=INK)

# --- Claim
f_h1 = ImageFont.truetype(BRI, 62)
for i, zeile in enumerate(["Dein Projekt findet", "die Stiftungen, die passen."]):
    d.text((86, 212 + i * 74), zeile, font=f_h1, fill=INK)

# --- Untertitel
f_p = ImageFont.truetype(HAN, 27)
d.text((86, 382), "Eine offene Karte für Stiftungen, Projekte,", font=f_p, fill=BODY)
d.text((86, 418), "Anstifter und Zustifter. Weltweit.", font=f_p, fill=BODY)

# --- Fusszeile
f_s = ImageFont.truetype(HAN, 23)
d.text((86, 512), "trustdonation.org", font=ImageFont.truetype(BRI, 26), fill=ORANGE)
d.text((86, 552), "Getragen vom Kollektiv Lichtung e.V.", font=f_s, fill=MUTED)

im.save("landing/og.png", "PNG", optimize=True)
print("og.png geschrieben:", im.size, os.path.getsize("landing/og.png"), "Bytes")
