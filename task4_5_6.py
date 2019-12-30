class Warehouse:
    """
        Склад
        address - адрес склада
    """
    def __init__(self, address):
        self.address = address
        self.technics = {}
        self.units = {}

    def __str__(self):
        result = ['\nОстатки на складе:']
        for type in self.technics.keys():
            result.append(f'  {self.technics[type][0].__class__.name()} - {len(self.technics[type])}')
        result.append('Техника в подразделениях:')
        for unit in self.units.keys():
            result.append(f'{unit}:')
            for item in self.units[unit]:
                result.append(f'  {globals()[item].name()} - {self.units[unit][item]}')

        return '\n'.join(result)

    """
        Приём техники на склад
        item - объект техники
        count - количество
    """
    def addTechnic(self, *items):
        print('Принимаем технику на склад')
        for item in items:
            if item.__class__.__name__ in self.technics.keys():
                self.technics[item.__class__.__name__].append(item)
            else:
                self.technics[item.__class__.__name__] = [item]

    """
        Передача определённой техники в подразделение
        class_name - наименование класса техники
        count - количество передаваемой техники
        unit - наименование подразделения
    """
    def transfer(self, class_name, count, unit):
        try:
            if type(count) != int:
                raise ValueError('Количество должно быть числом')
            if class_name not in globals().keys():
                raise ValueError('Вы ввели не существующий тип техники')
            print(f'Передаём технику в подразделение - {unit}')
            print(f'Наименование техники: {globals()[class_name].name()}. Количество: {count}')
            if len(self.technics[class_name]) >= count:
                if unit not in self.units.keys():
                    self.units[unit] = {}
                if class_name in self.units[unit].keys():
                    self.units[unit][class_name] += count
                else:
                    self.units[unit].update({class_name: count})
                for i in range(0, count):
                    self.technics[class_name].pop()
            else:
                raise ValueError('Не достаточно техники на складе для передачи в подразделение')
        except ValueError as e:
            print(e)

class Technic:
    """
        Оргтехника
        invent_number - Инвентаризационный номер
        name - Наименование
    """
    def __init__(self, invent_number, name):
        self.invent_number = invent_number
        self.name = name

    def __str__(self):
        return f'{self.invent_number} - {self.name}'

class Printer(Technic):
    """
        Принтер
        type - тип принтера(струйный, лазерный)
    """
    def __init__(self, invent_number, name, type):
        self.type = type
        super().__init__(invent_number, name)

    @classmethod
    def name(cls):
        return 'Принтеры'

class Scanner(Technic):
    """
        Сканер
        color_depth - глубина цвета
    """
    def __init__(self, invent_number, name, color_depth):
        self.color_depth = color_depth
        super().__init__(invent_number, name)

    @classmethod
    def name(cls):
        return 'Сканеры'

class Copier(Technic):
    """
        Ксерокс
        speed - скорость копирования лист/мин
    """
    def __init__(self, invent_number, name, speed):
        self.speed = speed
        super().__init__(invent_number, name)

    @classmethod
    def name(cls):
        return 'Ксероксы'

warehouse = Warehouse('г.Москва, ул.Ленина, д.1')

printer_1 = Printer(1, 'Принтер 1', 'Лазерный')
printer_2 = Printer(2, 'Принтер 2', 'Струйный')
printer_3 = Printer(3, 'Принтер 3', 'Лазерный')

scanner_1 = Scanner(10, 'Сканер 1', '24бит')
scanner_2 = Scanner(11, 'Сканер 2', '32бит')
copier_1 = Copier(20, 'Ксерокс 1', 100)
copier_2 = Copier(21, 'Ксерокс 2', 150)
copier_3 = Copier(22, 'Ксерокс 3', 180)
copier_4 = Copier(23, 'Ксерокс 4', 200)

warehouse.addTechnic(printer_1, printer_2, printer_3, scanner_1, scanner_2, copier_1, copier_2, copier_3, copier_4)
print(warehouse)
warehouse.transfer('Printer', 2, 'Бухгалтерия')
print(warehouse)
warehouse.transfer('Scanner', 1, 'Бухгалтерия')
print(warehouse)
warehouse.transfer('Copier', 1, 'Бухгалтерия')
print(warehouse)
warehouse.transfer('Copier', 2, 'ИТ')
print(warehouse)
warehouse.transfer('Printer', 5, 'ИТ')
print(warehouse)