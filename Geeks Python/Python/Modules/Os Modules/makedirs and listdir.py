
import os
directory = "mylove"
parent_dir = "D:/python project/darknet king pin/authors"
path = os.path.join(directory ,parent_dir)
os.makedirs(path)
print("directory '% s 'created" % directory)
print("........................................................................................................................")
import os
directory = "yash"
parent_dir = "D:/pycharm projects/girish/a/b"
mode = 0o666
path = os.path.join(parent_dir,directory)
os.makedirs(path , mode)
print("directory '% s ' created" % directory)

print("........................................................................................................................")
import os 
 
# Get the list of all files and directories 
# in the root directory 

path = "/"

dir_list = os.listdir(path) 
 

print("Files and directories in '", path, "' :") 
 
# print the list 

print(dir_list) 