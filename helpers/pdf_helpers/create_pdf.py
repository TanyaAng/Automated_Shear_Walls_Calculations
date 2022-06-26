#!/usr/bin/env python
# -*- coding: utf8 -*-

from fpdf import FPDF
import os


def create_PDF(dictionary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=16)

    pdf.cell(200, 20, txt=f"Shear Walls Max Values Per Level", ln=1, align='C')
    previous_wall_num = 0
    for key, value in dictionary.items():
        wall_num, storey_num = key[1:].split('-')
        if previous_wall_num != 0 and previous_wall_num != wall_num:
            pdf.cell(0, 6, ln=1)
            previous_wall_num = wall_num

        pdf.set_font('Arial', style='B', size=10)
        pdf.set_fill_color(118, 180, 180)
        pdf.cell(15, 6, txt=f'W{wall_num}', border=1, ln=0, align='C', fill=True)
        pdf.cell(20, 6, txt=f'Storey {storey_num}', border=1, ln=0, align='C')
        for type, v in value.items():
            pdf.set_font('Arial', style='', size=10)
            pdf.cell(20, 6, txt=f'{type} [cm2]', border=1, ln=0, align='C')
            pdf.set_font('Arial', style='B', size=10)
            pdf.set_fill_color(220, 235, 230)
            pdf.cell(20, 6, txt=f'{v}', border=1, ln=0, align='C', fill=True)
        pdf.cell(30, 6, ln=1)
        previous_wall_num = wall_num
    pdf.output("result.pdf").encode('latin1').decode('utf8')
    os.startfile("result.pdf")


# print(u"\u0428")