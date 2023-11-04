from collections.abc import Callable
from vec_op import *


def gradDescVariableStep(
        func: Callable[[tuple[float]], float],
        funcGrad: Callable[[tuple[float]], tuple[float]],
        secDer: tuple[float],
        initx: tuple[float],
        stepLength: float = 1e-1,
        eps: float = 16e-6,
        file = None
) -> float:
    '''
    Calculate minimum of multiple variable function using gradient descent method with variable step 
    '''

    xk = initx
    fxk = func(xk)
    gradxk = funcGrad(xk)
    iter = 0
    # coef = lambda iter : 1 / (iter + 1)
    coef = 99 / 100

    file.write("Метод градиентного спуска с переменынм шагом\n")
    file.write(
        "It\tX\t\t\t\t\t\t\t\t\t\t\t\tF(x)\t\tAlpha\t\tgrad F\t\t\t\t\t\t\t\t\tТруд. F\t Труд. grad\n")
   

    while(max([abs(gradxk[i]/secDer[i]) for i in range(4)]) > eps):
        iter += 1
        x = vecSum(xk, vecMultByScalar(gradxk, -stepLength))
        fx = func(x)

        if fx - fxk > -stepLength * eps * (vecNorm(gradxk) ** 2):
            stepLength *= coef
            # stepLength *= coef(iter)
            # stepLength *= random.uniform(0.0, 1.0)
            continue

        # file.write(f"{iter}\t\t{vecToString(x)}\t\t{fx : 0.4f}\t\t{stepLength : 0.4f} \
        #   \t\t{vecToString(gradxk)}\t\t{func.callsNumber}\t\t{funcGrad.callsNumber}\n")

        file.write(f"{iter}\t{hexVec(x)}\t{fx}\t{stepLength : 8.4f} \
                   \t{(hexVec(gradxk))}\t{func.callsNumber}\t{funcGrad.callsNumber}\n")
            

        xk = x
        fxk = fx
        gradxk = funcGrad(xk)

    # f.write("X_min = ", res)
    # print("min = ", fun(res))
    # print("Трудоемкость по f: ", fun.callsNumber)
    # print("Трудоемкость по grad f: ", grad.callsNumber)

    return xk
