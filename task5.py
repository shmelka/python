from random import randint

items = [randint(0, 10) for _ in range(5)]
with open('task5_file.txt', 'w', encoding='UTF-8') as f:
    f.write(' '.join(map(str, items)))
print(f'Числа: {items}')
print(f'Сумма чисел: {sum(items)}')