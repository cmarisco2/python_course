# even and odd lists from IF comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"entire list: {numbers}")

odd_nums = [x for x in numbers if x % 2 == 1]
even_nums = [x for x in numbers if x % 2 == 0]
print(f"odd numbers in list from 'if' list comprehension: {odd_nums}")
print(f"even numbers in list from 'if' list comprehension: {even_nums}")

# demo if/else list comprehension

weird_nums = [x*x if x % 2 == 1 else x*2 for x in numbers]
print(f"weird nums using if/else conditionals: {weird_nums}")
