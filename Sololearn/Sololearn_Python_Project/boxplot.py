import matplotlib.pyplot as plt

a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,6,5,4,7,8,9]
c = [9,8,7,1,2,3,6,5,4]
data = list([a,b,c])
plt.boxplot(data)
plt.violinplot(data,showmedians = True)
plt.savefig('plt.png')
plt.show()

