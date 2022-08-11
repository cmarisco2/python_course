# demo multiple inheritence features of python

class Aquatic:
    def __init__(self, name) -> None:
        self.name = name

    def swim(self):
        return f"{self.name} is swimming!"

    def hi(self):
        return f"{self.name} says 'hi' from the sea!"


class Ambulatory:
    def __init__(self, name) -> None:
        self.name = name

    def walk(self):
        return f"{self.name} is walking!"

    def hi(self):
        return f"{self.name} says 'hi' from a mountain top!"


class Penguine(Aquatic, Ambulatory):
    def __init__(self, name) -> None:
        super().__init__(name)


jaws = Aquatic("JAWS")
lassie = Ambulatory('LASSIE')
marina = Penguine("MARINA")

print(marina.swim())
print(marina.walk())
print(marina.hi())

print(
    f"\nMarina's hi method is prioritized by which class is inherited first [Rd as 'left-most arg'] in the multiple inheritance arguments passed"
)
