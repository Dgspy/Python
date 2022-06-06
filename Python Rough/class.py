import math
print(dir(math))
help(math.ceil)
X = 5.6
print(math.ceil(X))

class Student:
    def __init__(self,id,name,email,schoolname):
        self.id=id
        self.name=name
        self.email=email
        self.schoolname=schoolname
        print("value set...")        
    def displayStudent(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Email:",self.email)
        print("schoolname:",self.schoolname)
        print()
        

X = Student(1,"Yash Raj Aram bambale","Yashbambale7@gmail.com","j.r Gunjal English medium school")
X.displayStudent()
X = Student(46,"Girish Machhindra Unde","girishunde15@gmail.com","j.r Gunjal English medium school")
X.displayStudent()