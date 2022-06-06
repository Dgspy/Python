def shout(text):
	return text.upper()
print(shout("hello"))
yell = shout
print(yell("hello"))

print("~~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~~~~~")

def shout(text):
	return text.upper()
def whisper(text):
	return text.lower()
def greet(fun):
	greeting = fun("""hii i am created a wonder project in a Famous Standency with the Formal Aldehide""")
	print(greeting)
greet(shout)
greet(whisper)

print("~~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~~~~~")

def create(x):
	def add(y):
		return x+y
	return add
add_15 = create(15)
print(add_15(10))