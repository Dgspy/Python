#path of file (os.getcwd())
import os
cwd = os.getcwd()
print("current working directory::",cwd)
print("........................................................................................................................")
# changing dirictory (os.chdir())
import os
def current_path():
    print("current working directory before ::",os.getcwd())
    print()
current_path()
os.chdir('../../..')
current_path()
print("........................................................................................................................")
#make directory (os.mkdir()) , (os.makedirs())
#Python program to explain os.mkdir() method 
 
# importing os module 

import os 
 
# Directory 

directory = "GeeksforGeeks"
 
# Parent Directory path 

parent_dir = "D:/Pycharm projects/"
 
# Path 

path = os.path.join(parent_dir, directory) 
 
# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
os.mkdir(path) 

print("Directory '% s' created" % directory) 
 
# Directory 

directory = "Geeks"
 
# Parent Directory path 

parent_dir = "D:/Pycharm projects"
 
# mode 

mode = 0o666
 
# Path 

path = os.path.join(parent_dir, directory) 
 
# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
# with mode 0o666 
os.mkdir(path, mode) 

print("Directory '% s' created" % directory)