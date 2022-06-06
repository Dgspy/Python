from collections import OrderedDict
print("this is a dict:\n")
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4
for key,value in d.items():
	print(key,value)
print("this is an ordered dictionary:\n")
o = OrderedDict()
o["a"] = 1
o["b"] = 2
o["c"] = 3
o["d"] = 4
for key,value in o.items():
	print(key,value)
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
# A Python program to demonstrate working of key
# value change in OrderedDict
from collections import OrderedDict
print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
    print(key, value)
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

print("Before deleting:\n")

od = OrderedDict()

od['a'] = 1

od['b'] = 2

od['c'] = 3

od['d'] = 4
 

for key, value in od.items():

    print(key, value)
 

print("\nAfter deleting:\n")

od.pop('c')

for key, value in od.items():

    print(key, value)
 

print("\nAfter re-inserting:\n")

od['c'] = 3

for key, value in od.items():

    print(key, value)