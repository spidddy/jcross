import tkinter as tk


def add_row():
    global rows, canv_h, canv_w, crossword
    num = numbers.get().split()
    if len(num) == 0:
        return
    for i in range(len(num)):
        num[i] = int(num[i])
    rows.append(num)
    numbers.delete(0, tk.END)
    canv_size()
    canv.config(width=canv_w, height=canv_h)
    crossword = empty_cross()
    paint()

def add_col():
    global columns, canv_w, canv_h, crossword
    num = numbers.get().split()
    if len(num) == 0:
        return
    for i in range(len(num)):
        num[i] = int(num[i])
    columns.append(num)
    numbers.delete(0, tk.END)
    canv_size()
    canv.config(width=canv_w, height=canv_h)
    crossword = empty_cross()
    paint()


def paint():
    canv.create_rectangle(10, 10, 10 + row_max() * 24, 10 + col_max() * 24, fill='gray')
    left_side(10, 10 + col_max() * 24)
    top_side(10 + row_max() * 24, 10)
    paint_crossword()


def left_side(x, y):
    for i in range(len(rows)):
        for j in range(row_max()):
            a = x + j * 24
            b = y + i * 24
            canv.create_rectangle(a, b, a + 24, b + 24, fill='light gray')
            if j >= row_max() - len(rows[i]):
                amendment = row_max() - len(rows[i])
                canv.create_text(a + 12, b + 12, text=rows[i][j - amendment])


def top_side(x, y):
    for i in range(len(columns)):
        for j in range(col_max()):
            a = x + i * 24
            b = y + j * 24
            canv.create_rectangle(a, b, a + 24, b + 24, fill='light gray')
            if j >= col_max() - len(columns[i]):
                amendment = col_max() - len(columns[i])
                canv.create_text(a + 12, b + 12, text=columns[i][j - amendment])

def paint_crossword():
    global crossword
    x, y = 10 + row_max() * 24, 10 + col_max() * 24
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            a = x + j * 24
            b = y + i * 24
            if crossword[i][j] == 1:
                square_color = 'black'
            else:
                square_color = 'white'
            canv.create_rectangle(a, b, a + 24, b + 24, fill=square_color)



def row_max():
    global rows
    max_value = 0
    for row in rows:
        if len(row) > max_value:
            max_value = len(row)
    return max_value


def col_max():
    global columns
    max_value = 0
    for col in columns:
        if len(col) > max_value:
            max_value = len(col)
    return max_value


def canv_size():
    global canv_w, canv_h
    canv_width = (len(columns) + row_max()) * 24 + 20
    if canv_w < canv_width:
        canv_w = canv_width
    canv_height = (len(rows) + col_max()) * 24 + 20
    if canv_h < canv_height:
        canv_h = canv_height


def empty_cross():
    crossword = [[0] * len(columns)] * len(rows)
    return crossword


canv_w = 500
canv_h = 300
rows = []
columns = []
columns = [[1, 2], [3, 2], [3, 1], [1, 4], [1], [3, 1], [3, 1, 3], [5, 3], [4, 3], [4, 1]]
rows = [[2, 4], [4, 4], [2, 5], [1, 3], [5], [1], [1, 3], [3, 5], [2, 3], [1]]

root = tk.Tk()

head = tk.Frame(root)
numbers = tk.Entry(head, width=30)
tk.Button(head, text='Доб. строку', command=add_row).grid(row=0, column=1)
tk.Button(head, text='Доб. столбец', command=add_col).grid(row=0, column=2)
tk.Button(head, text='Решить').grid(row=0, column=3)
tk.Button(head, text='Очистить').grid(row=0, column=4)
numbers.grid(row=0, column=0)
head.pack(fill=tk.Y)
canv_size()
canv = tk.Canvas(root, width=canv_w, height=canv_h)
canv.pack()
crossword = empty_cross()
paint()
root.mainloop()
