"""
 Demonstrating Regular , Static and Class Method
"""


class Employees:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employees.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_method(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """
        This is a kind of alternative constructor
        :param emp_str:
        :return:
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employees('Neal', 'Ray', 7000)
emp_2 = Employees('John', 'Doe', 4000)


print(Employees.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


# set_raise_amount
Employees.set_raise_method(1.05)
print(Employees.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# Sometimes class method can also be used as alternative constructor
# below is the use case

emp_str_1 = 'Bruce-Wayne-7800'
emp_str_2 = 'Steve-Woz-8000'
emp_str_3 = 'Christ-Lewis-9000'

# first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employees(first, last, pay)

new_emp_1 = Employees.from_string(emp_str_1)

print(new_emp_1.__dict__)



