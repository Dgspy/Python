import string
import random

s1 = string.ascii_lowercase
#print(s1)

s2 = string.ascii_uppercase
#print(s2)

s3 = string.digits
#print(s3)

s4 = string.punctuation
#print(s4)

s5 = string.hexdigits
#print(s5)

sleng = int(input("Enter a Length of password:\n")) #ToDo: Handle Gibbersish
s = [ ]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
s.extend(list(s5))
random.shuffle(s)


print("".join(s[0:sleng]))


print(random.sample(s,10))