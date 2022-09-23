# Using a generator function to make an iterator for counting to max
# Similar to Range() and the custom_iterator.py but No need for a class

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)
print(
    f'counter is a generator function which ultimately is an iterator: {counter}')

print('Using a For loop on the generator fn (counting to 5):')
for num in counter:
    print(num)
