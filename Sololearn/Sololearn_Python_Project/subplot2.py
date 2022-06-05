import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from matplotlib import style

plt.subplot(3,3,1)

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


plt.subplot(3,3,2)

x = ["python","R","machine learning","artificial intellegence","data science"]
y = [45,15,35,25,30]
z = [0.1,0.1,0.1,0.1,0.1]
a = ["c","b","r","y","g"]
b = {"fontsize":14}
c = {"linewidth":4,"width":2,"edgecolor":"k"}
plt.pie(y,labels = x,explode = z,colors = a,autopct = '%0.2f%%',shadow = True ,radius = 1.2,startangle = 140,textprops = b,counterclock = True,wedgeprops = c,center = (2,2),frame = False,labeldistance = 1.4,rotatelabels = True)
plt.legend()


plt.subplot(3,3,3)

x = np.random.randint(15,440,(100))
y = np.random.randint(65,578,(100))
z = np.random.randint(98,658,(100))
plt.scatter(x,y,c = "b",marker = "*",s = 200,alpha = 0.5,linewidth = 7,edgecolor = "y")
plt.scatter(x,z,c = "r",marker = "+",s = 200,alpha = 0.5,linewidth = 7,edgecolor = "m")
plt.title('random')
plt.xlabel('randint')
plt.ylabel('randfloat')




plt.subplot(3,3,4)

a = np.random.randint(18,450,(100))
b = np.random.randint(15,440,(100))

style.use("ggplot")
plt.hist([a,b],bins = 15,rwidth = 20,histtype = "bar",color = ["m","y"],label = ["a","b"])
plt.xlabel("girish")
plt.title("names")
plt.ylabel("sirish")
plt.grid(color = "r")
plt.legend()

plt.subplot(3,3,5)
a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,6,5,4,7,8,9]
c = [9,8,7,1,2,3,6,5,4]
data = list([a,b,c])
plt.boxplot(data)
plt.violinplot(data,showmedians = True)


plt.subplot(3,3,6,projection = "polar",facecolor = "k")

plt.savefig('plt.png')
plt.show()