"""
Try for loop
"""

nums = [1, 2, 3, 4, 5]

# use break to skip iteration and come out of the loop
for num in nums:
    if num == 3:
        print('Found!!')
        break
    print(num)

# use continue to skip next iteration and continue all other iterations
for num in nums:
    if num == 3:
        print('Found!!')
        continue
    print(num)

# using nested inner loops
print('nested inner loops')
for num in nums:
    for letter in 'abc':
        print(num, letter)

# use range to iterate certain times
print('Use range() to iterate')
for i in range(1, 11):
    print(i)

# while loop keeps going until certain condition is met
print('Iterate using while loop')
x = 0
while x < 10:
    print(x)
    x += 1


# while and break
print('Using break in while')
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1