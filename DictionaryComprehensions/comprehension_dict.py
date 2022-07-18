# demo dictionary comprehensions

from math import comb


str1 = "ABC"
str2 = "123"
print(f"string 1: {str1}")
print(f"string 2: {str2}")

combo = {str1[i]: str2[i] for i in range(len(str1))}

print(f"string 1 chars as keys with string 2 chars as values via comprehension")
print(combo)

nums = dict(a=1, b=2, c=3)
print(f"nums: {nums}")
print("dict comprehensions to square the values")

double_nums = {num: value ** 2 for num, value in nums.items()}
print(double_nums)
