n = int(input("Enter a Armstrong Number::- ___"))
sum = 0
order = len(str(n))
copy_n = n
while(n > 0):
	digit = n % 10
	sum += digit ** order
	n1 = n//10
if(sum == copy_n):
	print(f"{n1} is an armstrong number")
else:
	print(f"{n1} is not an armstrong number")