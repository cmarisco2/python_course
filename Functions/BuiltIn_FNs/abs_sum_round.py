# demo abs() sum() and round():
nums = [2, 76, -11, 4, -3, -9000, 500]
print(f"absolute value of the greatest magnitude in {nums} is: ")

print(max(abs(x) for x in nums))

print(f"sum of all the values in {nums} is: ")
print(sum(x for x in nums))

value = 3.14159265
print(f"PI rounded to 8 sig figs: {round(value, 8)}")
print(f"PI rounded to 4 sig figs: {round(value, 4)}")
print(f"PI rounded to 2 sig figs: {round(value, 2)}")
print(f"PI rounded as an integer: {round(value)}")
