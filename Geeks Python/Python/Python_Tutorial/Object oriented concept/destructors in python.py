class employee:
	def __init__(self):
		print("employee created")
	def __del__(self):
		print("destructor called,emplyed deleted")
o = employee()

print("~~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~~~~~")

class employee:
	def __init__(self):
		print("employee created")
	def __del__(self):
		print("destructer called")
def create():
	print("making a object")
	o = employee()
	print("function end")
	return o
print("called create obj")
o = create()
print("program end")
print("~~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~~~~~")
class A:
	def __init__(self,bb):
		self.b = bb
class B :
	def __init__(self):
		self.a = A(self)
	def __del__(self):
		print("die")
def fun():
	b = B()
fun()