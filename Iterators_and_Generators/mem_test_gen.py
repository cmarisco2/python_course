# Create a list of fib numbers and a generator of fib numbers
# Compare memory usage


def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


def fib_gen(max):
    x, y = 0, 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count += 1
