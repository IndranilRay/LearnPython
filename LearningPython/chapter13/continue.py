"""
Using continue statement in  a while loop
"""
x = 10

# Find all even numbers between 1 to 10
# version 1 using continue statements

while x:
    x -= 1
    if x % 2 != 0: continue
    print("%d is odd" % x)
