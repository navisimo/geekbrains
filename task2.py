from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def name(self):
        print("Тип одежды:", end=' ')

    @abstractmethod
    def fabric_consumption(self):
        print("Расход ткани:", end=' ')


class Coat(Clothes):

    @property
    def name(self):
        super().name()
        return 'Пальто.'

    @property
    def fabric_consumption(self):
        super().fabric_consumption()
        return str(float(self.param) / 6.5 + 0.5)


class Suit(Clothes):

    @property
    def name(self):
        super().name()
        return 'Костюм.'

    @property
    def fabric_consumption(self):
        super().fabric_consumption()
        return str(2 * float(self.param) + 0.3)


suit = Suit(48)
print(suit.name)
print(suit.fabric_consumption)

print('_' * 30)

coat = Coat(170)
print(coat.name)
print(coat.fabric_consumption)
