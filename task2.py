class DivByZero(Exception):

    def __init__(self, txt):
        self.txt = txt

try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise DivByZero('Деление на ноль')
except DivByZero as e:
    print(e)
except ValueError:
    print('Не корректный ввод данных')
else:
    result = a / b
    print(f'Результат деления {a} на {b} равен {result}')