class test:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def __repr__(self):
		return "test a :%s b %s"%(self.a ,self.b)
	def __str__(self):
		return"from str method of test :a is %s,"\
		"b is %s"%(self.a , self.b)
t = test(1432,1515)
print(t)
print([t])

print("############~~~~~~~~^^^^^^^^^^^^^^^^^^^#############~~~~~~~~")

class test:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def __repr__(self):
		return "test a:%s  b:%s"%(self.a,self.b)
t = test(2314,1433)
print(t)
print("############~~~~~~~~^^^^^^^^^^^^^^^^^^^#############~~~~~~~~")
class test:
	def __init__(self,a,b):
		self.a = a
		self.b = b
t = test(2341,1243)
print(t)