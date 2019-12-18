items = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task4_file_new.txt', 'w', encoding='UTF-8') as fnew:
    with open('task4_file.txt', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            line = line.replace('\n', '').split(' - ')
            fnew.write(f'{items[line[0]]} - {line[1]}\n')