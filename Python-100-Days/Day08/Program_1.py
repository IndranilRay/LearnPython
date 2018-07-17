class Student(object):
    # init__ is a special method for initializing operation when creating Objects.
    # In other words it is Constructor.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('{} is learning {}'.format(self.name, course_name))

    # PEP8 requires the name of the attribute to be underlined with lowercase multiple words
    def watch_av(self):
        if self.age < 18:
            print('{} can only watch beer infested'.format(self.name))
        else:
            print('{} is watching the island country love action movie . '.format(self.name))


def main():
    # Create student object
    stu1 = Student('Neal', 31)

    # to study object of a message
    stu1.study('Python Programming')

    # to send the object a message
    stu1.watch_av()

    stu2 = Student('Deon Nash', 21)
    stu2.study('Ideology')
    stu2.watch_av()


if __name__== '__main__':
    main()








