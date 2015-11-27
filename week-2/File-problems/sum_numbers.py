import sys


def main():
    numbers_as_string = sys.argv[1]
    result = 0
    with open(numbers_as_string, 'r') as data:
        read_data = data.read()
        # numbers = read_data.split(' ')
        # for num in numbers:
        # 	result += int(num)
        result = sum([int(x) for x in read_data.split(' ') if x != ''])
    print (result)

if __name__ == '__main__':
    main()
