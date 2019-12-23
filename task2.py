class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        return f'Для покрытия всего дорожного полотна необходимо: {self._length * self._width * 25 * 5 / 1000} тонн асфальта'

rd = Road(5000, 10)
print(rd.weight())