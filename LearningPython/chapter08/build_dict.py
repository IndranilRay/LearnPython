# Build dict
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

D = {x: x ** 2 for x in range(1, 5)}
print(D)

D = {c: c*4 for c in 'SPAM'}
print(D)

# Initialzing a dict using 'fromkeys'
D = dict.fromkeys(['a', 'b', 'c', 'd'], 0)
print(D)

# Initialzing using comprehension
D = {k:0 for k in ['a', 'b', 'c']}
print(D)

# Initalize using None
D = dict.fromkeys(['a', 'b', 'c'])
print(D)




