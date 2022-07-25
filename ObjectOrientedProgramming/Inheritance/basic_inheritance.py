class Animal:
    def make_sound(self, sound):
        print(f'animal says {sound}')


class Dog(Animal):
    pass


a = Animal()
a.make_sound('Rawr!!!')

pepsi = Dog()
pepsi.make_sound('Woof')
