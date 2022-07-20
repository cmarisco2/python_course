# demo using min and max normally and with a lambda as key

nums = [1, 2, 3, 4]

print(f"min of {nums }: {min(nums)}")

print(f"min char of string 'hello' is: {min('hello')}")

names = ['Michael', 'Mariah', 'Christopher', 'Tim']
print(
    f"the names list is {names} and the minimus name by starting character is: {min(names)}"
)

min_length_name = min(names, key=lambda name: len(name))
print(f"minimum length name(via key=lambda) is: {min_length_name}")
