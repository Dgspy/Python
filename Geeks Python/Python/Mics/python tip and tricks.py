# 1. In-Place Swapping Of Two Numbers.
x , y = 10 ,20
print(x,y)
x,y = y, x
print(x,y)
#2. Reversing a string in Python
a = "darkside of the nature"
print("reverse is ::=",a[::-1])
print(".......................................................................................................................")
#3. Create a single string from all the elements in list
a = ["girish","machhindra","unde"]
print(a)
print("  ".join(a))
print("........................................................................................................................")
#4. Chaining Of Comparison Operators.
n = 10
result = 1 < n < 20
print(result)
result = 1 > n <= 9
print(result)
print(".......................................................................................................................")
#4. Print The File Path Of Imported Modules
import os
import math 
import socket
print(math)
print(socket)
print(os)
print(".......................................................................................................................")
#5. Use Of Enums In Python.
class name:
    girish ,machhindra ,unde = range(3)
print(name.girish)
print(name.machhindra)
print(name.unde)
print(".......................................................................................................................")
# 6. Return Multiple Values From Functions.
def x():
    return 1,2,3,4
a,b,c,d = x()
print(a,b,c,d)
print(".......................................................................................................................")
# 7. Find The Most Frequent Value In A List.
test = [1,2,3,4,2,3,3,1,2,3,2,4,3,2,3]
print(max(set(test), key = test.count))
print(".......................................................................................................................")
# 8. Check The Memory Usage Of An Object.
import sys
x = "girish machhindra unde"
print(sys.getsizeof(x))
print(".......................................................................................................................")
# 9. Print string N times.
n = 10
a = "girishisthewhitedevil"
c = (a * n)
print(".......................................................................................................................")
# 10. Checking if two words are anagrams
from collections import Counter
def anagram(str,str2):
    return Counter(str) == Counter(str2)
def anagram(str,str2):
    return sorted(str) == sorted(str2)
print(anagram("giri","rigi"))
print(anagram("girish","d2oi"))
