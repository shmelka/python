list = [512, 'Hello world', ['1', '2', '3'], True, (1, 2, 3), {2, 3, 4}]
for el in list:
    print(type(el))
    if type(el) == int:
        print('Тип элемента integer')
    elif type(el) == str:
        print('Тип элемента string')
    elif type(el) == bool:
        print('Тип элемента boolean')
    elif type(el) == tuple:
        print('Тип элемента tuple')
    elif type(el) == dict:
        print('Тип элемента dict')
    else:
        print('Тип элемента не определён')
