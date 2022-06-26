import os
from tkinter import messagebox


def delete_PDF():
    file = "result.pdf"
    try:
        os.remove(file)
    except PermissionError:
        messagebox.showwarning('Warning', 'Close the file!')
        delete_PDF()
