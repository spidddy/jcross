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

top_panel = tk.Frame(
    master=root
)
top_panel.grid(row=0, column=0)
numbers = tk.Entry(
    master=top_panel,
    width=30
)
numbers.grid(row=0, column=0)
button_enter = tk.Button(
    master=top_panel,
    text='Ввод'
)
button_enter.grid(row=0, column=1)

body = tk.Frame(
    master=root
)
body.grid(row=1, column=0)

top_left_square = tk.Frame(
    master=body
)
square_name = ['vvv']
top_left_square.grid(row=0, column=0)
for i in range(2):
    for j in range(2):
#        square_name = 'square_' + str(i) + '_' + str(j)
        square_name[0] = tk.Frame(
            master=top_left_square,
            width=29,
            height=29,
            borderwidth=1,
            relief=tk.RAISED,
            bg='gray'
        )
        square_name[0].grid(row=i, column=j)
        if i == 0 and j == 1:
            add_column = tk.Button(
                master=square_name[0],
                text='+',
            )
            add_column.grid(row=0, column=0)
        if i == 1 and j == 0:
            add_row = tk.Button(
                master=square_name[0],
                text='+',
            )
            add_row.grid(row=0, column=0)
cross_top = tk.Frame(
    master=body
)
cross_top.columnconfigure(0, minsize=29)
cross_top.grid(row=0, column=1)

i = 0
for col in columns:
    col_name = 'col_top' + str(i)
    col_name = tk.Frame(master=cross_top)
    col_name.grid(row=0, column=i)
    j = 0
    for sq in col:
        square_name = 'sq_' + str(i) + '_' + str(j)
        lable_name = 'lb_' + str(i) + '_' + str(j)
        square_name = tk.Frame(
            master=col_name,
            width=29,
            height=29,
            borderwidth=1,
            relief=tk.RAISED,
        )
        lable_name = tk.Label(
            master=square_name,
            text=sq
        )
        lable_name.grid(row=0, column=0, sticky="nsew")
        square_name.pack(fill=tk.X)
        j += 1
    i += 1


root.mainloop()