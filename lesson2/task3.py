season = {(12, 1, 2): 'Зима', (3, 4, 5): 'Весна', (6, 7, 8): 'Лето', (9, 10, 11): 'Осень'}
season_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
while True:
    try:
        month = int(input('Введите номер месяца: '))
    except ValueError:
        month = None
    if month in range(1, 13):
        # Решение через dict
        for months, name in season.items():
            if month in months:
                print(f'(dict) Месяц относится к времени года: {name}')
                break
        # Решение через list
        for i, months in enumerate(season_list):
            if month in months:
                print(f'(list) Месяц относится к времени года: {seasons[i]}')
                break
        break
    else:
        print('Укажите целое число от 1 до 12')