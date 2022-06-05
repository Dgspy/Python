def my_func():
	print("yash")
	print("girish")
	print("rocky")
my_func()
 #multiple time function called ex:-
def hello():
	print("hello world !")
hello()
hello()
hello()

#function argument
def print_with_exclamation(word):
	print(word + '!')
print_with_exclamation("girish")
print_with_exclamation("yash")
print_with_exclamation("python")
	
def print_sum(x , y):
	print(x + y)
	print(x + y)
print_sum(5,6 )

#returning from function 
def max( x ,y):
	if x >= y:
		return x
	else:
		return y
print(max(4,7))
z = max(8,5)
print(z)

def add_no(x ,y):
	total = x +y
	return total
	print("this won/'t be printed")
print(add_no(4,5))

def print_nums(x):
	for i in range(x):
		print(i)
		return
print_nums(10)

def func(x):
	res = 0
	for i in range(x):
		res += i
	return res
print(func(4))