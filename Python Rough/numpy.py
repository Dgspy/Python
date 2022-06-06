import numpy as np

x = np.arange(1,7).reshape(3,2)
print(x)

z = np.arange(0,10)
print(z[2:])
print(z[5:])
print(z[:2])
print(z[-3:])
print(z[z>4])
print(z[(z<5)&(z%2==0)])
print(z.sum())

x = np.arange(0,20)
y = x*2
print(y)
print(x.mean())
print(x.std())
print(np.median(x))

x = np.array([1,2,3])

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 

print(x.ndim)

print(x.size) 

print(x.shape) 
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 

print(x[1][2])

A = np.array([[3, 2, 1], [10, 5, 16], [7, 8, 9]])
B = np.array([[19, 11, 15], [13, 16, 12], [13, 41, 11]])
print(A*B)

i = np.array([1,1,1])
print(i)

i = np.ones([10])
print(i)

i = np.zeros([10])
print(i)
#show random value ,dtype = bool
i = np.empty([3])
print(i)

i = [1,2,3]
x = np.random.random(1)
print(x)
x = np.random.randint(1,4)
print(x)
x = np.random.randint(1,4,(2,4,4))
print(x)
x = np.random.rand(3,3)
print(x)
x = np.random.randn(3,3)
print(x)
x = np.random.choice(3)
for i in range(5):
    print(np.random.choice(3))
x = np.random.seed(1)
print(x)

