# demo try/except

import errno


try:
    foobar
except:
    print('Some error happend')
print('But we continued')

# demo catching a specific error:

d = {'name': 'bobby'}


def get(dictionary, key):
    try:
        dictionary[key]
    except KeyError:
        return None


print(d.get('name'))
print(d.get('city'))
