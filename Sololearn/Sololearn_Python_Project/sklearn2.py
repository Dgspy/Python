from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

X,y = load_boston(return_X_y=True)
print(X,y)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
mod = LinearRegression()
print(mod.fit(X,y))
LinearRegression()
print(mod.predict(X))
mod = KNeighborsRegressor().fit(X,y)
pred = mod.predict(X)
print("✓♥♥✓")
import matplotlib.pyplot as plt
plt.scatter(pred,y)
plt.savefig('plt.png')
plt.show()