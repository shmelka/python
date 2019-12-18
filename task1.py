with open('task1_file.txt', 'w', encoding='UTF-8') as f:
    while True:
        print('Введите данные. Для окончания ввода нажмите Enter')
        line = input()
        if line:
            f.write(line + '\n')
        else:
            break