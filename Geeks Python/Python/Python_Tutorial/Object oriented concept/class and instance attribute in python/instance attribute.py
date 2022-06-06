class emp:
	def __init__(self):
		self.name = "girish"
		self.salary = 143151431514315
	def show(self):
		print(self.name)
		print(self.salary)
e = emp()
print("dictionary form::",vars(e))
print(dir(e))