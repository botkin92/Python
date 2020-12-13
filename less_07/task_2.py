from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_calc(self):
        pass


class Coat(Clothes):
    @property
    def fabric_calc(self):
        return round(float(self.param / 6.5 + 0.5), 2)


class Costume(Clothes):
    @property
    def fabric_calc(self):
        return round(float(2 * self.param / 0.3), 2)


obj_1 = Coat(46)
obj_2 = Costume(180)

print(obj_1.fabric_calc)
print(obj_2.fabric_calc)
