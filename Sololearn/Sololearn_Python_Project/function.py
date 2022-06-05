def multiply(x , y):
   return x*y
a = 4
b = 7
operation = multiply
print(operation(a , b))

from math import pi
print(pi)
from math import pi ,sqrt
from math import sqrt as square_root
print(square_root(100))
from math import sqrt as multiply 
print(multiply(100))

def my_func():
  print("girish")
  print("machhindra")
  print("unde")
my_func()

def hello():
  print("hello world!")
hello()
hello()
hello()

def print_with_exclamation(word):
   print(word + "!")
print_with_exclamation("girish")
print_with_exclamation("yash")
print_with_exclamation("sarvesh")

def sum_twice(x,y,a,b):
  print(a + b)
  print(x + y)
sum_twice(5,12,3,5)

def max(x,y):
    if x >= y:
      return x
    else:
      return y
print(max(4,6))
z = (6,8)
print(z)

print("{0}{1}{0}".format("unde","girish"))


def factorial(x):
  if x == 1:
    return 1
  else:
    return x * factorial(x-1)
print(factorial(5))
def is_even(x):
  if x == 0:
    return true
  else:
    return is_odd(x-1)
def is_odd(x):
  return not is_even(x)
  

def countdown():
  i = 5
  while i > 0:
    yield i
    i -= 1
for i in countdown():
  print(i)

def nums(x):
  for i in range(x):
    if i % 2 == 0:
      yield i
print(list(nums(11)))


def test(func,arg):
 return func(func(arg))

def mult(x):
  return x*x
print(test(mult,2))


def power(x,y):
 if y == 0:
   return 1
 else:
   return x*power(x,y-1)
print(power(2,3))



def apply_twice(func,arg):
   return func(func(arg))
def add_five(x):
   return x + 5
print(apply_twice(add_five,10))


def polynomial(x):
  return x**2 + 5* + 4
print(polynomial(-4))
 #name vs lambdas
print((lambda x : x**2 + 5 + 4 )(-4))


def function(name_arg,*args):
  print(name_arg)
  print(args)
function(1,2,3,4,5)

def my_func(x,y = 7 ,*args ,**kwargs):
  print(kwargs)
my_func(2,3,4,5,6,a=7,b=8)