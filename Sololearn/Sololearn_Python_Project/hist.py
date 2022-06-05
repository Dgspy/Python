import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import style

a = np.random.randint(18,450,(100))
b = np.random.randint(15,440,(100))
print(a)
print(b)

style.use("ggplot")
plt.figure(figsize = (20,20))
plt.hist([a,b],bins = 15,rwidth = 20,histtype = "bar",color = ["m","y"],label = ["a","b"])
plt.xlabel("girish")
plt.title("names")
plt.ylabel("sirish")
plt.grid(color = "r")
plt.legend()
plt.savefig('plt.png')
plt.show()