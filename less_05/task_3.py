from statistics import mean

with open("text_task3.txt") as txt_f:
    lines = txt_f.readlines()

my_dict = {}
for line in lines:
    read_str = line.split()
    my_dict.update({read_str[0]: float(read_str[1])})

print('Сотрудники с окладом менее 20000: ')
for key in my_dict:
    if my_dict[key] < 20000:
        print(key)

print('\nСредний доход сотрудников: ', mean(my_dict[key] for key in my_dict))
