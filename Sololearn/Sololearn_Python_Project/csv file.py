import pandas as pd

mydata = {
    "name":["girish","omkar","sarvesh","pradip","yash"],
    "marks":[75,85,98,67,100],
    "citys":["ralegan","taleghar","gangapur","ambahatweej","borghar"]
}



df = pd.DataFrame(mydata)
print(df)
col = mydata['citys']
print(col)

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

print(df.head(50))
col = df['Fare']
print(col)
print(df['Fare'].values)
arr = df[['Pclass','Fare','Sex']].values
print(arr.shape)