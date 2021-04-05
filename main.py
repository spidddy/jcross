####################################
#                                  #
#    Решаем японские кроссворды    #
#                                  #
####################################

import tkinter as tk

# Временные переменные для отрисовки интерфейса
cr_width = 10
cr_height = 10

columns = [
    [1, 2],
    [3, 2],
    [3, 1],
    [1, 4],
    [1],
    [3, 1],
    [3, 1, 3],
    [5, 3],
    [4, 3],
    [4, 1]
]

root = tk.Tk()
root.title('Решаем японские кроссворды')
root.geometry('800x600')

head = tk.Frame(root)
numbers = tk.Entry(head, width=30).grid(row=0, column=0)
tk.Button(head, text='Ввод').grid(row=0, column=1)
tk.Button(head, text='Очистить').grid(row=0, column=2)
head.pack()

body = tk.Frame(root)
top_left = tk.Frame(body)
tk.Frame(top_left, width=25, height=25, bg='green').grid(row=0, column=0)
tk.Button(top_left, text='+').grid(row=0, column=1, sticky='nesw')
tk.Button(top_left, text='+').grid(row=1, column=0, sticky='nesw')
tk.Frame(top_left, width=25, height=25, bg='green').grid(row=1, column=1)
top_left.grid(row=1, column=0)
body.pack()

root.mainloop()