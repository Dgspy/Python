# Literal 9 is an object
b = 9

# Reference count of object 9
# becomes 0.
b = 4
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
def create_cycle():

	# create a list x
	x = [ ]

	# A reference cycle is created
	# here as x contains reference to
	# to self.
	x.append(x)

create_cycle()
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
x = []
x.append(1)
x.append(2)

# delete the list from memory or
# assigning object x to None(Null)
del x
# x = None
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#Automatic Garbage Collection of Cycles
import gc
print("garbage collection thresholds:",gc.get_threshold())

print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#Manual Garbage Collection
import gc
collected = gc.collect()
print("garbage collecter: collected","%d objects." % collected)
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")

def create():
	x = {}
	x[i+1] = x
	print(x)
collected = gc.collect()
print("garbage collecter: collected","%d objects." % (collected))
print("creating cycle .............")
for i in range(10):
	create()
collected = gc.collect()
print("garbage collecter: collected","%d objects." % collected)