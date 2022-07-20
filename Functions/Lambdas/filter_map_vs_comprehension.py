# demo all this functionality in a list comprehension

# given list of names
# filter to who we want
# map the filteredObj to manipulate what we want

# name list
names = ['john', 'lexie', 'chris', 'mike', 'colt', 'mariah', 'anthony']
print(f"all names: {names}")

# filter (nest to perform first) and map:
filtered_mapped_list = list(
    map(lambda x: f"Your instructor is {x}", filter(lambda x: len(x) < 5, names)))

print(f"list filtered and mapped: {filtered_mapped_list}")


# single line pythonic filtering and mapping with list comprehension
altered_list = [x.upper() for x in names if len(x) > 4]
print(
    f"filtered and mapped in 1 list comprehension for names greater than 4 characters uppercased: {altered_list}"
)
