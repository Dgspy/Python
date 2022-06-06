 
def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
def fun(arg1,**kwarg):
    for key,value in kwarg.items():
        print("%s == %s"%(key,value))
fun("hi",greeting="welcome",helpingverb="to",hackerid="D2oI")
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
def fun(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)
args = ("girish","love","python")
fun(*args)
kwargs = {"arg1":"girish","arg2":"love","arg3":"python"}
fun(**kwargs)
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
def fun(*args,**kwargs):
    print(args)
    print(kwargs)
fun("girish","machhindra","unde",first="devil",second="is",last="back")