# -*- coding: utf-8 -*-
"""Composants graphiques de la plaquette (cartes, mockups, formulaires)."""

import math

from reportlab.lib.colors import Color, HexColor

from render_base import (BLUE, CARD, GREY, INK, LINE, MUTED, WHITE, box, bullet_dot,
                         dot, field_line, hline, img, logo_word, mask_bar, para,
                         rrect, sw, text, wrap)

NAVY = HexColor("#173455")
SOFT = HexColor("#EDF1FA")
SOFT2 = HexColor("#F7F9FE")
BORDER = HexColor("#E3E9F7")
GREY_TXT = HexColor("#6B7280")
LIGHT_TXT = HexColor("#93A0B5")


def _chevron(c, x, y, size=3.2, color="#8FA0BF"):
    c.setStrokeColor(HexColor(color))
    c.setLineWidth(1.1)
    c.line(x - size, y + size, x, y)
    c.line(x, y, x - size, y - size)


def pill(c, x, y, w, h, label, bg, fg, size=8.6, border=None):
    box(c, x, y, w, h, h / 2, bg, stroke=1 if border else 0, sc=border)
    text(c, x + w / 2, y + h / 2 + size * 0.36, label, "PoppinsSB", size, fg, "center")


# ---------------------------------------------------------------------------
# Colonne gauche : levier + arguments
# ---------------------------------------------------------------------------
def lever_card(c, x, y, w, h, lever, headline, bullets, intro=None, step=48,
               first_bullet=None, bullet_size=13.6, intro_size=12.4,
               extra_line=24, intro_gap=36, intro_lead=25.5,
               lever_dy=57.8, head_dy=109.3):
    """Colonne gauche. Le pas des puces suit la règle de la plaquette d'origine :
    `step` pour la 1re ligne, `extra_line` par ligne supplémentaire."""
    rrect(c, x, y, w, h, 40, CARD)
    text(c, x + 16.7, y + lever_dy, lever, "PoppinsB", 30, BLUE)
    hb = y + head_dy
    for ln in headline.split("\n"):
        text(c, x + 16.7, hb, ln, "OpenSans", 25, BLUE)
        hb += 29.2
    by = first_bullet if first_bullet else hb + 12
    if intro:
        n = len(wrap(intro, "Poppins", intro_size, w - 60))
        para(c, x + 16.7, by, intro, "Poppins", intro_size, INK, intro_lead, w - 60)
        by += (n - 1) * intro_lead + intro_gap
    for b in bullets:
        lines = wrap(b, "Poppins", bullet_size, w - 60)
        bullet_dot(c, x + 27.5, by - 1)
        for i, ln in enumerate(lines):
            text(c, x + 40.5, by + i * (bullet_size * 1.62), ln, "Poppins", bullet_size, INK)
        by += step + (len(lines) - 1) * extra_line
    return by


# ---------------------------------------------------------------------------
# Colonne « Modération & Enrichissement »
# ---------------------------------------------------------------------------
def moderation_block(c, x, ybase, title, pairs, maxw, bottom, size=12.4):
    l1, l2 = title.split("\n")
    text(c, x, ybase, l1, "OpenSans", 25, BLUE)
    text(c, x, ybase + 29.3, l2, "OpenSans", 25, BLUE)
    y = ybase + 58
    for label, value in pairs:
        for ln in wrap(label, "PoppinsB", size, maxw):
            text(c, x, y, ln, "PoppinsB", size, BLUE)
            y += size * 1.55
        for ln in wrap(value, "Poppins", size, maxw):
            text(c, x, y, ln, "Poppins", size, INK)
            y += size * 1.55
    return y


