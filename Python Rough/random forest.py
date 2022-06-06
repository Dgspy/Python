from sklearn.datasets import make_circles
from sklearn.model_selection import Kfold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import numpy as np

x,y = make_circles(noise=0.2,factor=0.5,random_state=1)

kf = Kfold(n_splits = 5,shuffle = True,random_state = 1)
lr_scores=[]
rf_scores=[]
for train_index,test_index in kf.split(x):
	x_train,x_test=x[train_index],x[test_index]
	y_train,y_test=y[train_index],y[test_index]
	lr = LogisticRegression(solver='lbfgs')
	lr.fit(x_train,y_train)
	lr_score.append(lr.score(x_test,y_test))
	rf = RandomForestClassifier(n_estimators=100)
	rf.fit(x_train,y_train)
	rf_score.append(rf.score(x_test,y_test))
print('Lr accuracy:',np.mean(lr_score))
print('Rf accuracy:',np.mean(rf_score))