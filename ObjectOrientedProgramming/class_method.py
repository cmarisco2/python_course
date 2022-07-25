# demo creating class methods:

# class methods:
# use @classmethod decorator
# use 'cls' as convention for naming 1st arg

# Why?
# -common: preprocess data before passing to an instance(new obj)

class User:

    active_users = 0

    @classmethod
    def from_string(cls, data_string):
        first, last, age = data_string.split(',')
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.age = age
        self.last = last
        User.active_users += 1

    def __repr__(self) -> str:
        return f"This user is {self.full_name()} and is {self.age} years old"

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

    def logged_out(self):
        User.active_users -= 1
        return f"{self.first} has logged off"


user1 = User.from_string("Chris,Marisco,32")

print(user1)
