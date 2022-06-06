# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
	print(a, b, c, d)

# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)

print(" ")

# Error when len(args) != no of actual arguments
# required by the function

args = [0, 1, 4, 9]


def func(a, b, c):
	return a + b + c


# calling function with unpacking args
func(*args)
# it gives error argument