import time
start  = time.time()
s = "girish"
U = []
for i in s:
    U.append(i.upper())
print(U)
stop = time.time()
e = stop - start
print("time spent in function is:",e)
s = "girish"
start = time.time()
U = map(str.upper,s)
print(U)
stop = time.time() 
e1 = stop - start
print("time spent in built in function::",e1)
print(".......................................................................................................................")
from collections import deque
s = "girish"
d = deque(s)
d.append('y')
d.appendleft('i')
print(d)
d.pop()
d.popleft()
print(d)
print(list(reversed(d)))
print(".......................................................................................................................")
import itertools
iter = itertools.permutations([1,2,3])
print(list(iter))
print(".......................................................................................................................")
list = [1,-3,6,11,4]
list.sort()
print(list)
g = "darknetkingpin"
g = sorted(g)
print(len(g))
print(g)
print(".......................................................................................................................")
