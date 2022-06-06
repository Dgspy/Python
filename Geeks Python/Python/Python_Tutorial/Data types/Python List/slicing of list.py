#slicing of list
list = ["D","E","V","I","L","P","I","N","G"]
print(list)
print("slice from 1 to 5::",list[0:5])
print("slice from 5::",list[5:])
print("slice back 5::",list[-5:])
print("printing all element using slice operator::", list[:])

# Creating a List
List = ['G', 'E', 'E', 'K', 'S', 'F',
		'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)

# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

# Print elements of a range
# using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)
