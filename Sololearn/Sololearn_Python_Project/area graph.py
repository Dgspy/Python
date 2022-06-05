import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import style

style = ("ggplot")

x = pd.Series([x**3 for x in range(10)])
x.plot(kind='area')
plt.savefig('plt.png')
print(x.plot())
x=pd.Series([1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,29,21,22,23,24,25])
x.plot(kind='pie')
plt.savefig('plt.png')
print(x.plot())