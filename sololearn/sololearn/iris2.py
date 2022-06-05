from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
print(x_train.shape)
print(y_test.shape)
print(x_train.shape)
print(y_test.shape)
from sklearn.datasets import load_digits
digit = load_digits()
a = digit.data
y = digit.target
print(x,y)

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
clf = RandomForestClassifier(random_state=0)
x = [[1,2,3],[11,12,13]]
y = [0,1]
print(clf.fit(x,y))

print(clf.predict(x))
print(clf.predict([[4, 5, 6], [14, 15, 16]]))
x=[[0,15],[1,-10]]
print(StandardScaler().fit(x).transform(x))