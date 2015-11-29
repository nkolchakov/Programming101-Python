import datetime


def food():
    print ('Hello and welcome')
    print ('Choose an option.')
    print ('1. meal - to write what you are eating now.')
    print ('2. list <dd.mm.yyyy> - lista all the meals that you ate that day.')
    menu = {}
    now_date = datetime.datetime.now().strftime('%d.%m.%Y')

    while True:
        term_input = input('Enter command>> ')
        command = ''.join(term_input.split()[0])
        argument = ' '.join(term_input.split()[1::])    

        if command == 'meal':
            if now_date not in menu:
                menu[now_date] = [argument]
            else:
                if argument not in menu[now_date]:
                    menu[now_date].append(argument)
                else:
                    print ('Already exists')
                    continue
            print ('Ok it is saved.')

        elif command == 'list':
            if argument not in menu.keys():
                print ('No such date')
                continue
            for food in menu[argument]:
                print (food)
        else:
            print ('Wrong command.')
            print ('1. meal - to write what you are eating now.')
            print (
                '2. list <dd.mm.yyyy> - lista all the meals that you ate that day.')

food()
