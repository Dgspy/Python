import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
x = np.linspace(1,5,12).reshape(4,3)
y = np.array([['yash','yzprag','girish'],['omkar','sarvesh','vaibhav'],['sqrqzq','dcsgs','fsggs'],['fsgdy','ystth','hstsgh']])
sns.heatmap(x,vmin=0,vmax=21,cmap="coolwarm",annot=y,fmt="s")

plt.show()