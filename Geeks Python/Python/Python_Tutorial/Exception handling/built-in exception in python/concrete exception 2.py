#exception OSError([arg])
'''
def func():
	print (ans)
func()
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception OverFlowError
'''
import sys

print ('Regular integer: (maxint=%s)' % sys.maxint)
try:
	i = sys.maxint * 3
	print ('No overflow for ', type(i), 'i =', i)
except OverflowError, err:
	print ('Overflowed at ', i, err)

print()
print ('Long integer:')
for i in range(0, 100, 10):
	print ('%2d' % i, 2L ** i)

print()
print ('Floating point values:')
try:
	f = 2.0**i
	for i in range(100):
		print (i, f)
		f = f ** 2
except OverflowError, err:
	print ('Overflowed after ', f, err)
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
# exception reference error
'''
import gc
import weakref
class foo:
	def __init__(self,name):
		self.name = name
	def __del__(self):
		print('deleting %s'%self)
obj = foo("girish")
p = weakref.proxy(obj)
print("before",p.name)
obj = None
print("after ",p.name)
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
# exception StopIteration
'''
lst = [1,2,3,4]
i = iter(lst)
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
# exception syntax error
'''
try:
	print (eval('geeks for geeks'))
except SyntaxError, err:
	print ('Syntax error %s (%s-%s): %s' % \
		(err.filename, err.lineno, err.offset, err.text))
	print (err)
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception typeerror
'''
arr = ('girish',)+'girish'
print(arr)
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception UnBoundlocalError
'''
def global_name_error():
	print (unknown_global_name)

def unbound_local():
	local_val = local_val + 1
	print (local_val)

try:
	global_name_error()
except NameError, err:
	print ('Global name error:', err)

try:
	unbound_local()

except UnboundLocalError, err:
	print ('Local name error:', err)
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception value error
'''
print(int("a"))
'''
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
#exception ZeroDivisionError
print(1/0)