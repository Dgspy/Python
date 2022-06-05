import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()


data = [15, 16, 18, 19, 22, 24, 29, 30, 34]
x = pd.DataFrame(data)
print(x.quantile([0.25,0.75,0.5,1]))
c = np.percentile(data,50)
a = np.percentile(data,25)
b = np.percentile(data,75)
print('25 percent:',a,'50 percent:',b,'75 percent:',c)

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
print(df)
x = df['Sex']=='female'
print(x)
print(df[['Pclass','Sex','Survived']].head(n=10))
#print(df['Fare']) mi
#print(df['Fare'].values)
print(df[['Pclass','Sex','Survived']].values)
print("")
x = (df[['Pclass','Sex','Survived']].values)
print(x[0,:])

#plt.scatter(df['Age'],df['Fare'],c = df['Pclass'],marker = "*")
#plt.plot([80,5],[0,85])
#plt.savefig('plt.png')
#plt.show()

df['male']=df['Sex']=='male'
x = df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y = df['Survived'].values
model.fit(x,y)
#print(x)
#print(y)
#print(model.predict([[3, True, 22.0, 1, 0, 7.25]])) 
#print(model.predict(x[:5])) 
#print(y[:5]) 
model.fit(x,y)
y_pred = model.predict(x)
print((y == y_pred).sum())
print((y == y_pred).sum()/y.shape[0])
print(model.score(x,y))

a = df[['Fare','Age']].values 
b = df['Survived'].values
model.fit(a,b)
print(model.coef_,model.intercept_)

print("accuracy:",accuracy_score(y,y_pred))
print("precision:",precision_score(y,y_pred))
print("recall:",recall_score(y,y_pred))
print("f1 score:",f1_score(y,y_pred))
print("confusion matrix:",confusion_matrix(y,y_pred))

x_train,y_train,x_test,y_test=train_test_split(x,y)
print("whole dataset:", x.shape, y.shape)
print("training set:", x_train.shape, y_train.shape)
print("test set:", x_test.shape, y_test.shape)

from sklearn.metrics import recall_score
sensitivity_score = recall_score
print(sensitivity_score(y, y_pred)) 

from sklearn.metrics import precision_recall_fscore_support
print(precision_recall_fscore_support(y, y_pred))

def specificity_score(y, y_pred):
    p, r, f, s = precision_recall_fscore_support(y, y_pred)
    return r[0]
print(specificity_score(y, y_pred)) 

