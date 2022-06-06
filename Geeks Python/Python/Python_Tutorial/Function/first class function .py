def shout(text):
    return text.upper()
print(shout("hello"))
yell = shout
print(yell("hello"))
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
def shout(text):
    return text.lower()
def devil(text):
    return text.upper()
def greet(fun):
    greeting = fun(""" HI, I am created by a function passed as an argument>""")
    print(greeting)
greet(shout)
greet(devil)
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
def create(x):
    def adder(y):
        return x +y
    return adder
add = create(15)
print(add(10))