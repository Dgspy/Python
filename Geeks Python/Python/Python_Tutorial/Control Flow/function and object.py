import itertools
def simplegenerator():
    yield 1
    yield 2
    yield 3
for i in simplegenerator():
    print(i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
def simplegenerator():
    yield 1
    yield 2
    yield 3
x = simplegenerator()
n = iter(x)
print(n.__next__())
print(n.__next__())
print(n.__next__())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
def fib(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b,a+b
x = fib(5)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
for i in fib(5):
    print(i)