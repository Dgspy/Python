# default argument
def myfun(x, y = 50):
    print("x::",x)
    print("y::",y)
myfun(20)
myfun(10,34)

print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
#keyword argument
def student(firstname,lastname):
    print(firstname,lastname)
student(firstname="girish",lastname="unde")
student(firstname="yash",lastname="bambale")
student("onkar","ghode")

print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
#variable-length argument ,non-kryword argument
def myfun(*arg):
    for ar in arg:
        print(ar)
myfun("hello","welcome","to","D2OI")
print()
#variable with keyword argument
def myfun(**kwargs):
    for key ,value in kwargs.items():
        print("%s == %s"%(key,value))
myfun(first="internet",second="for",third="girish")
        
