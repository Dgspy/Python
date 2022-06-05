# Try multiple coding approaches
#slower
dict = {'g':1,'i':2,'r':3,'i':4,'r':5,'h':6}
word = "machhindra unde"
for i in word:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1
print(dict)
# faster
dict = {'g':1,'i':2,'r':3,'i':4,'r':5,'h':6}
word = "machhindra unde"
for i in word:
    try:
        dict[i] += 1
    except KeyError:
        dict[i] = 1
print(dict)
print("........................................................................................................................")
#Use xrange instead of range
x = [i for i in range(0,10,2)]
print(x)
print("........................................................................................................................")
#Use Python multiple assignment to swap variables
# slower
x = 2
y = 5
z = x
x = y
y = z
print(x,y)
# faster
x , y = 3,5
y,x = x,y
print(x,y)
# Use local variable if possible
print("........................................................................................................................")
class test:
    def fun(self,x):
        print(x + x)
o = test()
mytest = o.fun
n = 2
for i in range(n):
    mytest(i)