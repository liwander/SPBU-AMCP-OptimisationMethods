from vec_op import *
from common import *
from collections.abc import Callable

def gradDescConstStep(
        func : Callable[[tuple[float]], float],
        funcGrad : Callable[[tuple[float]], tuple[float]],
        secDer : tuple[float],
        initx : tuple[float],
        stepLength : float,
        eps : float =1e-6,
        file = None
        ) -> float: 
    
    '''
    Calculate minimum of multiple variable function using gradient descent method with constant step 
    '''

    x = initx
    grad = funcGrad(x)
    iter = 0

    file.write("Метод градиентного спуска с постоянным шагом\n")
    file.write(
        "Итерация\tТекущая координата\t\tF(x)\t\tТрудоемкость\n")
    file.write(f"Alpha = {stepLength} ({hex(stepLength)})\n")
    file.write("it \t x \t grad(x)\n")

    while(max([abs(grad[i]/secDer[i]) for i in range(4)]) > eps):
        iter += 1
        x = vecSum(x, vecMultByScalar(grad, -stepLength))
        grad = funcGrad(x)
        # file.write(f"{iter}\t\t{vecToString(X)}\t\t{vecToString(grad)}\t\t{funcGrad.callsNumber}\n")
        # file.write(f"{iter}\t{hexVec(x)}\t{grad}\t{func(x)}\n")
        file.write(f"{iter}\t{hexVec(x)}\t{hexVec(grad)}\n")

        # func.callsNumber -= 1

    return x