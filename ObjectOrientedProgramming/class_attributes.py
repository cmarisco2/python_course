# demo creating class attributes:

# class attributes == global variables in the class
# ACCESS via <Class>.<global>

class User:

    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.age = age
        self.last = last
        User.active_users += 1

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


user1 = User('Chris', 'Marisco', 32)
user2 = User('Mariah', 'Morey', 27)
print('first user: ' + user1.full_name())
print('second user: ' + user2.full_name())
print(f'active users: {User.active_users}')
print(user2.logged_out())
print(f'active users: {User.active_users}')
