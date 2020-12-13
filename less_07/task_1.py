class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        mtr = ''
        for row in self.matrix:
            for elem in row:
                mtr += str(elem) + ' '
            mtr += '\n'
        return mtr

    def __add__(self, other):
        mtr = self.matrix
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if len(self.matrix[i]) == len(other.matrix[i]):
                        mtr[i][j] = self.matrix[i][j] + other.matrix[i][j]
                    else:
                        return f'Размеры матрицы должны бать одинаковыми'
        else:
            return f'Размеры матрицы должны бать одинаковыми'
        return '\n'.join(str(' '.join(str(elem) for elem in row)) for row in mtr)


obj_1 = Matrix([[2, 3, 4], [23, 1, 1], [0, 0, 0]])
obj_2 = Matrix([[3, 3, 3], [2, 2, 2], [1, 1, 1]])
obj_3 = Matrix([[1, 2], [3, 4]])

print(obj_1)
print(obj_2)

print(obj_1 + obj_2)
# print(obj_1 + obj_3)
