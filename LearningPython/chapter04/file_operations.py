# File operations
# Make a new file in output mode ('w' is write)
f = open('data.txt', 'w')

# write strings of characters to it
f.write('Hello\n')
f.write('World\n')
f.write('Neal\n')

# close to flush output buffer to disk
f.close()

# 'r' is the default proessing mode
f = open('data.txt')
text = f.read()
f.close()
print(text)

# read file  without read
for line in open('data.txt'):
    print(line)

