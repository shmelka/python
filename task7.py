import json

with open('task7_file.txt', 'r', encoding='UTF-8') as f:
    firms = {}
    for line in f:
        attr = line.replace('\n', '').split(' ')
        firms[attr[0]] = int(attr[2]) - int(attr[3])
    profits = [int(el[1]) for el in firms.items() if el[1] > 0]
    list = [firms, {'average_profit': sum(profits) / len(profits)}]
with open('task7_file.json', 'w', encoding='UTF-8') as jf:
    json.dump(list, jf)