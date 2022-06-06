import array as asha
a = asha.array("i",[1,2,3,4,5])
print("first array::",a)
print('new creation array i::',end="")
for i in range(0,3):
    print(a[i],end="")
print( )

b = asha.array('d',[2.3,4.5,1.2])
print('second array::',b)
for i in range(0,3):
    print(b[i],end="")