# ---------------------------------------------------------------------------
# Carte RCS riche (visuel + accroche + bouton)
# ---------------------------------------------------------------------------
def rich_card(c, x, y, w, h, cfg):
    box(c, x, y, w, h, 22, WHITE, stroke=1, sc=BORDER)
    ih = 148
    img(c, cfg["image"], x, y, w, ih, radius=0)
    # bandeau bas du visuel (fond plein pour garantir la lisibilité)
    c.setFillColor(HexColor("#12263C"))
    c.rect(x, 810 - (y + ih), w, 26, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("PoppinsSB", 7.2)
    c.drawString(x + 14, 810 - (y + ih - 17), cfg["kicker"])

    ty = y + ih + 22
    for ln in wrap(cfg["title"], "PoppinsB", 10.4, w - 28)[:3]:
        text(c, x + 14, ty, ln, "PoppinsB", 10.4, INK)
        ty += 14.2
    ty += 3
    for ln in wrap(cfg["sub"], "Poppins", 8.4, w - 28)[:2]:
        text(c, x + 14, ty, ln, "Poppins", 8.4, GREY_TXT)
        ty += 11.4
    bw = sw(cfg["cta"], "PoppinsSB", 9) + 34
    by = y + h - 36
    pill(c, x + 14, by, bw, 24, cfg["cta"], SOFT, BLUE, 9, border=HexColor("#D7E2FA"))


def sms_card(c, x, y, w, h, cfg):
    box(c, x, y, w, h, 22, WHITE, stroke=1, sc=BORDER)
    # entête conversation
    c.setFillColor(SOFT2)
    c.circle(x + 24, 810 - (y + 26), 11, stroke=0, fill=1)
    text(c, x + 24, y + 30, "H", "PoppinsB", 9, BLUE, "center")
    text(c, x + 42, y + 23, cfg["sender"], "PoppinsSB", 9, INK)
    text(c, x + 42, y + 34, "RCS · vérifié", "Poppins", 7, GREY_TXT)
    text(c, x + w - 14, y + 26, cfg["time"], "Poppins", 7, LIGHT_TXT, "right")
    hline(c, x, y + 46, x + w, HexColor("#EDF0F7"))
    # carte enrichie RCS (ancrée en bas) : on réserve sa place avant les bulles
    card_h = 72
    cy = y + h - card_h - 16
    # bulles
    by = y + 62
    if cfg.get("header_msg"):
        hh = 12 + len(wrap(cfg["header_msg"], "Poppins", 6.8, w - 58)) * 9.2
        box(c, x + 12, by, w - 34, hh, 8, HexColor("#F7F9FE"))
        for j, ln in enumerate(wrap(cfg["header_msg"], "Poppins", 6.8, w - 58)):
            text(c, x + 21, by + 12 + j * 9.2, ln, "Poppins", 6.8, GREY_TXT)
        by += hh + 10
    for i, line in enumerate(cfg["lines"]):
        lines = wrap(line, "Poppins", 8, w - 58)
        bh = 13 + len(lines) * 10.6
        box(c, x + 12, by, w - 34, bh, 10,
            HexColor("#E7EEFF") if i == 0 else HexColor("#F1F3F8"))
        for j, ln in enumerate(lines):
            text(c, x + 21, by + 15 + j * 10.6, ln, "Poppins", 8, INK)
        by += bh + 9
    if cfg.get("reply"):
        rl = wrap(cfg["reply"], "Poppins", 8, w - 74)
        rh = 13 + len(rl) * 10.6
        ry = min(by, cy - rh - 12)
        box(c, x + 36, ry, w - 50, rh, 10, HexColor("#DCE8FF"))
        for j, ln in enumerate(rl):
            text(c, x + 45, ry + 15 + j * 10.6, ln, "Poppins", 8, NAVY)
        # accusé de lecture (deux chevrons dessinés, police non fournie en glyphes)
        c.setStrokeColor(HexColor("#7C9CE0"))
        c.setLineWidth(0.9)
        for k in range(2):
            bx = x + w - 34 + k * 5
            by_ = 810 - (ry + rh + 7)
            c.line(bx, by_ + 3.2, bx + 2.6, by_)
            c.line(bx + 2.6, by_, bx, by_ - 3.2)

    box(c, x + 12, cy, w - 24, card_h, 10, HexColor("#EEF3FE"),
        stroke=1, sc=HexColor("#D6E2F8"))
    text(c, x + 22, cy + 19, "Votre comparatif santé", "PoppinsB", 8.8, NAVY)
    text(c, x + 22, cy + 32, "100 % gratuit · sans engagement", "Poppins", 7.2, GREY_TXT)
    bw = w - 44
    box(c, x + 22, cy + 40, bw, 20, 10, WHITE, stroke=1, sc=HexColor("#C9D8F7"))
    text(c, x + 22 + bw / 2, cy + 53.6, cfg["cta"], "PoppinsSB", 8.4, BLUE, "center")


def landing_card(c, x, y, w, h, cfg):
    box(c, x, y, w, h, 20, WHITE, stroke=1, sc=BORDER)
    # barre navigateur
    c.setFillColor(SOFT2)
    c.rect(x, 810 - (y + 26), w, 26, stroke=0, fill=1)
    for i in range(3):
        c.setFillColor(HexColor("#D5DCEA"))
        c.circle(x + 15 + i * 9, 810 - (y + 13), 2.6, stroke=0, fill=1)
    box(c, x + 52, y + 7, w - 66, 12, 6, WHITE)
    # entête marque
    logo_word(c, x + 18, y + 54, 15)
    text(c, x + w - 18, y + 54, "SANTÉ", "PoppinsSB", 6.6, HexColor("#8FA0BF"), "right")
    hline(c, x + 18, y + 66, x + w - 18, HexColor("#EDF0F7"))
    ty = y + 92
    for ln in wrap(cfg["title"], "PoppinsB", 11.2, w - 36):
        text(c, x + 18, ty, ln, "PoppinsB", 11.2, NAVY)
        ty += 15
    ty += 4
    for ln in wrap(cfg["intro"], "Poppins", 7.8, w - 36):
        text(c, x + 18, ty, ln, "Poppins", 7.8, GREY_TXT)
        ty += 11
    ty += 14
    for label, value in cfg["fields"]:
        field_line(c, x + 18, ty, w - 36, label, value, size=8.4, h=30)
        ty += 38
    box(c, x + 18, ty + 2, w - 36, 30, 6, HexColor("#1B8CE3"))
    text(c, x + w / 2, ty + 21.5, cfg["cta"], "PoppinsSB", 9.4, WHITE, "center")
    ty += 44
    c.setStrokeColor(HexColor("#D5DCEA"))
    c.setLineWidth(0.7)
    c.line(x + 18, 810 - (ty + 8), x + w - 18, 810 - (ty + 8))
    text(c, x + w / 2, ty + 22, "Sans engagement · Réponse en 24 h", "Poppins", 7,
         GREY_TXT, "center")
    # réassurance
    iy = y + h - 86
    box(c, x + 18, iy, w - 36, 56, 8, SOFT2)
    for i, lab in enumerate(["Conseiller dédié, basé en France",
                             "Devis immédiat, sans engagement",
                             "Données protégées et confidentielles"]):
        ly = iy + 16 + i * 14
        c.setFillColor(BLUE)
        c.circle(x + 30, 810 - (ly - 2), 2.2, stroke=0, fill=1)
        text(c, x + 38, ly, lab, "Poppins", 6.8, HexColor("#3E4C63"))



# ---------------------------------------------------------------------------
# Page 5 — META
# ---------------------------------------------------------------------------
def meta_ad(c, x, y, w, h, cfg):
    box(c, x, y, w, h, 18, WHITE, stroke=1, sc=BORDER)
    c.setFillColor(HexColor("#E7EEFB"))
    c.circle(x + 24, 810 - (y + 26), 11, stroke=0, fill=1)
    text(c, x + 24, y + 29, "H", "PoppinsB", 9, BLUE, "center")
    text(c, x + 43, y + 23, cfg["page"], "PoppinsSB", 8.6, INK)
    text(c, x + 43, y + 34, cfg["sponsored"] + " · ", "Poppins", 7, GREY_TXT)
    dot(c, x + 43 + sw(cfg["sponsored"] + " · ", "Poppins", 7) + 3, 810 - (y + 31.5), 1.8,
        HexColor("#8B93A7"))
    text(c, x + w - 16, y + 27, "···", "PoppinsB", 10, GREY_TXT, "right")
    text(c, x + 14, y + 50, "Assurance pro : le bon contrat, au bon prix.",
         "Poppins", 8.2, INK)
    ih = 168
    img(c, cfg["image"], x + 12, y + 58, w - 24, ih, radius=6)
    ty = y + 58 + ih + 20
    for ln in wrap(cfg["copy"], "Poppins", 8, w - 28)[:3]:
        text(c, x + 14, ty, ln, "Poppins", 8, INK)
        ty += 11
    # bloc ciblage (remplit la carte et rappelle la logique d'audience)
    ty += 12
    box(c, x + 12, ty, w - 24, 74, 6, SOFT2)
    text(c, x + 22, ty + 16, "Ciblage", "PoppinsSB", 6.6, NAVY)
    for i, ln in enumerate(wrap(cfg.get("targeting", ""), "Poppins", 6.8, w - 44)[:3]):
        text(c, x + 22, ty + 28 + i * 10.5, ln, "Poppins", 6.8, GREY_TXT)
    text(c, x + 22, ty + 66, cfg.get("objective", ""), "PoppinsSB", 6.6, BLUE)
    text(c, x + 14, y + h - 54, "PUBLICITÉ · HELLODEVIS.FR", "Poppins", 6.2, LIGHT_TXT)
    # lien sponsorisé
    box(c, x + 12, y + h - 48, w - 24, 36, 5, HexColor("#F0F2F7"))
    text(c, x + 23, y + h - 35, "HELLODEVIS.FR", "Poppins", 6.2, GREY_TXT)
    text(c, x + 23, y + h - 24, cfg["headline"], "PoppinsB", 8.2, INK)
    box(c, x + w - 96, y + h - 41, 74, 22, 3, HexColor("#E4E7EE"))
    text(c, x + w - 59, y + h - 26.5, cfg["cta"], "PoppinsSB", 7.2, INK, "center")
    text(c, x + 14, y + h - 6, cfg["reactions"], "Poppins", 6.4, LIGHT_TXT)


def meta_form(c, x, y, w, h, cfg):
    box(c, x, y, w, h, 18, WHITE, stroke=1, sc=BORDER)
    c.setFillColor(NAVY)
    c.roundRect(x, 810 - (y + 82), w, 82, 18, stroke=0, fill=1)
    c.rect(x, 810 - (y + 82), w, 34, stroke=0, fill=1)
    text(c, x + w / 2, y + 28, cfg["brand"], "PoppinsB", 12, WHITE, "center")
    text(c, x + w / 2, y + 50, cfg["title"], "PoppinsSB", 8.6, HexColor("#9DB7E8"),
         "center")
    text(c, x + w / 2, y + 67, cfg["sub"], "Poppins", 7.4, WHITE, "center")
    ty = y + 104
    for label, value in cfg["fields"]:
        text(c, x + 18, ty, label, "PoppinsSB", 7.8, NAVY)
        box(c, x + 18, ty + 8, w - 36, 34, 6, WHITE, stroke=1, sc=HexColor("#CBD5E8"))
        text(c, x + 28, ty + 20, label.split(" ")[-2].lower() if False else "", "Poppins", 8)
        text(c, x + 28, ty + 30, value, "Poppins", 8.2, HexColor("#93A0B5"))
        _chevron(c, x + w - 34, 810 - (ty + 25))
        ty += 60
    # bloc de réassurance (remplit la carte et rassure avant l'envoi)
    ty += 6
    box(c, x + 18, ty, w - 36, 86, 6, SOFT2)
    text(c, x + 28, ty + 17, "Pourquoi ces questions ?", "PoppinsSB", 7.2, NAVY)
    for i, lab in enumerate(["Devis comparés auprès de plusieurs assureurs",
                             "Conseiller dédié, basé en France",
                             "Aucun engagement, réponse sous 24 h"]):
        ly = ty + 33 + i * 13
        c.setFillColor(BLUE)
        c.circle(x + 32, 810 - (ly - 2), 2, stroke=0, fill=1)
        text(c, x + 40, ly, lab, "Poppins", 6.6, HexColor("#3E4C63"))
    ty += 100
    box(c, x + 18, ty, w - 36, 32, 6, HexColor("#1877F2"))
    text(c, x + w / 2, ty + 20, cfg["cta"], "PoppinsSB", 9.2, WHITE, "center")
    text(c, x + w / 2, ty + 44, "Formulaire instantané Meta · étape 1/2", "Poppins", 6.6,
         LIGHT_TXT, "center")


# ---------------------------------------------------------------------------
# Page 6 — CRM (capture d'écran simulée)
# ---------------------------------------------------------------------------
def crm_mock(c, x, y, w, h, cfg):
    box(c, x, y, w, h, 6, WHITE, stroke=1, sc=HexColor("#C9D2E4"), lw=1)
    # barre supérieure
    c.setFillColor(HexColor("#E8EDF7"))
    c.rect(x, 810 - (y + 26), w, 26, stroke=0, fill=1)
    logo_word(c, x + 10, y + 17, 11)
    nx = x + 92
    for item in cfg["nav"]:
        text(c, nx, y + 17, item, "Poppins", 6.4, HexColor("#3C4A63"))
        nx += sw(item, "Poppins", 6.4) + 13
    text(c, x + w - 12, y + 11, cfg["campaign"], "Poppins", 5.8, HexColor("#5B6B85"),
         "right")
    text(c, x + w - 16, y + 21, "Pierre BONNEAU", "PoppinsSB", 5.8,
         HexColor("#3C4A63"), "right")
    # petit triangle "menu"
    c.setFillColor(HexColor("#3C4A63"))
    px0, py0 = x + w - 12, 810 - (y + 23)
    q = c.beginPath()
    q.moveTo(px0, py0 + 2.2)
    q.lineTo(px0 + 4.4, py0 + 2.2)
    q.lineTo(px0 + 2.2, py0 - 1.2)
    q.close()
    c.drawPath(q, stroke=0, fill=1)
    # ---- panneau gauche : coordonnées
    px, py, pw = x + 8, y + 34, w * 0.335
    c.setFillColor(HexColor("#F4F7FC"))
    c.rect(px, 810 - (y + h - 8), pw, h - 44, stroke=0, fill=1)
    text(c, px + 8, py + 13, "Coordonnées Acheteurs", "PoppinsSB", 6.6, NAVY)
    hline(c, px + 4, py + 18, px + pw - 4, HexColor("#D3DDEF"))
    col_w = (pw - 26) / 2
    col1, col2 = px + 8, px + 16 + col_w
    text(c, col1, py + 30, "Société", "PoppinsSB", 6, NAVY)
    text(c, col2, py + 30, "Acheteur", "PoppinsSB", 6, NAVY)
    rows = py + 36
    societe = ["MECAPRO INDUSTRIES", "14 avenue de la Forge", "44300 NANTES",
               "9•• ••• ••• 00031", "NAF 2562B · Mécanique ind.", "20 à 49 salariés"]
    acheteur = ["M. B•••••", "Directeur général", "contact@mecapro.fr",
                "Ligne directe 02 •• •• ••", "Décideur signataire", "Dispo : matin"]
    for i, (a, b) in enumerate(zip(societe, acheteur)):
        box(c, col1, rows + i * 16, col_w, 13, 2, WHITE, stroke=1, sc=HexColor("#CBD5E8"))
        text(c, col1 + 4, rows + i * 16 + 9.4, a, "Poppins", 5.4, HexColor("#2C3A52"))
        box(c, col2, rows + i * 16, col_w, 13, 2, WHITE, stroke=1, sc=HexColor("#CBD5E8"))
        text(c, col2 + 4, rows + i * 16 + 9.4, b, "Poppins", 5.4, HexColor("#2C3A52"))
    qy = rows + 6 * 16 + 14
    text(c, col1, qy, "Historique commentaires", "PoppinsSB", 5.8, NAVY)
    box(c, col1, qy + 6, pw - 16, 52, 3, WHITE, stroke=1, sc=HexColor("#CBD5E8"))
    for j, ln in enumerate(wrap(cfg["comment"], "Poppins", 5.4, pw - 26)[:4]):
        text(c, col1 + 4, qy + 17 + j * 9, ln, "Poppins", 5.4, HexColor("#5B6B85"))
    box(c, col1, qy + 64, col_w + 30, 14, 2, HexColor("#F2A93B"))
    text(c, col1 + (col_w + 30) / 2, qy + 73.4, "Valider la qualification", "PoppinsSB",
         5.2, WHITE, "center")
    # ---- panneau droit : fiche d'appel
    mx = x + w * 0.35
    mw = w - (mx - x) - 8
    by0 = y + 34
    box(c, mx, by0, mw, h - 42, 3, WHITE, stroke=1, sc=HexColor("#CBD5E8"))
    text(c, mx + 10, by0 + 16, cfg["fiche_title"], "PoppinsB", 6.8, NAVY)
    text(c, mx + mw - 10, by0 + 16, cfg["right_title"], "Poppins", 5.2,
         HexColor("#2F6FE4"), "right")
    hline(c, mx + 6, by0 + 22, mx + mw - 6, HexColor("#E3E9F7"))
    # colonne questions
    qw = mw - 138
    qy = by0 + 38
    for label, options, sel in cfg["questions"]:
        for ln in wrap(label, "PoppinsB", 6.2, qw - 18):
            text(c, mx + 12, qy, ln, "PoppinsB", 6.2, HexColor("#2C3A52"))
            qy += 9
        for i, opt in enumerate(options):
            col = i % 2
            row = i // 2
            rx = mx + 18 + col * (qw / 2)
            ry = qy + row * 11
            c.setFillColor(WHITE)
            c.setStrokeColor(HexColor("#7E8AA0"))
            c.setLineWidth(0.5)
            c.circle(rx, 810 - (ry + 1), 2.2, stroke=1, fill=1)
            if i == sel:
                c.setFillColor(HexColor("#1B4FD8"))
                c.circle(rx, 810 - (ry + 1), 1.2, stroke=0, fill=1)
            text(c, rx + 6, ry + 1, opt, "Poppins", 5.4,
                 HexColor("#1B4FD8") if i == sel else HexColor("#4A5870"))
        qy += (math.ceil(len(options) / 2)) * 11 + 9
    # encart matching
    bx, byr = mx + mw - 126, by0 + 30
    box(c, bx, byr, 116, 50, 3, HexColor("#FFF7E8"), stroke=1, sc=HexColor("#E2C68C"))
    text(c, bx + 7, byr + 13, "Résultat du matching :", "PoppinsB", 5.4,
         HexColor("#8A6A1F"))
    for i, m in enumerate(cfg["matching"]):
        c.setFillColor(HexColor("#1B4FD8"))
        c.rect(bx + 7, 810 - (byr + 24 + i * 10), 4.4, 4.4, stroke=0, fill=1)
        text(c, bx + 15, byr + 27 + i * 10, m, "PoppinsSB", 5.2, NAVY)
    box(c, bx, byr + 58, 116, 16, 3, HexColor("#EAF1FF"))
    text(c, bx + 58, byr + 68.4, "Lead à forte valeur ajoutée", "PoppinsSB", 4.8,
         HexColor("#1B4FD8"), "center")
    # script d'appel (sous les questions)
    sy = max(qy, byr + 84) + 12
    text(c, mx + 12, sy, "Script & écoutes de modération", "PoppinsSB", 6.2, NAVY)
    sy += 8
    for item in cfg.get("script", []):
        c.setFillColor(HexColor("#F2A93B"))
        c.circle(mx + 15, 810 - (sy + 1), 1.6, stroke=0, fill=1)
        text(c, mx + 21, sy + 1, item, "Poppins", 5.6, HexColor("#4A5870"))
        sy += 9.5
    box(c, mx + 10, y + h - 32, mw - 20, 16, 2, HexColor("#F4F7FC"))
    text(c, mx + 16, y + h - 21.5, cfg.get("stats", ""), "Poppins", 5.4,
         HexColor("#5B6B85"))


def crm_photo(c, x, y, w, h, name, stats=None):
    box(c, x, y, w, h, 8, WHITE, stroke=1, sc=HexColor("#E3E9F7"))
    img(c, name, x + 4, y + 4, w - 8, h - 8, radius=6)
    if stats:
        n = len(stats)
        bw = (w - 8) / n
        c.setFillColor(Color(0.04, 0.09, 0.15, alpha=0.66))
        c.rect(x + 4, 810 - (y + h - 4), w - 8, 42, stroke=0, fill=1)
        for i, (head, lab) in enumerate(stats):
            bx = x + 18 + i * bw
            text(c, bx, y + h - 26, head, "PoppinsSB", 8.6, WHITE)
            text(c, bx, y + h - 14, lab, "Poppins", 6.4, HexColor("#AEBDD4"))


# ---------------------------------------------------------------------------
# Page 7 — Emailing
# ---------------------------------------------------------------------------
def email_card(c, x, y, w, h, cfg):
    box(c, x, y, w, h, 12, WHITE, stroke=1, sc=BORDER)
    text(c, x + 12, y + 15, "De : Patrimoine & Transmission", "Poppins", 5.6, LIGHT_TXT)
    text(c, x + w - 12, y + 15, "9:41", "Poppins", 5.6, LIGHT_TXT, "right")
    hline(c, x + 12, y + 22, x + w - 12, HexColor("#EDF0F7"))
    theme = cfg.get("theme")
    band = {"dark": (NAVY, WHITE), "gold": (HexColor("#F4EFE3"), HexColor("#8A6A1F"))}.get(
        theme, (HexColor("#F7F9FE"), NAVY))
    c.setFillColor(band[0])
    c.rect(x, 810 - (y + 56), w, 34, stroke=0, fill=1)
    text(c, x + w / 2, y + 44, cfg["brand"], "PoppinsSB", 7.2, band[1], "center")
    cy = y + 56
    if cfg.get("image"):
        ih = cfg.get("img_h", 132)
        img(c, cfg["image"], x, cy, w, ih, crop="center")
        cy += ih
    text(c, x + 14, cy + 18, cfg["subject"], "Poppins", 6.2, LIGHT_TXT)
    ty = cy + 34
    for ln in wrap(cfg["title"], "PoppinsB", 9.8, w - 28)[:2]:
        text(c, x + 14, ty, ln, "PoppinsB", 9.8, NAVY)
        ty += 12.6
    ty += 5
    for ln in wrap(cfg["body"], "Poppins", 7.4, w - 28)[:3]:
        text(c, x + 14, ty, ln, "Poppins", 7.4, HexColor("#5B6B85"))
        ty += 10.2
    # arguments
    ty += 10
    for arg in cfg.get("args", []):
        c.setFillColor(HexColor("#1B4FD8"))
        c.circle(x + 18, 810 - (ty - 2), 1.8, stroke=0, fill=1)
        text(c, x + 25, ty, arg, "Poppins", 6.6, HexColor("#3E4C63"))
        ty += 10.5
    bw = sw(cfg["cta"], "PoppinsSB", 8) + 28
    by = ty + 8
    box(c, x + 14, by, bw, 23, 11, NAVY if theme != "gold" else HexColor("#8A6A1F"))
    text(c, x + 14 + bw / 2, by + 15.2, cfg["cta"], "PoppinsSB", 8, WHITE, "center")
    text(c, x + w / 2, y + h - 13, "Se désabonner · Mentions légales", "Poppins", 5.8,
         HexColor("#B6BECD"), "center")


# ---------------------------------------------------------------------------
# Page 7 — bandeau « séquence de nurturing »
# ---------------------------------------------------------------------------
def sequence_strip(c, x, y, w, h, steps, title="Séquence de nurturing"):
    box(c, x, y, w, h, 12, WHITE, stroke=1, sc=BORDER)
    text(c, x + 16, y + 22, title, "PoppinsB", 9.2, NAVY)
    text(c, x + w - 16, y + 22, "Emailing", "PoppinsSB", 6.6, LIGHT_TXT, "right")
    ly = y + h / 2 + 6
    c.setStrokeColor(HexColor("#DCE4F5"))
    c.setLineWidth(1.2)
    c.line(x + 26, 810 - ly, x + w - 26, 810 - ly)
    n = len(steps)
    for i, (when, what) in enumerate(steps):
        cx = x + 46 + i * ((w - 92) / max(1, n - 1))
        c.setFillColor(BLUE if i == 0 else WHITE)
        c.setStrokeColor(BLUE)
        c.setLineWidth(1.4)
        c.circle(cx, 810 - ly, 4.2, stroke=1, fill=1)
        text(c, cx, ly - 14, when, "PoppinsSB", 6.8, BLUE, "center")
        for j, ln in enumerate(wrap(what, "Poppins", 6.4, (w - 60) / max(1, n))):
            text(c, cx, ly + 14 + j * 8.6, ln, "Poppins", 6.4, HexColor("#5B6B85"),
                 "center")
