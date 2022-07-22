# demo raising error

"""
Common Errors:

SyntaxError - invalid syntax
NameError - variable not defined
TypeError - wrong type of argument used
IndexError - invalid index
ValueError - valid arg, but incorrect arg ex: int('5') -> good int('hi') -> bad
KeyError - non-existent key requested from dictionary
AttributeError - attribute non-existent for class/type ex] 'hi'.giggle() -> bad
"""
print('\n\n\nThe Following is NOT an ERROR: \n\n\n')
raise NameError('This is a DEMO of creating an error')
