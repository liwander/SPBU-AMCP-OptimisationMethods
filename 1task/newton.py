import general as g
import math as m
import sys

def newton(f, a, b, eps=g.default_accuracy):
    x = m.pi
    k = 0

    while abs(g.deriv(x)) > eps:

        k += 1
        c = input()

        print(f'iter: {k} x: {float.hex(x)}   f(x): {float.hex(f(x))}  f\'(x){float.hex(g.deriv(x))}  f\'\'(x){float.hex(g.deriv2(x))}')

        x = x - g.deriv(x) / g.deriv2(x)
        print(x)
        
        # print(f'\t{g.count1}\t\t{g.count2}')

    return x, f(x)
