# Like nested but returns function instead

from random import choice


def make_laugh_func():
    def get_laugh():
        return choice(('Hahaha', 'lmao', 'lol'))
    return get_laugh


laugh = make_laugh_func()
print(laugh())
