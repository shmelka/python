from abc import ABC, abstractmethod

# класс одежда
class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption

# класс пальто
class Coat(Clothes):

    @property
    def fabric_consumption(self):
        return self.param / 6.5 + 0.5

# класс костюм
class Suit(Clothes):

    @property
    def fabric_consumption(self):
        return 2 * self.param + 0.3

coat = Coat(13)
print(f'Расход ткани на пальто: {coat.fabric_consumption}')

suit = Suit(4)
print(f'Расход ткани на костюм: {suit.fabric_consumption}')

print(f'Общий расход ткани на пальто и костюм: {coat + suit}')