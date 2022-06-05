import pandas as pd



ca-covid.csv = {'pecient'[1,2,3,4,5,6,7],'ward'[12,23,34,36,43,23,85]}

df = pd.read_csv("ca-covid.csv")
print(df)

df = pd.DataFrame("ca-covid.csv")
print(df)

print(df.head())
df.info()
df.drop()

# it is in next

file = open("/usercode/files/books.txt", "r")

cont = file.readlines()
for line in cont:
    words = line.split()
    for word in words:
        print(word[0], end = "")
    print()
file.close()