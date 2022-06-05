
def max( x, y):
    if x >= y:
       return x
    else:
       return y
print(max(4,7))
z = max( 8,5 )
print(z)

def add_numbers(x,y):
  total = x + y
  return total
  print("this won't be printed")
print(add_numbers(4,5)) 

            #COMMENT

x = 365
y = 7
# it is a comment

print(x%y)

             #docstring

def shout(word):
  """ 
  print a word with a
  excamation mark following it
  """
  print(word + "!")
print("girish")

def welcome():
  print("welcome to python")
welcome()

def sq(x):
  print(x**2)
sq(2)
sq(4775)

def power(x,n):
  print(x**n)
power(2,6)
power(2,7)

def myfun():
  return 1,2,3
a,b,c=myfun()
print('a=',a)

def sum(a,b):
  print("a=",a)
  print("b=",b)
  
sum(b=3,a=7)

def mass(a=3,b=6):
  print("sum =",a+b)
  print("a=",a)
  print("b=",b)
mass()

def addition(a,b):
  return a + b
def subtraction(a,b):
  return a - b
def division(a,b):
  return a / b
def multiplication(a,b):
  return a * b
c= addition(10,20)
print("Add is :",c)
c= subtraction(10,20)
print("sub is :",c)