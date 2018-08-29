# Aggregate embedded objects into composite


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person %s %s]' %(self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus=1.0):
        self.person.give_raise(percent+bonus)

    def __getattr__(self, item):
        return getattr(self.person, item)

    def __repr__(self):
        return str(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def give_raise(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='Dev', pay=10000)
    tom = Manager('Tom Jones', 5000)

    development = Department(bob, sue)
    development.addMember(tom)
    development.give_raise(.10)
    development.show_all()






