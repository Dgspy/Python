# This function uses global variable s
def f():
	print("Inside Function", s)

# Global scope
s = "I love you"
f()
print("Outside Function", s)

# This function has a variable with
# name same as s.
def f():
	s = "Me too."
	print(s)

# Global scope
s = "I love Geeksforgeeks"
f()
print(s)

# This function uses global variable s
def f():
	s += 'GFG'
	print("Inside Function", s)

# Global scope
s = "I love Geeksforgeeks"
f()
