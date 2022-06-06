#empty class object
class Dog:
	pass
	
#object

class Dog:
	attr = "mammal"
	def __init__(self,name):
		self.name = name
guru = Dog("guru")
tommy = Dog("tommy")
print("guru is a {}".format(guru.__class__.attr))
print("tommy is a {}".format(tommy.__class__.attr))
print("my name is {}".format(guru.name))
print("my name is {}".format(tommy.name))
print("############~~~~~~~~^^^^^^^^^^^^^^^^^^^#############~~~~~~~~")

class Dog:
	attr = "mammal"
	def __init__(self,name):
		self.name = name
	def speak(self):
		print("my name is {}".format(self.name))
jambo = Dog("jambo")
tommy = Dog("tommy")
jambo.speak()
tommy.speak()