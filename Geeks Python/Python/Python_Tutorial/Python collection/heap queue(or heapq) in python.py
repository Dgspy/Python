import heapq
li = [1,2,3,4,5]
heapq.heapify(li)
print("the created heap is ::",list(li))
heapq.heappush(li,6)
print("the modify list after pust is::",list(li))
print("the popped and smallest element is::",heapq.heappop(li))
print("........................................................................................................................")

l = [1,4,3,1,5]
l1 = [1,4,3,1,5]
heapq.heapify(l)
heapq.heapify(l1)
print("heapq.heappushpop item using::",heapq.heappushpop(l,2))
print("heapq.heapreplace() item using::",heapq.heapreplace(l,2))
print("........................................................................................................................")
l = [1,2,3,4,5,6,7,8]
heapq.heapify(l)
print("the 3 largest number in list are::",heapq.nlargest(3,l))
print("the 3 smallest element in the list::",heapq.nsmallest(3,l))