# demo lambda functions in python

# normal function
def square(num):
    return num ** 2


# normal function call:
print(f"normal fn call of square(4): {square(4)}")

# lambda function stored in a variable:
square2 = lambda num : num * num
add = lambda a,b : a + b
print(f"lambda function call of square(4): {square(4)}")
print(add(2,3))

# print to show lambda's are anonymous
print(square.__name__)
print(square2.__name__)
print(add.__name__)

