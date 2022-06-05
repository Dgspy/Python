g = "darkdevil of internet"
list = " "
for i in g:
    list = list + i
print(list)
gt = "darknet king pin"
list = " ".join([i for i in g])
print(list)
# better way to iterate range
even = [i for i in range(10) if i % 2 == 0]
print(even)
# less faster
i = 0
even = []
while i < 10:
    if i % 2 == 0:
        i += 1
        print(i)
# slow
v = "machhindra"
g = "girish" + v + "unde"
print(g)
#fast
g = "girish %s unde " % v
print(g)
print("girish unde")
