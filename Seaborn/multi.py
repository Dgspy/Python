import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import norm
x=sns.load_dataset("tips")
sns.distplot(x['total_bill'],fit=norm,bins=9,label="total_bill")
sns.distplot(x['tip'],fit=norm,bins=9,label="tip")
sns.distplot(x['size'],fit=norm,bins=9,label="size")
plt.show()
