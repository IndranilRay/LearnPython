"""
 Testing json module to store json object and read back to file
"""
import json
name = dict(first='Bob', last='Smith')

rec = {'name': name, 'job': ['dev', 'mgr'], 'age': 40.5}

print(type(rec))
S = json.dump(rec, fp=open('test_json.txt', 'w'), indent=4)
print(type(S))

# reading back this json file
F = open('test_json.txt', 'r')

S = json.load(F)

print(S)

