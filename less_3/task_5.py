def my_sum():
    total_sum = 0
    param = 0
    while param == 0:
        str_num = input('Введите числа через пробел или q для выхода: ').split()
        result = 0
        for i in str_num:
            if str_num.count('q') > 0:
                param = 1
                break
            result += int(i)
        total_sum += result
        print(total_sum)
    return total_sum


print(my_sum())
