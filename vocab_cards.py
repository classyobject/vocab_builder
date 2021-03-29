"""
    Copyright (c) 2021 SS
    File name: vocab_cards.py
    Author: SS
    Date created: 2021-3-28
    Date last modified: 2021-3-28
    Python Version: 3.8
"""


from fpdf import FPDF

import words


# Constants
LETTER_HEIGHT_in    = 11.0
MARGIN_in           = 0.5
PAGE_HEIGHT_in      = LETTER_HEIGHT_in-(MARGIN_in*2)
ROWS                = 4
CARD_HEIGHT_in      = PAGE_HEIGHT_in/ROWS
FONT_HEIGHT_in      = 0.35
POINT_PER_INCH      = 72


# Methods
def setup_card(h):
    h = FPDF("P", "in", "letter")
    h.set_title("Vocab words")
    h.set_author('words')

    h.set_font('times', 'BIU', FONT_HEIGHT_in*POINT_PER_INCH)
    h.set_margin(0.5)
    h.set_xy(0.5,0.5)

    return h;


def add_cards(h,words,num_cols):
    h.add_page()

    card_height = CARD_HEIGHT_in
    card_width = pdf.epw / num_cols

    for iword in range(0,len(words),num_cols):
        for w in words[iword:iword+num_cols]:
            pdf.cell(card_width, card_height, w, border=1, ln=0, align='C')
        h.ln()
    return h


def close(h):
    h.output('words.pdf')
    return h


# Script
pdf = FPDF()
pdf = setup_card(pdf)
for words in words.All():
    pdf = add_cards(pdf,words,2)
pdf = close(pdf)
