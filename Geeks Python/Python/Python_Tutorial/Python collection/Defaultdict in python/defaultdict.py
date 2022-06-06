dict = {1 : 'girish',2: 'machhindra' ,3 :'unde'}
print(dict)
print(dict[1])
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
from collections import defaultdict
def value():
	return "not present"
d = defaultdict(value)
d["a"] = 1
d["b"] = 2
print(d["a"])
print(d["b"])
print(d["c"])