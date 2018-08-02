"""
Code in this file show some samples to  iterate over a dictionary.
"""
D = {'a': 1, 'b': 2, 'c': 3}

# extract keys without using dict method

for key in D:
    print(key, '=>', D[key])

# Iterate over both keys and values using dict method

for (key, value) in D.items():
    print(key, '=>', value)



