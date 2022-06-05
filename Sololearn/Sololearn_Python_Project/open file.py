# Open a file
data = open("data.txt", "wb")
print ("Name of the file: ", data.name)
print ("Closed or not : ", data.closed)
print ("Opening mode : ", data.mode)
data.close()  #closed data.txt file

# Open a file
data = open("data.txt", "w")
data.write("Welcome to ApkZube's Python Tutorial")
print("done")
data.close()

# Open a file
data = open("data.txt", "r+")
file_data = data.read(18) # read 18 byte only
full_data = data.read() #read all byte into file from last cursor
print(file_data)
print(full_data)
data.close()

# Open a file
data = open("data.txt", "r+")
file_data = data.read(18) # read 18 byte only
print("current position after reading 18 byte :",data.tell())
data.seek(0) #here current position set to 0 (starting of file)
full_data = data.read() #read all byte
print(file_data)
print(full_data)
print("position after reading file : ",data.tell())
data.close()

import os
os.rename('data.txt','my_data.txt')

import os
os.remove('my_data.txt')

import os
os.mkdir('apkzube')

import os
# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")

import os
print(os.getcwd(my_data.txt))

import os
# This would remove "/home/apkzube" directory.
os.rmdir( "/home/apkzube" )

file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

a = open("hello.txt","w")
a.write("My name is girish")
a.close()

a = open("hello.txt","r")
print(a.read())
a.close()

a = open("hello.txt","w")
a.write(str(2+2*3))
a.close()

a = open("hello.txt","r")
print(a.read())
a.close()
