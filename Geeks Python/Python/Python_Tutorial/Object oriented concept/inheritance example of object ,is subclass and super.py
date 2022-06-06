class person(object):
	def __init__(self,name):
		self.name = name
	def getname(self):
		return self.name
	def employee(self):
		return False
class employee(person):
	def employ(self):
		return True
e = person("girish")
print(e.getname(),e.employee())
e = employee("yash")
print(e.getname(),e.employ())

print("#################%&&&&&&&&&^^^^^^^^^^^##########")
class base(object):
	pass
class derived(base):
	pass
print(issubclass(derived,base))
print(issubclass(base,derived))
d = derived()
b = base()
print(isinstance(b,derived))
print(isinstance(d,base))
print("#################%&&&&&&&&&^^^^^^^^^^^##########")

class base:
	def __init__(self):
		self.str = "girish"
		print(base)
class base1:
	def __init__(self):
		self.str1 = "yash"
		print(base1)
class derived(base,base1):
	def __init__(self):
		base.__init__(self)
		base1.__init__(self)
		print("derived")
	def print(self):
		print(self.str,self.str1)
ob = derived()
ob.print()
print("#################%&&&&&&&&&^^^^^^^^^^^##########")
class base:
	def __init__(self,x):
		self.x = x
class derived(base):
	def __init__(self,x,y):
		base.x = x
		self.y = y
	def print(self):
		print(base.x,self.y)
d = derived(10,23)
d.print()
print("#################%&&&&&&&&&^^^^^^^^^^^##########")

class base:
	def __init__(self,x):
		self.x = x
class floor(base):
	def __init__(self,x,y):
		super(floor,self).__init__(x)
		self.y = y
	def print(self):
		print(self.x,self.y)
a = floor(12,34)
a.print()

print("#################%&&&&&&&&&^^^^^^^^^^^##########")
#excersice

class X(object):
	def __init__(self, a):
		self.num = a
	def doubleup(self):
		self.num *= 2

class Y(X):
	def __init__(self, a):
		X.__init__(self, a)
	def tripleup(self):
		self.num *= 3

obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)

print("#################%&&&&&&&&&^^^^^^^^^^^##########")
# Base or Super class
class Person(object):
	def __init__(self, name):
		self.name = name
		
	def getName(self):
		return self.name
	
	def isEmployee(self):
		return False

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
	def __init__(self, name, eid):

		''' In Python 3.0+, "super().__init__(name)"
			also works'''
		super(Employee, self).__init__(name)
		self.empID = eid
		
	def isEmployee(self):
		return True
		
	def getID(self):
		return self.empID

# Driver code
emp = Employee("Geek1", "E101")
print(emp.getName(), emp.isEmployee(), emp.getID())
