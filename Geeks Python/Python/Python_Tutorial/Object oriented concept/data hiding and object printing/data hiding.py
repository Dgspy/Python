class myclass:
	__hidden = 0
	def add(self,increment):
		self.__hidden += increment
		print(self.__hidden)
a = myclass()
a.add(2)
a.add(5)
#print(a.__hidden)#raise the erro

print("############~~~~~~~~^^^^^^^^^^^^^^^^^^^#############~~~~~~~~")
#access hidden member
class myclass:
	__hidden = 10
o = myclass()
print(o._myclass__hidden)
