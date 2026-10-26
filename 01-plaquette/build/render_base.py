# -*- coding: utf-8 -*-
"""
Générateur des pages sectorisées « Assurance » de la plaquette HelloLead.

Principe : les pages 1, 2, 8 et 9 sont reprises telles quelles du PDF source,
la page 4 (assurance agricole) est également conservée à l'identique.
Les pages 3, 5, 6 et 7 sont reconstruites sur la même grille graphique
(cartes #F4F5FC, bleu #0A5BFF, Poppins / Open Sans) avec un contenu assurance.

Usage :
    python build_plaquette.py                      # plaquette complète
    python build_plaquette.py --page 3 --preview   # une page en PNG (contrôle)
"""

import argparse
import hashlib
import os
import sys

from PIL import Image
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTS = os.path.join(ROOT, "assets", "fonts")
IMG = os.path.join(ROOT, "assets", "img")
OUT = os.path.join(ROOT, "out")
CACHE = os.path.join(HERE, ".imgcache")
SRC_PDF = os.environ.get(
    "SRC_PDF",
    os.path.join(ROOT, "assets", "source", "Plaquette_HelloLead_source.pdf"),
)
if not os.path.exists(SRC_PDF):   # repli pour un poste de travail ad hoc
    SRC_PDF = "/tmp/arena-coding-uploads/Plaquette HelloLead.pdf"

W, H = 1440.0, 810.0
BLUE = HexColor("#0A5BFF")
CARD = HexColor("#F4F5FC")
INK = HexColor("#0B0B0B")
GREY = HexColor("#A29F9F")
MUTED = HexColor("#5A6675")
WHITE = HexColor("#FFFFFF")
LINE = HexColor("#DDE3F5")

for name, file in [
    ("Poppins", "Poppins-Regular.ttf"),
    ("PoppinsSB", "Poppins-SemiBold.ttf"),
    ("PoppinsB", "Poppins-Bold.ttf"),
    ("PoppinsXB", "Poppins-ExtraBold.ttf"),
    ("OpenSans", "OpenSans-Regular.ttf"),
    ("OpenSansSB", "OpenSans-SemiBold.ttf"),
    ("OpenSansB", "OpenSans-Bold.ttf"),
]:
    pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, file)))


# ---------------------------------------------------------------------------
# Helpers de dessin (repère : origine en haut à gauche, comme la maquette)
# ---------------------------------------------------------------------------
def Y(y):
    return H - y


def sw(text, font, size):
    return pdfmetrics.stringWidth(text, font, size)


def wrap(text, font, size, maxw):
    out = []
    for para in text.split("\n"):
        words, line = para.split(), ""
        for w_ in words:
            test = (line + " " + w_).strip()
            if sw(test, font, size) <= maxw or not line:
                line = test
            else:
                out.append(line)
                line = w_
        out.append(line)
    return out


def text(c, x, ybase, s, font="Poppins", size=13, color=INK, align="left", track=0):
    c.setFont(font, size)
    c.setFillColor(color)
    w = sw(s, font, size)
    dx = {"left": 0, "center": -w / 2, "right": -w}[align]
    c.drawString(x + dx, Y(ybase), s)


def para(c, x, ybase, s, font="Poppins", size=13, color=INK, leading=None,
         maxw=300, align="left"):
    leading = leading or size * 1.45
    lines = wrap(s, font, size, maxw)
    for i, ln in enumerate(lines):
        text(c, x, ybase + i * leading, ln, font, size, color, align)
    return ybase + (len(lines) - 1) * leading


def rrect(c, x, y, w, h, r=40, fill=CARD, stroke=0, stroke_color=None):
    c.saveState()
    if stroke:
        c.setStrokeColor(stroke_color or LINE)
        c.setLineWidth(stroke)
    if fill is None:
        c.setFillColor(Color(1, 1, 1), alpha=0)
    else:
        c.setFillColor(fill)
    c.roundRect(x, Y(y + h), w, h, r, stroke=1 if stroke else 0, fill=1 if fill else 0)
    c.restoreState()


