class Car:

    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        diction = {}
        diction['car'] = self.car
        diction['model'] = self.model
        diction['max_speed'] = self.max_speed
        return str(diction)

    def __repr__(self):
        return str(self)
