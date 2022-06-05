list1 = ['a','e','i','o','u']
iter_list1 = iter(list1)
try:
    print(next(iter_list1))
    print(next(iter_list1))
    print(next(iter_list1))
    print(next(iter_list1))
    print(next(iter_list1))
    print(next(iter_list1))    
except:
    pass
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
l1 = [11,22,33,44,55]
l = iter(l1)
while True:
    try:
        print(l.__next__())
    except:
        break
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
lb = ["tiger","lion","cat"]
i = iter(lb)
try:
    print(i.__next__())
    print(i.__next__())
    print(i.__next__())
    print(i.__next__())
except:
    print("\nthrowing stop iteration error ","i cannot count more")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
    
class counter:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start - 1            
if __name__ == "__main__":
    a,b = 2,5
    c1 = counter(a,b)
    c2 = counter(a,b)
    for i in c1:
        print(i,end=" ")
    obj = iter(c2)
    try:
        while True:
            print(next(obj))
    except:
        print("gameover")
        