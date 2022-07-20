# demo filter() w/ lambda

names = ['alex', 'austin', 'bailey', 'haley', 'andrea', 'jeremiah']
print(f"list of all names: {names}")

# filter

a_names = list(filter(lambda x: x[0] == 'a', names))
print(f"list of all names beginning with the letter 'a': {a_names}")
