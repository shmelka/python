from itertools import cycle
from random import randint

source_list = [randint(0, 10) for i in range(5)]
print(f'Исходный список: {source_list}')
i = 0
for el in cycle(source_list):
    print(el, end=' ')
    if i > 50:
        break
    i += 1