import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
t=sns.load_dataset("tips")
kwargs={'alpha':0.9,"linestyle":":","edgecolor":"b","linewidth":5,'errwidth':3,'capsize':0.3}
sns.barplot(x = "day",y="total_bill",hue="sex",data=t,**kwargs)
plt.show()
