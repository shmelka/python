def devision_func(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Деление на ноль'

def input_num(input_text):
    while True:
        try:
            return int(input(input_text))
            break
        except ValueError:
            print('Введите число')

num1 = input_num('Введите первое число: ')
num2 = input_num('Введите второе число: ')
result = devision_func(num1, num2)
print(f'Результат деления: {result}')