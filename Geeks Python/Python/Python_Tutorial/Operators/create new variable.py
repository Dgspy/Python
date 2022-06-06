a = 10
print("id of a ::",id(10),"value::",a)
print(id(47))
print()

a = 10 # Assigning value to variable creats new object
print(" id of a : ", id(a) ," Value : ", a )

a = a + 10 # Modifying value of variable creats new object
print(" id of a : ", id(a) ," Value : ", a )

a += 10 # Modifying value of variable creats new object
print(" id of a : ", id(a) ," Value : ", a )

print()

a = [0, 1] # stores this array in memory and assign its reference to a
print("id of a: ",id(a) , "Value : ", a )

a = a + [2, 3] # this will also behave same store data in memory and assign ref. to variable
print("id of a: ",id(a) , "Value : ", a )

a += [4, 5]
print("id of a: ",id(a) , "Value : ", a )

#But now this will now create new ref. instead this will modify the current object so
# all the other variable pointing to a will also gets changes
print()

list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4] # modifying value in current reference

print(list1)
print(list2) # as on line 4 it modify the value without creating new object
			# variable list2 which is pointing to list1 gets changes
print()

list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [1, 2, 3, 4]

# Contents of list1 are same as above
# program, but contents of list2 are
# different.
print(list1)
print(list2)
