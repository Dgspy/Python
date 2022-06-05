from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV 
import matplotlib.pyplot as plt
import pandas as pd

X,y = load_boston(return_X_y=True)

pipe = Pipeline([
    ("scale",StandardScaler()),
    ("model",KNeighborsRegressor(n_neighbors = 1))
])
pipe.get_params()
mod = GridSearchCV(estimator=pipe,
                   param_grid={'model__n_neighbors':[1,2,3,4,5,6,7,8,9,10]},
                   cv=3)
mod.fit(X,y);
x = pd.DataFrame(mod.cv_results_)
print(x)
print(load_boston()['DESCR'])
