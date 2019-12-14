from random import randint

source_list = [randint(0, 10) for i in range(20)]
print(f'Исходный список: {source_list}')
result = [el for el in source_list if source_list.count(el) == 1]
print(f'В списке не повторяются числа: {result}')