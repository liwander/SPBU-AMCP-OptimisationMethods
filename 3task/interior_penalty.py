from common import *
from intpen_uncmin import gradDescVariableStep as minimize
from collections.abc import Callable


@call_counted
def barrierFunction(x: vector) -> float:
    # return - 1 / (x[0] - x[1] * cf)
    # return -np.log(-(x[0] - x[1] * cf))    
    return -np.log(-(constraintFunction(x)))


@call_counted
def barrierFunctionGradient(x: vector) -> float:
    # return (1 / (x[0] - x[1] * cf) ** 2) * np.array([1, -cf])
    # return -(1 / (x[0] - x[1] * cf)) * np.array([1, -cf])
    return -(1 / constraintFunction(x)) * constraintFunctionGradient



def barrierCoef(step: float) -> float:
    return 10 ** (-step)
    # return 1e-1


def generateBarrieredFunc(step: float) -> Callable[[vector], float]:
    def phi(x): return objectFunction(x) + barrierCoef(step) * barrierFunction(x)
    # def phi(x) : return - r / (x[0] - x[1] * cf) + np.cosh(cfs[0] * x[0]) + np.cosh(cfs[2] * x[1]) + x[0] + cfs[1] * x[1]
    return phi


def generateBarrieredFuncGrad(step: float) -> Callable[[vector], vector]:
    def phistreak(x): return objectFunctionGradient(x) + barrierCoef(step) * barrierFunctionGradient(x)
    # def phistreak(x) : return np.array([cfs[0] * np.sinh(cfs[0] * x[0]) + 1,
    #         cfs[2] * np.sinh(cfs[2] * x[1]) + cfs[1]]) + r * (1 / (x[0] - x[1] * cf) ** 2) * np.array([1, -cf])
    return phistreak


def intpen():
    # print(barrierCoef(1)*barrierFunction(np.array([ -2.873583,-50.75413516])))
    x = np.array([cf - 2, 1])
    # xprev = x * 1000
    k = 0
    while abs(barrierCoef(k)*barrierFunction(x)) > 1e-2:
        print(k + 1, x, np.sign(constraintFunction(x)))
        f = generateBarrieredFunc(k)
        fstreak = generateBarrieredFuncGrad(k)
        # xprev = x
        x = minimize(f, fstreak, constraintFunction, initx=x)
        k += 1
        # print('\n==================\n')

    # print(k + 1, x)
    return x
