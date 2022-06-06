def eo(x):
    if(x % 2 == 0):
        print("Even")
    else:
        print("Odd")
print(eo.__doc__)
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
#the return statement
def square(num):
    return num ** 2
print(square(2))
print(square(5))
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
def myfun(x):
    x[0] = 20
l1 = [10,20,30,40,50]
myfun(l1)
print(l1)
print()
def myfun(x):
    x = [20,30,40]
l1 = [10,11,12,13,14,15]
myfun(l1)
print(l1)
print()
def myfun(x):
    x = 20
x = 10
print(x)
myfun(20)
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
def swap(x,y):
    temp = x
    x = y
    y = temp
x = 2
y = 3
swap(x,y)
print(swap(5,5))
print(x)
print(y)