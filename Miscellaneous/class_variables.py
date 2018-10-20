"""
    Demonstrating use of class variables.
    Def: Class Variable are variables that are shared among the instances of a class.
"""


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee('Neal', 'Ray', 5000)
emp_2 = Employee('Code', 'Jarvis', 10000)

print(emp_1.pay)
print(emp_1.apply_raise())
print(emp_1.pay)


