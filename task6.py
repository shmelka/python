def int_func(text):
    return text.title()

print(' '.join(list(map(int_func, input('Введите предложение: ').split(' ')))))
