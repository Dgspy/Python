import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(16,9))
titanic = sns.load_dataset("titanic")
sns.scatterplot(x="age",y="fare",data=titanic)
sns.lineplot(x="age",y="fare",data=titanic)
sns.barplot(x="age",y="fare",data=titanic)

plt.show()