# declare a tuple

T = (1, 2, 3, 4)

# length of a tuple
print(len(T))

# concatenate a tuple
T = T + (5, 6)
print(T)

# count no of appearance of an item in tuple
print(T.count(4))

# tuple are immutable
# T[0] = 'neal' # error

# make a new tuple with a new value
T = (2,) + T[1:]
print(T)



