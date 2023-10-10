from common import *

def main():

    coefs = getCoefs('.config.json')
    scalarFunction = constructLossScalarFunction(coefs)
    scalarFunction = lambda x : 2 * x
    vecFunction = constructLossVecFunction(coefs)
    vecFunction = lambda x: (x[0] - 1) ** 2 + (x[1] - 1) ** 2

    lb, rb = tuple([-5] * 2), tuple([5] * 2)
    print(lb, rb)
    print(vectorTriadMethod(vecFunction, lb, rb))


if __name__ == '__main__':
    main()