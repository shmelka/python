from functools import reduce


def func(prev_el, el):
    return prev_el * el


source_list = [el for el in range(100, 1001) if el % 2 == 0]
print(source_list)
print(f'Произведение всех элементов: {reduce(func, source_list)}')