import tkinter as tk


def add_row():
    global rows, canv_h, canv_w, crossword, cr_height
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
    cr_height = len(rows)
    paint()


def add_col():
    global columns, canv_w, canv_h, crossword, cr_width
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
    cr_width = len(columns)
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
    canv.delete()
    x, y = 10 + row_max() * 24, 10 + col_max() * 24
    for i in range(cr_height):
        for j in range(cr_width):
            a = x + j * 24
            b = y + i * 24
            if crossword[i][j] == 1:
                square_color = 'black'
            elif crossword[i][j] == 0.5:
                square_color = 'gray70'
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
    global canv_w, canv_h, cr_height, cr_width
    canv_width = (cr_width + row_max()) * 24 + 20
    if canv_w < canv_width:
        canv_w = canv_width
    canv_height = (cr_height + col_max()) * 24 + 20
    if canv_h < canv_height:
        canv_h = canv_height


def empty_cross():
    crossword = [[0.5 for x in range(len(columns))] for y in range(len(rows))]
    return crossword


def cross_row(n):
    return crossword[n]


def new_cross_row(n, line):
    crossword[n] = line


def cross_col(n):
    return [crossword[i][n] for i in range(len(crossword))]


def new_cross_col(n, line):
    for i in range(len(line)):
        crossword[i][n] = line[i]


def analyze(line, nums):
    start_sq = 0
    if sum(nums) + len(nums) - 1 > len(line) / 2:
        k = len(line) - sum(nums) - len(nums) + 1
        for num in nums:
            if num > k:
                for i in range(start_sq + k, start_sq + num):
                    line[i] = 1
            start_sq += num + 1
    line_values = []
    for i in range(len(line)):
        if i == 0:
            current_value = [line[i], 1]
            line_values.append(current_value)
        else:
            if line[i] == line[i - 1]:
                current_value[1] += 1
            else:
                current_value = [line[i], 1]
                line_values.append(current_value)

    return line



def solu():
    flag, cr_cols, cr_rows = check()
    zzz = 0
    while zzz < 1:
        for i in range(cr_height):
            line = cross_row(i)
            new_line = analyze(line, rows[i])
            new_cross_row(i, new_line)
        for i in range(cr_width):
            line = cross_col(i)
            new_line = analyze(line, columns[i])
            new_cross_col(i, new_line)
        zzz += 1
    paint_crossword()



