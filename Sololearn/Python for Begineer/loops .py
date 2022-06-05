x = ["white","evil","devil","ping"]
for g in x:
	print(g+"!")
	
#A for loop can be used to iterate over strings.
str = "string is testing for loop"
count = 0
for x in str:
	if(x == 't'):
		count += 1
print(count)

list = [2,3,4,5,6,7]
for x in list:
	if(x%2 == 1 and x > 4):
		print(x)
		break