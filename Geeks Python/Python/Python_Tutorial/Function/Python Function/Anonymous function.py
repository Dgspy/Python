def cube(x):
    return x*x*x
cube2 = lambda x : x*x*x
print(cube(7))
print(cube2(7))
print(">>>>>>>>>>>>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<<<<<<<<<<")
#function within function
def f1():
    s = "i love you"
    def f2():
        print(s)
    f2()
f1()