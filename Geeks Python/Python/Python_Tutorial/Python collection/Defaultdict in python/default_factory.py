#default factory
from collections import defaultdict
d = defaultdict(lambda :"not present")
d["a"] = 1
d["b"] = 2
print(d["a"])
print(d["b"])
print(d["c"])
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

#__missing__()
d = defaultdict(lambda :"not present")
d["a"] = 1
d["b"] = 2
print(d.__missing__('a'))
print(d.__missing__('b'))
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

#default_factory
d = defaultdict(list)
for i in range(5):
	d[i].append(i)
print(d)
print("  ")
d = defaultdict(int)
l = [1,2,3,4,5,6,7,8]
for i in l:
	d[i] += 2
print(d)
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
