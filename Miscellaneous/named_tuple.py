"""
Demonstrating use of named tuple
"""
from collections import  namedtuple

# Def : namedtuple is kind of light weight object  that works more like
# a regular object but it more readable
# it is compromise between dictionary and tuple


# color code
#color = (55, 155, 255)

# We can use dict like this
#color = {'red': 55, 'green': 155, 'blue': 255}

# but we are loosing immutabilty feature

# create a namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55, 155, 255)
white = Color(255, 255, 255)

print(color.red)
print(white.green)
