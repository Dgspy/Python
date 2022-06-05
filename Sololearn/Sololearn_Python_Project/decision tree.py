from sklearn.datasets import load_breast_cancer
bc = load_breast_cancer()
x = bc['data']
y = bc['target']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2020)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='gini')
model.fit(x_train,y_train)
print(model.score(x_test,y_test))
model1 = DecisionTreeClassifier(criterion='entropy')
model1.fit(x_train,y_train)
print(model1.score(x_test,y_test))
from sklearn.preprocessing import StandardScaler
s = StandardScaler()
s.fit(x_train)
x_train_s = s.transform(x_train)
x_test_s = s.transform(x_test)
model2 = DecisionTreeClassifier(criterion='gini')
model2.fit(x_train_s,y_train)
print(model2.score(x_test,y_test))

print("***************+++++++++++****************")

import pandas as pd
from sklearn.datasets import load_iris
i = load_iris()
x = i['data']
y = i['target']
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2020)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(criterion='mse')
model.fit(x_train,y_train)
print(model.score(x_test,y_test))
pred = model.predict(x_test)
print(pred)
print(y_test)

print("")
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
iris = load_iris()
x = iris.data
y = iris.target
print(x,y)
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state = 22)
model = DecisionTreeClassifier()
model.fit(x,y)
print(model.predict([[3,True,29,4.28]]))

