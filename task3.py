with open('task3_file.txt', 'r', encoding='UTF-8') as f:
    persons = list(map(lambda line: tuple(line.replace('\n', '').split(' ')), f.readlines()))
print(persons)
print(f'Сотрудники с окладом менее 20 000: {[person[0] for person in persons if int(person[1]) < 20000]}')
print(f'Средний доход: {sum([int(person[1]) for person in persons])/len(persons)}')
