from random import randint

source_list = [randint(0, 1000) for i in range(30)]
print(f'Исходный список: {source_list}')
result_list = [el for index, el in enumerate(source_list) if index > 0 and el > source_list[index - 1]]
print(f'Результат: {result_list}')