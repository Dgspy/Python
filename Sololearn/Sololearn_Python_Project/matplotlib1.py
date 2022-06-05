import pandas as pd
import matplotlib.pyplot as plt

x = pd.Series([10,9,8,7,6,5,4,3,2,1])
x.plot(kind='bar')
plt.savefig('plt.png')
print(x.plot())

x = pd.Series([x**3 for x in range(11)])
x.plot(kind='box')
plt.savefig('plt.png')
print(x.plot())

x = pd.Series([1,2,3,4,5,6,7,8,9,10])
x.plot(kind='hist')
plt.savefig('plt.png')
print(x.plot())

x = pd.Series([1,2,3,4,3,2,1,2,3,4])
x.plot(kind='line')
plt.savefig('plt.png')
print(x.plot())


x = pd.Series([i**2 for i in range(11)])
x.plot(kind='area')
plt.savefig('plt.png')
print(x.plot())


x = pd.Series([i**2 for i in range(11)])
x.plot(kind='pie')
plt.savefig('plt.png')
print(x.plot())


