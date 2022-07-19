# demo functions with parameters(in def) and arguments(in call)

def say_hello(name):
    return f"say hello to {name}"


def multiply(var1, var2=2):
    return var1 * var2


print(say_hello('Janice'))

print(multiply(3, 4))

# default arg
print(multiply(10))
