import general as g
import math as m
import sys
from pandas import DataFrame as df
from general import hex


def newton(f, deriv, deriv2, a, b, eps=g.default_accuracy):
    header_row = ['iteration', 'X', 'F(X)', 'F\'(X)', 'F\'\'(X)', 'prime1 calls', 'prime2 calls']
    print_table_rows = []
   

    x = (a + b) / 2
    k = 0

    while abs(d1 := deriv(x)) > eps:

        k += 1

        # d1 = g.deriv(x) 
        d2 = deriv2(x)
        row = [k, hex(x), hex(f(x)), hex(d1), hex(d2)]

        x = x - d1 / d2
        # print(x)

        row += [deriv.callsNumber, deriv2.callsNumber] 
        print_table_rows.append(row)



    y = df(data=print_table_rows, columns=header_row)
    y.to_markdown('newton_output.md', index=False)
    return x, f(x)
