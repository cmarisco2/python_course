"""
Use ext. modules - pyfiglet, termcolor 
terminal_input - string word, string color

"""

import termcolor as t

# f is Figlet obj? that has renderText as a method
from pyfiglet import Figlet
f = Figlet()

# Once color is set
# print(f.renderText('text to render'))


def write_text():
    while True:
        word = input('Enter your desired phrase: ')
        color = input('Enter your color: ')
        if color not in t.COLORS:
            print('sorry, pick another color')
        else:
            # word = t.colored(word, color)
            word = f.renderText(word)
            break

    # print(f.renderText(word))
    print(t.colored(word, color))


write_text()

# Note: do ascii conversion first. Then the color change
