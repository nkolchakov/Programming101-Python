import datetime
from functools import wraps

def get_promotion(promotion_months):
    def accepter(func):
        def decorated(months, user_id):
            if months >= promotion_months:
                months += 1
            return func(months, user_id)
        return decorated
    return accepter

def accepts(*dec_args):
    def accepter(func):
        def decorated(*func_args):
            for x in range(0, len(dec_args)):
                if not isinstance(func_args[x], dec_args[x]):
                    return ('{} is not {}'.format(func_args[x], dec_args[x] ))
            return func(*func_args)
        return decorated
    return accepter

def encrypt(offset):
    def accepter(func):
        def decorated():
            text = list(func())
            for i in range(0,len(text)):
                if text[i] != ' ':
                    text[i] = chr(ord(text[i]) + offset)
            return "".join(text)
        return decorated
    return accepter

def log(name):
    def accepts(func):
        def decorated():
            with open(name, 'a') as f:
                f.write(func() + '\n')
            print ('{} was called {}'.format(func.__qualname__, datetime.datetime.now()))
        return decorated
    return accepts




@log('log.txt')
@encrypt(3)
def get_low():
    return "Get get get low"

print(get_low())


@get_promotion(3)
def pay_net(months, user_id):
    return("{} payed Internet for {} months".format(user_id, months))

@accepts(str)
def say_hello(name):
    return ("Hello, I am {}".format(name))

@accepts(str, int)
def deposit(name, money):
    return ("{} sends {} $!".format(name, money))
    return True


print(deposit("RadoRado", 10))
print(pay_net(5, "rado"))
print(say_hello('x'))