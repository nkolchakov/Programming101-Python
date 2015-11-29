import json


def read_json():
    with open('calories.json', 'r') as f:
        data = json.load(f)

    return data


def write_json(kv_pair):
    data = read_json()

    data.update(kv_pair)

    with open('calories.json', 'w') as f:
        json.dump(data, f)


def calculate_calories():

    while True:
        database = read_json()
        command = input('Enter command>')
        if command == 'goodbye':
            break;
        meal = ' '.join(command.split()[1:])
        eaten_quantity = input('How much have you eaten?>')

        weight = 0
        measurement = ''
        if eaten_quantity[len(eaten_quantity) - 2] == 'k':
            weight = int(eaten_quantity.split('kg')[0])
            measurement = 'kg'
        else:
            weight = int(eaten_quantity.split('g')[0])
            measurement = 'g'
        calories_per_100 = 0
        if meal not in database:
            print (format('I don\'t have %s in the calories database.' % meal))
            calories_per_100 = int(input('How much calories per 100g?>'))
            write_json({meal: calories_per_100})
        else:
            calories_per_100 = int(database[meal])

        total = calories_per_100/100*weight
        if measurement == 'kg':
            total *= 1000
        print (format(
                'OK, this is a total of %d calories for this meal.' % total))

    print ("Goodbye!")
calculate_calories()
