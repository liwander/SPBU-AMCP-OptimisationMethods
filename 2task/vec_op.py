import math
from common import hex

vector = tuple[float]

def vecSum(a: vector, b: vector):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return tuple(c)

def vecMultByScalar(a: vector, c: float):
    d = []
    for i in range(len(a)):
        d.append(a[i] * c)
    return tuple(d)

def dotProduct(a: vector, b: vector):
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s

def vecNorm(x: vector):
    return math.sqrt(dotProduct(x, x))

def vecToString(x: vector):
    s = "["
    for el in x:
        s += f"{el:0.4f}, "
    return s[:len(s)-2] + "]"

def hexVec(x : vector):
    return [hex(y) for y in x]