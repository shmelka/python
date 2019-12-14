from sys import argv

script_name, output, rate, priz = argv
try:
    print(f'Выработка: {output}, ставка: {rate}, премия: {priz}. Итого зарплата: {((float(output) * float(rate)) + float(priz))}')
except ValueError:
    print('Принимаются только числовые значения')