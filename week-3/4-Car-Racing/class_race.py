from random import uniform


class Race:

    def __init__(self, drivers):
        self.drivers = drivers
        self.crash_chance = uniform(0.5, 1)

    # ranking after every race
    def result(self):
        pass
        # save result in 'result.json'

    def __str__(self):
        diction = eval(str(self.drivers[0]))
        diction['crash_chance_for_race'] = self.crash_chance
        return str(diction)

    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        diction = eval(str(self))
        return diction[index]
# For first place - 8
# Second place - 6
# Third place - 4.
# All other places are scored with 0.
