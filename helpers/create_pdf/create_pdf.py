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
    pdf.output("result.pdf")
    os.startfile("result.pdf")

a=5

# dictionary = {'Ш1-3': {'Aa1': 36.93, 'Aa2': 36.93, 'Aav': 6.01, 'Aah': 9.03},
#               'Ш1-2': {'Aa1': 29.1, 'Aa2': 29.1, 'Aav': 4.74, 'Aah': 6.39},
#               'Ш1-1': {'Aa1': 21.62, 'Aa2': 21.62, 'Aav': 3.52, 'Aah': 4.57},
#               'Ш2-2': {'Aa1': 50.94, 'Aa2': 50.94, 'Aav': 4.15, 'Aah': 11.63},
#               'Ш2-1': {'Aa1': 43.64, 'Aa2': 43.64, 'Aav': 3.55, 'Aah': 9.35},
#               'Ш3-2': {'Aa1': 78.26, 'Aa2': 78.26, 'Aav': 5.64, 'Aah': 13.21},
#               'Ш3-1': {'Aa1': 64.28, 'Aa2': 64.28, 'Aav': 4.64, 'Aah': 9.65},
#               'Ш4-3': {'Aa1': 55.11, 'Aa2': 55.11, 'Aav': 4.03, 'Aah': 10.71},
#               'Ш4-2': {'Aa1': 47.1, 'Aa2': 47.1, 'Aav': 3.44, 'Aah': 4.85},
#               'Ш4-1': {'Aa1': 41.61, 'Aa2': 41.61, 'Aav': 3.04, 'Aah': 7.44},
#               'Ш5-3': {'Aa1': 33.44, 'Aa2': 33.44, 'Aav': 2.71, 'Aah': 5.02},
#               'Ш5-2': {'Aa1': 39.59, 'Aa2': 39.59, 'Aav': 3.2, 'Aah': 6.42},
#               'Ш5-1': {'Aa1': 39.53, 'Aa2': 39.53, 'Aav': 3.2, 'Aah': 5.87},
#               'Ш6-2': {'Aa1': 74.1, 'Aa2': 74.1, 'Aav': 2.71, 'Aah': 11.85},
#               'Ш6-1': {'Aa1': 64.08, 'Aa2': 64.08, 'Aav': 2.34, 'Aah': 9.84},
#               'Ш7-3': {'Aa1': 73.78, 'Aa2': 73.78, 'Aav': 6.31, 'Aah': 7.43},
#               'Ш7-2': {'Aa1': 80.79, 'Aa2': 80.79, 'Aav': 6.91, 'Aah': 10.64},
#               'Ш7-1': {'Aa1': 70.25, 'Aa2': 70.25, 'Aav': 6.01, 'Aah': 9.93},
#               'Ш8-3': {'Aa1': 58.64, 'Aa2': 58.64, 'Aav': 7.59, 'Aah': 5.55},
#               'Ш8-2': {'Aa1': 83.17, 'Aa2': 83.17, 'Aav': 10.76, 'Aah': 10.02},
#               'Ш8-1': {'Aa1': 80.86, 'Aa2': 80.86, 'Aav': 10.47, 'Aah': 9.86},
#               'Ш9-3': {'Aa1': 39.46, 'Aa2': 39.46, 'Aav': 5.11, 'Aah': 5.19},
#               'Ш9-2': {'Aa1': 42.63, 'Aa2': 42.63, 'Aav': 5.52, 'Aah': 8.15},
#               'Ш9-1': {'Aa1': 40.42, 'Aa2': 40.42, 'Aav': 5.23, 'Aah': 8.33}}
#
# create_PDF(dictionary)
