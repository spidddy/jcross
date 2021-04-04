####################################
#                                  #
#    Решаем японские кроссворды    #
#                                  #
####################################

import tkinter as tk

root = tk.Tk()
root.title('Решаем японские кроссворды')

body = tk.Frame(
    master=root
)
body.grid(row=0, column=0)
top_left_square = tk.Frame(
    master=body
)
top_left_square.grid(row=0, column=0)
for i in range(2):
    for j in range(2):
        square_name = 'square_' + str(i) + '_' + str(j)
        square_name = tk.Frame(
            master=top_left_square,
            width=25,
            height=25,
            borderwidth=1,
            relief=tk.RAISED
        )
        square_name.grid(row=i, column=j)

# код ниже почему-то не работает

add_column = tk.Button(
    master=square_0_1,
    text='+',
)
add_row = tk.Button(
    master=square_1_0,
    text='+',
)
add_column.grid(row=0, column=0)
root.mainloop()