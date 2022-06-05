
for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else:
   print("Unbroken 2")

try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)
try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)


#if statement
print("~~|`♥`|~~")

num = 3
if num == 1:
 print("one")
elif num == 2:
 print("two")
elif num == 3:
 print("three")
else:
 print("something else")

num = 5
if num >2:
    print("two")
    if num >3:
        print("one")
        
num = 12
if num >= 5:
    print("wellcome")
    if num <= 42:
       print("rocky bhai")

x = 5
if x<10:
  print('positive number')
  if x%2==0:
    print('even number')
  else:
    print('odd number')
elif x<0:
  print('negative number')
else:
  print('zero')

n = 23
if n<10:
  print([i**2 for i in range(100)])
elif n>10:
  print('Nan',"=",'not a number')
else:
  print([i**3 for i in range(100)])
