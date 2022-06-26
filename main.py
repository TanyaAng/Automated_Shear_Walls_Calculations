from tkinter import Tk
from helpers.pdf_helpers.delete_pdf import delete_PDF
from view.render_main_view import render_main_view

if __name__ == '__main__':
    tk = Tk()
    tk.geometry("600x600")
    tk.title("Shear Walls Automation")
    render_main_view(tk)
    open("db/database.txt", 'w').close()
    delete_PDF()



