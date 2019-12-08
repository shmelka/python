my_list = [7, 5, 3, 3, 2]
print('Введите натуральное число или "exit" для выхода')
print(f'Исходный рейтинг: {my_list}')
while True:
    number = input('Новый элемент: ')
    if number == 'exit':
        break
    else:
        try:
            number = int(number)
        except ValueError:
            number = None
            print('Ошибка ввода')
    if number:
        index = 0
        for i, el in enumerate(my_list):
            if el >= number:
                index = i + 1
        my_list.insert(index, number)
        print(my_list)