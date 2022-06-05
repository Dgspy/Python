print( "list iteration::")
l = ["darknet","king","ping"]
for i in l:
    print(i)
    
print( "\n tuple iteration::")
t = ("darknet","king","ping")
for i in t:
    print(i)
    
print( "\nstring iteration::")
s = "darknet king ping"
for i in s:
    print(i)
       
print( "\ndictionary iteration::")
d = dict()
d['abc']=123
d['xyz']=456
for i in d:
    print("%s %d"%(i,d[i]))
    
    