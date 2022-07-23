# demo the name property variable difference in the running file
from other_name import thy_name


def my_name():
    print(f"Hi! My __name__ is {__name__}")


my_name()
thy_name()
