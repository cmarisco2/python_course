
def add_positive_nums(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y


print(add_positive_nums(1, 1))
print(add_positive_nums(-1, 1))
