number_1 = float(input('Введите делимое: '))
number_2 = float(input('Введите делитель: '))


def func_division(param_1, param_2):
    try:
        param_1 / param_2
    except ZeroDivisionError:
        return print('Деление на 0 невозможно')
    return param_1 / param_2


print(round(func_division(number_1, number_2), 2))
