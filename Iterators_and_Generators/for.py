# Custom For Loop:
# Get an iterator via iter()
# While No StopIteration Error is Raised:
# next(iterator)


# Print each element in iterable objects
def my_for(iterable, func):
    # Grabs iterator via iter() on an iterable
    iterator = iter(iterable)
    # Use while loop until Stop Iteration Error
    while True:
        try:
            # Store each element via next()
            thing = next(iterator)
        except StopIteration:
            # Need break statement else -> INFINITE LOOP
            break
        else:
            # Note thing is one element of the iterator object
            func(thing)


def square(x):
    print(x*x)


my_for("HELLO", print)
print()
my_for([1, 2, 3, 4], square)
