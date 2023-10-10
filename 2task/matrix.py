import math

class Matrix:
    def __new__(
            cls,
            shape: tuple[int],
            buffer: list[list[float]] = None) -> 'Matrix':
        if len(shape) != 2:
            raise TypeError('a matrix has only 2 dimensions')
        
        obj = super().__new__(cls)
        obj.shape = shape
        obj._table = [[None] * shape[1]] * shape[0]

        if buffer is not None:
            if len(buffer) != shape[0] or len(buffer[0]) != shape[1]:
                raise TypeError("buffer does not match the shape")
            
            for i in range(obj.shape[0]):
                obj._table[i] = buffer[i] 

        return obj

    def __add__(self, Matrix2: 'Matrix') -> 'Matrix':

        if self.shape != Matrix2.shape :
            raise TypeError("mismatching matrixes dimensions")
        
        resTable = [[None] * self.shape[1]] * self.shape[0]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                resTable[i][j] = self._table[i][j] + Matrix2._table[i][j]

        return Matrix(self.shape, resTable)
    
    def __mul__(self, other: 'Matrix') -> 'Matrix':

        if isinstance(other, float) or isinstance(other, int):
            return self.__multByScalar(other)

        if self.shape[1] != other.shape[0]:
            raise TypeError("mismatching matrixes dimensions")
        
        resShape = (self.shape[0], other.shape[1])
        resTable = [[None] * resShape[1]] * resShape[0]

        for i in range(resShape[0]):
            for j in range(resShape[1]):
                resTable[i][j] = sum(self[i, w] * other[w, j] for w in range(self.shape[1]))

        return Matrix(resShape, resTable)

    def __rmul__(self, num: float) -> float:
        return self.__multByScalar(num)

    # def __getitem__(self, pos: tuple[int, ...]) -> float:
    #     if len(pos) != 2:
    #         raise TypeError('Unable to determine element position')
    #     return self._table[pos[0]][pos[1]]

    def __getitem__(self, positions: tuple[list[int]]) -> float:
        # if len(pos) != 2:
        #     raise TypeError('Unable to determine element position')
        rows = positions[0]
        cols = positions[1]
        return self._table[*rows][*cols]
    
    def __str__(self) -> str:
        res : list[str]= []
        for i in range(self.shape[0]):
            res.append('  '.join(str(x) for x in self._table[i]))
        return '\n'.join(res)

    def __multByScalar(self,
                    num: float) -> 'Matrix':
        resTable = [[None] * self.shape[1]] * self.shape[0]
        for i in range(len(self._table)):
            for j in range(len(self._table[0])):
                resTable[i][j] = num * self._table[i][j]
        return Matrix(self.shape, resTable)
    

    def transposed(self) -> 'Matrix':
        newShape = (self.shape[1], self.shape[0])        
        newTable = [list(i) for i in zip(*self._table)]
        return Matrix(newShape, newTable)


    def row(self, number: int ) -> 'Matrix':
        rowShape = (1, self.shape[1])
        rowBuffer = [ [ self._table[number][j] for j in range(rowShape[1])] ]
        return Matrix(rowShape, rowBuffer)
    
    def col(self, number: int ) -> 'Matrix':
        colShape = (self.shape[0], 1)
        colBuffer = [ [ self._table[i][number] ] for i in range(colShape[0]) ]
        return Matrix(colShape, colBuffer)
    
    def norm(self) -> float:
        return math.sqrt(sum([math.pow(self._table[i][j], 2) for i in range(self.shape[0]) for j in range(self.shape[1])]))

    def det(self) -> float:
        if self.shape[0] != self.shape[1]:
            raise TypeError('Matrix is not square')
        
        if self.shape[0] == 2:
            return self._table[0][0] * self._table[1][1] - self._table[1][0] * self._table[0][1]

        res = 0.0
        for i in range(self.shape[0]):
            # res += det()
            pass

        pass