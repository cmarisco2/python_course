# respect _private attributes by using property tag for getters
# and using the property name.setter for setters

# TEST
# create instance
# set age as if an attribute: <instance>.age = num
# retrieve age as if an attribute
class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self._age = age

    def __repr__(self) -> str:
        return f'{self.name} is {self._age} years old'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


person = Human('johnny', 17)
print(person)
person.age += 5
print(person)
