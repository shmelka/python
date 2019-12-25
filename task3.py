class Cell:

    def __init__(self, cells = 0):
        self.cells = cells

    def __str__(self):
        return f'Клетка с количеством ячеек - {self.cells}'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells) if self.cells > other.cells else 'Количество ячеек первой клетки меньше, чем второй'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, row):
        return '\n'.join(['*' * row for i in range(0, self.cells // row)] + ['*' * (self.cells % row)])


cel_1 = Cell(17)
cel_2 = Cell(3)
print(f'Сумма: {cel_1 + cel_2}')
print(f'Разность: {cel_1 - cel_2}')
print(f'Произведение: {cel_1 * cel_2}')
print(f'Деление: {cel_1 / cel_2}')
print(f'Ячейки по рядам:\n{cel_1.make_order(5)}')