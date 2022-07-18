# demo list comprehensions in python

# Classical loop version
numbers = [1, 2, 3, 4, 5]
double_numbers = []

for num in numbers:
    double_num = 2 * num
    double_numbers.append(double_num)

print(f"List using loop is: {double_numbers}")

# List Comprehension Version
