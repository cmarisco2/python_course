# Pattern for creating decorator fn with multi-args


# Create a decorator fn that returns the upper case of any string with any number of positional/keyword arguments

# Preserves metadata of the original wrapped function
from functools import wraps


def shout(fn):
    @wraps
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def order(main, side):
    return f"I would like an order of {main} with a side of {side} please"


@shout
def greet(name):
    return f"Hello, my name is {name}"


@shout
def lol():
    return 'lol'


print(greet('Michael'))
print(order('steak', 'potatoes'))
print(order(main='salad', side='burger'))
print(lol())
