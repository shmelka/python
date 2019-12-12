def my_func(x, y):
    """
    Возведение числа в степень без оператора *
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: число с плавающей точкой
    """
    if y == 0:
        return 1
    elif y == 1:
        return x
    result = x
    for _ in range(1, my_func(x, abs(y) - 1)):
        result += x
    return result if y > 0 else 1. / result

def my_func2(x, y):
    """
    Возведение в степень числа с помощью оператора *
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: число с плавающей точкой
    """
    if y == 0:
        return 1
    elif y == 1:
        return x
    result = x
    for _ in range(0, abs(y) - 1):
        result *= x
    return result if y > 0 else 1. / result

while True:
    try:
        num1 = int(input('Введите целое положительно число: '))
    except ValueError:
        print('Ошибка ввода')
        continue
    if num1 > 0:
        break

while True:
    try:
        num2 = int(input('Введите целое отрицательное число: '))
    except ValueError:
        print('Ошибка ввода')
        continue
    if num2 < 0:
        break

print(f'Число {num1} в степени {num2} равно: {my_func(num1, num2)}')
print(f'Число {num1} в степени {num2} равно: {my_func2(num1, num2)}')

print(pow(num1, num2))