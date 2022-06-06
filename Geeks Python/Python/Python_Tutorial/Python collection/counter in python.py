from collections import Counter
print(Counter(['A','A','A','B','C','A','B','B','A','C']))
print(Counter({'A':3,'B':5,'C':7}))
print(Counter(A = 3,b = 5,c = 7))
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

from collections import Counter
c = Counter()
c.update([1,2,3,4,5,6,7,8])
print(c)
c.update([1,2,4])
print(c)
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
from collections import Counter
c = Counter(A = 4,B = 3,C = 10)
s = Counter(A = 10,B = 3,C = 4)
c.subtract(s)
print(c)
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

from collections import Counter
z = ['blue','red','violet','yellow','blue','red']
print(Counter(z))