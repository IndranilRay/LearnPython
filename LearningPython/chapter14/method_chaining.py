"""
    script demonstrate few string method chaining operations in list comprehension
"""
#1
print([line.upper() for line in open('script_test.py')])

#2
print([line.rstrip().upper() for line in open('script_test.py')])

#3
print([line.split() for line in open('script_test.py')])

#4
print([line.replace(' ', '!') for line in open('script_test.py')])

#5
print([('sys' in line, line[:5]) for line in open('script_test.py')])



