import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

df['male']=df['Sex']=='male'
x = df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y = df['Survived'].values
model.fit(x,y)
x_train,x_test,y_train,y_test=train_test_split(x,y)
y_pred = model.predict(x_test)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
print("accuracy:{0:.5f}".format(accuracy_score(y_test,y_pred)))
print("precision:{0:.5f}".format(precision_score(y_test,y_pred)))
print("recall:{0:.5f}".format(recall_score(y_test,y_pred)))
print("f1_score:{0:.5f}".format(f1_score(y_test,y_pred)))
print(confusion_matrix(y_test,y_pred))

a = 132+53/131+53+17+21
print(a)