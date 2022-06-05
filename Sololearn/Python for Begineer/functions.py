#List Function
num = [1,2,3,4,5,6]
print(len(num))

#append function
num = [1,2,3]
num.append(4)
print(num)
#insert function
words = ['python','fun']
index = 1
words.insert(index,'is')
print(words)
letter = ['p','q','r','s','t','p','u']
print(letter.index('r'))
print(letter.index('u'))
print(letter.index('s'))

#string function
#.format argument
num = [4,5,6]
msg = "numbers: {0} {1} {2}". format(num[0],num[1],num[2])
print(msg)
a = "{x} ,{y}".format(x = 5,y = 12)
print(a)
#join function
print(",".join(["girish","omkar","yash","sarvesh"]))
#replace function
print("hello me".replace("me","world"))
#startswith function
print("This is a sentence".startswith("This"))

#endswith function
print("This is a sentence".endswith("sentence"))

#upper case
print("This is a sentence".upper())
#lower case
print("This is a sentence".lower())
#split fumction
print("girish,omkar,yash,sarvesh".split(", "))
