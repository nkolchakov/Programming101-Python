from bookreader import BookReader

def chain(*args):
    res = []
    for i in range(0, len(args)):
        for el in args[i]:
            res.append(el)
    return res

def compress(iterable, mask):
    res = []
    for i in range(0,len(mask)):
        if mask[i]:
            res.append(iterable[i])
    return res

def cycle(iterable):
    size = len(iterable)
    while True:
        for i in range(0, size):
            yield i

def main():
    file_name = '001.txt'
    br = BookReader(file_name)
    endless = cycle(range(0,10))
    for item in endless:
        print(item)

    # for i in iterator:
    #     input("Press Enter from next chapter:)")
    #     print(i)
    # print (chain(range(0,4),range(4,8)))
    # print(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
    #print(compress(range(11,15), [False, False, True]))

if __name__ == '__main__':
    main()