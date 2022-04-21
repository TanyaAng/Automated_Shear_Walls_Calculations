from tkinter import *
import json
from shear_walls_automation import main_function_calculate
from clear_sheet_cells import main_function_clear
from get_txt_results import main_function_get_results
import re
from tkinter import messagebox

MAIN_COLOUR = '#fce5cd'
MAIN_FONT = 'ArialNarrow 10 bold'
SECONDARY_FONT = 'ArialNarrow 8'


def clear_view():
    for slave in tk.grid_slaves():
        slave.destroy()


def render_main_view():
    clear_view()
    Label(tk, text="TXT file", bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=0, padx=5, pady=5)
    txt_path = Entry(tk)
    txt_path.grid(column=1, row=0, padx=5, pady=5)

    Label(tk, text="XLS file*", bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=1, padx=5, pady=5)
    file_path_entry = Entry(tk)
    file_path_entry.grid(column=1, row=1, padx=5, pady=5)

    Label(tk, text="Sheet Name*", bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=2, padx=5, pady=5)
    sheet_name_entry = Entry(tk)
    sheet_name_entry.grid(column=1, row=2, padx=5, pady=5)

    Label(tk, text='Shear Walls Count*', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=3, padx=5, pady=5)
    num_shear_walls_entry = Entry(tk)
    num_shear_walls_entry.grid(column=1, row=3, padx=5, pady=5)

    Label(tk, text='Storey Levels Count*', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=4, padx=5,
                                                                                pady=5)
    levels_entry = Entry(tk)
    levels_entry.grid(column=1, row=4, padx=5, pady=5)
    Button(tk, text='Get Information', bg='#2878BD', fg='white', font=MAIN_FONT,
           command=lambda: get_value(txt_path, file_path_entry, sheet_name_entry, num_shear_walls_entry,
                                     levels_entry)).grid(
        column=0, row=5, padx=5, pady=5)
    Button(tk, text="Clear Cells in Sheet", bg='#A80000', fg='white', font=MAIN_FONT,
           command=main_function_clear).grid(column=1, row=5, padx=5, pady=5)
    Button(tk, text="Get Tower Results", bg='#107C10', fg='white', font=MAIN_FONT,
           command=main_function_get_results).grid(column=0, row=6, padx=5, pady=5)
    Button(tk, text="Calculate Reinf.", bg='#107C10', fg='white', font=MAIN_FONT,
           command=main_function_calculate).grid(column=0, row=7, padx=5, pady=5)

    Label(tk, text='*required fields', bg=MAIN_COLOUR, font=SECONDARY_FONT).grid(column=0, row=8, padx=5, pady=5)
    # Label(tk,
    #       text='NOTE: Before using the app all files MUST be closed.\n'
    #            'All shear walls in the txt file MUST be named in Tower, starting with "Ш"\n'
    #            'Name (for example "Ш1.2") is not allowed, rename it (for example "Ш122")\n'
    #            'It is not allowed to duplicate names for shear walls',
    #       bg=MAIN_COLOUR, font=SECONDARY_FONT).grid(column= 0, row=9, padx=5, pady=5)


def get_value(txt_path, file_path, sheet_name, num_shear_walls, levels):
    get_list = [txt_path.get(), file_path.get(), sheet_name.get(), num_shear_walls.get(), levels.get()]
    # write only the last input from desktop app
    with open('database.txt', 'w') as file:
        json.dump(get_list, file)
    if get_list == ["", "", "", "", ""] or get_list == []:
        messagebox.showwarning("Warning", "Empty Input")
    else:
        pattern_txt = r'(?<=\\)\w+\s?\w+\.txt'
        txt_data = ''.join(re.findall(pattern_txt, get_list[0]))
        pattern_xlsx = r'(?<=\\)\w+\s?\w+\.xlsx'
        file_data = ''.join(re.findall(pattern_xlsx, get_list[1]))
        get_list_to_print = get_list[2:5]
        get_list_to_print.insert(0, txt_data)
        get_list_to_print.insert(1, file_data)
        text_to_print = f'txt file: {txt_data}\nFile name: {file_data} \nSheet Name: {get_list_to_print[2]} \nShear Walls: {get_list_to_print[3]} \nLevels: {get_list_to_print[4]}'
        messagebox.showinfo("Info", text_to_print)


if __name__ == '__main__':
    tk = Tk()
    tk.geometry('300x300')
    tk.title("Shear Walls Automation Excel")
    tk.configure(bg=MAIN_COLOUR)
    render_main_view()
    tk.mainloop()
    open("database.txt", 'w').close()
