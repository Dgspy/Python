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

x = np.linspace(1,10,1000)
print(x)

x = 23
y = 12
x = np.add(x,y)
print(x)
x = np.multiply(x,y)
print(x)
x = np.divide(x,y)
print(x)

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
print(x.argmin)
print("explain:",np.exp(x))
print("login:",np.log(x))
print("logout:",np.log10(x))
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],ndmin = 1) 
print(x[1][2])
x = np.sqrt(25)
print(x)
i = 16
print("square:",np.sqrt(i))

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


x = [1,2,3,45,6,4,8,9,5]
a = np.array(x)
print(a)
a = np.ones(10)
print(a)
a = np.zeros(10)
print(a)
a = np.full((2,2),7)
print(a)
a = np.eye(2,2)
print(a)
dt = np.dtype(np.int32)
print(dt)
dt = np.dtype([('age',np.int8)])
print(dt)
x = (20)
a = np.arange(x).reshape(4,5)
print(a)
b = np.ravel(a)
print(b)
c = np.transpose(a)
print(c)
c = np.array(a)

a = np.array([2,2,4,5,6,7,8],ndmin=10)
print(a)


x = np.sin(180)
print(x)
x = np.sin(90)
print(x)
x = np.cos(180)
print(x)
x = np.tan(180)
print(x)
i = np.arange(0,3*np.pi,0.1)
print(i)
a = np.sin(i)
print(a)


x = np.array([15, 16, 18, 19, 22, 24, 29, 30, 34])
print(x.shape)
print(x.size)
print(x.mean())
print(x.sum())
print(x.std())
print(x.var())
x = 207
y = 9
i = np.divide(x,y)
print(i)

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]
print("mean:",np.mean(data))
print("median:",np.median(data))
print("50th percentile(median):",np. percentile(data,50))
print("25th percentile(median):",np. percentile(data,25))
print("75th percentile(median):",np. percentile(data,75))
print("standard deviation:",np.std(data))
print("vatiance:",np.var(data))











