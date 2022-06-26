from tkinter import messagebox

from controller.calculate_shear_wall import calculate_shear_walls
from helpers.get_info_from_database import get_info_from_database


def calculate():
    with open('db/database.txt', 'r') as file:
        try:
            number_shear_walls, storey_levels, sheet, txt_path, workbook, file_path = get_info_from_database(file)
            calculate_shear_walls(number_shear_walls, storey_levels, sheet)
            workbook.save(file_path)
            messagebox.showinfo("Information", "Successful")
        except:
            messagebox.showwarning("Warning", "Invalid Input")
