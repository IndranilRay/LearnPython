# sorting a dictionary

# Method 1
D = {'a': 1, 'b': 2, 'c': 3}
ks = D.keys()

try:
    ks.sort()
except AttributeError:
    ks = list(ks)
    ks.sort()
    for k in ks:
        print(k, D[k])

# Method 2
D = {'b': 2, 'c': 3, 'a': 1}
for k in sorted(D.keys()):
    print(k, D[k])










