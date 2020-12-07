with open('text_task6.txt', encoding='utf-8') as txt_f:
    lines = txt_f.readlines()

my_dict = {}
for line in lines:
    splitted_line = line.split()
    key = splitted_line[0]
    sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line if '(' in x])
    my_dict.update({key: sum_lessons})

print(my_dict)
