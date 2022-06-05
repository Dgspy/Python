try:
   print("hello")
   print(1/0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("this code will run no matter what")


try:
   nums1 = 7
   nums2 = 0
   print(nums1/nums2)
   print("Done calculation")
except ZeroDivisionError:
   print("an error occurred")
   print("due to Zero Division")

name = input()
friend = ("Girish","yash","sarvesh","omkar")
if name in friend:
    print("found")
else:
    print("not found")

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()