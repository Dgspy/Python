import numpy as np
import matplotlib.pyplot as plt
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
a = heights[3] = 180
print(a)
data = heights
x = np.array(data)
print(x.shape)
x = 0
for height in heights:
  if height < 188:
    x += 1
    print(x)

x = np.array(heights)
print((x > 188).sum())

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]
g = heights + ages
a = np.array(g)
print(a)
data = heights + ages
x = np.array(data)
print(x[0:3])
print(x[:3])
print(x[3])
print(x[-3:]<50)
print(x[-3:]>50)
print(x[-3:]==50)
print((x[1:]>50).sum())

print(a.dtype)
ages = [57, 61, 57, 57, 58.0, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 6.9, 64, 46, 54, 47, 70]
x = np.array(ages)
print(x.dtype)

x = np.array(heights).reshape(45,1)
print(x)
y = np.array(ages).reshape(45,1)
print(y)
c = np.concatenate((x,y),axis = 1)
print(c)
d = np.concatenate((x,y),axis = 0)
h = (d[-6],245)
print(h)
height_age = x + y
print(height_age.sum())
print(x[:,0]*0.0328084)
print(x[:,0]/100)
print(x[:,0]*10)

mask = height_age[:,0]>=182
print(mask.sum())