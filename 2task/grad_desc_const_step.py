from vec_op import *
from deriv import *
from collections.abc import Callable

def gradDescConstStep(
        func : Callable[[tuple[float]], float],
        initX : tuple[float],
        stepLength : float,
        eps : float =1e-6
        ) -> float: 
    
    '''
    Calculate minimum of multiple variable function using gradient descent method with constant step 
    '''

    X = initX
    grad = funcGrad(func)

    while(vecNorm(func(X)) > eps):
        X = sumVec(X,  scalVecProduct(-stepLength, grad(X)))
        
    return X