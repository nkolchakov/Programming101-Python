# cat2.py
import sys


def main():	
	file_names = sys.argv[1:]
	for f in file_names:
		with open(f, 'r') as data:
			print (data.read())


if __name__ == '__main__':
    main()