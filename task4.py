class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('Car went')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        print(f'Car turned {direction}')

    def show_speed(self):
        print(f'Current speed of the car: {self.speed}')

class TownCar(Car):

    def __init__(self, color, name):
        super().__init__(0, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Current speed of the car: {self.speed}. Attention!!! High speed')
        else:
            super().show_speed()

class SportCar(Car):

    def __init__(self, color, name):
        super().__init__(0, color, name, False)

class WorkCar(Car):

    def __init__(self, color, name):
        super().__init__(0, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Current speed of the car: {self.speed}. Attention!!! High speed')
        else:
            super().show_speed()

class PoliceCar(Car):

    def __init__(self, color, name):
        super().__init__(0, color, name, True)

town = TownCar('Green', 'TownCar name')
town.go()
town.speed = 30
town.show_speed()
town.turn('right')
town.speed = 70
town.show_speed()
print(f'Attributes: name - {town.name}, color - {town.color}, speed - {town.speed}, is_police - {town.is_police}')
town.stop()

print('**********************************')

sport = SportCar('Red', 'SportCar name')
sport.go()
sport.speed = 50
sport.show_speed()
sport.turn('left')
sport.speed = 150
sport.show_speed()
print(f'Attributes: name - {sport.name}, color - {sport.color}, speed - {sport.speed}, is_police - {sport.is_police}')
sport.stop()

print('**********************************')

work = WorkCar('Yellow', 'WorkCar name')
work.go()
work.speed = 20
work.show_speed()
work.turn('left')
work.speed = 50
work.show_speed()
print(f'Attributes: name - {work.name}, color - {work.color}, speed - {work.speed}, is_police - {work.is_police}')
work.stop()

print('**********************************')

police = PoliceCar('Blue', 'PoliceCar name')
police.go()
police.speed = 40
police.show_speed()
police.turn('right')
police.speed = 80
police.show_speed()
print(f'Attributes: name - {police.name}, color - {police.color}, speed - {police.speed}, is_police - {police.is_police}')
police.stop()