# Christopher Marisco

"""
Higher Order Functions come in 2 Varieties:
    1) Taking FNs as Args
    2) Creating Nested FNs:
       a) returning val/obj/nothing
       b) returning the Nested FN

Decorators 1) take FN arg 2) Nest & Return the Nested FN
"""


def be_polite(fn):
    def wrapper():
        print('Some Statement')
        fn()
        print('Following Statement')
    return wrapper


def greet():
    print("Hello, My Name is Chris")


greet = be_polite(greet)
greet()
