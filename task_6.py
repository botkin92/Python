a = int(input('Текущий результат, км: '))
b = int(input('Целевой результат, км: '))
n = 1

if b < a:
    print('Ошибка')
else:
    while a < b:
        a = a * 1.1
        n += 1
    print('Требуется дней: ', n)
