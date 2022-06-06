#creating a tuples
t1=()
print("\ncreate a empty tuple::",t1) 

t2 = ("girish","unde")
print("\nt2 with string::",t2)

t3 = ([1,2,3,4,5,6,7,8,9])
print("\nt3 with a list ::",t3)

t4 = tuple('Girish')
print("\ncreate a tuple with a in-built function",t4)

#create a tuple with amixed data types
t1=("D",2,"O","I")
print("\nmixed datatype::",t1)

t2=(0,1,2,3,4,5,6,7)
t3=("darkdevil","of","internet")
t4=(t2,t3)
print("\ncreating a tuple with nested::",t4)

t1=("girish")*3
print("\ncreate tuple with a repetition::",t1)

t1=('Girish')
n = 5
print('\ntuple with a loop')
for i in range(int(n)):
    t1 = (t1,)
    print(t1)
