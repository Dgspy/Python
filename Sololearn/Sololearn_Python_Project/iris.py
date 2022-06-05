from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
iris = load_iris()
x = iris['data'][:,3:]
y = (iris['target']==2).astype(np.int)
#print(list(iris.keys()))
#print(iris['data'].shape)
#print(iris['target'].shape)
#print(iris['DESCR'])
clf = LogisticRegression()
clf.fit(x,y)
clf1 = clf.predict(([[1.0]]))
print(clf1)
new = np.linspace(0,3,1000).reshape(-1,1)
#print(new)
proba = clf.predict_proba(new)
#print(proba)
plt.plot(new,proba[:,1],"g-")
plt.title("virginaca")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend("new_proba")
plt.savefig('plt.png')
plt.show()

