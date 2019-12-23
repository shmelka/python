class Stationery:

    def __init__(self, title):
        self.title = title
        print(f'Создан объект: {self.title}')

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print('Инструмент ручка')

class Pencil(Stationery):

    def draw(self):
        print('Инструмент карандаш')

class Handle(Stationery):

    def draw(self):
        print('Инструмент маркер')

stat = Stationery('Канцелярская принадлежность')
stat.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()