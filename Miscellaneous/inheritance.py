"""
Demonstrating inheritance concept
"""


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amt = 1.20

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        if self.employees:
            for emp in self.employees:
                print('-->', emp.fullname())


dev_1 = Developer('John', 'Doe', 7000, 'Python')
dev_2 = Developer('Neal', 'Ray', 5000, 'Java')

# print(help(Developer))
# print(dev_1.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)


mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1, dev_2])

print(mgr_1.email)
print(mgr_1.print_emps())
print(mgr_1.remove_employee(dev_1))
print(mgr_1.print_emps())

# demostrating issubclass and isinstance

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

# One of the best example w.r.t inheritance you can find in Python exception WSGI library
# class HTTPException