def box(c, x, y, w, h, r=6, fill=WHITE, stroke=0, sc=LINE, lw=0.8):
    c.saveState()
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(sc)
        c.setLineWidth(lw)
    c.roundRect(x, Y(y + h), w, h, r, stroke=1 if stroke else 0, fill=1)
    c.restoreState()


def hline(c, x1, y, x2, color=LINE, lw=0.8):
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x1, Y(y), x2, Y(y))


def bullet_dot(c, x, ybase, r=2.6, color=INK):
    c.setFillColor(color)
    c.circle(x, Y(ybase - 4.2), r, stroke=0, fill=1)


def arrow(c, x1, y1, x2, y2, bendx=0.0, bendy=0.0, color=BLUE, lw=7.0, size=13):
    """Flèche courbe : bézier quadratique + pointe triangulaire."""
    cx, cy = (x1 + x2) / 2 + bendx, (y1 + y2) / 2 + bendy
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.setLineCap(1)
    p = c.beginPath()
    p.moveTo(x1, Y(y1))
    p.curveTo(cx, Y(cy), cx, Y(cy), x2, Y(y2))
    c.drawPath(p, stroke=1, fill=0)

    # direction en fin de courbe
    dx, dy = x2 - cx, -(y2 - cy)
    import math
    ang = math.atan2(dy, dx)
    for s in (-1, 1):
        c.setLineWidth(lw)
    a1, a2 = ang + 2.6, ang - 2.6
    tip = (x2, Y(y2))
    p1 = (x2 - size * 1.9 * math.cos(ang - 0.55), Y(y2) - size * 1.9 * math.sin(ang - 0.55))
    p2 = (x2 - size * 1.9 * math.cos(ang + 0.55), Y(y2) - size * 1.9 * math.sin(ang + 0.55))
    c.setFillColor(color)
    q = c.beginPath()
    q.moveTo(*tip)
    q.lineTo(*p1)
    q.lineTo(*p2)
    q.close()
    c.drawPath(q, stroke=0, fill=1)
    c.restoreState()


_ = None


