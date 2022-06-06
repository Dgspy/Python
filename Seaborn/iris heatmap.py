import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
x = load_iris()
df = pd.DataFrame(np.c_[x['data'],x['target']],columns=np.append(x['feature_names'],['target']))
ax = sns.heatmap(df.corr(),annot=True,linewidth=3)
ax.tick_params(size=10,color='w',labelsize=10,labelcolor='w')
plt.show()