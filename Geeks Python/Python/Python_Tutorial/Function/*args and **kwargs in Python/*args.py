def fun(*args):
    for i in args:
        print(i)
fun("darkdevil","of","internet")
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
def fun(arg1,*arg2):
    print("first argument::",arg1)
    for i in arg2:
        print("next argument::",i)
fun("darkdevil","of","internet")