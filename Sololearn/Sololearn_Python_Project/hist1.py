import matplotlib.pyplot as plt
import numpy as np
import random

a = np.random.randint(18,45,(100))
b = np.random.randint(15,440,(100))
print(a)
print(b)

plt.hist(a,bins = 15,rwidth = 20,histtype = "bar",orientation = "horizontal",color = "m")
plt.hist(b,bins = 15,rwidth = 20,histtype = "bar",orientation = "vertical",color = "y")
plt.xlabel = ("girish")
plt.title = ("names")
plt.ylabel = ("sirish")
plt.legend()
plt.savefig('plt.png')
plt.show()