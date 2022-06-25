from tkinter import Tk
from view.render_main_view import render_main_view

if __name__ == '__main__':
    tk = Tk()
    tk.geometry("600x600")
    tk.title("Shear Walls Automation")
    render_main_view(tk)
    open("db/database.txt", 'w').close()



