import json

import openpyxl


def get_info_from_database(file):
    user_input = json.load(file)
    txt_path = user_input['txt file']
    file_path = user_input['xls file']
    sheet_name = user_input['sheet name']
    number_shear_walls = int(user_input['count walls'])
    storey_levels = int(user_input['count levels'])
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    return number_shear_walls, storey_levels, sheet, txt_path, workbook, file_path

