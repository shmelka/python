products = []
print('Для добавления товара введите "+". Для выхода введите "exit"')
while True:
    command = input('Введите команду: ')
    if command == '+':
        print('Добавляем товар')
        i = len(products) + 1
        name = input('Название: ')
        price = None
        while price is None:
            try:
                price = int(input('Цена: '))
            except ValueError:
                print('Введите число')
        quantity = None
        while quantity is None:
            try:
                quantity = int(input('Количество: '))
            except ValueError:
                print('Введите число')
        unit = input('Ед. измерения: ')
        products.append((i, {"название": name, "цена": price, "количество": quantity, "ед": unit}))
    elif command == 'exit':
        break
analytics = {"название": [], "цена": [], "количество": [], "ед": []}
print('\nСписок товаров: ')
for product in products:
    print(product)
    for key, value in product[1].items():
        analytics[key].append(value)

for key, value in analytics.items():
    analytics[key] = list(set(analytics[key]))

print('\nАналитика: ')
for key, items in analytics.items():
    print(key + ':', items)