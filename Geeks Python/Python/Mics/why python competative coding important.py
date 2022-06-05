arr = [10,20,34,57,75,86,90,95,95,95,100]
print("maximum no ::",max(arr))
print("minimum no ::",min(arr))
print("the sorted array is::",sorted(arr))
print("number of occurreces95 is::",arr.count(95))
print(".......................................................................................................................")
arr = [00,11,22,33,44,55,77,88,99]
print("original array::",arr)
del arr[5]
print("after delet index 5::",arr)
arr.remove(22)
print("after removing 22::",arr)
arr[-1] = "A Random Number"
print(arr)
k = arr[:2]
print(k)
print(".......................................................................................................................")
def multiply(*arr):
    k1 = arr[0]
    k2 = arr[1]
    return k1,k2
a,b = multiply(11,22)
print(a,'  ',b)
a,b = multiply(55,66,77,88,99)
print(a, '  ',b)
print(".......................................................................................................................")
arr = [1,2,3,4,5,6,7,8,9]
if 3 in arr:
    print("Yes")
else:
    print("No")
for i in arr:
    print(i,end=" ")
    
print(".......................................................................................................................")
a = {'a','b','c','d','e','a'}
print(a)
dict = {'Name':'Girish','Age':16,'Class':'Eleventh'}
print("dict[Name]:: ",dict['Name'])
print("dict['Age']::",dict["Age"])
print(".......................................................................................................................")
arr = [str(a) for a in input().strip().split("  ")]# girish
print(arr)
print(".......................................................................................................................")
arr = [int(a) for a in input().strip().split("  ")]# 43
print(arr)