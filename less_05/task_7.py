import json

with open("text_task7.txt", encoding='utf-8') as txt_f:
    lines = txt_f.readlines()

firm_dict = {}
sum_profit = 0
n = 0
for line in lines:
    param = line.split()
    profit = float(param[2]) - float(param[3])
    firm_dict.update({param[0]: profit})
    if profit > 0:
        n += 1
        sum_profit += profit
average_profit = sum_profit / n
out_file =[firm_dict, {'average_profit': average_profit}]

print(out_file)

with open("text_task7.json", 'w', encoding='utf-8') as txt_f:
    json.dump(out_file, txt_f)
