"""
    Script illustrates best way to sort a dict by keys
"""
# create a dict
A = dict(a=1, b=2, c=3)
# Method 1

# dictionary sorting method
for key in sorted(A.keys()):
    print(key, A[key])

# list sorting method

for key in sorted(A):
    print(key, A[key])





