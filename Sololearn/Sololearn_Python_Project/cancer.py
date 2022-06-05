
import pandas as pd
from sklearn.datasets import load_breast_cancer
g = load_breast_cancer()
#print(g.keys())
#print(g['DESCR'])
x = g['data']
y = g['target']
a = g['feature_names']
print(x.shape)
print(y.shape)
print(a.shape)
df = pd.DataFrame(x,
columns = a)
df['target']=y
print(df.head())
from sklearn.linear_model import LogisticRegression
p = df[g.feature_names].values
m = df['target'].values
model = LogisticRegression(solver = 'liblinear')
model.fit(p,m)
print("prediction for datapoint 0:",model.predict([x[0]]))
print(model.score(p,m))