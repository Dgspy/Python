import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
bc = load_breast_cancer()
x = bc.data
y = bc.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size = 0.3,random_state=33)
print(x_train.shape) 
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
from sklearn.neighbors import KNeighborsRegressor
knr = KNeighborsRegressor(n_neighbors=8)
knr.fit(x_train,y_train)
print(knr.score(x_test,y_test))
print("")
print("♥♥classifier♥♥")

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
bc = load_breast_cancer()
x = bc.data
y = bc.target
z = bc.feature_names
w = bc.target_names
#print(x,y,z,w)
df = pd.DataFrame(np.c_[x,y],columns=[list(z)+['target']])
x = df.iloc[:,0:-1]
y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2020)
from sklearn.neighbors import KNeighborsClassifier
knc = KNeighborsClassifier()
knc.fit(x_train,y_train)
y_pred = knc.predict(x_test)
print(knc.score(x_test,y_test))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
print((45+61)/(45+61+5+3))
pa = np.linspace(1,5,30)
pac = np.array([pa])
#print(pac)
pred = knc.predict(pac)
print(pred)
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,pred)
rmse = np.sqrt(mse)
print(rmse)
print(mse)
from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))



