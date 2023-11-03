from common import *
from unconditional_optim import gradDescVariableStep as minimize
from collections.abc import Callable


@call_counted
def barrierFunction(x: vector) -> float:
    # return - 1 / (x[0] - x[1] * cf)
    return -np.log(-(x[0] - x[1] * cf))


@call_counted
def barrierFunctionGradient(x: vector) -> float:
    # return (1 / (x[0] - x[1] * cf) ** 2) * np.array([1, -cf])
    return -(1 / (x[0] - x[1] * cf)) * np.array([1, -cf])


def barrierCoef(step: float) -> float:
    return 10.0 ** step


def generateBarrieredFunc(step: float) -> Callable[[vector], float]:
    r = barrierCoef(step)
    def phi(x): return objectFunction(x) + r * barrierFunction(x)
    return phi


def generateBarrieredFuncGrad(step: float) -> Callable[[vector], vector]:
    r = barrierCoef(step)
    def phistreak(x): return objectFunctionGradient(x) + r * barrierFunctionGradient(x)
    return phistreak





def intpen():
    print(barrierCoef(1)*barrierFunction(np.array([ -2.873583,-50.75413516])))
    x = np.array([cf - 2, 1])
    xprev = x * 1000
    k = 0
    # while abs(barrierCoef(k)*barrierFunction(x)) > 1e-2:
    while np.linalg.norm(x - xprev) > 1e-2:
        print(k + 1, x)
        f = generateBarrieredFunc(k)
        fstreak = generateBarrieredFuncGrad(k)
        xprev = x
        x = minimize(f, fstreak, initx=x)
        k += 1
        # print('\n==================\n')

    # print(k + 1, x)
    return x
