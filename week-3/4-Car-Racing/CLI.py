from class_championship import Championship


class CLI:
    def __init__(self, command, chmpnship_name, races_count):
        self.chmpnship_name = chmpnship_name
        self.races_count = races_count
        self._act = command

    # new crash_coef every time
    def _commands(self, command_param):
        self.operation = {
            "start": self._start,
            "standings": self._standings
        }
        self.operation[command_param]()

    # redirects to which command to go
    def begin(self):
        self._commands(self._act)

    def _hello_message(self):
        return ("Hello PyRacer!")

    def _menu_message(self):
        return ("Please, call command with the proper argument:")

    def _help_message(self):
        return ("$ python3 race.py start <name> <races_count> -> This will start a new championship with the given name, races count and drivers from cars.json \n"
        "$ python3 race.py standings -> This will return the standings for each championship that has ever taken place.")

    def _start(self):
        print ("Starting a new championship called {} with {} races.".format(
            self.chmpnship_name, self.races_count))
        print ("Running {} races ...".format(self.races_count))

        my_championship = Championship(
            self.chmpnship_name, self.races_count)

        my_championship.begin_championship()

    def _standings(self):
        print ("standing")
