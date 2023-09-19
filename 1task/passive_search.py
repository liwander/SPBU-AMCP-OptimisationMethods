from general import acc
import math


def passive_search(f, a, b, eps=1e-4):
    n = math.ceil((b - a) / acc((a + b) / 2))  # количество разбиений интервала
    delta = (b - a) / n  # шаг разбиения
    x_min = a  # начальное значение аргумента минимума
    f_min = f(x_min)  # начальное значение функции в точке минимума
    x = a

    print("iter, a, x_min, f_min")
    for i in range(1, n + 1):
        print("{},    {:.7},   ".format(i, float.hex(x)),
               end='  ')

        x = a + i * delta  # текущее значение аргумента
        f_x = f(x)  # текущее значение функции
        if f_x < f_min:
            x_min = x
            f_min = f_x
        elif f_x > f_min:
            break

        print(" {:.9}".format(float.hex(f_min)))

    print('\n')
    from general import count

    return count, x_min, f_min
