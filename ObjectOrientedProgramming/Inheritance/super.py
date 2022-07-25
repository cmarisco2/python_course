# demo super() to pass data to base class

# Animal:
#   name
#   species
# Dog:
#   name
#   species
#   breed
#   favorite_toy

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self) -> str:
        f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f'animal says {sound}')


class Dog(Animal):
    def __init__(self, name,  breed, favorite_toy):
        super().__init__(name, species='Dog')
        self.breed = breed
        self.toy = favorite_toy
