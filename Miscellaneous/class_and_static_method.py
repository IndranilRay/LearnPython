# Python program to demonstrate
# class method and static method

from datetime import  date

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age  = age


    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


if __name__ == '__main__':
    person1 = Person('neal', 31)
    person2 = Person.fromBirthYear('Meenu', 1990)

    print('Person1 age {}'.format(person1.age))
    print('Person2 age {}'.format(person2.age))

    #Person.isAdult(22)
