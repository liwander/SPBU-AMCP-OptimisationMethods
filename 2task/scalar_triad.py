from dataclasses import dataclass

# 1. x = x0 + h
# 2. if f(x) > f(x0) -> h = -h -> (1)
# 3. 

# memcache all forward needed info - fixed
# crossing out boundaries 

@dataclass
class ArgValPair:
    arg: float
    funcVal: float

def isInBoundaries(x, a, b):
    if abs(b - x) + abs(a - x) == b - a :
        return True
    return False

def scalarTriadMethod(f, a, b, eps=1e-6):
    x = (a + b) / 2
    h = (b - a) / 2
    current = ArgValPair(x, f(x))

    while abs(h) > eps:
        if not(isInBoundaries(current.arg + h, a, b)):
            h = -h/2
        forward = ArgValPair(current.arg + h, f(current.arg + h))
        if forward.funcVal > current.funcVal:
            h = -h

            if not(isInBoundaries(current.arg + h, a, b)):
                h = -h/2
            backward = ArgValPair(current.arg + h, f(current.arg + h))
            if backward.funcVal > current.funcVal:
                h /=  -2
            else:
                current = backward
        else:
            current = forward
        print(current.arg)

    return current.arg