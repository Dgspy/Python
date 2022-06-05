import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

plt.subplot(2,2,1)

X,y = load_boston(return_X_y=True)
mod = LinearRegression()
LinearRegression()
mod = KNeighborsRegressor().fit(X,y)
pipe = Pipeline([
    ("scale",StandardScaler()),
    ("model",KNeighborsRegressor(n_neighbors=1))
])
pipe.fit(X,y)
Pipeline(steps=[('scale',StandardScaler()),('model',KNeighborsRegressor())])
pred = pipe.predict(X)
plt.scatter(pred,y,marker="*",color="r")

plt.subplot(2,2,2)

X,y = load_boston(return_X_y=True)
mod = LinearRegression()
LinearRegression()
mod = KNeighborsRegressor().fit(X,y)
pipe = Pipeline([
    ("scale",StandardScaler()),
    ("model",KNeighborsRegressor())
])
pipe.fit(X,y)
Pipeline(steps=[('scale',StandardScaler()),('model',KNeighborsRegressor())])
pred = pipe.predict(X)
plt.scatter(pred,y,marker="*",color="r")

plt.savefig('plt.png')
plt.show()