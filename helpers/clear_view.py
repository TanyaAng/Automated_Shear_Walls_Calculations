import tk

def clear_view():
    for slave in tk.grid_slaves():
        slave.destroy()

