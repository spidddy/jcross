####################################
#                                  #
#    Решаем японские кроссворды    #
#                                  #
####################################

import tkinter as tk

# Временные переменные для отрисовки интерфейса
cr_width = 10
cr_height = 10

columns = [[1, 2], [3, 2], [3, 1], [1, 4], [1], [3, 1], [3, 1, 3], [5, 3], [4, 3], [4, 1]]
rows = [[2, 4], [4, 4], [2, 5], [1, 3], [5], [1], [1, 3], [3, 5], [2, 3], [1]]

root = tk.Tk()
root.title('Решаем японские кроссворды')
root.geometry('800x600')

head = tk.Frame(root)
numbers = tk.Entry(head, width=30).grid(row=0, column=0)
tk.Button(head, text='Ввод').grid(row=0, column=1)
tk.Button(head, text='Очистить').grid(row=0, column=2)
head.pack()


top_left = tk.Frame(root)
tk.Frame(top_left, width=25, height=25, bg='green').grid(row=0, column=0)
tk.Button(top_left, text='+').grid(row=0, column=1, sticky='nesw')
tk.Button(top_left, text='+').grid(row=1, column=0, sticky='nesw')
tk.Frame(top_left, width=25, height=25, bg='green').grid(row=1, column=1)
top_left.pack()

top_right = tk.Frame(root)
h = 0

for col in columns:
    if len(col) > h:
        h = len(col)
for i in range(len(columns)):
    for j in range(h):
        if j < h - len(columns[i]):
            txt = ''
        else:
            txt = str(columns[i][j - (h - len(columns[i]))])
        sq = tk.Frame(top_right, width=25, height=25, borderwidth=1, relief=tk.RIDGE)
        tk.Label(sq, text=txt).grid(row=0, column=0)
        sq.grid(row=j, column=i, sticky='snwe')
    top_right.columnconfigure(i, minsize=25)
top_right.grid(row=0, column=1)
body = tk.Frame(root)
left = tk.Frame(body)
r = 0
for row in rows:
    if len(row) > r:
        r = len(row)
for i in range(len(rows)):
    for j in range(r):
        if j < r - len(rows[i]):
            txt = ''
        else:
            txt = str(rows[i][j - (r - len(rows[i]))])
        sq = tk.Frame(left, width=25, height=25, borderwidth=1, relief=tk.RIDGE)
        tk.Label(sq, text=txt).grid(row=0, column=0)
        sq.grid(row=i, column=j, sticky='snwe')
    left.columnconfigure(i, minsize=25)

left.grid(row=1, column=0)

crossword = tk.Frame(body)
for i in range(len(rows)):
    for j in range(len(columns)):
        sq = tk.Frame(left, width=25, height=25, borderwidth=1, relief=tk.RIDGE)
        sq.grid(row=i, column=j, sticky='snwe')
crossword.grid(row=1, column=1)

body.pack()


root.mainloop()