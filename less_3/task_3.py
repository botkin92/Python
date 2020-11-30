def my_func(arg_1, arg_2, arg_3):
    arg_list = [arg_1, arg_2, arg_3]
    arg_list.remove(min(arg_list))
    arg_sum = sum(arg_list)
    return arg_sum


print(my_func(float(input('Число #1: ')), float(input('Число #2: ')), float(input('Число #3: '))))
