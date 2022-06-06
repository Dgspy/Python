def decor(*arg,**kwarg):
	def inner(fun):
		'''
		do operation with func
		'''
		return fun
	return inner
@decor
def func():
	'''
	function implemented
	'''
	
print("~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~")

def decor(func):
	print("inner func")
	def inner(*arg,**kwarg):
		print("inside inner func")
		print("decorated the func")
		func()
	return inner
@decor
def fun():
	print("inside actual function")
fun()

print("~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~")

def decor(func):
	print("inside func")
	def inner(*arg,**kwarg):
		print("inner inside func")
		print("decorated the func")
		func()
	return inner
def fun():
	print("inside actual function")
decor(fun)()
print("~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~")

#example1
def decor(*arg,**kwarg):
	print("inside function")
	def inner(func):
		print("inside inner func")
		print("i like",kwarg['like'])
		fun()
	return inner
@decor(like = "darkdevil of internet")
def fun():
	print("inside actual function")
print("~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~")

#example 2
def decor(x,y):
	def inner(func):
		def wrapper(*arg,**kwarg):
			print("i like darknet king ping")
			print("summation of value - {}".format(x + y))
			fun(*arg,**kwarg)
		return wrapper
	return inner
def fun(*arg):
	for i in arg:
		print(i)
decor(12,15)(fun)("darkdevil","of","internet")
print("~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~")

# Python code to illustrate
# Decorators with parameters in Python (Multi-level Decorators)
def decodecorator(dataType, message1, message2):
	def decorator(fun):
		print(message1)
		def wrapper(*args, **kwargs):
			print(message2)
			if all([type(arg) == dataType for arg in args]):
				return fun(*args, **kwargs)
			return "Invalid Input"
		return wrapper
	return decorator
@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
	st = ''
	for i in args:
		st += i
	return st
@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
	summ = 0
	for arg in args:
		summ += arg
	return summ
print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))
