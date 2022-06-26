import os
from tkinter import messagebox


def delete_PDF():
    if os.path.exists("result.pdf"):
        try:
            file = "result.pdf"
            os.remove(file)
        except PermissionError:
            messagebox.showwarning('Warning', 'Close the file!')
            delete_PDF()
