# demo iterating over dictionary
instructor = {
    "name": "Chris",
    "age": 32,
    "isCool": True
}

# iterate over values:
for val in instructor.values():
    print(val)

# iterate over keys:
for key in instructor.keys():
    print(key)

# iterate over keys and values:

for key, value in instructor.items():
    print(key, value)
