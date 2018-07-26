myfile = open('myfile.txt', 'w') # Open for text output:create/empty
myfile.write('hello text file \n') # Write a line of text:string

myfile.write('goodbye text file\n')
myfile.close()

# reading a file line by line
myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
myfile.close()

# reading a file all at once to string
print(open('myfile.txt').read())

# scan a text file line by line'
for line in open('myfile.txt'):
    print(line, end='')
