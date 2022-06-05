import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
boston_dataset = load_boston()
import pandas as pd
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target
print(boston)
print(boston.shape)
print(boston.columns)
print(boston.head())
print(boston.tail())
print(boston.describe())
print(boston.corr())

boston.hist(column = "CHAS",color = "r")
plt.savefig('plt.png')
plt.show()


boston.hist(column = "LSTAT",color = "b")
plt.savefig('plt.png')
plt.show()

X=(1,2,3,4,5)
Y=(2,5,9,1,5)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=1)

print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)