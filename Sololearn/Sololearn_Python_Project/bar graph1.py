import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(11)
print(x)

x = pd.Series([10,9,8,7,6,5,4,3,2,1])
x.plot(kind='barh')
plt.savefig('plt.png')
plt.show()

x=[1,2,3,4,5]
y=[5,10,15,20,25]
plt.bar(x,y,tick_label=tick_label,width=0.9)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Bar Graph")
plt.savefig("graph.png")
print(plt.show())