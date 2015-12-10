from class_car import Car
from class_driver import Driver
from class_race import Race
import json
import os


class Championship:

    def __init__(self, name, races_count):
        self.name = name
        self.races_count = races_count

    def _read_json(self, name):
        with open(name) as f:
            data = json.load(f)
        return data

    def _generate_json(self, list_to_convert):
        curr_json = {}
        for person in list_to_convert:
            splitted = str(person).split(' - ')
            name = splitted[0]
            points = splitted[1]
            curr_json[name] = points
        try:
            data = self._read_json('result.json')
        except:
            # if json file doesn't exist
            self._write_json('result.json', curr_json)
            return

        for person in curr_json:
            if person in data:
                points = int(data[person])
                points_to_add = int(curr_json[person])
                data[person] = points + points_to_add
            else:
                # if driver doesn't exist in json, add it
                data[person] = curr_json[person]

        self._write_json('result.json', data)
        print (self._read_json('result.json'))

    def _write_json(self, name, data):
        with open(name, 'w') as f:
            json.dump(data, f)

    def _generate_race(self):
        drivers_for_curr_race = []
        participants = self._read_json('cars.json')

        for person in participants['people']:
            person_car = Car(person['car'], person['model'], person['max_speed'])
            curr_driver = Driver(person['name'], person_car)
            drivers_for_curr_race.append(curr_driver)

        curr_race = Race(drivers_for_curr_race)
        return curr_race

        # generate staing using concentration level of each driver
    def generate_standing(self, drivers):
        concentr_level = {}
        standings = []
        for dr in drivers:
            concentr_level[dr['concentration']] = dr['name']
        for level in sorted(concentr_level):
            standings.append(concentr_level[level])
        return standings[::-1]

    def visualize_standing(self, standing):
        places = {
            0: 8,
            1: 6,
            2: 4
        }

        result = []
        index = 0
        for driver in standing:
            result.append(str("{} - {}".format(driver, places[index])))
            index += 1
            if index == 3:
                break
        return result

    def begin_championship(self):
        for i in range(0, int(self.races_count)):
            print ("#### Race {} ####".format(i + 1))
            curr_race = self._generate_race()
            participants = curr_race.drivers
            survived_drivers = []
            for part in participants:
                if (part['crash_coef'] < curr_race.crash_chance):
                    survived_drivers.append(part)
                else:
                    print ('Unfortunately, {} has crashed.'.format(
                        part['name']))

            curr_standing = self.generate_standing(survived_drivers)
            standing_with_points = self.visualize_standing(curr_standing)
            print (standing_with_points)
            self._generate_json(standing_with_points)
        
        os.remove('result.json')

    def top3(self):
        pass
