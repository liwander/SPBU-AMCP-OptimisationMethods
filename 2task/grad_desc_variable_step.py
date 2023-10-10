import random
from collections.abc import Callable
from vec_op import *


def gradDescVariableStep(
        func: Callable[[tuple[float]], float],
        funcGrad: Callable[[tuple[float]], tuple[float]],
        secDer: tuple[float],
        initx: tuple[float],
        stepLength: float,
        eps: float = 16e-6
) -> float:
    '''
    Calculate minimum of multiple variable function using gradient descent method with constant step 
    '''

    xk = initx
    fxk = func(xk)
    gradxk = funcGrad(xk)


    iter = 0
    coef = lambda iter : 1 / (iter + 1)

    while(max([abs(gradxk[i]/secDer[i]) for i in range(4)]) > eps):
        iter += 1
        x = vecSum(xk, vecMultByScalar(gradxk, -stepLength))
        fx = func(x)

        if fx - fxk > -stepLength * eps * vecNorm(gradxk):
            stepLength *= coef(iter)
            # stepLength *= random.uniform(0.0, 1.0)
            continue

        xk = x
        fxk = fx
        gradxk = funcGrad(xk)

    return xk
