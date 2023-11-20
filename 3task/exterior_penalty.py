from common import *
from extpen_uncmin import gradDescVariableStep as minimize
from collections.abc import Callable

@call_counted
def extPenaltyFunction(x: vector) -> float:
    return max(0, constraintFunction(x)) ** 2


@call_counted
def extPenaltyFunctionGradient(x: vector) -> float:
    return max(0, constraintFunction(x)) * 2 * constraintFunctionGradient


def extPenaltyCoef(step: float) -> float:
    return 10 ** step


def generateExtPenaltiedFunc(step: float) -> Callable[[vector], float]:
    # r = extPenaltyCoef(step)
    # def phi(x): return np.cosh(cfs[0] * x[0]) + np.cosh(cfs[2] * x[1]) + x[0] + cfs[1] * x[1] + \
    #     r * ((x[0] - cf * x[1]) ** 2)
    def phi(x): return objectFunction(x) + extPenaltyCoef(step) * extPenaltyFunction(x)
    return phi


def generateExtPenaltiedFuncGrad(step: float) -> Callable[[vector], vector]:
    # r = extPenaltyCoef(step)
    # def phistreak(x): return np.array([cfs[0] * np.sinh(cfs[0] * x[0]) + 1,
    #                                    cfs[2] * np.sinh(cfs[2] * x[1]) + cfs[1]]) +  r * ((x[0] - cf * x[1]) * 2) * np.array([1, -cf])
    def phistreak(x): return objectFunctionGradient(x) + extPenaltyCoef(step) * extPenaltyFunctionGradient(x)
    return phistreak


def expen():
    x = np.array([cf + 10, 1])
    k = 0
    while extPenaltyFunction(x) > 1e-6:
        print(k, extPenaltyFunction(x), x)
        f = generateExtPenaltiedFunc(k)
        fstreak = generateExtPenaltiedFuncGrad(k)
        x = minimize(f, fstreak, initx=x)
        k += 1

    return x
