import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
boston_dataset = load_boston()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

x = pd.DataFrame(boston_dataset.data,  columns=boston_dataset.feature_names)
x['MEDV'] = boston_dataset.target
X = x['RM']
Y = x['MEDV']
print(x.shape)

 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=1)
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

model = LinearRegression()
model.fit(X_train,Y_train)
model.intercept_.round(2)
model.coef_.round(2)

new_RM = np.array([6.5]).reshape(-1,1)
model.predict(new_RM)
model.intercept_+model.coef_*6.5
Y_test_predict=model.predict(X_test)
print(Y_test_predict.shapetype(Y_test_predict))
print(Y_test.shape)

plt.scatter(X_test,Y_test ,label='testing data')
plt.plot(X_test,Y_test_predict,label='prediction',linewidth=3)
plt.savefig('plt.png')
plt.show()






















