import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import nor
x=sns.load_dataset("tips")
sns.distplot(x['total_bill'],hist_kws={'color':"b",'edgecolor':'r',"linestyle":"--","alpha":0.5,"linewidth":3},fit=norm)
plt.show()
