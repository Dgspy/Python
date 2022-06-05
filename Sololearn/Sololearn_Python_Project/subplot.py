import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style .use('ggplot')

x = np.arange(1,11)
a = x*2
b = x*3
plt.subplot(1,2,1)
plt.plot(x,a,color = "g",linestyle = "--",linewidth = 5)
plt.subplot(1,2,2)
plt.plot(x,b,color = "r",linestyle = ":",linewidth = 7)
plt.grid()
plt.savefig("plt.png")
plt.show()

