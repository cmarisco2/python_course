# demo creating instance methods:

class User:

    def __init__(self, first, last, age):
        self.first = first
        self.age = age
        self.last = last

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.full_name()} likes {thing}."

    def is_senior(self):
        return self.age >= 65

    def add_to_age(self, num):
        self.age += num
        return self.age


user1 = User('Christopher', 'Marisco', 32)
print(f"User: {user1.full_name()}")
print(f"User's initials: {user1.initials()}")
print(f"User's likes: {user1.likes('curry')}")
print(f"User is senior?: {user1.is_senior()}")
print(f"User's age  plus 5: {user1.add_to_age(5)}")
