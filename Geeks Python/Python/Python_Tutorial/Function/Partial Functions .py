from functools import partial
def f(a,b,c,x):
    return 1000*a + 100*b +10*c + 1*x
g = partial(f,3,1,4)
print(g(5))
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
from functools import *
def add(a,b,c):
    return 100*a +10 * b +c
ad = partial(add,c = 2,b = 1)
print(ad(3))