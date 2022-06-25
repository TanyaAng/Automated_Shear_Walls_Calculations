import json
from tkinter import messagebox


def get_value(txt_path, file_path, sheet_name, num_shear_walls, levels):
    get_list = [txt_path.get(), file_path.get(), sheet_name.get(), num_shear_walls.get(), levels.get()]
    # write only the last input from desktop app
    with open('db/database.txt', 'w') as file:
        json.dump(get_list, file)
    if get_list==['','','','','']:
        messagebox.showwarning("Warning", "Invalid Input")
    else:
        messagebox.showinfo('Info', 'Valid Input')

