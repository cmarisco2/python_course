import string


def add_nums(a, b):
    return a + b


def is_funny(person):
    if not isinstance(person, str):
        raise TypeError("person must be of type string")
    if person == 'Tim':
        return False
    return True


if __name__ == "__main__":
    demo = add_nums(1, 5)
    print(demo)
