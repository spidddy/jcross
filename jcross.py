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
    print(line)
    print(nums)
    print(line_values)
    print()

    for j in range(2):
        line.reverse()
        nums.reverse()
        line_values.reverse()
        if line[0] == 1:
            for i in range(nums[0]):
                line[i] = 1
            if nums[0] < len(line):
                line[nums[0]] = 0
        if line[0] == 0.5:
            next_position = line_values[0][1]
            if next_position < len(line):
                if line[next_position] == 1:
                    if nums[0] > next_position:
                        for i in range(next_position, nums[0]):
                            line[i] = 1
                    if nums[0] == next_position:
                        if nums[0] == line_values[1][1]:
                            for i in range(next_position):
                                line[i] = 0
                            for i in range(next_position, next_position + nums[0]):
                                line[i] = 1
                            line[next_position + nums[0]] = 0
                        else:
                            line[0] = 0





    return line



def solu():
    flag, cr_cols, cr_rows = check()
    zzz = 0
    while zzz < 10:
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
