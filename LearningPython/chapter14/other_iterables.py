"""
    Script demonstrate tools that process  iterables
"""
import functools, operator

# 1'Map'
mapped = map(str.upper,open('script_test.py'))
print(list(mapped))

# 2 'Sorted'
srted = sorted(open('script_test.py'))
print(list(srted))

# 3.Zip
print(list(zip(open('script_test.py'),open('script_test.py'))))

# 4.enumerate
print(list(enumerate(open('script_test.py'))))

# 5.bool
print(list(filter(bool, open('script_test.py'))))

# 6.reduce
print(functools.reduce(operator.add, open('script_test.py')))

