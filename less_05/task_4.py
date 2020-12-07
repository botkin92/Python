with open("text_task4.txt") as txt_f:
    lines = txt_f.readlines()

transl_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_task4_ru.txt', 'w', encoding='utf-8') as txt_f:
    for line in lines:
        line = line.split(' — ')
        line[0] = transl_dict.get(line[0])
        txt_f.write(line[0] + ' — ' + line[1])
