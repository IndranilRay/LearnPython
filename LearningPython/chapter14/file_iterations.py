"""
 This file demonstrate ways to read a text file using iteration protocols
 and figure out the best way to read a text file.
"""

"""
    1. Using file 'readline' method.
    !. Not Recommended. Not memory efficient
"""

for line in open('script_test.py').readlines():
    print(line.upper(), end='')


"""
    1. Using 'While' loop
    !. Better than 1st one but not so efficient as it is using. 
    !. Not Recommended 
"""
x = '='
print(x * 20)
f = open('script_test.py')
while True:
    line = f.readline()
    if not line:break
    print(line.upper(), end='')

f.close()
print(x * 20)

"""
    1. Using 'for' loop
    !. Better than above two in performance and memory usage
    !. Recommended way of reading a file 
"""
for line in open('script_test.py'):
    print(line.upper(), end='')







