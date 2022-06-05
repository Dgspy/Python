class Animal:
    def eat(self):
      print('Eating...')
class Dog(Animal):
   def bark(self):
      print('Barking...')
class BabyDog(Dog):
    def weep(self):
        print('Weeping...')
d=BabyDog()
d.eat()
d.bark()
d.weep()

class First(object):
  def __init__(self):
    super(First, self).__init__()
    print("first")
class Second(object):
  def __init__(self):
    super(Second, self).__init__()
    print("second")
class Third(Second, First):
  def __init__(self):
    super(Third, self).__init__()
    print("third")
Third()

class C(object):
  def __init__(self):
    self.c = 21
    self.__d = 42
    
class D(C):
  def __init__(self):
    self.e = 84
    C.__init__(self)

object1 = D()
print(D)
