import json
from  functools import reduce

personalData = {}
with open('./config.json', 'r') as f:
    personalData = json.load(f)

coefs = [   len(personalData['name']),
            len(personalData['surname']),
            len(personalData['patronymic'])]

def constructLossFunction(coefs):
    def lossFunction(vecX):
        print(coefs)
        if len(vecX) != 4:
            raise TypeError('argument vector must contain 4 items')
        quadraticPart = reduce(lambda x, y : x + y, [coefs[i] * (vecX[i] ** 2) for i in range(len(vecX) -1)]) \
                        + (coefs[0] + coefs[2]) * (vecX[3] ** 2)
        linearPart = reduce(lambda x, y : x + y, [coefs[i] * vecX[i] for i in range(len(vecX) - 1)]) \
                        + (coefs[0] + coefs[2])
        return quadraticPart + linearPart
    return lossFunction
