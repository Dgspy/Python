
class cat:
  def __init__(self,color,legs):
    self.color = color
    self.legs = legs

felix = cat("ginger",4)
rover = cat("dog_colored",4)
stumpy = cat("brown",3)

class dog:
  def __init__(self,name,color):
    self.name = name
    self.color = color

  def bark(self):
    print("Girish!")
monti = dog("monti","brown")
print(monti.name)
monti.bark()
print("♥")
class Animal:
  def __init__(self,color, name):
    self.color = color
    self.name = name
class Cat(Animal):
  def purr(self):
    print("purr...")
class Dog(Animal):
  def bark(self):
    print("woof!")
fido = Dog("fido","brown")
print(fido.color)
fido.bark()
print("♥")
class A:
  def method(self):
    print("A method")
class B(A):
  def another_method(self):
    print("B method")
class C(B):
  def third_method(self):
    print("C method")
c = C()
c.method()
c.another_method()
c.third_method()



class Wolf:
  def __init__(self,name,color):
    self.name = name
    self.color = color
  def bark(self):
    print("rony")

class Dog(Wolf):
  def bark(self):
    print("Rocky")
husky = Dog("Monti","grey")
husky.bark()

class Vector2D:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __add__(self,other):
    return Vector2D(self.x + other.x,self.y + other.y)
first = Vector2D(5,7)
second = Vector2D(3,9)
result = first + second
print(result.x)
print(result.y)
