"""
Demonstrating use of getter setter and deleter
"""


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@email.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        #return '{} {}'.format(self.first, self.last)
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last  = None



emp_1 = Employee('John', 'Smith')
# emp_1.first = 'Jim'

# emp_1.fullname = 'Neal Ray'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.email)