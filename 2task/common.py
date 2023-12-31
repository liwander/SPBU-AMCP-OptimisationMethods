from  functools import reduce, lru_cache
from collections.abc import Callable
import math as m
import json

def counted(function):
    '''
    Decorator for counting function calls 
    '''
    def func_wrapper(*args, **kvargs):
        func_wrapper.callsNumber += 1
        return function(*args, **kvargs)
    
    func_wrapper.callsNumber = 0
    return func_wrapper

def vecLossFunction(
        coefs: tuple[float]
        ) -> Callable[[tuple[float]],float]:
    """
    Constructs a loss vector function with substituted coefficents
    """
    @counted
    def lossFunction(vecX : tuple[float]):
        if len(vecX) != 4:
            raise TypeError('argument vector must contain 4 items')
        quadraticPart = reduce(lambda x, y : x + y, [coefs[i] * (vecX[i] ** 2) for i in range(len(vecX) -1)]) \
                        + (coefs[0] + coefs[2]) * (vecX[3] ** 2)
        linearPart = reduce(lambda x, y : x + y, [coefs[i] * vecX[i] for i in range(len(vecX) - 1)]) \
                        + (coefs[0] + coefs[2] + coefs[1]) * vecX[3]
        return quadraticPart + linearPart
    
    return lossFunction

def scalarLossFunction(
        coefs: tuple[float]
        ) -> Callable[[tuple[float]],float]:
    ''' Constructs a loss scalar function with substituted coefficents '''
    @counted
    def lossFunction(x):
        return reduce(lambda x, y : x + y, [m.e ** ((coefs[i] * 1e-1) * x) for i in range(len(coefs))]) \
                                            - (sum(coefs)) * m.sin(x)
    
    return lossFunction

def funcGrad(
        coefs: tuple[float]
        ) -> Callable[[tuple[float]],tuple[float]]:
    """
    Constructs loss function gradient with substituted coefficents
    """
    @counted
    # @lru_cache(maxsize=2, typed=False)
    def lossFunctionGrad(
        vecX : tuple[float]
    ) -> tuple[float]:
        if len(vecX) != 4:
            raise TypeError('argument vector must contain 4 items')
        
        grad = [None] * 4
        for i in range(3):
            grad[i] = coefs[i] * (2 * vecX[i] + 1)
        grad[3] = (coefs[0] + coefs[2]) * (2 * vecX[3] + 1) + coefs[1]
        
        return tuple(grad)
    
    return lossFunctionGrad

def secDerivVec(
        coefs: tuple[float]
        ) -> tuple[float]:
    """
    Calculates loss function second derivative vector with substituted coefficents
    """
    # @counted
    # def secDerVec(vecX : tuple[float]):
    #     if len(vecX) != 4:
    #         raise TypeError('argument vector must contain 4 items')
        
    secDer = [None] * 4
    for i in range(3):
        secDer[i] = coefs[i] * 2
    secDer[3] = (coefs[0] + coefs[2]) * 2
    
    return secDer
    
    # return secDerVec
    

def getCoefs(
        pathToJson: str
        ) -> tuple[float]:
    
    personalData = {}
    with open(pathToJson, 'r') as f:
        personalData = json.load(f)
    
    coefs = (len(personalData['name']),
             len(personalData['surname']),
             len(personalData['patronymic']))
    return coefs

def hex(
        f: float,
        n=4
) -> str:
    
    h = float.hex(float(f))
    a, B = h.split(".")
    B = B.split("p")
    end = ""
    if len(B) > 1:
        end = "p" + B[1]
    B[0] += "00000"
    return a + "." + B[0][:n] + end