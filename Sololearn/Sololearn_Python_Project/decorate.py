
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap
def print_text():
  print("hello world!")
decorated = decor (print_text)
decorated()

def print_text():
  print("hello world!")
print_text = decor (print_text)
@decor
def print_text():
  print("hello world!")

class specialstring:
  def __init__(self,cont):
    self.cont = cont
  def __truediv__(self,other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont,line,
    other.cont])
spam = specialstring("spam")
hello = specialstring("hello world!")
print(spam / hello)



class specialstring:
  def __init__(self,cont):
    self.cont = cont
  def __gt__(self,other):
    for index in range (len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)
spam = specialstring("spam")
hello = specialstring("hello world!")
spam > hello



import random
class VagueList:
  def __init__(self,cont):
    self.cont = cont
  def __getitem__(self,index):
    return self.cont[index +
random.randint(-1,1)]
  def __len__(self):
    return random.randint(0,len(self.cont)*2)
vague_list = VagueList(["A","B","C","D","E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])


a = 42#/. # create object <42>
b = a #Increase ref.count of <42>
c = [a] # Increase ref.count of <42>

del a # Decrease ref.count of <42>
b = 100 #Decrease ref.count of <42>
c = [0] # Decrease ref.count of <42>
