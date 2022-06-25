from tkinter import *

from helpers.get_value_from_database import get_value
from model.calculate_shear_walls import calculate
from model.clear_sheet_cells_in_xls_file import clear_cells
from model.get_results_from_txt_file import get_results_from_txt

if __name__ == '__main__':
    tk = Tk()
    tk.geometry("600x600")
    tk.title("Shear Walls Automation")
    tk.configure(bg="#c8c8c8")
    canvas = Canvas(tk, bg="#c8c8c8", height=600, width=600, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    entry0_img = PhotoImage(file=f"db/images/img_textBox0.png")
    entry0_bg = canvas.create_image(448.0, 60.0, image=entry0_img)
    txt_path = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    txt_path.place(x=358.0, y=45, width=180.0, height=28)

    entry1_img = PhotoImage(file=f"db/images/img_textBox1.png")
    entry1_bg = canvas.create_image(448.0, 127.0, image=entry1_img)
    file_path_entry = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    file_path_entry.place(x=358.0, y=112, width=180.0, height=28)

    entry2_img = PhotoImage(file=f"db/images/img_textBox2.png")
    entry2_bg = canvas.create_image(448.0, 194.0, image=entry2_img)
    sheet_name_entry = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    sheet_name_entry.place(x=358.0, y=179, width=180.0, height=28)

    entry3_img = PhotoImage(file=f"db/images/img_textBox3.png")
    entry3_bg = canvas.create_image(448.0, 261.0, image=entry3_img)
    num_shear_walls_entry = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    num_shear_walls_entry.place(x=358.0, y=246, width=180.0, height=28)

    entry4_img = PhotoImage(file=f"db/images/img_textBox4.png")
    entry4_bg = canvas.create_image(448.0, 328.0, image=entry4_img)
    levels_entry = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    levels_entry.place(x=358.0, y=313, width=180.0, height=28)

    img0 = PhotoImage(file=f"db/images/img0.png")
    b0 = Button(image=img0, borderwidth=0, highlightthickness=0,
                command=lambda: get_value(txt_path, file_path_entry, sheet_name_entry, num_shear_walls_entry,
                                          levels_entry), relief="flat",
                background="#C8C8C8", activebackground="#C8C8C8")
    b0.place(x=350, y=366, width=200, height=40)

    img1 = PhotoImage(file=f"db/images/img1.png")
    b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=get_results_from_txt, relief="flat",
                background="#C8C8C8", activebackground="#C8C8C8")
    b1.place(x=350, y=424, width=200, height=40)

    img2 = PhotoImage(file=f"db/images/img2.png")
    b2 = Button(image=img2, borderwidth=0, highlightthickness=0, command=calculate, relief="flat",
                background="#C8C8C8", activebackground="#C8C8C8")
    b2.place(x=350, y=482, width=200, height=40)

    img3 = PhotoImage(file=f"db/images/img3.png")
    b3 = Button(image=img3, borderwidth=0, highlightthickness=0, command=clear_cells, relief="flat",
                background="#C8C8C8", activebackground="#C8C8C8")
    b3.place(x=350, y=540, width=200, height=40)

    background_img = PhotoImage(file=f"db/images/background.png")
    background = canvas.create_image(260.5, 299.0, image=background_img)

    tk.resizable(False, False)
    tk.mainloop()
    open("db/database.txt", 'w').close()



