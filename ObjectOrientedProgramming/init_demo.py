# demo init in Vehicle class:

# The constructor holds the attributes of the class (and their names)
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.year = year
        self.model = model


mazda = Vehicle('mazda6', '6 Series', 2008)

# use obj.attribute_name to access the fields

print(mazda.make)
print(mazda.model)
print(mazda.year)
