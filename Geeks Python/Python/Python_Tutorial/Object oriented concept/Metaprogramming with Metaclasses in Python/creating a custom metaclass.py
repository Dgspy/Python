def test(self):
	print("this is test class")
class base:
	def fun(self):
		print("this is inherited method")
Test = type('test',(base,),dict(x = "girish",method = test))
print("type of test class::",type(Test))
test_obj = Test()
print("type of test obj::",type(test_obj))
test_obj.fun()
test_obj.method()
print(test_obj.x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
# our metaclass
class MultiBases(type):
	# overriding __new__ method
	def __new__(cls, clsname, bases, clsdict):
		# if no of base classes is greater than 1
		# raise error
		if len(bases)>1:
			raise TypeError("Inherited multiple base classes!!!")
		
		# else execute __new__ method of super class, ie.
		# call __init__ of type class
		return super().__new__(cls, clsname, bases, clsdict)

# metaclass can be specified by 'metaclass' keyword argument
# now MultiBase class is used for creating classes
# this will be propagated to all subclasses of Base
class Base(metaclass=MultiBases):
	pass

# no error is raised
class A(Base):
	pass

# no error is raised
class B(Base):
	pass

# This will raise an error!
class C(A, B):
	pass
