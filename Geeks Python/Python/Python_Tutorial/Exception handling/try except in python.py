def div(x,y):
	try:
		result = x//y
		print("yeah your answer is :",result)
	except ZeroDivisionError:
		print("sorry !! you are dividing by zero")
div(35,5)
print(" ")
div(43,0)
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#else clause
# Program to depict else clause with try-except

# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

#finally keyword in python
# Python program to demonstrate finally
	
# No exception Exception raised in try block
try:
	k = 5//0 # raises divide by zero exception.
	print(k)
	
# handles zerodivision exception	
except ZeroDivisionError:
	print("Can't divide by zero")
		
finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')

