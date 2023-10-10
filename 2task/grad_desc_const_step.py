from vec_op import *
from common import *
from collections.abc import Callable

def gradDescConstStep(
        funcGrad : Callable[[tuple[float]], tuple[float]],
        secDer : tuple[float],
        initX : tuple[float],
        stepLength : float,
        eps : float =1e-6
        ) -> float: 
    
    '''
    Calculate minimum of multiple variable function using gradient descent method with constant step 
    '''

    X = initX
    grad = funcGrad(X)

    while(max([abs(grad[i]/secDer[i]) for i in range(4)]) > eps):
        X = vecSum(X, vecMultByScalar(grad, -stepLength))
        grad = funcGrad(X)
        
    return X