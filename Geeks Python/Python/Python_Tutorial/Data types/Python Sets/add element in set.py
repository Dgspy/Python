set1 = set()
print("blank set",set1)

set1.add(1)
set1.add(4)
set1.add(3)
set1.add((1,5))
print("\nadd a no in set::",set1)

for i in range(1,6):
    set1.add(i)
print("set create using iterator::",set1)

set2 = set([1,2,34,5,6,7,8,9,0])
set2.update(["girish",143])
print("create set using update method::",set2)
