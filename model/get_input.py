import json
from tkinter import messagebox

from helpers.user_input_validators import is_valid_path, is_valid_name, is_valid_count


def get_input(txt_path, file_path, sheet_name, num_shear_walls, levels):
    user_input = {'txt file': txt_path.get().strip(),
                  'xls file': file_path.get().strip(),
                  'sheet name': sheet_name.get().strip(),
                  'count walls': num_shear_walls.get().strip(),
                  'count levels': levels.get().strip()}

    is_valid_txt_file_path = is_valid_path(user_input['txt file'])
    if not is_valid_txt_file_path:
        is_valid_txt_file_path = messagebox.askyesnocancel('Warning', "Are you sure you don't need txt file?")

    is_valid_xls_file_path = is_valid_path(user_input['xls file'])
    if not is_valid_xls_file_path:
        messagebox.showerror('Error message', 'Empty input for file location!')

    is_valid_sheet_name = is_valid_name(user_input['sheet name'])
    if not is_valid_sheet_name:
        messagebox.showerror('Error message', 'Empty input for sheet name!')

    is_valid_walls_count = is_valid_count(user_input['count walls'])
    if not is_valid_walls_count:
        messagebox.showerror('Error message', 'Shear walls count must be integer!')

    is_valid_levels_count = is_valid_count(user_input['count levels'])
    if not is_valid_levels_count:
        messagebox.showerror('Error message', 'Levels count must be integer!')

    if is_valid_txt_file_path and is_valid_xls_file_path and is_valid_sheet_name and is_valid_walls_count and is_valid_levels_count:
        with open('db/database.txt', 'w') as file:
            json.dump(user_input, file)

        messagebox.showinfo('Information', 'Successful')
