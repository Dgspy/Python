
nums = {1,2,3,4,5,6}
nums = {0,1,2,3} & nums
nums = filter(lambda x:x>1,nums)
print(len(list(nums)))

a,b,*c,d,e = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)
print(e)

print ("hii")

a,b,c,d,*e = range(20)
print(len(e))

m = lambda x:print(x*2)
m(5)

x = lambda a,b:print(a**b)
x(4,3)

def evalute(a,b,c):
  return lambda x:a*x**2+b*x+c
ans = evalute(3,5,2)
print(ans(4))
print(ans(9))

def evalute():
  return lambda :input('enter no')
  
ans = evalute()
print(ans())
print(ans())