# 3 X 3 Matrix
M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

# Get row 2 of the matrix
print(M[1])

# Get column 2 of the matrix
col2 = [row[1] for row in M]
print(col2)

# Add 1 to each item in column 2
new_col2 = [row[1] + 1 for row in M]
print(new_col2)

# Filter out odd items
print([row[1] for row in M if row[1]%2 == 0])

# Collect diagonal of the matrix
print([M[i][i] for i in [0, 1, 2]])

# Repeat character in string
print([c * 2 for c in 'spam'])

# create a list -6 to 6
print(list(range(-6, 7, 2)))


# Create a generator of row sums
G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

# map built in can do the similar work for generating sum of rows
print(list(map(sum, M)))

# create a dict from this list
dict_list = {sum(row) for row in M}
print(dict_list)

# create key:value pair of row sums
print({i: sum(M[i]) for i in range(3)})

# built a list with comprehension
print([ord(x) for x in 'spam'])

# built a set
print({ord(x) for x in 'spaam'})

# built a dict
print({x: ord(x) for x in 'spaam'})

# build a generator obj
Gen = (ord(x) for x in 'spaam')
print(next(Gen), next(Gen))




