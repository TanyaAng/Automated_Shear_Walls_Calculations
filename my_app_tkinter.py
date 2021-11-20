from tkinter import *
import json
from shear_walls_automation import main_function_calculate
from clear_sheet_cells import main_function_clear


def clear_view():
    for slave in tk.grid_slaves():
        slave.destroy()


def render_main_view():
    clear_view()
    Label(tk, text="Enter your file path").grid(column=0, row=0, padx=35, pady=35)
    file_path_entry = Entry(tk)
    file_path_entry.grid(column=1, row=0, padx=35, pady=35)

    Label(tk, text="Enter sheet name").grid(column=0, row=1, padx=35, pady=35)
    sheet_name_entry = Entry(tk)
    sheet_name_entry.grid(column=1, row=1, padx=35, pady=35)

    Label(tk, text='Enter number of shear wall').grid(column=0, row=2, padx=35, pady=35)
    num_shear_walls_entry = Entry(tk)
    num_shear_walls_entry.grid(column=1, row=2, padx=35, pady=35)

    Label(tk, text='Enter number of storey levels').grid(column=0, row=3, padx=35, pady=35)
    levels_entry = Entry(tk)
    levels_entry.grid(column=1, row=3, padx=35, pady=35)
    Button(tk, text='Get Information', bg='blue', fg='white',
           command=lambda: get_value(file_path_entry, sheet_name_entry, num_shear_walls_entry, levels_entry)).grid(
        column=0, row=4, padx=35,pady=35)
    Button(tk, text="Clear Cells in Sheet", bg='green', fg='white',
           command=main_function_clear).grid(column=1, row=5, padx=35, pady=35)
    Button(tk, text="Calculate Required Reinforcement", bg='green', fg='white',
           command=main_function_calculate).grid(column=1, row=6, padx=35, pady=35)


def get_value(file_path, sheet_name, num_shear_walls, levels):
    get_list = [file_path.get(), sheet_name.get(), num_shear_walls.get(), levels.get()]
    Label(tk, text=f'{get_list}').grid(column=1, row=4, padx=35, pady=35)
    # write only the last input from desktop app
    with open('database.txt', 'w') as file:
        json.dump(get_list, file)


if __name__ == '__main__':
    tk = Tk()
    tk.geometry('700x700')
    tk.title("Shear Walls Automation Excel")
    tk.configure(bg='#6ACCBC')
    render_main_view()
    tk.mainloop()
