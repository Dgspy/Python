class base:
	def __init__(self):
		self.a = "darkside"
		self.__c = "darktype"
class floor(base):
	def __init__(self):
		base.__init__(self)
		print("calling private member of base class:")
		print(self.__c)
o = base()
print(o.a)
print(o.__c)#it raise an error like attribute error
