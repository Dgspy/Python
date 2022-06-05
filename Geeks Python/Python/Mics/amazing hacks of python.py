print("........................................................................................................................")
list1 = ['girish','yash','omkar','sarvesh']
print("simple list :-:",list1)
print('list by using join method:%s' % ','.join(list1))
print("directory applied the join method ::",(" , ".join(list1)))
print("........................................................................................................................")
friends = ['girish','yash','mohit','gurunath','sarvesh','onkar','pratik','ganesh','pradip','aditya','mukund','prajwal']
partition = list(zip (*[iter(friends)] * 2))
print (partition)
print("........................................................................................................................")
# Printing more than one list’s items simultaneously 
list2 = [1,2,3,4,5,6]
list1 = [7,8,9,1,2,3]
for a,b in zip(list2,list1):
    print(a,b)
print("........................................................................................................................")
# Take the string as input and convert it into the list:
format = list(map(int,input().split()))
print(format)#1 2 3 4 5 6 7 8
print("........................................................................................................................")
# Convert the list of list into a single list
import itertools
num = [[1,2],[3,4],[6,7],[8,9]]
lst = list(itertools.chain.from_iterable(num))
print(lst)
print("........................................................................................................................")
# Printing the repeated characters:
print("G" + "i"*5 + "r" *2 +"i" +"s"*3 +"h")