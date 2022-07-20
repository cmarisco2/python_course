# demo lambda functions in python

# normal function
def square(num):
    return num ** 2


# normal function call:
print(f"normal fn call of square(4): {square(4)}")

# lambda function called at creation:
square2 = lambda num : num * num
print(f"lambda function call of square(4): {square(4)}")

