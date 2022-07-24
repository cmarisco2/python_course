# demo python underscores conventions:

# _single -> conventionally private
# __double -> Name Mangled for Inheritance Purposes
# __dunder__ -> overriding Python Class Methods

class Underscore:
    def __init__(self, normal, private, mangled):
        self.normal = normal
        self._private = private
        self.__mangled = mangled


underscore = Underscore('normal', 'private', 'mangled')
print(f"normal access: {underscore.normal}")
print(
    f"private is only a convention and can be accessed normally too: {underscore._private}")
print(
    f"I need private class name for the mangled. ex <Underscore_Instance>._Underscore__mangled: {underscore._Underscore__mangled}")
