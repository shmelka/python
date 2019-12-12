result = 0
while True:
    list = input('Введите числа разделённые пробелом или "q" для выхода: ').lower().split(' ')
    result += sum([int(i) for i in list if i.isdigit()])
    print(f'Итоговая сумма: {result}')
    if 'q' in list:
        break