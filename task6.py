def to_int(value):
    value = ''.join([el for el in list(value) if el.isdigit()])
    return int(value) if value.isdigit() else 0

dict = {}
with open('task6_file.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.replace('\n', '').split(' ')
        dict[line[0]] = sum([to_int(el) for el in line[1:]])
    print(dict)