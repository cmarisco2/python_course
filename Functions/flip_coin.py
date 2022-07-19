# demo return statement

from random import random


def flip_coin():
    chance = random()
    if chance > 0.5:
        return "Heads"
    else:
        return "Tails"


print(flip_coin())
