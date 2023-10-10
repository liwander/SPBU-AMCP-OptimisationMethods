from matrix import *
from deriv import *
from collections.abc import Callable



# implement newton gd method
# implement speeded up gd method

def newtonStepCoef(
        prevLen: float
) -> float:
    curStepLength = 0
    pass


def constStepLen(
        prevLen: float
) -> float:
    pass


def gradDesc(
        func: Callable[[tuple[float]], float],
        initX: tuple[float],
        stepLength: Callable[[float], float],
        eps: float = 1e-6
) -> float:
    '''
    Calculate minimum of multiple variable function using gradient descent method with constant step 
    '''

    X = initX
    grad = funcGrad(func)

    while (grad(X).norm > eps):
        X = X - stepLength * grad(X)

    return X
