from tkinter import messagebox

from controller.clear_cells_from_Tower_input import clear_cell
from helpers.get_info_from_database import get_info_from_database


def clear_cells():
    with open('db/database.txt', 'r') as file:
        try:
            number_shear_walls, storey_levels, sheet, txt_path, workbook, file_path = get_info_from_database(file)
            clear_cell(number_shear_walls, storey_levels, sheet)
            workbook.save(file_path)
            messagebox.showinfo("Information", "Successful")
        except:
            messagebox.showwarning("Warning", "Invalid Input")

