from datetime import date
class person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	@classmethod
	def birthyear(cls,name ,year):
		return cls(name,date.today().year - year)
	@staticmethod
	def adult(age):
		return age > 18
p1 = person("girish",26)
p2 = person.birthyear("girish",2005)
print(p1.age)
print(p2.age)
print(person.adult(16))