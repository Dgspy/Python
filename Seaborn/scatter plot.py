import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(16,9))
titanic = sns.load_dataset("titanic")
sns.scatterplot(x="age",y="fare",data=titanic,hue = 'sex',style='who',size='who',sizes=(50,200))
plt.show()