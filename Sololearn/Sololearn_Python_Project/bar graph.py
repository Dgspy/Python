import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


data = {'month':[1,2,3,4,5,6,7,8],'cases':[12,34,56,65,4,14,55,47]}
df = pd.DataFrame(data)
print(df)
x = pd.DataFrame([12,34,56,65,4,14,55,47])
y = pd.DataFrame([1,2,3,4,5,6,7,8])
x.plot(kind='bar',stacked = True,width = 0.5,color = "b" ,edgecolor = "y" ,linewidth = 5,alpha = 0.9,linestyle = "--",label = "cases",visible = True)
y.plot(kind='barh',stacked = True,width = 0.5,color = "r" ,edgecolor = "m" ,linewidth = 5,alpha = 0.9,linestyle = "--",label = "months",visible = True)
plt.style.use('ggplot')
plt.title("data",fontsize = 18)
plt.xlabel("month",fontsize = 15)
plt.ylabel("cases",fontsize = 15)
plt.xlabel("month")
plt.legend("sing")
plt.savefig('plt.png')
plt.show()