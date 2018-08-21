"""
    Script demonstrates iteration protocol employed by a list iterable
    using 'while' and 'for' loop
"""

L = [1, 2, 4, 5, 6]

for l in L:
    print(l ** 2)

c = '='
print(c*25,)
Iter = iter(L)  # passing list in iter() to obtain iterators

while True:
    try:
        X = next(Iter)
    except StopIteration:
        break
    print(X ** 2, end=' ')



