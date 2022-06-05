import pandas as pd
import matplotlib.pyplot as plt

x=[1,2,3,5,6,72,56,84,5,6,4,58,2,58,45,86,55,52,55,58,4,5]
y=[5,10,15,20,58,2,58,55,58,4,5,45,65,45,86,55,52,55,58,4,5,25]
z=[3,11,17,58,2,58,45,86,55,52,55,58,4,5,45,25,56,42,8,47,52,65]
plt.subplot(1,2,1)
plt.scatter(x,y,marker ="*",color = "g",s = 90)
plt.subplot(1,2,2)
plt.scatter(x,z,marker ="<",color = "r",s = 90)
plt.savefig('plt.png')
print(plt.show())