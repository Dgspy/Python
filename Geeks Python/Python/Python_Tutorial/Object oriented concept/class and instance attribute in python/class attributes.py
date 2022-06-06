class python:
	count = 0
	def increase(self):
		python.count += 1
c1 = python()
c1.increase()
print(c1.count)
c2 = python()
c2.increase()
print(c2.count)
print(python.count)

