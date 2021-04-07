import tkinter as tk


def add_row():
    global canv_h
    canv_h += 5
    canv.config(height=canv_h)

def add_col():
    pass


canv_w = 600
canv_h = 600
root = tk.Tk()

head = tk.Frame(root)
numbers = tk.Entry(head, width=30)
tk.Button(head, text='Доб. строку', command=add_row).grid(row=0, column=1)
tk.Button(head, text='Доб. столбец', command=add_col).grid(row=0, column=2)
tk.Button(head, text='Решить').grid(row=0, column=3)
tk.Button(head, text='Очистить').grid(row=0, column=4)
numbers.grid(row=0, column=0)
head.pack(fill=tk.Y)
canv = tk.Canvas(root, width=canv_w, height=canv_h)
canv.pack()
root.mainloop()
