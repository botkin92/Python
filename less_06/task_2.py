class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, density, depth):
        mass = self._length * self._width * (density / 1000) * (depth / 100)
        return mass

obj = Road(5000, 20)
print(obj.weight(25, 5), 'tons')
