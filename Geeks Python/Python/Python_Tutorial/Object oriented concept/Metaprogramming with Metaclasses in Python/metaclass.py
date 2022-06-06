num = 143
print("type of num is::",type(num))
lst = [1,4,3] 
print("type of num is::",type(lst))
name = "girish"
print("type of num is::",type(name))
print("~~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~~~~~")

class student:
	pass
obj = student()
print("type of obj is ::",type(obj))

print("~~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~~~~~")

class person:
	pass
print("type of person is ::",type(person))
print("~~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~~~~~")

class test:pass
test.x = 25
test.y = lambda self:print("hello")
obj = test()
print(obj.x)
obj.y()