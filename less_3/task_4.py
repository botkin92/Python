def power_v1(x, y):
    result = float(x) ** int(y)
    return result


def power_v2(x, y):
    i = 0
    mult_x = 1
    while True:
        i += 1
        mult_x *= float(x)
        result = 1 / mult_x
        if i == abs(int(y)):
            break
    return result


print('Вариант_1')
print(power_v1(input('Введите действительное положительное число: '), (input('Введите целое отрицательное число: '))))
print('Вариант_2')
print(power_v2(input('Введите действительное положительное число: '), (input('Введите целое отрицательное число: '))))
