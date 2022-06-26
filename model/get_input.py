import json
from tkinter import messagebox

from helpers.user_input_validators import is_valid_txt_path, is_valid_xls_path, is_valid_name, is_valid_count


def get_input(txt_path, file_path, sheet_name, num_shear_walls, levels):
    user_input = {'txt file': txt_path.get().strip(),
                  'xls file': file_path.get().strip(),
                  'sheet name': sheet_name.get().strip(),
                  'count walls': num_shear_walls.get().strip(),
                  'count levels': levels.get().strip()}

    is_valid_txt_file_path = is_valid_txt_path(user_input['txt file'])
    is_valid_xls_file_path = is_valid_xls_path(user_input['xls file'])
    is_valid_sheet_name = is_valid_name(user_input['sheet name'])
    is_valid_walls_count = is_valid_count(user_input['count walls'])
    is_valid_levels_count = is_valid_count(user_input['count levels'])

    if is_valid_txt_file_path and is_valid_xls_file_path and is_valid_sheet_name and is_valid_walls_count and is_valid_levels_count:
        with open('db/database.txt', 'w') as file:
            json.dump(user_input, file)
        messagebox.showinfo('Information', 'Successful')
