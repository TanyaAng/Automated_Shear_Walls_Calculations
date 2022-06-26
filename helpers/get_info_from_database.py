import json

import openpyxl


def get_info_from_database(file):
    user_input = json.load(file)
    txt_path = user_input[0]
    file_path = user_input[1]
    sheet_name = user_input[2]
    number_shear_walls = int(user_input[3])
    storey_levels = int(user_input[4])
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    return number_shear_walls, storey_levels, sheet, txt_path, workbook, file_path
