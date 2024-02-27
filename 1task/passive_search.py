from general import acc, hex
from pandas import DataFrame as df
import math


def passive_search(f, a, b, eps=1e-4):
    header_row = ['iteration', 'X', 'F(x)', 'x_min', 'F(x_min)', 'calls']
    print_table_rows = []
   

    n = math.ceil((b - a) / acc((a + b) / 2))  # количество разбиений интервала
    delta = (b - a) / n  # шаг разбиения
    x_min = a  # начальное значение аргумента минимума
    f_min = f(x_min)  # начальное значение функции в точке минимума
    # x = a
    # f_x = f(x)

    print("iter, a, x_min, f_min")
    for i in range(0, n + 1):
        # print("{},    {:.7},   ".format(i, float.hex(x)),end='  ')

        x = a + i * delta  # текущее значение аргумента
        f_x = f(x)  # текущее значение функции
        row = [i, hex(x), hex(f_x)]
        if f_x < f_min:
            x_min = x
            f_min = f_x
        elif f_x > f_min:
            break

        row += [hex(x_min), hex(f_min), f.callsNumber]
        print_table_rows.append(row)
        # print(" {:.9}".format(float.hex(f_min)))

    # print('\n'



    y = df(data=print_table_rows, columns=header_row)
    y.to_markdown('passive_search_output.md', index=False)

    return f.callsNumber, x_min, f_min