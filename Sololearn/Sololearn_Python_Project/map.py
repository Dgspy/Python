

print(", ".join(["spam", "eggs", "ham"]))
print("hello me".replace("me","world"))
print('yash','girish','ganesh'.split(", "))
print("this is a sentence.".upper())
print("THIS IS A SENTENCE.".lower())

x = ["hii","hello","welcome"]
print(x[2])

age = {
       'Girish':16,
       'Yash':17,
       'Sarvesh':14,
       'Omkar':16
}
print(age["Sarvesh"])
print(age["Girish"])

pairs = {
    1:"apple",
    "orange":[2,3,4],
    "True":"False",
}
print(pairs.get("orange"))
print(pairs.get(2,42))
print(pairs.get(True))

pairs = {
    1:"apple",
    "orange":[2,3,4],
    True:False,
    12:"True"
}
print(pairs.get("orange"))
print(pairs.get(2,42))
print(pairs.get(12345,"True"))