set1 = set(["geeks","for","geeks"])
print(set1)

for i in set1:
    print(i,end=" ")
print("\ngeeks" in set1)

set1 = set([1,2,3,4,5,6,7,8,9])
print(set1)
set1.remove(5)
set1.remove(6)
print("\nset remove element by remove method",set1)
set1.discard(7)
set1.discard(9)
print("\nset remove element by discard element",set1)

for i in range(1,5):
    set1.remove(i)
print("\nset remove with help of iterator method::",set1)

set2 = set([1,2,3,4,5,6,7,8,9,10])
print("\nset2::",set2)
set2.pop()
print("\nremove element with help of poop  method",set2)

set3 = set([1,2,3,4,5])
print("\nset3 element::",set1)
set1.clear()
print("\nSet after clearing all the elements::",set1)

string = ('g','i','r','i','s','h','u','n','d','e')
fset = frozenset(string)
print("\nfrozenset is::",fset)
print("\nempty frozenset ::",frozenset())