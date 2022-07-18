# demo accessing and iterating nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# row major OR first indices id's list elem, 2nd id's elem in list

print("Show entire list")
print(nested_list)

print(f"\nfirst list within the nested list is: {nested_list[0]}\n")
print(f"Second elem of first list is: {nested_list[0][1]}")


# iterate over list
print("all elements of the list are:")

for num_list in nested_list:
    for val in num_list:
        print(val)

# nested list comprehension:

board = [["x" if num % 2 == 1 else "o" for num in range(
    1, 4)] for val in range(1, 5)]
print(board)
