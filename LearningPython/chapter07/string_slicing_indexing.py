# Slice section from s
s = 'spammy'
print(s[:3] + 'xx' + s[5:])

# using method
print(s.replace('mm', 'xx'))

# replace method is more general
print('aa$bb$cc$dd'.replace('$','SPAM'))

# search for a position and replace
S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')
print(S[:where] + 'EGGS' + S[where+4:])

# use replace with 3rd argument
print(S.replace('SPAM', 'EGGS', 2))

# join operations
print('SPAM'.join(['eggs', 'sausage', 'ham', 'text']))

# split method
line = 'aaa bbb ccc'
print(line.split())
new_line = 'bob,hacker,40'
print(new_line.split())

