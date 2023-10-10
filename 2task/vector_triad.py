from dataclasses import dataclass
from collections.abc import Callable


@dataclass
class ArgValPair:
    args: tuple[float]
    funcVal: float


def isInBorders(
        x: tuple[float],
        lBorder: tuple[float],
        rBorder: tuple[float]
) -> bool:

    pointToBordersDistance = sum(
        [abs(rBorder[i] - x[i]) + abs(lBorder[i] - x[i]) for i in range(len(x))])
    bordersDistance = sum([abs(rBorder[i] - lBorder[i])
                          for i in range(len(rBorder))])
    if pointToBordersDistance == bordersDistance:
        return True
    return False


def getPointNear(
        cur: tuple[float],
        argIncrement: float,
        argNumber: int
) -> tuple[int]:

    newArgs = list(cur)
    newArgs[argNumber] += argIncrement
    return tuple(newArgs)


def getArgValPairNear(
        function: Callable[[tuple[float]], float],
        cur: ArgValPair,
        argIncrement: float,
        argNumber: int
) -> ArgValPair:

    newArgs = getPointNear(cur.args, argIncrement, argNumber)
    return ArgValPair(newArgs, function(newArgs))


def vectorTriadMethod(
        f: Callable[[tuple[float]], float],
        a: tuple[float],
        b: tuple[float],
        eps: float = 1e-6
) -> tuple[float]:

    h = [((b[i] - a[i]) / 2) for i in range(len(a))]
    # h = list(b)
    x = tuple((a[i] + b[i]) / 2 for i in range(len(a)))

    # print(x)
    current = ArgValPair(x, f(x))

    while max(list(map(abs, h))) > eps:
        for i in range(len(x)):

            if not (isInBorders(getPointNear(current.args, h[i], i), a, b)):
                h[i] = h[i] / (-2)
                break

            forward = getArgValPairNear(f, current, h[i], i)
            if forward.funcVal > current.funcVal:
                h[i] = -h[i]

                if not (isInBorders(getPointNear(current.args, h[i], i), a, b)):
                    h[i] = h[i] / (-2)
                    break

                backward = getArgValPairNear(f, current, h[i], i)

                if backward.funcVal > current.funcVal:
                    h[i] /= -2
                    break
                else:
                    current = backward
            else:
                current = forward

    print(h)
    return current.args