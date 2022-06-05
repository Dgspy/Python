# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]

# Single dictionary holds prices of cars and
# its accessories.
# First three items store prices of cars and
# next two items store prices of accessories.
prices = {1:"570000$", 2:"68000$", 3:"450000$",
		4:"8900$", 5:"4500$"}

# Printing prices of cars
for index, c in enumerate(cars, start=1):
	print("Car: %s Price: %s"%(c, prices[index]))

# Printing prices of accessories
for index, a in enumerate(accessories,start=1):
	print("Accessory: %s Price: %s"\
		%(a,prices[index+len(cars)]))
print()

# Python program to demonstrate unzip (reverse
# of zip)using * with zip function

# Unzip lists
l1,l2 = zip(*[('Aston', 'GPS'),
			('Audi', 'Car Repair'),
			('McLaren', 'Dolby sound kit')
		])

# Printing unzipped lists	
print(l1)
print(l2)
print()

# Python program to demonstrate the working of zip

# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit",
			"Dolby sound kit"]

# Combining lists and printing
for c, a in zip(cars, accessories):
	print("Car: %s, Accessory required: %s"\
		%(c, a))
