import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
x = df[['Age', 'Fare']].values[:6]
y = df['Survived'].values[:6]
kf = KFold(n_splits=3, shuffle=True)
for train,test in kf.split(x):
    print(train,test)
splits = list(kf.split(x))
first_split = splits[0]
print(first_split)
train_indices, test_indices = first_split
print("training set indices:", train_indices)
print("test set indices:", test_indices)
x_train = x[train_indices]
x_test = x[test_indices]
y_train = y[train_indices]
y_test = y[test_indices]
print("x_train",x_train)
print("y_train", y_train)
print("x_test",x_test)
print("y_test", y_test)

df['male']=df['Sex']=='male'
x = df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y = df['Survived'].values
kf = KFold(n_splits=5, shuffle=True)
x_train = x[train_indices]
x_test = x[test_indices]
y_train = y[train_indices]
y_test = y[test_indices]
model = LogisticRegression()
model.fit(x_train,y_train)
print("score:",model.score(x_test,y_test))

scores = []
kf = KFold(n_splits=5, shuffle=True)
for train_index, test_index in kf.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model = LogisticRegression()
    model.fit(x_train, y_train)
    scores.append(model.score(x_test, y_test))
print(scores)
print(np.mean(scores))

x1 = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
x2 = df[['Pclass', 'male', 'Age']].values
x3 = df[['Fare', 'Age']].values
y = df['Survived'].values

print("log reg with all feature:")
score_model(x1,y,kf)

print("log reg with pclass,sex & age feature:")
score_model(x2,y,kf)

print("log reg with fare & age feature:")
score_model(x3,y,kf)


