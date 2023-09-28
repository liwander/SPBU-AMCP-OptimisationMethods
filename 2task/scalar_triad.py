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


def scalarTriadMethod(f, a, b, eps=1e-6):
    x = (a + b) / 2
    h = (b - a) / 2
    current = ArgValPair(x, f(x))
    k = 1

    while abs(h) > eps:
        print(k)
        k += 1
        forward = ArgValPair(current.arg + h, f(current.arg + h))
        if forward.funcVal > current.funcVal:
            h = -h
            backward = ArgValPair(current.arg + h, f(current.arg + h))
            if backward.funcVal > current.funcVal:
                h /=  -2
            else:
                current = backward
        else:
            current = forward
        print(current.arg)

    return current.arg