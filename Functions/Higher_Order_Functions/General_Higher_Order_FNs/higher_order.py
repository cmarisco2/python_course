# We can pass functions as args to other functions

"""
    Higher Order Function Concept:
        1) Pass Functions as arguments AND/OR
        2) Return Functions as results

    Often demonstratred with lamda fn's
"""

#############################################################
# define basic functions to pass as args


def square(num):
    return num ** 2


def cube(num):
    return num ** 3

#################################################################

# PASSED A FUNCTION ARG!


def sum_values(n, func):
    total = 0
    for k in range(n):
        total += func(k)
    return total


print(sum_values(4, square))
print(sum_values(4, cube))
