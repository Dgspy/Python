import matplotlib.pyplot as plt

fruit = ['apple','orange','mango','gauva']
quality = [67,35,100,56]
plt.pie(quality,labels = fruit,autopct = '%0.1f%%',colors = ['red','orange','yellow','green'],radius = 1.5)
plt.pie([1],colors = ['w'],radius = 0.5)
plt.savefig('plt.png')
plt.show()
plt.pie([40,30,20])
plt.savefig("pie_char",dpi = 1000,quality = 99,facecolor = "g")