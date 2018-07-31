"""
This file contains some basic print functions usage
in python version 3.X
"""

x = 'spam'
y = 99
z = ['eggs']

print(x, y, z)  # without suppress separator
print(x, y, z, sep='')  # with suppress separator
print(x, y, z, sep=',')  # with custom separator
print(x, y, z, end='')  # suppress the line break
print(x, y, z, end='');print(x, y, z)  # two prints same output line
print(x, y, z, end='...\n')
print(x, y, z, sep='......', file=open('data.txt', 'w'))  # print to a file
print(x, y, z)  # back to std out
print(x, y, z)  # display file text







