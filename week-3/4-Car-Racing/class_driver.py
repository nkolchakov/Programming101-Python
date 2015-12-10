from random import uniform
from class_car import Car


class Driver:

    def __init__(self, name, car):
        self.name = name
        self.car = car
        self.crash_coef = uniform(0, 1)
        self.concentration = uniform(0.5, 1)

    def __str__(self):
        diction = {}
        diction['name'] = self.name
        diction['car'] = self.car
        diction['concentration'] = self.concentration
        diction['crash_coef'] = self.crash_coef
        return str(diction)

    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        diction = eval(str(self))
        return diction[index]
