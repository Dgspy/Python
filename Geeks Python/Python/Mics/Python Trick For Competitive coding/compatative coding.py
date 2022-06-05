#The most_common function of the Counter Package. 
from collections import Counter
arr = [1,2,3,4,5,4,5,3,5,4,4,3,3,5,5,6,7,9,9,9,8]
counter = Counter(arr)
top = counter.most_common(3)
print(top)
print("........................................................................................................................")
#The n-largest/n-smallest function of the heapq Package. 
import heapq
grades = [100,23,35,75,79,75,86]
print(heapq.nlargest(3,grades))
print(heapq.nsmallest(4,grades))
print("........................................................................................................................")
#Dictionary and concept of zipping Dictionaries 
import heapq
stocks = {"google":1502.12,"yahoo":234.33,"tesla":150000,"amazon":762.43}
zips = zip(stocks.values(),stocks.keys())
print(sorted(zips))
zips = zip(stocks.keys(),stocks.values())
print(sorted(zips))