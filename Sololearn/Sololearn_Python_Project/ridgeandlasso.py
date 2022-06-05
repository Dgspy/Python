from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size = 0.3)
from sklearn.linear_model import Ridge, Lasso
rd = Ridge()
rd.fit(x_train,y_train)
print(rd.score(x_test,y_test))
ls = Lasso()
ls.fit(x_train,y_train)
print(ls.score(x_test,y_test))
rdg = Ridge(alpha = 2)
rdg.fit(x_train,y_train)
print(rdg.score(x_test,y_test))
lsg = Lasso(alpha = 3)
lsg.fit(x_train,y_train)
print(lsg.score(x_test,y_test))