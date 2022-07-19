# demo functions with parameters(in def) and arguments(in call)

def say_hello(name):
    """returns string 'say hello to' concatenated with a string argument provided by the user"""
    return f"say hello to {name}"


def multiply(var1, var2=2):
    return var1 * var2


def exponent(base, power=2):
    return base ** power


print(say_hello('Janice'))

print(multiply(3, 4))

# default arg
print(multiply(10))

# keyword args
print(exponent(power=3, base=4))

# print doc for fn documentation
print(say_hello.__doc__)
