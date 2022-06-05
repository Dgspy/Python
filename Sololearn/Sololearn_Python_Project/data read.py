import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as png

x = np.random.randint(1,456,50)
plt.plot(x)
plt.savefig("plt.png")
img = png.imread("plt.png")
print(img)
print(x.shape)
print(x.ndim)