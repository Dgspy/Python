class girish:
	def __init__(self):
		self.girish = "darkdevil of internet"
	def print(self):
		print(self.girish)
g = girish()
g.print()

print("~~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~~~~~")

class add:
	first = 0
	second = 0
	answer = 0
	def __init__(self,f,s):
		self.first = f
		self.second = s
	def display(self):
		print("first number ::" + str(self.first))
		print("second number ::" + str(self.second))
	def cal(self):
		self.answer = self.first + self.second
o = add(1000,2000)
o.cal()
o.display()