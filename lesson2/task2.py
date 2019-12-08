list = []
print('Для добавления элемента в список укажите значение')
print('Для прекращения ввода введите "exit"')
while True:
    item = input('Добавить значение: ')
    if item == 'exit':
        print('Исходный список:')
        print(list)
        break
    else:
        list.append(item)
for i in range(1, len(list), 2):
    tmp = list[i]
    list[i] = list[i - 1]
    list[i - 1] = tmp
print('Итоговый список:')
print(list)