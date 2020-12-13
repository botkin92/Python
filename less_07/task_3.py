class Cell:
    def __init__(self, int_nums):
        self.nums = int(int_nums)

    def __add__(self, other):
        return self.nums + other.nums if self.nums or other.nums > 0 else 'value cannot be negative or zero'

    def __sub__(self, other):
        return self.nums - other.nums if (self.nums - other.nums) > 0 else 'value cannot be negative or zero'

    def __mul__(self, other):
        return self.nums * other.nums if self.nums or other.nums > 0 else 'value cannot be negative or zero'

    def __truediv__(self, other):
        return self.nums // other.nums if self.nums > other.nums else \
            'number in first cell must be greater than in second'

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)


cell_1 = Cell(20)
cell_2 = Cell(10)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_1.make_order(7))
