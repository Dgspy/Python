try:
	b = 10/0
	print(b)
except ArithmeticError:
	print("this statement is raising an arithemetic exception")
else:
	print("success")
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
try:
	a = [1,2,3,4,5]
	print(a[5])
except LookupError:
	print("index out of bound error.")
else:
	print("success")