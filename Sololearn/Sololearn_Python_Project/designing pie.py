import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize =(4,3))
colors = ['r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w',]
labels = np.ones(20)
plt.pie([1],colors = "k",radius = 2.05)
plt.pie(labels,colors = colors,radius = 2.0)
plt.pie([1],colors = "g",radius = 1.8)
plt.pie([1],colors = "y",radius = 1.6)
plt.pie([1],colors = "c",radius = 1.3)
plt.pie([1],colors = "b",radius = 1.2)
plt.pie([1],colors = "m",radius = 0.9)
plt.pie([1],colors = "b",radius = 0.31)
plt.pie(labels,colors = colors,radius = 0.3)
plt.pie([1],colors = "w",radius = 0.2)
plt.pie([1],colors = "k",radius = 0.1)
plt.savefig('plt.png')
plt.show()