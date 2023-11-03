from common import *
from unconditional_optim import gradDescVariableStep as minimize
from collections.abc import Callable

# @call_counted


def extPenaltyFunction(x: vector) -> float:
    return max(0, x[0] - cf * x[1]) ** 2

# @call_counted


def extPenaltyFunctionGradient(x: vector) -> float:
    return max(0, x[0] - cf * x[1]) * 2 * np.array([1, -cf])


def extPenaltyCoef(step: float) -> float:
    return 10.0 ** step


def generateExtPenaltiedFunc(step: float) -> Callable[[vector], float]:
    r = extPenaltyCoef(step)
    phi = lambda x : objectFunction(x) + r * extPenaltyFunction(x)
    return phi


def generateExtPenaltiedFuncGrad(step: float) -> Callable[[vector], vector]:
    r = extPenaltyCoef(step)
    phistreak = lambda x : objectFunctionGradient(x) + r * extPenaltyFunctionGradient(x)
    return phistreak


def expen():
    x = np.array([cf + 1, 1])
    k = 0
    while extPenaltyFunction(x) > 1e-2:
        print(k, extPenaltyFunction(x))
        print(x)
        f = generateExtPenaltiedFunc(k)
        fstreak = generateExtPenaltiedFuncGrad(k)
        x = minimize(f, fstreak, initx=x)
        k += 1

    return x
