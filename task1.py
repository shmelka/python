class Date:

    def __init__(self, text_date):
        if len(text_date.split('-')) != 3:
            raise ValueError('Не верный формат даты')
        self.text_date = text_date
        self.day, self.month, self.year = self.toInt(text_date)
        self.validate(self.day, self.month, self.year)

    def __str__(self):
        return f'День - {dt.day}, месяц - {dt.month}, год - {dt.year}'

    @classmethod
    def toInt(cls, text_date):
        return list(map(int, text_date.split('-')))

    @staticmethod
    def validate(day, month, year):
        if day not in range(1, 32):
            raise ValueError('День указан не корректно')
        if month not in range(1, 13):
            raise ValueError('Месяц указан не корректно')
        if year not in range(1970, 2100):
            raise ValueError('Год указан не корректно')


dt = Date('04-12-1988')
print(dt)
print('*' * 30)

print('Пример не корректного ввода дня')
try:
    dt = Date('00-12-1988')
except ValueError as e:
    print(e)