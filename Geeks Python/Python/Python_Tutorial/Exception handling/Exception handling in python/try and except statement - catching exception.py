a = [1,2,3,4,5,6,7,8]
try:
	print("second element:: %d" %(a[1]))
	print("fourth element:: %d" %(a[9]))
except:
	print("an error occurred")
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

#catching specific error
def fun(a):
	if a < 4:
		b = a/(a-3)
	print("valueof b::",b)
try:
	fun(3)# if you write an char it occured name error
	fun(5)
except ZeroDivisionError:
	print("zerodivisionerror occureed and it will handle")
except NameError:
	print("name error occured and handied")
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

#try with else clause
def abc(a,b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a ,b result is 0")
	else:
		print(c)
abc(44,2)
abc(2,2)
