# demo abs() sum() and round():
nums = [2, 76, -11, 4, -3, -9000, 500]
print(f"absolute value of the greatest magnitude in {nums} is: ")

print(max(abs(x) for x in nums))

print(f"sum of all the values in {nums} is: ")
print(sum(x for x in nums))
