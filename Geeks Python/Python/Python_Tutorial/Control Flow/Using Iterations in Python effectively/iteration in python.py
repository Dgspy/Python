# A C-style way of accessing list elements
cars = ["Aston", "Audi", "McLaren"]
i = 0
while (i < len(cars)):
	print(cars[i])
	i += 1
print()

# Accessing items using for-in loop

cars = ["Aston", "Audi", "McLaren"]
for x in cars:
	print(x)
print()

# Accessing items using indexes and for-in

cars = ["Aston", "Audi", "McLaren"]
for i in range(len(cars)):
	print(cars[i])
print()

# Accessing items using enumerate()

cars = ["Aston" , "Audi", "McLaren "]
for i, x in enumerate(cars):
	print (x)
print()

# Accessing items and indexes enumerate()

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars):
	print (x[0], x[1])
print()
# Printing return value of enumerate()

cars = ["Aston" , "Audi", "McLaren "]
print(enumerate(cars))
print()

# demonstrating the use of start in enumerate

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars, start=1):
	print (x[0], x[1])
