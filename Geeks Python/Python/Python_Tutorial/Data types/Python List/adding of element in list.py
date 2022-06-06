#adding the list element
#create the list 
list = []
print("blank list::",list)

#add a element
list.append(1)
list.append(4)
list.append(3)
list.append(0)
print("add element display::",list)

#adding element to the list by using iterator
for i in range(1,5):
    list.append(i)
print("iterator list element",list)
    
#adding tuple to the list
list.append((5,6))
print("tuple element::",list)

#adding of list to list
list.append(["darkdevil","of","internet"])
print("list to list",list)

#use insert method
#create list 
list1 = [1,2,3,4,5]
#adding elementin list with insert method
list1.insert(3,12)
list1.insert[1,10)
print("list of inserting::",list)

#create a list
list2 = [1,2,3,4]
#use extend method
list2.extend([4,"I","love","U"])
print("extend method::",list2)