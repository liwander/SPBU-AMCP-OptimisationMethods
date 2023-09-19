from  functools import reduce
import math as m
import json

def counted(function):

    def func_wrapper(*args, **kvargs):
        func_wrapper.callsNumber += 1
        return function(*args, **kvargs)
    
    func_wrapper.callsNumber = 0
    return func_wrapper

personalData = {}
with open('./config.json', 'r') as f:
    personalData = json.load(f)

coefs = [   len(personalData['name']),
            len(personalData['surname']),
            len(personalData['patronymic'])]

def constructLossVecFunction(coefs):
    @counted
    def lossFunction(vecX):
        if len(vecX) != 4:
            raise TypeError('argument vector must contain 4 items')
        quadraticPart = reduce(lambda x, y : x + y, [coefs[i] * (vecX[i] ** 2) for i in range(len(vecX) -1)]) \
                        + (coefs[0] + coefs[2]) * (vecX[3] ** 2)
        linearPart = reduce(lambda x, y : x + y, [coefs[i] * vecX[i] for i in range(len(vecX) - 1)]) \
                        + (coefs[0] + coefs[2])
        return quadraticPart + linearPart
    return lossFunction

def constructLossVecFunction(coefs):
    
    @counted
    def lossFunction(x):
        return reduce(lambda x, y : x + y, [m.e ** ((coefs[i] * 1e-1) * x) for i in range(len(coefs))]) \
                                            - (sum(coefs)) * m.sin(x)
    return lossFunction