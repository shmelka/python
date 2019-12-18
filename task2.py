with open('task2_file.txt', 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f, 1):
        print(f'Строка - {i}, слов - {len(line.split(" "))}')