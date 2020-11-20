a = int(input('Введите число: '))
b = list(str(a))
iter_a = 0
max_a = b[0]

while (iter_a + 1) < len(b):
    if int(max_a) < int(b[iter_a + 1]):
        max_a = b[iter_a + 1]
    iter_a += 1
print('Наибольшая цифра: ', max_a)
