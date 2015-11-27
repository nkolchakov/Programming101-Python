# generate_numbers.py
import sys
from random import randint


def main():
    file_name = sys.argv[1]
    n = sys.argv[2]

    with open(file_name, 'w') as data:
    	for i in range(0,int(n)):
        	data.write(str(randint(1, 1000)) + " ")

if __name__ == '__main__':
    main()
