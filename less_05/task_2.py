with open("text_task2.txt") as txt_f:
    lines = txt_f.readlines()
i = 0
for line in lines:
    i += 1
    print('В строке: {}, символов: {}'.format(i, len(line) - 1))
print('Всего строк: ', i)
