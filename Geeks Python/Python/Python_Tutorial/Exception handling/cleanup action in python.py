def divide(x,y):
	try:
		result = x//y
	except ZeroDivisionError:
		print("sorry !! you are dividing by zero")
	else:
		print("yeah! your answer is",result)
	finally:
		print("I'am finally clause ,alway raised!!")
divide(3,2)
print()
divide(4,0)
print()
divide(3,6)