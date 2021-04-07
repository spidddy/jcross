####################################
#                                  #
#    Решаем японские кроссворды    #
#                                  #
####################################

import tkinter as tk

rows = [[3, 4]]
columns = [[3, 2]]


def add_row():
    num = numbers.get().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    rows.append(num)
    numbers.delete(0, tk.END)
    return rewrite()


def add_col():
    num = numbers.get().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    columns.append(num)
    numbers.delete(0, tk.END)
    return rewrite()

# Временные переменные для отрисовки интерфейса

cr_width = 10
cr_height = 10

# columns = [[1, 2], [3, 2], [3, 1], [1, 4], [1], [3, 1], [3, 1, 3], [5, 3], [4, 3], [4, 1]]
# rows = [[2, 4], [4, 4], [2, 5], [1, 3], [5], [1], [1, 3], [3, 5], [2, 3], [1]]

#################################################

root = tk.Tk()
root.title('Решаем японские кроссворды')
# root.geometry('800x600')
print(rows)
print(columns)
c_max = 0
for i in columns:
    if len(i) > c_max:
        c_max = len(i)
r_max = 0
for i in rows:
    if len(i) > r_max:
        r_max = len(i)
head = tk.Frame(root)
numbers = tk.Entry(head, width=30)
tk.Button(head, text='Доб. строку', command=add_row).grid(row=0, column=1)
tk.Button(head, text='Доб. столбец', command=add_col).grid(row=0, column=2)
tk.Button(head, text='Очистить').grid(row=0, column=3)
numbers.grid(row=0, column=0)
head.pack(fill=tk.Y)


def rewrite():
    body = tk.Frame(root)
    top_left = tk.Frame(body)
    for i in range(c_max):
        for j in range(r_max):
            tk.Frame(top_left, width=25, height=25, bg='green').grid(row=i, column=j)

    top_left.pack(side=tk.LEFT)

    top_right = tk.Frame(body)
    for i in range(len(columns)):
        for j in range(c_max):
            if j < c_max - len(columns[i]):
                txt = ''
            else:
                txt = str(columns[i][j - (c_max - len(columns[i]))])
            sq = tk.Frame(top_right, width=25, height=25, bg='light gray', borderwidth=1, relief=tk.RIDGE)
            tk.Label(sq, text=txt, bg='light gray').grid(row=0, column=0)
            sq.grid(row=j, column=i, sticky='snwe')
        top_right.columnconfigure(i, minsize=25)
    top_right.pack(side=tk.LEFT)
    body.pack()

    body2 =tk.Frame(root)
    left = tk.Frame(body2)
    for i in range(len(rows)):
        for j in range(r_max):
            if j < r_max - len(rows[i]):
                txt = ''
            else:
                txt = str(rows[i][j - (r_max - len(rows[i]))])
            sq = tk.Frame(left, width=25, height=25, bg='light gray', borderwidth=1, relief=tk.RIDGE)
            tk.Label(sq, text=txt, bg='light gray').grid(row=0, column=0)
            sq.grid(row=i, column=j, sticky='snwe')
        left.columnconfigure(i, minsize=25)
    left.pack(side=tk.LEFT)

    crossword = tk.Frame(body2)
    for i in range(len(rows)):
        for j in range(len(columns)):
            sq = tk.Frame(left, width=25, height=25, borderwidth=1, relief=tk.RIDGE)
            sq.grid(row=i, column=j+r_max, sticky='snwe')
    crossword.pack(side=tk.RIGHT)

    body2.pack()


root.update()
root.mainloop()