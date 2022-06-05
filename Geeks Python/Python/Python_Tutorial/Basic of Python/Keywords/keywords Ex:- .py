# keyword
"""  and 	as	 assert	 break 	class continue 	def 	elif 	else 	except	 false	 finally 	for 	from global 	if	 import 	in	 is	 lambda 	None nonlocal	 not 	or	 pass 	raise	 return 	True 	try 	while 	with yield """

#pyton code to demoatrated at working of iskeywords ()
#importing keywords for keyword operation 
import keyword
# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)
#true keyword
print(False == 0)
print(True == 1)
#false keywords
print(True + True + True )
print(True + False + False)
#none keywords
print(None == 0)
print(None ==[])
# logical operators
print(True or False)
print(False or True )
print(not True)
# using "in "to check 
if 's' in 'geeksforgeeks':
	print("start progrming")
else:
	print("stop programing")
#using "in" to loop through 
for i in 'geeksforgeeks':
	print(i, end=" ")
print("\r")
print('	'  is  '	')
print({} is {})
#ex :-  For , while, break ,continue keywords

#using for loop
for i in range(10):
	print(i , end = " ")
	if i == 6:
		break
print()
# loop from 1 to 10
i = 0
while i<10 :
	if i == 6:
		i += 1
		continue
	else:
		print(i , end = ' ')
		
	i += 1
	
# eg: if else and elif keywords
i = 20
if i ==10:
	print (" i si 10")
elif i == 20:
	print('i is 20')
else:
	print('i dont know')
	
#eg: def keyword
def fun():
	print("hii girish")
fun()

# eg : return and yield
def fun():
	s = 0
	for i in range(10):
		s += i
		yield s
for i in fun():
	print(i)
#eg: class
class Dog:
	no1 = "mammalia"
	no2 = "dog"
	def fun(self):
		print("i am a",self.no1)
		print("i am a",self.no2)
rocky = Dog()
print(rocky.no1)
rocky.fun()

#eg: with keywords
with open('file_path ', 'w') as file:
	file.write("hello world !")
	
# as keywords
import math as girish
print(girish.factorial(5))
print(girish.sqrt(4))
#pass keywords
n = 10
for i in range(n):
	# pass can be used  as placeholder
	#when code is to added later
	pass

# lambda keywords
l = lambda x: x * x*x
print(l(4))
#import ,from keywords
#import keywords
import math
print(math.factorial(10))
#from keywords
from math import factorial
print(factorial(10))
# try , except, raise, finally andassert keywords
a = 4
b = 0
try:
	k = a//b
	print(k)
except ZeroDivisionError:
	print("can't devide by zero")
finally:
	print("this is always execute")
print("this evalue of a and b is :")
"""assert b != 0 , "Divide by 0 error"
print(a / b)"""
#print AssertionError:Divide by 0 error
#del keywords
var1 = 20
var2 = "python is powerfull wepon"
print(var1)
print(var2)
del var1
del var2
"""print(var1)
print(var2)"""
#print NameError:name 'var1'
# global and non-local keywords
a = 15
b = 10
def add():
	c = a + b
	print(c)
add()
def fun():
	no1 = 10
	def gun():
		nonlocal no1
		no1 = no1 + 10
		print(no1)
	gun()
fun()
#https://pastebin.com/PFANwc1F
a = 10
def read():
	print(a)
def mod1():
	global a
	a = 5
def mod2():
	a = 15
read()
mod2()
read()
print("value of a using nonlocal :",end=" ")
def outer():
	a = 5
	def inner():
		a = 10
	inner()
	print(a)
outer()