# A Python program to demonstrate both packing and unpacking.
# A sample python function that takes three arguments and prints them
def fun1(a, b, c):
	print(a, b, c)

# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):

	# Convert args tuple to a list so we can modify it
	args = list(args)

	# Modifying args
	args[0] = 'Geeksforgeeks'
	args[1] = 'awesome'

	# UNPACKING args and calling fun1()
	fun1(*args)

# Driver code
fun2('Hello', 'beautiful', 'world!')


#** use for dictionary
# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
	print(a, b, c)

# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
fun(**d)

print(" ")

# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):

	# kwargs is a dict
	print(type(kwargs))

	# Printing dictionary items
	for key in kwargs:
		print("%s = %s" % (key, kwargs[key]))

# Driver code
fun(name="geeks", ID="101", language="Python")
