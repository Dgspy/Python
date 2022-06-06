'''#class derived_classname(super-classname):
class pet:
	def __init__(self,name,age):
		self.name = name
		slef.age = age
class cat(pet):
	def __init__(self,name,age):
		super().__init__(name,age)
def main():
	the_pet = pet("pet",1)
	gangu = cat("gangu",3)
	print("is gangu a cat" + str(isinstance(gangu,cat)))
	print("is gangu a pet" + str(isinstance(gangu,pet)))
	print("is the_pet is cat" + str(isinstance(the_pet,cat)))
		print("is the_pet is pet" + str(isinstance(the_pet,pet)))
		print(gangu.name)
if __name__ == '__main__':
	main()
'''	
	
# Syntax for inheritance

# A Python program to demonstrate working of inheritance
class Pet:
		#__init__ is an constructor in Python
		def __init__(self, name, age):	
				self.name = name
				self.age = age

# Class Cat inheriting from the class Pet
class Cat(Pet):		
		def __init__(self, name, age):
				# calling the super-class function __init__
				# using the super() function
				super().__init__(name, age)

def Main():
		thePet = Pet("Pet", 1)
		jess = Cat("Jess", 3)
		
		# isinstance() function to check whether a class is
		# inherited from another class
		print("Is jess a cat? " +str(isinstance(jess, Cat)))
		print("Is jess a pet? " +str(isinstance(jess, Pet)))
		print("Is the pet a cat? "+str(isinstance(thePet, Cat)))
		print("Is thePet a Pet? " +str(isinstance(thePet, Pet)))
		print(jess.name)

if __name__=='__main__':
		Main()
