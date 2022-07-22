# demo errors


def colorize(text, color):
    """text is a string of any kind, color is a string of fixed set of colors"""
    colors = {'red', 'blue', 'yellow', 'orange', 'green', 'indigo', 'violet'}
    if type(text) != str or type(color) != str:
        raise TypeError('text and color must be string arguments')
    if color not in colors:
        raise ValueError('color must be of the rainbow spectrum (roygbiv)')
    print(f"Printed {text} in {color}")


# colorize('hi', 'red')
# colorize(1, 'red')
# colorize('hi', 1)
colorize('favorite', 'teal')
