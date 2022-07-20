# demo any and all fns

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# all(<iterable>)
# passing list comprehension that returns list of bools rather than numbers
print(f"are all numbers even? {all([num % 2 == 0 for num in numbers])}")
print(f"are any numbers even? {any([num % 2 == 0 for num in numbers])}")

# Using Generator Expression (no need to return the whole list)
# More lightweight
print(
    f"are any numbers even? (using gen exp) {any(num % 2 == 0 for num in numbers)}"
)
