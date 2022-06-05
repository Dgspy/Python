import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

a = pd.Series([1,2,3],index = ('a','b','c'))
print(a)
b = pd.Series({1:'a',2:'b',3:'c'})
print(b)

import pandas as pd
presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')

#print(presidents_df )
print(presidents_df.shape)
print(presidents_df.head(10))
print(presidents_df.tail(10))
print(presidents_df.info())

print(presidents_df.loc["George Washington"])
print(presidents_df.iloc[15:18])
print(presidents_df['age'].median())
print(presidents_df['age'].mean())
print(presidents_df['age'].quantile([0.25,0.5,0.75,1]))
print(presidents_df['age'].min())
print(presidents_df['age'].max())

print(presidents_df.std())
print(presidents_df.var())
print(presidents_df.describe())

print(presidents_df.groupby('party').mean())
print(presidents_df.groupby('party')['height'].agg(['min',np.median,max]))

plt.plot(presidents_df['height'],linestyle = "--",color = "b")
plt.plot(presidents_df['age'],linestyle = "--",color = "r")
plt.xlabel('height')
plt.ylabel('age')
plt.legend('president')
plt.title('president',size = 20)
plt.savefig('plt.png')
plt.show()
