"""
	Demo simple class inheriting objects
"""
class SharedData:
	spam = 42

x = SharedData()

# SharedData.spam = 99

x.spam = 45
SharedData.spam = 99
print(x.spam)

class MixedNames:
	data  = 'spam'
	def __init__(self, values):
		self.data = values
	def display(self):
		print(self.data, MixedNames.data)

print("Values of object X", end="\nx")
x = MixedNames(1)
y = MixedNames(2)

print(x.display())
print(y.display())
# print(MixedNames.display())

class NextClass:
	def printer(self, text):
		self.message = text
		print(self.message)


x = NextClass()
x.printer('instance call')
print(NextClass.printer(x, 'Call by class'))
NextClass.printer('Bad call')