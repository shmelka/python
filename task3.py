class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

pos1 = Position('Иван', 'Иванов', 'Директор', 50000, 30000)
print(f'Полное имя: {pos1.get_full_name()}')
print(f'Доход с учетом премии: {pos1.get_total_income()}')

pos2 = Position('Петров', 'Фёдор', 'Зам.директора', 40000, 20000)
print(f'Полное имя: {pos2.get_full_name()}')
print(f'Доход с учетом премии: {pos2.get_total_income()}')