class NumberListException(Exception):

    def __init__(self, my_list):
        self.my_list = my_list

    @classmethod
    def validate(cls, item):
        return item.isnumeric()

mylist = []
while True:
    el = input('Введите число. Для выхода введите "q": ')
    if el.lower() == 'q':
        break
    try:
        if NumberListException.validate(el):
            mylist.append(el)
        else:
            raise NumberListException('Вы ввели не число')
    except NumberListException as e:
        print(e)
    else:
        print(f'Список: {mylist}')