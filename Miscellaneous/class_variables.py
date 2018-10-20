"""
    Demonstrating use of class variables.
    Def: Class Variable are variables that are shared among the instances of a class.
"""


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Neal', 'Ray', 5000)
emp_2 = Employee('Code', 'Jarvis', 10000)

print(Employee.num_of_emps)

# print(emp_1.pay)
# print(emp_1.apply_raise())
# print(emp_1.pay)

print(Employee.raise_amount)

# instance accessing class raise amount raise_amount attr
print(emp_1.raise_amount)

# instance accessing class raise amount raise_amount attr
print(emp_2.raise_amount)

# Get namespace of emp_1
print(emp_1.__dict__)

print(Employee.__dict__)


emp_1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)