import numpy as np

x = "my name is girish"
y = "from ralegan"
i = np.char.add(x,y)
print(i)
x = np.char.lower(x)
print(x)
x = np.char.upper(x)
print(x)
a = np.char.center(x,30,fillchar="♥")
print(a)
x = np.char.split(x)
print(x)
x = np.char.splitlines("my name is girish /n ftom ralegan")
print(x)
x = np.sin(180*np.pi/180)
print(x)
x1 = "hello"
x2 = "world"

x = np.char.equal(x1,x2)
print(x)
x = np.char.count(x,"l")
print(x)
x = np.char.find(x,"e")
print(x)
x = np.char.join([":","/"],x,y)
print(x)