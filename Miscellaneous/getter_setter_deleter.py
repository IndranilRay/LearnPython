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

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

