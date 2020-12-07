with open("text_task5.txt", 'w') as txt_f:
    lines = input('enter numbers separated by a space: ')
    txt_f.write(lines)
    numbers = map(float, lines.split())
    sum_num = sum(numbers)

print('sum of numbers: ', sum_num)
