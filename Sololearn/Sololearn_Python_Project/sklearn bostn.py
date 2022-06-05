from sklearn.datasets import load_boston
boston_dataset = load_boston()
import matplotlib.pyplot as plt



import pandas as pd
x = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
x['MEDV'] = boston_dataset.target

print(x.shape)
print(x.columns)
print(x[['CHAS','MEDV','RM','CRIM','INDUS']].head())
print(x['MEDV'].describe())

#x.hist(column="CHAS")
#x.hist(column="MEDV",color = "b",grid = False)
#plt.savefig('plt.png')
#plt.show()

print(x.corr().round(2))


plt.subplot(1,2,1)
x.plot(kind = 'scatter',x = 'RM',y = 'MEDV',figsize = (8,6))

plt.subplot(1,2,2)
x.plot(kind = 'scatter',x = 'INDUS',y = 'MEDV',figsize = (8,6))
plt.savefig('plt.png')

plt.show()