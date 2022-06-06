from collections import UserDict
d = {'a':1, 'b':2, 'c':3}
user = UserDict(d)
print(user.data)
user = UserDict()
print(user.data)
print("........................................................................................................................")

class dict(UserDict):
    def __del__(self):
        raise RuntimeError("deletion not allowed")
    def pop(self,s = None):
        raise RuntimeError("deletion not allowed")
    def popitem(self,s = None):
        raise RuntimeError("deletion not allowed")
d = dict({'a':1, 'b':2, 'c':3})
print("original dictionary::",d)
d.pop(1)