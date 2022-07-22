# demo importing an external module and using it
"""

# INSTALL:
# $ python3 -m pip install <pkg name>

# See Docs:
# help(<obj/module>) Note: must be imported in module or terminal

"""


from termcolor import colored

# to SEE DOCUMENTATION use help(<obj>) ie. help(termcolor)

# help(termcolor)

text = colored('Hello, World', color='red')
print(text)
