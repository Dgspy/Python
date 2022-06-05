from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
iris = load_iris()
x ,y = iris.data,iris.target
x1,y1 = x[:,:2],y
#print(x1,y1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state=33)
print(x_train.shape,x_test.shape,y_train.shape,y_test.shape )
model = StandardScaler().fit(x_train)
x_train = model.transform(x_train)
x_test = model.transform(x_test)
print(x_train,x_test)