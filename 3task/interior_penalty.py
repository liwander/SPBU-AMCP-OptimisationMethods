from common import *
from unconditional_optim import gradDescVariableStep as minimize
from collections.abc import Callable

# @call_counted


def barrierFunction(x: vector) -> float:
    return - 1 / (x[0] - x[1] * cf)

# @call_counted


def barrierFunctionGradient(x: vector) -> float:
    return (1 / (constraintFunction(x) ** 2)) * np.array([1, -cf])


def barrierCoef(step: float) -> float:
    return 10.0 ** (-step)


def generateBarrieredFunc(step: float) -> Callable[[vector], float]:
    r = barrierCoef(step)
    phi = lambda x : objectFunction(x) + r * barrierFunction(x)
    return phi


def generateBarrieredFuncGrad(step: float) -> Callable[[vector], vector]:
    r = barrierCoef(step)
    phistreak = lambda x : objectFunctionGradient(x) + r * barrierFunctionGradient(x)
    return phistreak


# print(barrierCoef(1)*barrierFunction(np.array([-100.28171817,    1.        ])))

def intpen():
    x = np.array([cf - 1, 1])
    k = 0
    while abs(barrierCoef(k)*barrierFunction(x)) > 1e-2:
        print(k + 1, x)
        f = generateBarrieredFunc(k)
        fstreak = generateBarrieredFuncGrad(k)
        x = minimize(f, fstreak, initx=x)
        k += 1
        print('\n==================\n')

    print(k + 1, x)
    return x
