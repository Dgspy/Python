from collections import namedtuple
student = namedtuple("student",["name","age","DOB"])
s = student("girish",16,26_06_2005)
print("the student age using index is::",s[1])
print("the student name using keyname is ::",s.name)
print("the student dob using getattr() is ::",getattr(s,"DOB"))
print("........................................................................................................................")

student = namedtuple("student",["name","age","DOB"])
g = student("girish",16,26_06_2005)
y = ["yash",17,15_11_2004]
d = {'name':"omkar",'age':16,'DOB':20_06_2005}
print(student._make(d))
print(g._asdict())
print(student(**d))
print(g._fields)
print(g._replace(name = "rocky"))
print(g)