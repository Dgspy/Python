from scipy import cluster
from scipy import special
#help(cluster)
import scipy
#scipy.info(cluster )
#scipy.source(cluster)
from scipy import integrate
i = scipy.integrate.quad(lambda x:special.exp10(x),0,1)
print(i)
e = lambda x,y:x*y**2
f = lambda x:1
g = lambda x:-1
print(integrate.dblquad(e,0,2,f,g))
from scipy.fftpack import fft,ifft
import numpy as np
x = np.array([1,2,3,4])
a = fft(x)
print(a)
from scipy import linalg
a = np.array([[1,2],[4,7]])
x = linalg.inv(a)
print(x)

i = special.exp10(10)
v = special.exp2(2)
print(i,v)
import matplotlib.pyplot as plt
from scipy import interpolate
x = np.arange(5,20)
y = np.exp(x/3.0)
g = interpolate.interp1d(x,y)
x1 = np.arange(6,12)
y1 = g(x1)
plt.plot(x,y,"*",x1,y1,"--",color ="b")
plt.savefig('plt.png')
plt.show()