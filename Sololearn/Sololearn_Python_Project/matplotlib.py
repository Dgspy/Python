import matplotlib.pyplot as plt

x = ["python","R","machine learning","artificial intellegence","data science"]
y = [45,15,35,25,30]
z = [0.1,0.1,0.1,0.1,0.1]
a = ["c","b","r","y","g"]
b = {"fontsize":14}
c = {"linewidth":4,"width":2,"edgecolor":"k"}
plt.pie(y,labels = x,explode = z,colors = a,autopct = '%0.2f%%',shadow = True ,radius = 1.2,startangle = 140,textprops = b,counterclock = True,wedgeprops = c,center = (2,2),frame = False,labeldistance = 1.4,rotatelabels = True)
plt.legend()
plt.savefig('plt.png')
plt.show()


