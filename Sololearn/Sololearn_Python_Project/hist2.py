import matplotlib.pyplot as plt

data = [1,2,3,4,5,6,7,8,9]
plt.hist(data,color = "r",bins = 4)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("histogram")
plt.grid(True)
plt.savefig('plt.png')
plt.show()