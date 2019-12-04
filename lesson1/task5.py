revenue = int(input('Укажите выручку: '))
cost = int(input('Укажите издержки: '))

if revenue > cost:
    print('Фирма прибыльна')
    print(f'Рентабельность: {((revenue - cost) / revenue) * 100:.0f}%')
    persons = int(input('Укажите количество сотрудников: '))
    print(f'Прибыль фирмы в расчёте на одного сотрудника равна: {((revenue - cost) / persons):.2f}')
elif cost > revenue:
    print('Фирма убыточна')