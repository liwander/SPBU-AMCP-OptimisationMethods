def sumVec(
            *vectors: tuple[tuple[float]]) -> tuple[float]:
    '''
    calculates vector which components are sums of corresponding input vectors components
    '''
    if len(vectors) < 2:
        raise TypeError("Lack of vectors to sum")
    
    for j in range(1, len(vectors)):
        if vectors[j] != vectors[j-1]:
            raise TypeError("Different lengths of input vectors")

    res = []
    for i in range(len(vectors[0])):
        comp = 0
        for j in range(len(vectors)):
            comp += vectors[j][i]
        res.append(comp)

    return res


def scalVecProduct(
                scalar : float,
                vec : tuple[float]) -> tuple[float]:
    '''
    Calculates product of scalar and vector
    '''
    return [scalar * vecComponent for vecComponent in vec]

def vecProduct(vec1 : tuple[float],
               vec2 : tuple[float]) -> tuple[float]:
    '''
    Calcluates vector product
    '''
    s = 0
    for i in range(len(vec1)):
        s += vec1[i] * vec2[i]
    return s


def vecNorm(
            vec: tuple[float]) -> tuple[float]:
    '''
    Calculates norm of vector
    '''
    return vecProduct(vec, vec)