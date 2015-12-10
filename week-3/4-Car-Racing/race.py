import json
import sys
from CLI import CLI


def hello_message():
    return ("Hello PyRacer!")


def menu_message():
    return ("Please, call command with the proper argument: \n$ python3 race.py start <name> <races_count> -> This will start a new championship with the given name, races count and drivers from cars.json \n"
    "$ python3 race.py standings -> This will return the standings for each championship that has ever taken place.")


def main():

    if len(sys.argv) > 1:
        command = sys.argv[1]
        chmpship_name = sys.argv[2]
        chmpship_races_count = sys.argv[3]
        interface = CLI(command, chmpship_name, chmpship_races_count)
        interface.begin()
    else:
        print (hello_message())
        print (menu_message())

if __name__ == '__main__':
    main()
