spam = 'SPAM'  # basic assignments
print('spam is = %s\n' % spam)

spam, ham = 'yum', 'YUM'  # tuple assignment positional
print('spam = %s and ham = %s \n' % (spam, ham))

[spam, ham] = ['yum', 'YUM']  # List assignment (positional)
print('Value of [spam, ham] = [{},{}] \n'.format(spam, ham))

a, b, c, d = 'spam'  # Sequence assignment ,generalized
print('Value of a,b,c,d is {},{},{},{} \n'.format(a, b, c, d))

a, *b = 'spam'  # extended sequence unpacking
print('Value of a,b is {} {}\n'.format(a, b))








