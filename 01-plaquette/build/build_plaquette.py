# -*- coding: utf-8 -*-
"""
Assemblage de la plaquette HelloLead — édition « Assurance ».

    python build_plaquette.py --page 3 --preview     # contrôle visuel d'une page
    python build_plaquette.py                        # PDF final + PDF pages 3-7 + aperçus

Sorties (dossier ../out) :
    Plaquette_HelloLead_Assurance.pdf           9 pages (1, 2, 4, 8, 9 reprises du PDF source)
    Plaquette_HelloLead_Assurance_pages3-7.pdf  extrait pour validation par le métier
    apercu/pN.png                               aperçus 110 dpi
"""

import argparse
import os

import pymupdf
from reportlab.pdfgen import canvas

from pages import PAGE_FUNCS
from render_base import OUT, ROOT, SRC_PDF, W, H

SECTOR_PAGES = (3, 5, 6, 7)


def render_page(n, path):
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setTitle("Plaquette HelloLead — Assurance")
    c.setAuthor("HelloLead")
    c.setSubject("Plaquette commerciale sectorisée — Assurance")
    PAGE_FUNCS[n](c)
    c.showPage()
    c.save()
    return path


def render_sector_pdf(path):
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setTitle("Plaquette HelloLead — Assurance (pages sectorisées)")
    c.setAuthor("HelloLead")
    for n in SECTOR_PAGES:
        PAGE_FUNCS[n](c)
        c.showPage()
    c.save()
    return path


def assemble(sector_pdf, out_pdf):
    """Pages 1, 2, 4, 8, 9 reprises du PDF d'origine ; 3, 5, 6, 7 régénérées."""
    src = pymupdf.open(SRC_PDF)
    gen = pymupdf.open(sector_pdf)
    new = pymupdf.open()
    order = {n: i for i, n in enumerate(SECTOR_PAGES)}
    for p in range(1, 10):
        if p in order:
            new.insert_pdf(gen, from_page=order[p], to_page=order[p])
        else:
            new.insert_pdf(src, from_page=p - 1, to_page=p - 1)
    new.set_metadata({"title": "Plaquette commerciale HelloLead — Assurance",
                      "author": "HelloLead", "subject": "Génération de leads — secteur assurance",
                      "keywords": "lead generation, assurance, SMS RCS, Meta Ads, SEA, call, emailing"})
    new.save(out_pdf, deflate=True, garbage=3)
    new.close()
    return out_pdf


def extract_37(out_pdf, path):
    src = pymupdf.open(out_pdf)
    new = pymupdf.open()
    for i in (2, 3, 4, 5, 6):          # pages 3 à 7
        new.insert_pdf(src, from_page=i, to_page=i)
    new.save(path, deflate=True, garbage=3)
    new.close()
    return path


def previews(pdf, folder, pages=(3, 5, 6, 7), dpi=110):
    os.makedirs(folder, exist_ok=True)
    doc = pymupdf.open(pdf)
    for p in pages:
        doc[p - 1].get_pixmap(dpi=dpi).save(os.path.join(folder, f"p{p}.png"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", type=int, choices=list(SECTOR_PAGES))
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    os.makedirs(OUT, exist_ok=True)

    if a.page and a.preview:
        pdf = render_page(a.page, os.path.join(OUT, f"_p{a.page}.pdf"))
        png = pdf.replace(".pdf", ".png")
        pymupdf.open(pdf)[0].get_pixmap(dpi=110).save(png)
        os.remove(pdf)
        print(png)
        return

    final = a.out or os.path.join(OUT, "Plaquette_HelloLead_Assurance.pdf")
    sector = render_sector_pdf(os.path.join(OUT, "_pages_secteur.pdf"))
    assemble(sector, final)
    os.remove(sector)
    extract_37(final, os.path.join(OUT, "Plaquette_HelloLead_Assurance_pages3-7.pdf"))
    previews(final, os.path.join(OUT, "apercu"))
    print(final)


if __name__ == "__main__":
    main()
