
My_Boolean=True
print(My_Boolean)
print(1==2)
print("hello"=="hello")
print(11!=5)
print(11!=11)
print("hello"!="hello")
print(10<=10)
print(9>=5)
print(7>=7.0)


print("♠♠♪♥♥")

print('true' == 'true' and 'false')
print('true' =='false' and 'false')

grade = 78
if (grade >=75 and grade <=100):
   print("passed!")


print(3 == 3 and 1 == 1)
print(2 == 2 and 4 == 5)
print(5 < 2 or 3 > 4)
print( 5 > 7 and 5 < 7)


import re
pattern = r"Girish"
if re.match(pattern,"GirishGirishGirish"):
   print("false")
else:
   print("true")

nums = {
  1:"one",
  2:"two",
  3:"three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

num_set = [1,2,3,4,5,6]
print(3 in num_set)

list = [1,2,3,4,5,6,9,]
x = 5
c = 7
print(x in list)
print(c in list)
print(x not in list)
