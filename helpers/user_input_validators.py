from tkinter import messagebox


def is_valid_txt_path(file):
    if file == '':
        return messagebox.askyesnocancel('Warning', "Are you sure you don't need txt file?")
    else:
        return True


def is_valid_xls_path(file):
    if file != '':
        return True
    messagebox.showerror('Error message', f'Empty input for xls file location!')
    return False


def is_valid_name(name):
    if name != '':
        return True
    messagebox.showerror('Error message', f'Empty input for sheet name!')
    return False


def is_valid_count(count):
    if count.isdigit():
        return True
    messagebox.showerror(f'Error message', f'Shear walls and levels count must be integer!')
    return False
