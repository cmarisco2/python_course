from copy import copy


class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self) -> str:
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You can't add that"

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "Cannot be multiplied"


j = Human("Jenny", "Larson", 47)
k = Human("Kevin", "Jones", 52)
print(j)
print(k)
print(f"Length of j: {len(j)}")
print(f"Length of k: {len(k)}")
print(j + k)
copies_of_j = j * 5
print(copies_of_j)
print((k + j) * 3)  # triplets
