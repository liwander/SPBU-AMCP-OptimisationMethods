from collections.abc import Callable
import numpy as np

vector = np.array

def gradDescVariableStep(
        func: Callable[[vector], float],
        funcGrad: Callable[[vector], vector],
        fconstr: Callable[[vector], float],
        stepLength: float = 1,
        initx: vector = np.array([0,0]),
        eps: float = 1e-3,
        # file = None
) -> vector:
    
    xk = initx
    fxk = func(xk)
    gradxk = funcGrad(xk)
    iter = 0
    # coef = lambda iter : 1 / (iter + 1)
    coef = 1 / 2

    # file.write("Метод градиентного спуска с переменынм шагом\n")
    # file.write(
    #     "It\tX\t\t\t\t\t\t\t\t\t\t\t\tF(x)\t\tAlpha\t\tgrad F\t\t\t\t\t\t\t\t\tТруд. F\t Труд. grad\n")
   

    while (np.linalg.norm(gradxk) > eps) :
        iter += 1
        x = xk - gradxk * stepLength
        if fconstr(x) >= 0:
            stepLength *= coef
            continue
        fx = func(x)

        # print(iter, x, np.linalg.norm(gradxk))

        if fx - fxk > -stepLength * 1e-3 * (np.linalg.norm(gradxk) ** 2):
            stepLength *= coef
            continue

        # file.write(f"{iter}\t{hexVec(x)}\t{fx}\t{stepLength : 8.4f} \
        #            \t{(hexVec(gradxk))}\t{func.callsNumber}\t{funcGrad.callsNumber}\n")
            
        
        xk = x
        fxk = fx
        gradxk = funcGrad(xk)

    # f.write("X_min = ", res)
    # print("min = ", fun(res))
    # print("Трудоемкость по f: ", fun.callsNumber)
    # print("Трудоемкость по grad f: ", grad.callsNumber)

    print(iter)
    return xk
