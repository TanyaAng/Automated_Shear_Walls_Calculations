import openpyxl
import json
from tkinter import messagebox

from helpers.tower_helpers.set_Tower_results_to_xls_file import paste_Tower_results_in_xls


def get_results_from_txt():
    with open('db/database.txt', 'r') as file:
        try:
            user_input = json.load(file)
            txt_path = user_input[0]
            file_path = user_input[1]
            sheet_name = user_input[2]
            number_shear_walls = int(user_input[3])
            storey_levels = int(user_input[4])
            print(user_input)
            data = open(txt_path, encoding='utf-8', mode='r')
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook[sheet_name]
            print(sheet)
            paste_Tower_results_in_xls(number_shear_walls, storey_levels, file_path, sheet, workbook, data)
            print(user_input)
            messagebox.showinfo("Info", "Successful")
        except:
            messagebox.showwarning("Warning", "Invalid input")

