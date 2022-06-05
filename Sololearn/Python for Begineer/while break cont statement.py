x = 1
while x < 10:
	if x % 2 == 0:
		print(str(x) + "is even")
	else:
		print(str(x)+ "is odd")
	x += 1
	
#break statement
i = 0
while True:
	print(i)
	i += 1
	if i >= 5:
		print("breaking")
		break
print("finished")

#continue statement
i = 1
while i <= 5:
	print(i)
	i += 1
	if i == 3:
		print("skipping 3")
		continue