import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
bc = load_breast_cancer()
a = bc['data']
b = bc['target']
c = bc['feature_names']
df = pd.DataFrame(np.c_[a,b],columns = [list(c)+['target']])
print(df.head())
x = df.iloc[:,0:-1]
y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2020)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100,criterion='gini')
model.fit(x_train,y_train)
print(model.score(x_test,y_test))


import pandas as pd
from sklearn.datasets import load_digits
d = load_digits()
x = d['data']
y = d['target']
print(x.shape)
print(y.shape)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2020)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100,criterion='mse')
model.fit(x_train,y_train)
print(model.score(x_test,y_test))

model1 = RandomForestRegressor(n_estimators=50,criterion='mse')
model1.fit(x_train,y_train)
print(model1.score(x_test,y_test))

