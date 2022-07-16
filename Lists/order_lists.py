# list to use:

numbers = [5, 6, 2, 1, 5, 3, 7]

# demo index
print(f"list: {numbers}")
print(f"index of 2: {numbers.index(2)}")

# demo count
print(f"5 occurs: {numbers.count(5)} times")

# demo reverse
numbers.reverse()
print(f"list reversed is: {numbers}")

# demo sort
numbers.sort()
print(f"list sorted in ascending order is {numbers}")

# bonus string method join

# loop to change each element to a string
i = 0
while i < len(numbers):
    numbers[i] = str(numbers[i])
    i += 1
# join to add delimiter between elements of string list
string = ' Good Number: '.join(numbers)
print(f"list as a string: {numbers}")
print("Joining the elements of the list:\n " + string)
