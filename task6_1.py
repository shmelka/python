from itertools import count

def generator(start):
    for el in count(start):
        yield el

start = None
while True:
    if start == None:
        try:
            start = int(input('С какого числа начинаем генерацию? - '))
            list = generator(start)
        except ValueError:
            print('Введите число')
    else:
        key = input('Для генерации нажмите Enter, для выхода любой символ - ')
        if key == '':
            print(f'Сгенерированное число равно: {next(list)}')
        else:
            break