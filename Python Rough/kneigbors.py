from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
x = iris.data
y = iris.target
print(x[0],y[0])
model = KNeighborsClassifier()
model.fit(x,y)
y_pred = model.predict([[31,1,1,1]])
print(y_pred)