def solution():
    for i in range(len(rows)):
        position = 0
        if sum(rows[i]) + len(rows[i]) - 1 > len(columns) / 2:
            k = len(columns) - sum(rows[i]) - len(rows[i]) + 1
            for num in rows[i]:
                if num > k:
                    for j in range(position + k, position + num):
                        crossword[i][j] = 1
                        paint_crossword()
                position += num + 1
    for i in range(len(columns)):
        position = 0
        if sum(columns[i]) + len(columns[i]) - 1 > len(rows) / 2:
            k = len(rows) - sum(columns[i]) - len(columns[i]) + 1
            for num in columns[i]:
                if num > k:
                    for j in range(position + k, position + num):
                        crossword[j][i] = 1
                        paint_crossword()
                position += num + 1
    flag, cr_cols, cr_rows = check()
    for i in range(cr_width):
        col = cross_col(i)
        col_values = analysis(col)

        # проверка верхнего края
        start_sq = 0
        for j in range(len(col_values)):
            if col_values[j][0] == 1:
                break
            start_sq += col_values[j][1]
        if start_sq == 0:
            for k in range(columns[i][0]):
                crossword[k][i] = 1
            if k + 1 < cr_height:
                crossword[k + 1][i] = 0
        else:
            if columns[i][0] > start_sq:
                for k in range(start_sq, columns[i][0]):
                    crossword[k][i] = 1
            if columns[i][0] == start_sq:
                crossword[0][i] = 0
        # проверка нижнего края
        start_sq = cr_height - 1
        for j in range(len(col_values), 0, -1):
            if col_values[j - 1][0] == 1:
                break
            start_sq -= col_values[j - 1][1]
        if start_sq == cr_height - 1:
            for k in range(cr_height, columns[i][0], -1):
                crossword[k][i] = 1
            if k - 1 < cr_height:
                crossword[k - 1][i] = 0
        else:
            if cr_height - columns[i][-1] < start_sq:
                for k in range(start_sq - 1, cr_height - 1 - columns[i][-1], -1):
                    crossword[k][i] = 1
            if cr_height - 1 - columns[i][-1] == start_sq:
                crossword[-1][i] = 0



    for i in range(cr_height):
        row = cross_row(i)
        row_values = analysis(row)

        # проверка левого края
        start_sq = 0
        for j in range(len(row_values)):
            if row_values[j][0] == 1:
                break
            start_sq += row_values[j][1]
        if start_sq == 0:
            for k in range(rows[i][0]):
                crossword[i][k] = 1
            if k + 1 < cr_width:
                crossword[i][k + 1] = 0
        else:
            print(start_sq, j)
            if rows[i][0] > start_sq:
                for k in range(start_sq, rows[i][0]):
                    crossword[i][k] = 1
            if rows[i][0] == start_sq:
                crossword[i][0] = 0
        # проверка правого края
        start_sq = cr_width - 1
        for j in range(len(row_values), 0, -1):
            if row_values[j - 1][0] == 1:
                break
            start_sq -= row_values[j - 1][1]
        if start_sq == cr_width - 1:
            for k in range(cr_width, rows[i][0], -1):
                crossword[i][k] = 1
            if k - 1 < cr_width:
                crossword[i][k - 1] = 0
        else:
            print(start_sq)
            if cr_width - rows[i][-1] < start_sq:
                for k in range(start_sq, cr_width - 1 - rows[i][-1], -1):
                    crossword[i][k] = 1
            if cr_width - 1 - rows[i][-1] == start_sq:
                crossword[i][-1] = 0

    paint_crossword()



def check():
    cr_rows = []
    for j in range(len(crossword)):
        row = cross_row(j)
        numbers = []
        k = 0
        for i in range(len(row)):
            if row[i] == 1:
                if i == 0:
                    numbers.append(1)
                else:
                    if row[i - 1] == 1:
                        numbers[k] += 1
                    else:
                        numbers.append(1)
            elif i > 0 and row[i - 1] == 1:
                k += 1
        cr_rows.append(numbers)
    cr_cols = []
    for j in range(len(crossword[0])):
        col = cross_col(j)
        numbers = []
        k = 0
        for i in range(len(col)):
            if col[i] == 1:
                if i == 0:
                    numbers.append(1)
                else:
                    if col[i - 1] == 1:
                        numbers[k] += 1
                    else:
                        numbers.append(1)
            elif i > 0 and col[i - 1] == 1:
                k += 1
        cr_cols.append(numbers)
    if cr_cols == columns and cr_rows == rows:
        flag = True
    else:
        flag = False
    return flag, cr_cols, cr_rows


canv_w = 500
canv_h = 300
rows = []
columns = []
columns = [[1, 2], [3, 2], [3, 1], [1, 4], [1], [3, 1], [3, 1, 3], [5, 3], [4, 3], [4, 1]]
rows = [[2, 4], [4, 4], [2, 5], [1, 3], [5], [1], [1, 3], [3, 5], [2, 3], [1]]
cr_width = 0
cr_height = 0
cr_width = len(columns)
cr_height = len(rows)
root = tk.Tk()

head = tk.Frame(root)
numbers = tk.Entry(head, width=30)
tk.Button(head, text='Доб. строку', command=add_row).grid(row=0, column=1)
tk.Button(head, text='Доб. столбец', command=add_col).grid(row=0, column=2)
tk.Button(head, text='Решить', command=solu).grid(row=0, column=3)
tk.Button(head, text='Очистить').grid(row=0, column=4)
numbers.grid(row=0, column=0)
head.pack(fill=tk.Y)
canv_size()
canv = tk.Canvas(root, width=canv_w, height=canv_h)
canv.pack()
crossword = empty_cross()
paint()
root.mainloop()
