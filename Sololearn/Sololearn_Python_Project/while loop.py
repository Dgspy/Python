
i = 1
while i <=5:
    print(i)
    i = i + 1
print("finished!")

i = 3
while i>=0:
    print(i)
    i = i - 1

x = 1
while x < 10:
  if x%2 == 0:
    print(str(x) + "is even")
  else :
    print(str(x) + "is odd")
    
  x += 1


words = ["YASH", "GIRISH", "ONKAR",
"SARVESH"]
for word in words:
  print(word)

str = "testing for loops"
count = 0
for x in str:
  if(x == 't'):
    count +- 1
print(count)

list = [2,3,4,5,6,7]
for x in list:
  if(x%2 == 1 and x > 4):
    print(x)
    break 

i = 0
while True:
    print(i)
    i = i+1
    if i <= 5:
       print("breaking")
       break
print("finished")

i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
      print("skipping 3")
      continue 
      
words = ["cat","dog","cow","monkey"]
for x in words:
  print("animals:",x)

for item in range(1,10,1):
  print("item:",item)
  
for i in range(1,10,1):
  for j in range(1,(i+1),1):
    print(j,"",end="")
  print("")

for item in range(1,10,1):
  if item==6:
    break
  print("item:",item)
  
for item in range(1,10,1):
  if item==6:
    continue 
  print("item:",item)
  
for item in range(1,10,1):
  if item==6:
    pass
  else:
    print("item:",item)
    
a = 0
while(a<10):a+=1;print("value is :",a)
  

x = 10
for i in range(x):
  for j in range(5,i-1,-1):
    print("*",end = "")
  print("")
