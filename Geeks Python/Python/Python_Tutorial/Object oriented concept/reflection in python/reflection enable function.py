#callable
x = 5
def testfun():
	print("Test")
y = testfun
if (callable(x)):
	print("x is callable")
else:
	print("x is not callable")
if (callable(y)):
	print("y is callable")
else:
	print("y is not callable")

class fool:
	def __cell__(self):
		print("print i am girish")
print(callable(fool))
print(fool())

print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
# dir
num = [1,2,3,4,5,6,8,7]
print(dir(num))
char = ["g","i","r","i","s","h"]
print(dir(char))

print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

#getattr
class employee:
	salary = 1430000
	company_name = "d2oi"
emp = employee()
print("the salary is :",getattr(emp,"salary"))
print("the salary is :",emp.salary)
print("the company is :",getattr(emp,"company_name"))
print("the company is :",emp.company_name)
