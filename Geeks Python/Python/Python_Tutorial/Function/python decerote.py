def hello(fun):#2 step
	def inner():#3 step     step6
		print("i will be first")#step 7
		fun()#step 8
		print("this is second")#step 11
	return inner#4 step
def function():#step 9
	print("thhis is third and inside the function")#step10
function = hello(function)#1 step
function()#5 step step 12
print("~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~")

import time
import math
def calculate(fun):
	def inner(*args,**kwargs):
		start = time.time()
		fun(*args,**kwargs)
		end = time.time()
		print("total time taken is::",fun.__name__,end - start)
	return inner
@calculate
def factorial(num):
	time.sleep(2)
	print(math.factorial(num))
factorial(10)
print("~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~")

def hello(fun):
	def inner(*arg,**kwarg):
		print("bfore execute")
		value = fun(*arg,**kwarg)
		print("after execute")
	return inner
@hello
def sum(a,b):
	print("inside the function")
	return a + b
x , y = 1,2
print("sum = ",sum(x , y))
print("~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~")

# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner
def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner
@decor1
@decor
def num():
	return 10
print(num())
