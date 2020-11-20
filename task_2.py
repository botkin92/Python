time_inp = int(input('Введите время в секундах: '))
time_h = time_inp // 3600
time_m = (time_inp // 60) - (time_h * 60)
time_s = time_inp - (time_h * 3600) - (time_m * 60)

print(f'{time_h}:{time_m}:{time_s}')
