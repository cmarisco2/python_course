# Timing generator expressions vs list comprehensions

from time import time

# Timing list comprehension summing to 100 million
list_start_time = time()
print(sum([n for n in range(100000000)]))
list_stop_time = time() - list_start_time

print(f"List Comprehension Summing to 100 Million Time: {list_stop_time}")

# Timing generator expression summing to 100 million
gen_start_time = time()
print(sum((n for n in range(100000000))))
gen_stop_time = time() - gen_start_time

print(f"Generator Expression Summing to 100 Million Time: {gen_stop_time}")