def _cached(path, w_pt, h_pt, crop="center"):
    os.makedirs(CACHE, exist_ok=True)
    key = hashlib.md5(f"{path}{w_pt:.0f}x{h_pt:.0f}{crop}{os.path.getmtime(path)}".encode()).hexdigest()[:16]
    dst = os.path.join(CACHE, key + ".jpg")
    if not os.path.exists(dst):
        im = Image.open(path).convert("RGB")
        target = w_pt / h_pt
        iw, ih = im.size
        if iw / ih > target:                       # trop large -> on rogne les côtés
            nw = int(ih * target)
            if crop == "top":
                box_ = (0, 0, nw, ih)
            else:
                box_ = ((iw - nw) // 2, 0, (iw + nw) // 2, ih)
            im = im.crop(box_)
        else:                                      # trop haut -> on rogne en bas
            nh = int(iw / target)
            box_ = (0, 0, iw, nh) if crop != "bottom" else (0, ih - nh, iw, ih)
            im = im.crop(box_)
        px = max(2, int(w_pt * 2))
        im = im.resize((px, max(2, int(px * h_pt / w_pt))), Image.LANCZOS)
        im.save(dst, "JPEG", quality=90)
    return dst


def img(c, name, x, y, w, h, radius=0, crop="center"):
    path = name if os.path.isabs(name) else os.path.join(IMG, name)
    f = _cached(path, w, h, crop)
    c.saveState()
    if radius:
        p = c.beginPath()
        p.roundRect(x, Y(y + h), w, h, radius)
        c.clipPath(p, stroke=0, fill=0)
    c.drawImage(f, x, Y(y + h), width=w, height=h, mask=None)
    c.restoreState()


def mask_bar(c, x, ybase, w=60, h=13, color=GREY):
    c.setFillColor(color)
    c.rect(x, Y(ybase + 2), w, h, stroke=0, fill=1)


def logo_word(c, x, ybase, size=22, dark="#173455"):
    """Logo texte 'HelloLead' simplifié (le vrai logo est repris sur les pages conservées)."""
    text(c, x, ybase, "HelloLead", "PoppinsB", size, HexColor(dark))
    cx = x + sw("HelloLead", "PoppinsB", size) + size * 0.38
    cy = Y(ybase - size * 0.42)
    dot(c, cx, cy - 0, size * 0.3, HexColor("#F0932B"))


def dot(c, x, y, r, color):
    """Petit disque plein (coordonnées PDF natives)."""
    c.setFillColor(color)
    c.circle(x, y, r, stroke=0, fill=1)


def field_line(c, x, y, w, label, value, size=8.6, h=26, label_color=MUTED,
               value_color=HexColor("#173455"), fill=WHITE):
    box(c, x, y, w, h, r=5, fill=fill, stroke=1, sc=HexColor("#CBD5E8"))
    text(c, x + 9, y + 9.5, label, "Poppins", 6.4, label_color)
    text(c, x + 9, y + 20, value, "PoppinsSB", size, value_color)
    # chevron
    c.setStrokeColor(HexColor("#8FA0BF"))
    c.setLineWidth(1.1)
    cx, cy = x + w - 14, Y(y + h / 2)
    c.line(cx - 3, cy + 3, cx, cy)
    c.line(cx, cy, cx - 3, cy - 3)


# ---------------------------------------------------------------------------
# Mise en page adaptative : garantit qu'un bloc ne dépasse jamais sa carte
# ---------------------------------------------------------------------------
def build_flow(pairs, maxw, size=12.6, label_size=None, label_font="PoppinsB",
               value_font="Poppins"):
    """Transforme [(label, valeur), ...] en lignes atomiques typées."""
    label_size = label_size or size
    lines = []
    for label, value in pairs:
        for ln in wrap(label, label_font, label_size, maxw):
            lines.append(("label", ln, label_size, label_font))
        for ln in wrap(value, value_font, size, maxw):
            lines.append(("value", ln, size, value_font))
    return lines


def draw_flow(c, x, y, lines, bottom, leading=19.5, color_label=BLUE, color_value=INK,
              min_leading=13.0):
    """Dessine les lignes en réduisant l'interligne si nécessaire pour tenir."""
    if not lines:
        return y
    lead = min(leading, (bottom - y) / len(lines))
    lead = max(lead, min_leading)
    for kind, txt, size, font in lines:
        col = color_label if kind == "label" else color_value
        text(c, x, y, txt, font, size, col)
        y += lead
    return y


def fit_buyer(c, x, y, raw_lines, maxw, bottom, size=12.6, leading=19.5, footnote=True):
    """Lignes acheteur ; la valeur '__MASQUE__' devient une barre grise."""
    m = "__MASQUE__"
    lines = []
    for ln in raw_lines:
        if ln.endswith(m):
            lines.append(("mask", ln[: -len(m)], size, "Poppins"))
            continue
        if " : " in ln:
            head, val = ln.split(" : ", 1)
            for part in wrap(head + " : " + val, "Poppins", size, maxw):
                lines.append(("kv", part, size, "Poppins"))
        else:
            for part in wrap(ln, "Poppins", size, maxw):
                lines.append(("txt", part, size, "Poppins"))
    reserve = 14 if footnote else 0
    lead = min(leading, (bottom - reserve - y) / max(len(lines), 1))
    lead = max(lead, 13.0)
    for kind, txt, sz, font in lines:
        if kind == "mask":
            text(c, x, y, txt, "Poppins", sz, INK)
            mask_bar(c, x + sw(txt, "Poppins", sz) + 4, y, 74, 12, GREY)
        elif kind == "kv" and " : " in txt:
            # « Clé : valeur » -> clé en bleu, valeur en gras bleu foncé
            head, val = txt.split(" : ", 1)
            text(c, x, y, head + " : ", "Poppins", sz, HexColor("#33506F"))
            text(c, x + sw(head + " : ", "Poppins", sz), y, val, "PoppinsSB", sz,
                 HexColor("#33506F"))
        else:
            text(c, x, y, txt, "Poppins", sz, INK)
        y += lead
    if footnote:
        text(c, x, y + 8, "Exemple illustratif — données anonymisées", "Poppins", 8.4,
             HexColor("#8B93A7"))
    return y
