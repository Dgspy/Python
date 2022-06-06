# class Error is derived from super class Exception
class Error(Exception):
	pass
class TransitionError(Error):
	def __init__(self, prev, nex, msg):
		self.prev = prev
		self.next = nex
		self.msg = msg
try:
	raise(TransitionError(2,3*2,"Not Allowed"))
except TransitionError as error:
	print('Exception occured: ',error.msg)		
	
print("~~~~~~~~~~~~~~~~~~~~####################~~~~~~~~~~~~~~~~~~~~")
# NetworkError has base RuntimeError
# and not Exception
class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg

try:
	raise Networkerror("Error")

except Networkerror as e:
	print (e.args)
