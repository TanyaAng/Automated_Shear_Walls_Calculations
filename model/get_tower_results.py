from tkinter import messagebox

from controller.set_Tower_results_to_xls_file import paste_Tower_results_in_xls
from helpers.get_info_from_database import get_info_from_database


def get_results_from_txt():
    with open('db/database.txt', 'r') as file:
        try:
            number_shear_walls, storey_levels, sheet, txt_path, workbook, file_path = get_info_from_database(file)
            data = open(txt_path, encoding='utf-8', mode='r')
            paste_Tower_results_in_xls(number_shear_walls, storey_levels, sheet, data)
            workbook.save(file_path)
            messagebox.showinfo("Information", "Successful")
        except:
            messagebox.showwarning("Warning", "Invalid input")
