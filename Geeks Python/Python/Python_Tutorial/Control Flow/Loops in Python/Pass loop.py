# An empty loop
for letter in 'geeksforgeeks':
	pass
print('Last Letter :', letter)

#examples
print()
# A simple for loop example

fruits = ["apple", "orange", "kiwi"]
for fruit in fruits:
    print(fruit)
    
fruits = ["apple", "orange", "kiwi"]

# Creating an iterator object
# from that iterable i.e fruits
iter_obj = iter(fruits)

# Infinite while loop
while True:
    try:
	
    	# getting the next item
    	fruit = next(iter_obj)
    	print(fruit)
    except StopIteration:
		
    	# if StopIteration is raised,
	    # break from loop
	    break



