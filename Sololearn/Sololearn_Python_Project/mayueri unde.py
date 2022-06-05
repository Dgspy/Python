import matplotlib.pyplot as plt
import numpy as np
import random

x = np.random.randint(15,440,(50))
y = np.random.randint(65,578,(50))
z = np.random.randint(98,658,(50))

plt.scatter(x,y,c = "b",marker = "*",s = 300,alpha = 0.9,linewidth = 7,edgecolor = "y")
plt.scatter(x,z,c = "r",marker = "+",s = 300,alpha = 0.9,linewidth = 7,edgecolor = "m")
plt.title('random')
plt.xlabel('randint')
plt.ylabel('randfloat')
plt.savefig('plt.png')
plt.show()