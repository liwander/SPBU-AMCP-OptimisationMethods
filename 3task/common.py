from functools import lru_cache
import numpy as np

vector = np.array

def call_counted(function):
    '''
    Decorator for counting function calls 
    '''
    def func_wrapper(*args, **kvargs):
        func_wrapper.callsNumber += 1
        return function(*args, **kvargs)
    
    func_wrapper.callsNumber = 0
    return func_wrapper

personalData = {'Name' : 'Anver',
                'Surname' : 'Gadzhiev',
                'Patronymic' : 'Pulatovich'}

roflCoefTransformer = lambda c : 10**-len(str(c)) * c

objectFunctionCoefficents = np.array(
                             [roflCoefTransformer(len(personalData['Name'])),
                              len(personalData['Surname']),
                              roflCoefTransformer(len(personalData['Patronymic']))])

constraintFunctionCoefficent = roflCoefTransformer(
    len(personalData['Name']) + \
    len(personalData['Surname']) - \
    len(personalData['Patronymic']) 
)

cfs = objectFunctionCoefficents
cf = constraintFunctionCoefficent

@call_counted
def objectFunction(x : vector) -> float:
    return  np.cosh(cfs[0] * x[0]) + np.cosh(cfs[2] * x[1]) + x[0] + cfs[1] * x[1] 
    
@call_counted
def objectFunctionGradient(x : vector) -> float:
    return  np.array([cfs[0] * np.sinh(cfs[0] * x[0]) + 1,
            cfs[2] * np.sinh(cfs[2] * x[1]) + cfs[1]])

@call_counted
# @lru_cache(maxsize=1)
def constraintFunction(x : vector) -> float:
    return x[0] - cf * x[1]

constraintFunctionSlope = np.array([cf, 1])