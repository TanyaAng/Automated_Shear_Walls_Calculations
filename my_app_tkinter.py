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
    # Label(tk, text="TXT file", bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=0, padx=5, pady=5)
    # txt_path = Entry(tk)
    # txt_path.grid(column=1, row=0, padx=5, pady=5)

    # Label(tk, text="XLS file*", bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=1, padx=5, pady=5)
    # file_path_entry = Entry(tk)
    # file_path_entry.grid(column=1, row=1, padx=5, pady=5)
    #
    # Label(tk, text="Sheet Name*", bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=2, padx=5, pady=5)
    # sheet_name_entry = Entry(tk)
    # sheet_name_entry.grid(column=1, row=2, padx=5, pady=5)
    #
    # Label(tk, text='Shear Walls Count*', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=3, padx=5, pady=5)
    # num_shear_walls_entry = Entry(tk)
    # num_shear_walls_entry.grid(column=1, row=3, padx=5, pady=5)
    #
    # Label(tk, text='Storey Levels Count*', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=4, padx=5,
    #                                                                             pady=5)
    # levels_entry = Entry(tk)
    # levels_entry.grid(column=1, row=4, padx=5, pady=5)

    # Button(tk, text='Get Information', bg='#2878BD', fg='white', font=MAIN_FONT,
    #        command=lambda: get_value(txt_path, file_path_entry, sheet_name_entry, num_shear_walls_entry,
    #                                  levels_entry)).grid(
    #     column=0, row=5, padx=5, pady=5)
    # Button(tk, text="Clear Cells in Sheet", bg='#A80000', fg='white', font=MAIN_FONT,
    #        command=main_function_clear).grid(column=1, row=5, padx=5, pady=5)
    # Button(tk, text="Get Tower Results", bg='#107C10', fg='white', font=MAIN_FONT,
    #        command=main_function_get_results).grid(column=0, row=6, padx=5, pady=5)
    # Button(tk, text="Calculate Reinf.", bg='#107C10', fg='white', font=MAIN_FONT,
    #        command=main_function_calculate).grid(column=0, row=7, padx=5, pady=5)

    # Label(tk, text='*required fields', bg=MAIN_COLOUR, font=SECONDARY_FONT).grid(column=0, row=8, padx=5, pady=5)
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
    if get_list==['','','','','']:
        messagebox.showwarning("Warning", "Invalid Input")
    else:
        messagebox.showinfo('Info', 'Valid Input')

        # pattern_txt = r'(?<=\\)\w+\s?\w+\.txt'
        # txt_data = ''.join(re.findall(pattern_txt, get_list[0]))
        # pattern_xlsx = r'(?<=\\)\w+\s?\w+\.xlsx'
        # file_data = ''.join(re.findall(pattern_xlsx, get_list[1]))
        # get_list_to_print = get_list[2:5]
        # get_list_to_print.insert(0, txt_data)
        # get_list_to_print.insert(1, file_data)
        # text_to_print = f'TXT file: {txt_data}\nXLS file: {file_data} \nSheet Name: {get_list_to_print[2]} \nShear Walls: {get_list_to_print[3]} \nLevels: {get_list_to_print[4]}'
        # messagebox.showinfo("Info", text_to_print)


if __name__ == '__main__':
    tk = Tk()
    tk.geometry("600x600")
    tk.title("Shear Walls Automation")
    tk.configure(bg="#c8c8c8")
    canvas = Canvas(tk, bg="#c8c8c8", height=600, width=600, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    entry0_img = PhotoImage(file=f"img_textBox0.png")
    entry0_bg = canvas.create_image(448.0, 60.0, image=entry0_img)
    txt_path = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    txt_path.place(x=358.0, y=45, width=180.0, height=28)

    entry1_img = PhotoImage(file=f"img_textBox1.png")
    entry1_bg = canvas.create_image(448.0, 127.0, image=entry1_img)
    file_path_entry = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    file_path_entry.place(x=358.0, y=112, width=180.0, height=28)

    entry2_img = PhotoImage(file=f"img_textBox2.png")
    entry2_bg = canvas.create_image(449.0, 194.0, image=entry2_img)
    sheet_name_entry = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    sheet_name_entry.place(x=359.0, y=179, width=180.0, height=28)

    entry3_img = PhotoImage(file=f"img_textBox3.png")
    entry3_bg = canvas.create_image(448.0, 261.0, image=entry3_img)
    num_shear_walls_entry = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    num_shear_walls_entry.place(x=358.0, y=246, width=180.0, height=28)

    entry4_img = PhotoImage(file=f"img_textBox4.png")
    entry4_bg = canvas.create_image(448.0, 328.0, image=entry4_img)
    levels_entry = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    levels_entry.place(x=358.0, y=313, width=180.0, height=28)

    img0 = PhotoImage(file=f"img0.png")
    b0 = Button(image=img0, borderwidth=0, highlightthickness=0,
                command=lambda: get_value(txt_path, file_path_entry, sheet_name_entry, num_shear_walls_entry,
                                          levels_entry), relief="flat",
                background="#C8C8C8", activebackground="#C8C8C8")
    b0.place(x=350, y=366, width=200, height=40)

    img1 = PhotoImage(file=f"img1.png")
    b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=main_function_get_results, relief="flat",
                background="#C8C8C8", activebackground="#C8C8C8")
    b1.place(x=350, y=424, width=200, height=40)

    img2 = PhotoImage(file=f"img2.png")
    b2 = Button(image=img2, borderwidth=0, highlightthickness=0, command=main_function_calculate, relief="flat",
                background="#C8C8C8", activebackground="#C8C8C8")
    b2.place(x=350, y=482, width=200, height=40)

    img3 = PhotoImage(file=f"img3.png")
    b3 = Button(image=img3, borderwidth=0, highlightthickness=0, command=main_function_clear, relief="flat",
                background="#C8C8C8", activebackground="#C8C8C8")
    b3.place(x=350, y=540, width=200, height=40)

    background_img = PhotoImage(file=f"background.png")
    background = canvas.create_image(260.5, 299.0, image=background_img)
    tk.resizable(False, False)
    tk.mainloop()
    open("database.txt", 'w').close()

    # tk = Tk()
    # tk.geometry('300x300')
    # tk.title("Shear Walls Automation Excel")
    # tk.configure(bg=MAIN_COLOUR)
    # render_main_view()
    # tk.mainloop()
