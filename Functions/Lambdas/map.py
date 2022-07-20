# demo map

nums = [1, 2, 3, 4, 5]
print(f"nums: {nums}")

# use map (vice list_comprehension) to double every num value
double_nums = list(map(lambda x: x * 2, nums))
print(f"double_nums via map: {double_nums}")
