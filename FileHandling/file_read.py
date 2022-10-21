# demo opening and reading a file

file = open("story.txt")
print(file.read())

# cursor is at end -> doesn't read anything
print(file.read())
