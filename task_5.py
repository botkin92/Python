proceeds = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))

if proceeds > costs:
    print('Период прибыльный')
    profitability = (proceeds - costs) / proceeds
    print('Рентабельность: ', profitability)
else:
    print('Период убыточный')

total_employees = int(input('Введите численность сотрудников: '))
profit_per = (proceeds - costs) / total_employees
print('Прибыль на сотрудника: ', profit_per)
