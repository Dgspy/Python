#exception AssertionError
'''
assert False, 'the assertion failed'
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception AttributeError
'''
class Attributes(object):
	pass
object = Attributes()
print(object.attribute)
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception EOFError
'''
while True:
	data = input("Enter name::")
	print("hello", data
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")	
#exception floting pointerror
'''
import math
print (math.exp(1000))
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

#exception generatorexit
def generator():
	try:
		for i in range(5):
			print('yilding',i)
			yield i
	except GeneratorExit:
		print('exicting early')
g = generator()
print(g.__next__())
g.close()
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception import error
'''
import module_does_not_exist
#or
from exceptions import Userexception
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception IndexError
'''
array = [0,1,2,3,4]
print(array[5])
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception keyerror
'''
array = {'a':1,'b':2}
print(array['c'])
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception keyboardinterrupt
'''
try:
	print ('Press Return or Ctrl-C:',)
	ignored = input()
except Exception(err):
	print ('Caught exception:', err)
except KeyboardInterrupt(err):
	print ('Caught KeyboardInterrupt')
else:
	print ('No exception')
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception memoryerror
'''
def fact(a):
	factors = []
	for i in range(1, a+1):
		if a%i == 0:
			factors.append(i)
	return factors

num = 600851475143
print (fact(num))
'''
class BaseClass(object):
	"""Defines the interface"""
	def __init__(self):
		super(BaseClass, self).__init__()
	def do_something(self):
		"""The interface, not implemented"""
		raise NotImplementedError(self.__class__.__name__ + '.do_something')

class SubClass(BaseClass):
	"""Implementes the interface"""
	def do_something(self):
		"""really does something"""
		print (self.__class__.__name__ + ' doing something!')

SubClass().do_something()
BaseClass().do_something()

'''
# excepttion name error
def fun():
	print(ans)
fun()
'''
#exception NotImplementedError
class BaseClass(object):
	"""Defines the interface"""
	def __init__(self):
		super(BaseClass, self).__init__()
	def do_something(self):
		"""The interface, not implemented"""
		raise NotImplementedError(self.__class__.__name__ + '.do_something')

class SubClass(BaseClass):
	"""Implementes the interface"""
	def do_something(self):
		"""really does something"""
		print (self.__class__.__name__ + ' doing something!')

SubClass().do_something()
BaseClass().do_something()
	