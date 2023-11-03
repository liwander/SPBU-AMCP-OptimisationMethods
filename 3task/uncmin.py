from collections.abc import Callable
import numpy as np
from common import constraintFunction

vector = np.array


def stepl(f : Callable[[float], float] ) -> float:
    a, b, eps = 0, 1, 1e-2
    n = int(np.ceil((b - a) / eps))  # количество разбиений интервала
    delta = (b - a) / n  # шаг разбиения
    x_min = a + delta  # начальное значение аргумента минимума
    f_min = f(x_min)  # начальное значение функции в точке минимума

    for i in range(1, n + 1):
        x = a + i * delta  # текущее значение аргумента
        
        if constraintFunction()
            f_x = f(x)  # текущее значение функции
            if f_x < f_min:
                x_min = x
                f_min = f_x

    return x_min


def uncmin(
        f: Callable[[vector], float],
        grad: Callable[[vector], vector],
        initx: vector,
        eps: float = 1e-3,
        file = None
) -> vector:

    x = initx
    grx = grad(x)
    iter = 0

    while (np.linalg.norm(grx) > eps):
        iter += 1
        grx = grad(x)
        minarg = lambda a : f(x - a * grx)
        x -= grx * stepl(minarg)

    print(iter, f(x))
    return x