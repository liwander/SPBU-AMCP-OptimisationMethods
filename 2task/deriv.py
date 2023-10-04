import math
from collections.abc import Callable

def machineEpsilon() -> float:
    '''
    Caculates machine epsilon
    '''
    eps : float = float(1)
    prevEps : float = eps
    while (float(1) + 0.5 * eps) != float(1):
        prevEps = eps
        eps *= 0.5

    return prevEps

machineEpsilon = machineEpsilon()

def deriv(
        func : Callable[[float], float],
        point : float
        ) -> float:
    '''
    Calculates derivative for single argument function
    '''
    h : float = 1e-6
    if (point != 0):
        h = point * math.sqrt(machineEpsilon)
    
    derivVal : float = (func(point + h) - func(point - h)) / (2 * h)
    return derivVal


def makeOneArgFunc(
        func : Callable[[tuple[float]], float],
        vPoint : tuple[float],
        volatileArgPos : int
        ) -> Callable[[float], float]:
    '''
    Fixate funciton positional arguments at possition except volatileArgPos
    '''

    return lambda x : func([vPoint[i] if i != volatileArgPos else x for i in range(len(vPoint))])


def funcGrad(  
        func : Callable[[tuple[float]], float]) -> Callable[[tuple[float]], tuple[float]]:
    '''
    Construct function gradient vector function
    '''

    def grad(
            vPoint : tuple[float]) -> tuple[float]:
        
        gr = []
        for i in range(len(vPoint)):
            gr.append(deriv(makeOneArgFunc(func, vPoint,volatileArgPos=i), point=vPoint[i]))
        return gr

    return grad