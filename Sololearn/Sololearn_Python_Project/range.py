

numbers = list(range(1,11))
print(numbers)
print("")
numbers = list(range(3,8))
print(numbers)
print(range(20) == range(0,20))

# in range 5,20 there is gap of 2
numbers = list(range(5,20,2))
print(numbers)

for i in range(5):
  print("hello!")

list = [1,1,2,3,5,8,15]
print(list[list[4]])

for i in range(20):
  print("Girish","Yash")

x = 78
y = 67
def yash():
  x = 5
  y = 10
  print("(x,y)(",x,",",y,")")
yash()
print("Global x :",x)
print("Local y :",y)