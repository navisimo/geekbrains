from statistics import mean
import json

average_profit = []
firms_data = {}
data = []
try:
    for line in open("task_7.txt", encoding='utf-8'):
        name, ownership, revenue, costs = line.split('   ')
        profit = int(revenue) - int(costs)
        firms_data[name] = profit
        if profit >= 0:
            average_profit.append(profit)
except IOError:
    print("Файла не существует!")


data.append(firms_data)
data.append({'average_profit': mean(average_profit)})

with open("my_file.json", "w") as write_f:
    json.dump(data, write_f)
