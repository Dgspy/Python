from collections import ChainMap
d = {'a':1,'b':2}
d1 = {'c':3,'d':4}
d2 = {'e':5,'f':6}
c = ChainMap(d,d1,d2)
print(c)
print("........................................................................................................................")
dict = {'a':1,'b':2}
dict1 = {'c':3,'d':4}
chain = ChainMap(dict,dict1)
print("print chainmap containt is ::",chain.maps)
print("all key of chain map is ::",list(chain.keys()))
print("all values in chain map::",list(chain.values()))
print("........................................................................................................................")

dict = {'a':1,'b':2}
dict1 = {'c':3,'d':4}
dict2 = {'e':5}
chain = ChainMap(dict,dict1,dict2)
print("print chainmap containt is ::",chain.maps)
chain1 = chain.new_child(dict2)
print("displaying new chainmap::",chain1.maps)
print(chain1['b'])
chain1.maps = reversed(chain1.maps)
print(chain1['b'])