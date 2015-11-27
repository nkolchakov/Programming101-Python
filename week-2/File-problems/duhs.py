import sys
import os

RESULT = 0


def calculate_size(root):

    files = os.listdir(root)
    rs = 0
    for f in files:
        if os.path.isfile(root + '/' + f):
            res = os.stat(root + '/' + f).st_size
            print root + '/' + f
            print res

            # print root + '/' + f

        else:
            # print root + '/' + f
            calculate_size(root + '/' + f)

def main():

    result = calculate_size("/home/kolchakov/HackBulgaria101-Python/")
    print result


if __name__ == '__main__':
    main()
