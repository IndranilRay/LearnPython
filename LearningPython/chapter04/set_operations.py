x = set('abcde')
y = set('bdxyz')

# difference
diff_x = x - y
print(diff_x)

# union of two sets
union = x | y
print(union)

# intersection of two sets
intersect = x & y
z = x.intersection(y)
print(intersect)
print(z)

# Insert one item
z.add('SPAM')
print(z)

# Merge in place union
z.update(['X', 'Y'])
print(z)

# remove an element
z.remove('X')
print(z)

# set support iteration protocol
for item in set('abc'):
    print(item * 3)

