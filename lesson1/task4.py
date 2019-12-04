while True:
    max_number = 0
    digital = int(input('Введите челое положительное число: '))
    while digital > 0:
        i = digital % 10
        if i > max_number:
            max_number = i
        digital = int((digital - i) / 10)
    if max_number:
        print(f'Максимальная цифра: {max_number}')
        break