from functools import wraps


def print_more(func):
    @wraps(func)
    def inner(*args):
        print ('from decorator')
        return func(*args)
    return inner

@print_more
def prnt(msg):
    print (msg)

prnt('adas')