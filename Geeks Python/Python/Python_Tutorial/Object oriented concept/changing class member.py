class student:
	stream = "ssc"
	def __init__(self,name,roll):
		self.name = name
		self.roll = roll
a = student("girish",68)
b = student("yash",1)
print("before changeing stream")
print("a ::",a.stream)
print("b::",b.stream)
a.stream = "cbse"
print("afterchanging a stream")
print("a ::",a.stream)
print("b ::",b.stream)

print("~~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~~~~~")
class student:
	stream = "ssc"
	def __init__(self,name,roll):
		self.name = name
		self.roll = roll
a = student("yash",3)
print("a stream::",a.stream)
student.stream = "cbse"
b = student("girish",4)
print("a.stream::",a.stream)
print("b.stream::",b.stream)
