import itertools
print("printing the number repeatedly:")
print(list(itertools.repeat(143,15)))
print("\n")
from itertools import product
print("use a cartesian product::")
print(list(product([1,2],repeat = 2)))
print()
print(list(product(["darknet","king","ping"],"2")))
print()
print(list(product(["AB",[143,15]])))
print("\n")

from itertools import permutations
print(list(permutations([1,"yash"],2)))
print()
print(list(permutations("AB")))
print()
print(list(permutations(range(5),2)))
#print(list(permutations("@$#@ Unde")))
print("\n")

from itertools import combinations
print(list(combinations(['A',3],3)))
print()
print(list(combinations('AB',2)))
print()
print(list(combinations(range(2),1)))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^*^^^^^^^^^^^^")
from itertools import combinations_with_replacement
print(list(combinations_with_replacement("AB",2)))
print()
print(list(combinations_with_replacement([1,2],2)))
print()
print(list(combinations_with_replacement(range(2),1)))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

import itertools
import operator
list1 = [1,2,3,4]
print(list(itertools.accumulate(list1)))
print()
print(list(itertools.accumulate(list1,operator.mul)))
print()
print("addition:",list(itertools.accumulate(list1,operator.add)))
print()
print(list(itertools.accumulate(list1,operator.sub)))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

l = [1,2,3,4]
l1 = [5,6,7,8]
l2 = [9,10,11,12]
l3 = [l,l1,l2]
print(l3)
print()
print(list(itertools.chain.from_iterable(l3)))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

print(list(itertools.compress("DEVILPINGIRISH",[1,0,1,0,0,1,0,0,1,0,0,0,0])))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

import itertools
a = [1,2,3,4,5,6,7,8]
print(list(itertools.dropwhile(lambda x : x % 2 == 0,a)))
print()
print(list(itertools.filterfalse(lambda x : x % 2 == 0,a)))
print()
print(list(itertools.takewhile(lambda x : x % 2 == 0,a)))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

b = [2,4,6,8,10,12,14,16,18,20]
print(list(itertools.islice(b,1,6,2)))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

li = [(1,2,3),(4,5,6),(7,8,9)]
print(list(itertools.starmap(min,li)))
print()
print(list(itertools.starmap(max,li)))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

a = [1,2,3,4,5,6,7,8]
iti = iter(a)
it = itertools.tee(iti,3)
for i in range(0,3):
    print(list(it[i]))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

print(*(itertools.zip_longest("darkdevil","internet",fillvalue = '_')))
