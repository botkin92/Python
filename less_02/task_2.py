my_list = input('Введите элементы списка через пробел: ').split()
new_list = []

for i in range(len(my_list)):
    if (i + 1) % 2 == 0:
        new_list.append(my_list[i-1])
    else:
        try:
            new_list.append(my_list[i+1])
        except IndexError:
            new_list.append(my_list[i])
print(new_list)
