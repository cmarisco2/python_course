# list to remove from
my_list = [123.45, "Something Random", 22, True, False, True, 17.3, "1221", 1]
print(my_list)

# demo pop() and pop(<index>)
removed_item = my_list.pop()
print(f"demo pop(). removed item: {removed_item}")
removed_item = my_list.pop(2)
print(f"demo pop(2). removed item: {removed_item}")
print(my_list)

# demo remove(obj)
removed_item = 17.3
print(f"Item I wish to remove: {removed_item}")
my_list.remove(removed_item)
print(my_list)

# demo clear()
print(f"remove all items from {my_list}")
my_list.clear()
print(f"my list: {my_list}")
