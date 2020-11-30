import itertools
print('Итератор, генерирующий целые числа')
start_num = int(input('Enter number "from": '))
iter_list = []
for el in itertools.count(start=start_num, step=1):
    print(el)
    if el > start_num + 5:
        break

print('\nИтератор, повторяющий элементы списка')
my_list = [300, 2, 12, 78, 123]
stop_iter = 0
for num in itertools.cycle(my_list):
    if stop_iter > 12:
        break
    print(num)
    stop_iter += 1
