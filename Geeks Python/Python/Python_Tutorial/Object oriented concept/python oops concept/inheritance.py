class person:
	def __init__(self,name,idnumber):
		self.name = name
		self.idnumber = idnumber
	def display(self):
		print(self.name)
		print(self.idnumber)
	def details(self):
		print("my name is {}".format(self.name))
		print("my idnumber is {}".format(self.idnumber))

class employ(person):
	def __init__(self,name,idnumber,salary,post):
		self.salary = salary
		self.post = post
		person.__init__(self,name,idnumber)
	def __details(self):
		print("my name is{}".format(self.name))
		print("my idnumber is{}".format(self.idnumber))
		print("my post is {}".format(self.post))
		
a = employ("girish",14315,2000000,"pro-hacker")
b = employ("yash",111,1000000,"software engineer")
a.display()
a.details()
b.display()
b.details()