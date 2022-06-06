try:
	k = 5//0
	print(k)
except ZeroDivisionError:
	print("can't divide by zero")
finally:
	print("these is always executed")
	