import math


def fact(n):
    res = []
    n = int(n)
    for i in range(1, n+1):
        res.append(math.factorial(i))
    yield res


for el in fact(4):
    print(el)
