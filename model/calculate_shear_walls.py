import openpyxl
import json
from tkinter import messagebox

from controller.calculate_shear_wall import calculate_shear_walls


def calculate():
    with open('db/database.txt', 'r') as file:
        try:
            user_input = json.load(file)
            txt_path = user_input[0]
            file_path = user_input[1]
            sheet_name = user_input[2]
            number_shear_walls = int(user_input[3])
            storey_levels = int(user_input[4])

            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook[sheet_name]
            calculate_shear_walls(number_shear_walls, storey_levels, sheet)
            workbook.save(file_path)
            # print(user_input)
            messagebox.showinfo("Info", "Successful")
        except:
            messagebox.showwarning("Warning", "Invalid Input")
