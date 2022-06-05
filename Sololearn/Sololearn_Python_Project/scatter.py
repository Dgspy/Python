import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
boston_dataset = load_boston()
import pandas as pd
boston = pd.DataFrame(boston_dataset.data, 
columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target
print(boston.corr())

boston.plot(kind = "scatter",x = "MEDV",y = "RM" ,figsize = (5,10),smarker = "*" ,color = "b")
plt.savefig('plt.png')
plt.show()


