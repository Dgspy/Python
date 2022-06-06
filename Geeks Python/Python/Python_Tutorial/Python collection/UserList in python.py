from collections import UserList
l = [1,2,3,4]
user = UserList(l)
print(user.data)
user = UserList()
print(user.data)
print("........................................................................................................................")
class list(UserList):
    def remove(self , s = None):
        raise RuntimeError("deletion not allowed")
    def pop(self , s = None):
        raise RuntimeError("deletion not allowed")
l = list([1,2,3,4])
print("original list::",l)
l.remove()