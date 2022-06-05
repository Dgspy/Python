# os. name
import os
print(os.name)
print("........................................................................................................................")
# os.error
import os
try:
    filename = "d2oi.txt"
    f = open(filename,"rU")
    text = f.read()
    f.close()
except IOError:
    print("problem reading:" + filename)
print("........................................................................................................................")
# os.popen
import os
fd = "girish.txt"
file = open(fd, 'w')
file.write('hello girish')
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
file = os.popen(fd, 'w')
file.write("hello girish")
print("........................................................................................................................")
#os.ciose()
import os
fd = "girish.txt"
file = open(fd, 'r')
text = file.read()
print(text)
#os.close(file)
#Note: The same error may not be thrown, due to the non-existent file or permission privilege.

print("........................................................................................................................")
#os.rename()
"""
import os
fd = "girish.txt"
os.rename(fd,'new.txt')
os.rename(fd,'new.txt')
#A file name “GFG.txt” exists, thus when os.rename() is used the first time, the file gets renamed. Upon calling the function os.rename() second time, file “New.txt” exists and not “GFG.txt” thus Python throws FileNotFoundError.
"""
print("........................................................................................................................")
# remove file
import os
os.remove("girish.txt")
print("........................................................................................................................")
# os.path.exists()
import os
result = os.path.exists("girish.txt")
print(result)
#As in the above code, the file does not exist it will give output False. If the file exists it will give us output True. 
print("........................................................................................................................")
#os.path.getsize()
import os
size = os.path.getsize("girish.txt")
print("size of the file is ",size,"bytes.")

import os
girish = "hii am a girish"
d = os.path.getsize("girish")
print(d)