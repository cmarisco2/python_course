# demo memory used in a list comprehension vs a generator expression
import sys
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# use sys.getsizeof() to get bytes of data used
list_size = sys.getsizeof([x * 10 for x in range(10000)])
gen_size = sys.getsizeof((x * 10 for x in range(10000)))

print("The amount of memory used for identical tasks:")
print(f"List Comprehension: {list_size} bytes")
print(f"Generator Expression: {gen_size} bytes")
