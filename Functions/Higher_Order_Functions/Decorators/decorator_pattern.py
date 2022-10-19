# Pattern for creating decorator fn with multi-args


# Create a decorator fn that returns the upper case of any string with any number of positional/keyword arguments

# Preserves metadata of the original wrapped function
from functools import wraps


def shout(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def order(main, side):
    """Uses main and side args for dish orders"""
    return f"I would like an order of {main} with a side of {side} please"


@shout
def greet(name):
    """Greets the name passed"""
    return f"Hello, my name is {name}"


@shout
def lol():
    """returns string 'lol' """
    return 'lol'


print(greet('Michael'))
print(order('steak', 'potatoes'))
print(order(main='salad', side='burger'))
print(lol())
