# -*- coding: utf-8 -*-
"""Composition des 4 pages sectorisées Assurance."""

from components import (crm_mock, crm_photo, email_card, landing_card, lever_card,
                        meta_ad, meta_form, moderation_block, rich_card,
                        sequence_strip, sms_card)
from content import PAGE3, PAGE5, PAGE6, PAGE7
from render_base import BLUE, CARD, arrow, fit_buyer, rrect, text


def _moderation_and_buyer(c, x, y_title, title, pairs, buyer, maxw, bottom,
                          size=12.4, buyer_size=12.4):
    y = moderation_block(c, x, y_title, title, pairs, maxw, bottom, size=size)
    fit_buyer(c, x, y + 6, buyer, maxw, bottom, size=buyer_size,
              leading=buyer_size * 1.38)


# ---------------------------------------------------------------------------
def page3(c):
    d = PAGE3
    lever_card(c, 44.7, 10.3, 421.2, 696, d["lever"], d["headline"], d["bullets"],
               first_bullet=191)

    rrect(c, 483, 40.3, 581.9, 720.5, 40, CARD)
    text(c, 512.7, 108.5, d["mid_headline"], "OpenSans", 25, BLUE)
    rich_card(c, 517, 140, 245, 300, d["rich_card"])
    sms_card(c, 517, 444, 245, 304, d["sms_card"])
    landing_card(c, 768, 145, 282, 490, d["lp"])

    arrow(c, 966, 656, 1012, 640, bendx=6, bendy=22, lw=4.6, size=9)
    for i, ln in enumerate(d["annotation"].split("\n")):
        text(c, 786, 668 + i * 18, ln, "Poppins", 15.2, BLUE)

    rrect(c, 1080.2, 166.3, 315.1, 634, 40, CARD)
    _moderation_and_buyer(c, 1098.9, 204.8, d["moderation_title"], d["moderation"],
                          d["buyer"], 272, 790, size=12.3, buyer_size=12.3)


# ---------------------------------------------------------------------------
def page5(c):
    d = PAGE5
    lever_card(c, 51.8, 37.3, 329.3, 572.5, d["lever"], d["headline"], d["bullets"],
               intro=d["intro"], first_bullet=202.6, step=42, extra_line=21,
               bullet_size=13.8, intro_size=13.8, intro_lead=25.8,
               lever_dy=48.3, head_dy=100.4)

    rrect(c, 396.4, 93.6, 660.4, 591.1, 40, CARD)
    text(c, 425, 157, d["mid_headline"], "OpenSans", 25, BLUE)
    meta_ad(c, 402, 178, 300, 468, d["ad"])
    meta_form(c, 724, 172, 312, 470, d["form"])

    arrow(c, 358, 116, 398, 160, bendx=6, bendy=-16, lw=4.6, size=9)
    arrow(c, 1046, 206, 1073, 240, bendx=-6, bendy=-12, lw=4.6, size=9)

    rrect(c, 1073.1, 152, 315.1, 620, 40, CARD)
    _moderation_and_buyer(c, 1091.8, 190, d["moderation_title"], d["moderation"],
                          d["buyer"], 272, 764, size=12.1, buyer_size=12.1)


# ---------------------------------------------------------------------------
def page6(c):
    d = PAGE6
    lever_card(c, 44.7, 13.5, 329.3, 545.5, d["lever"], d["headline"], d["bullets"],
               intro=d["intro"], first_bullet=168.6, step=42, extra_line=21,
               bullet_size=13.8, intro_size=13.8, intro_lead=26.2,
               lever_dy=41.8, head_dy=90.0)

    rrect(c, 389.3, 96, 660.5, 650.3, 40, CARD)
    text(c, 418, 152, d["mid_headline"], "OpenSans", 25, BLUE)
    crm_mock(c, 404.8, 172, 631.3, 336, d["crm"])
    crm_photo(c, 404.8, 524, 631.3, 196, d["crm"]["photo"], d["crm"]["photo_stats"])

    arrow(c, 370, 104, 400, 146, bendx=6, bendy=-12, lw=4.6, size=9)
    arrow(c, 1040, 300, 1067, 336, bendx=-6, bendy=-10, lw=4.6, size=9)

    rrect(c, 1066, 243, 329.3, 553.2, 40, CARD)
    _moderation_and_buyer(c, 1084.7, 279, d["moderation_title"], d["moderation"],
                          d["buyer"], 285, 788, size=12.0, buyer_size=12.0)


# ---------------------------------------------------------------------------
def page7(c):
    d = PAGE7
    lever_card(c, 44.7, 7.8, 329.3, 592.2, d["lever"], d["headline"], d["bullets"],
               first_bullet=172.9, step=42, bullet_size=13.8, extra_line=21,
               lever_dy=47.5, head_dy=99.9)

    rrect(c, 389.3, 7.8, 661.4, 793.2, 40, CARD)
    h1, h2 = d["mid_headline"].split("\n")
    text(c, 418, 74, h1, "OpenSans", 25, BLUE)
    text(c, 418, 103, h2, "OpenSans", 25, BLUE)

    email_card(c, 420, 134, 286, 520, d["mails"][0])
    email_card(c, 730, 134, 288, 250, d["mails"][1])
    email_card(c, 730, 396, 288, 258, d["mails"][2])
    sequence_strip(c, 420, 666, 598, 96, d["sequence"])

    arrow(c, 360, 300, 400, 330, bendx=2, bendy=-10, lw=4.6, size=9)
    arrow(c, 1024, 250, 1062, 288, bendx=-6, bendy=-8, lw=4.6, size=9)

    rrect(c, 1065.7, 194.4, 329.4, 608.5, 40, CARD)
    _moderation_and_buyer(c, 1084.4, 224, d["moderation_title"], d["moderation"],
                          d["buyer"], 285, 790, size=11.9, buyer_size=11.9)


PAGE_FUNCS = {3: page3, 5: page5, 6: page6, 7: page7}
