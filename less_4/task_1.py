import sys


def calc_wage(salary, rate, prize):
    try:
        salary, rate, prize = float(salary), float(rate), float(prize)
        result = (salary * rate) + prize
    except ValueError:
        print('float check')
    return result


print(calc_wage(sys.argv[1], sys.argv[2], sys.argv[3]))
