from collections import namedtuple
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob)

# accessing named tuples by position
print(bob[0])
print(bob[1])

# access named tuple by attribute
print(bob.name)
print(bob.age)
