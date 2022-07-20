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
