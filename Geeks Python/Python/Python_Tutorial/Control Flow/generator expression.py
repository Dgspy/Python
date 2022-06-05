def generator():
    t = 1
    print("first result is ",t)
    yield t
    t += 1
    print("second result is ",t)
    yield t
    t += 1
    print("third result is ",t)
    yield t
call = generator()
next(call)
next(call)
next(call)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    

generator = (n ** 2 for n in range(10))
for i in generator:
    print(i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    

string = "darkdevil of internet"
l = list(string[i]for i in range(len(string)-1,-1,-1))
print(l)