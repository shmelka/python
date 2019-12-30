class ComplecsNumber:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number

a = ComplecsNumber(complex(5j + 9))
b = ComplecsNumber(complex(6j - 5))
print(f'Сумма: {a + b}')
print(f'Произведение: {a * b}')
