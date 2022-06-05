
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

class Cars:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model
x1=Cars("ford","icon")
x2=Cars("maruti","nano")
print(x1.model,x1.brand)
print(x2.model,x2.brand)

class Student:
  "To get information"
  schoolname = "Shri j.r Gunjal English Medium School"
  id = 46
  name = "Girish"
  email = "girishunde143@gmail.com"
  def __init__(self,id,name,email):
    self.id=id
    self.name=name
    self.email=email
    print("value set...")
  def displaystudentdata(self):
    print("id:",self.id)
    print("name:",self.name)
    print("email:",self.email)
    print()
x = Student(1,"yash","yashbambale7@gmail.com")
x.displaystudentdata()

class Student:
   'Common base class for all students'
   student_count=0

   def __init__(self, name, id):
      self.name = name
      self.id = id
      Student.student_count+=1

   def printStudentData(self):
      print ("Name : ", self.name, ", Id : ", self.id)

std1=Student("vishal",101)
std2=Student("Jignesh",102)
std3=Student("Ravi",103)
print("Total Student : ",Student.student_count)
print ("Student.__doc__:", Student.__doc__)
print ("StudentStudent.__name__:", Student.__name__)
print ("Student.__module__:", Student.__module__)
print ("Student.__bases__:", Student.__bases__)
print ("Student.__dict__:", Student.__dict__ )


class ComplexNumber:
    def __init__(self,r=0,i=1):
        self.real=r;
        self.imag=i;

    def getData(self):
        print('{0}+{1}j'.format(self.real,self.imag))


c1=ComplexNumber(5,6)
c1.getData()

class Student:
    # Constructor - parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name

    def show(self):
        print("Hello",self.name)

student = Student("vishal")
student.show()

class Parent: # define parent class
    parentAttr = 100

    def __init__(self):
       print ("Calling parent constructor")

    def parentMethod(self):
       print ('Calling parent method')

    def setAttr(self, attr):
       Parent.parentAttr = attr

    def getAttr(self):
       print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
    def __init__(self):
       print ("Calling child constructor")

    def childMethod(self):
       print ('Calling child method')

c = Child() # instance of child
c.childMethod() # child calls its method
c.parentMethod() # calls parent's method
c.setAttr(200) # again call parent's method
c.getAttr() # again call parent's method

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

class JustCounter:
   __secretCount = 0

   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print (counter.__secretCount)
print("........................")
print (counter._JustCounter__secretCount)

class Complexno():
  def __init__(self,r=0,i=1):
    self.real = r
    self.image = i
  def getdata(self):
    print('{0}+{1}j'.format(self.real,self.image))
c1 = Complexno(5,6)
c1.getdata()
print("")
def product(a, b):
    p = a * b
    print(p)
def products(a,b,c):
    p = a*b*c
    print(p)
g = products(6,5,8)
print(g)
d = product(4,7)
print(d)

def fib(n):
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
print(fib(1000))
print("")
a = 50
b = 9
def __init__(a,b):
  a = 8
  b = 5
print("a,b:",a,',',b)
print("Global a :",a)
print("Local b :",b)