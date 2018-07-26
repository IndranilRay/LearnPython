X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s, %s, %s \n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

F = open('datafile.txt', 'r')
line = F.readline()
print(line.rstrip())
line = F.readline()
P = line.split(',')
numbers = [int(P) for P in P]
print(numbers)
line = F.readline()
parts = line.split('$')
objects = [eval(P) for P in parts]
print(objects)
F.close()



