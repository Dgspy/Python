# part 1 calculate the factorial of given number
# part 2 find a number in trailing zero in that factorial
def factorial(number):
	if number == 0 or number ==1:
		return 1
	else:
		return number * factorial(number - 1)
def factorialTrailingZeros(number):
	pass
	
if __name__ == '__main__':
	number = int (input("enter a number :\n"))
	fac = factorial(number)
	print(f"the factorial is {fac}")
	
	
	
	
# part 1 calculate the factorial of given number
# part 2 find a number in trailing zero in that factorial
def factorial(number):
	if number == 0 or number ==1:
		return 1
	else:
		return number * factorial(number - 1)
def factorialTrailingZeros(number):
	fac = factorial(number)
	print(fac)
	count = 0
	while(number%10 == 0):
		count = count + 1
		number = number/10
	return count
	
if __name__ == '__main__':
	#number = int (input("enter a number :\n"))
	#fac = factorial(number)
	#print(f"the factorial is {fac}")
	
	print(factorialTrailingZeros(6))