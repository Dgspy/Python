from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import numpy as np
a = np.array(['low','low','high','medium']).reshape(-1,1)
print(a)
print(a.dtype)
x = OneHotEncoder(sparse = False)
print(x.fit_transform(a))

X,y = load_boston(return_X_y=True)
print(X,y)
mod = LinearRegression()
print(mod.fit(X,y))
LinearRegression()
print(mod.predict(X))
mod = KNeighborsRegressor().fit(X,y)
pipe = Pipeline([
    ("scale",StandardScaler()),
    ("model",KNeighborsRegressor())
])
pipe.fit(X,y)
Pipeline(steps=[('scale',StandardScaler()),('model',KNeighborsRegressor())])
pred = pipe.predict(X)
print("✓♥♥✓")
plt.scatter(pred,y,marker="*",color="r")
plt.savefig('plt.png')
plt.show()s