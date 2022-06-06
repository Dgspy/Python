import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
x = load_breast_cancer()
bc=pd.DataFrame(np.c_[x['data'],x['target']],columns=np.append(x['feature_names'],['target']))
print(bc)
sns.pairplot(bc)
#plt.show()