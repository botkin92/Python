from functools import reduce
my_list = [i for i in range(100, 1001, 2)]


def my_f(num1, num2):
    return num1 * num2


print(my_list)
print(reduce(my_f, my_list))
