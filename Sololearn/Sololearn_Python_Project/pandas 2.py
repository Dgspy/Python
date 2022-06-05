import pandas as pd
import numpy as np

data = {
    'ages':[12,14,16,18,20],'height':[220,52,114,253,526]
}
df = pd.DataFrame(data)
print(df)

df=pd.DataFrame(data,index=['james','yash','girish','vaibhav','puspa'])
print(df)
print(df.loc["puspa"])
print(df.iloc[1:5])

data = {
    "a":[1,2],
    "b":[3,4],
    "c":[5,6]
}
df = pd.DataFrame(data)
print(df)

data = {'birth':[23,45,67,78,45],'death':[23,67,56,53,98]}
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data,index=["matosri","saisiddhi","saikrupa","om sai","om chaytanya"])
print(df)
df = pd.DataFrame(data,index=["a","b","c","d","e"])
print(df)


data = {
    "name":["girish","omkar","sarvesh","pradip","yash"],
    "marks":[75,85,98,67,100],
    "citys":["ralegan","taleghar","gangapur","ambahatweej","borghar"]
}

df = pd.DataFrame(data)
print("°°°°°°°°°°°°°°")
x = df.info(data)
print(x)
print("°°°°°°°°°°°°°°")
print(df)
print(df.head(2))
print(df.tail(2))
print(df.describe())
print(df.count())
print(df.max())
print(df.min())
print(df.mean())
print(df.std())
print(df.median())
print(df.var())
data = {
    'student id':[1001,1002,1003,1004,1005],'section':['A','B','A','c','c'],'class':[10,10,10,11,12],'study hrs':[2,6,3,0,5],'social media use hrs':[3,2,2,1,2],'percentage':[50,80,60,45,75]
}
df = pd.DataFrame(data,index = ['A','B','A','c','c'])
print(df)

i = df.groupby(by = 'section')
print(i.groups)
for section,df_1 in i:
    print(section)
    print(df_1)
x = df.groupby(['section']).groups
x = df.groupby('class').get_group(10)
print(x)
print(df.groupby(['section','class']).groups)
print(df.groupby('section').get_group('A'))
print(x.sum)
print(x.mean())
print(x.describe)
print(x.agg(['sum','max','min']))

data = {
    'id':[1,2,3,4,5],'class':[10,10,10,11,12]
}
df1 = pd.DataFrame(data)
print(df1)

file = {'id':[1,2,3,4,6],'death':[23,67,56,53,98]}
df2 = pd.DataFrame(file)
print(df2)

x = pd.merge(df1,df2)
print(x)
print(pd.merge(df1,df2,on ='id',how = 'inner'))
print(pd.merge(df1,df2,on ='id',how = 'outer',indicator = 'True'))
print(pd.merge(df1,df2,on = 'id',how = 'left'))
print(pd.merge(df1,df2,on ='id',how = 'right'))
print(pd.merge(df1,df2,left_index = True,right_index = True))


s1 = pd.Series([0,1,2,3])
print(s1)
s2 = pd.Series([4,5,6,7])
print(s2)
x = pd.concat([s1,s2])
print(x)
x = pd.DataFrame({
    'age':[2,3,4,5,7],'height':[123,456,756,743,667]
})
print(x)
i = pd.DataFrame({
    'cold':[4,5,6,9,8],'hot':[193,796,456,343,678]
})
print(i)
print(pd.concat([x,i]))
a = pd.concat([x,i],axis = 1)
print(a)
a = pd.concat([x,i],axis = 0)
print(a)
b = pd.concat([x,i],axis = 1,ignore_index = True)
print(b)

x = pd.DataFrame({
    'age':[2,3,4,5,7],'height':[123,456,756,743,667]
})
print(x)
i = pd.DataFrame({
    'cold':[6,9,8],'hot':[456,343,678]
})
print(i)
a = pd.concat([x,i],axis = 1)
print(a)
b = pd.concat([x,i],keys = ['df1','df2'])
print(b)
c = pd.concat([x,i],axis = 1 ,keys = ['df1','df2'])
print(b)

x = pd.DataFrame({
    'age':[2,3,4,5,7],'height':[123,456,756,743,667]
})
print(x)
y = pd.DataFrame({'marks':[23,45,76,19,85]})
print(y)
print(x,y)
i = pd.concat([x,i],sort = False)
print(i)


data = {
    'A':[1,2,3],'B':[10,20,30]
}
df1 = pd.DataFrame(data)
print(df1)

file = {'C':[4,5,6],'D':[40,50,60]}
df2 = pd.DataFrame(file)
print(df2)


x = df1.join(df2)
print(x)
x = df2.join(df1)
print(x)

data = {
    'A':[1,2,3],'B':[10,20,30]
}
df1 = pd.DataFrame(data,index = ['a','b','c'])
print(df1)

file = {'C':[4,5,6],'D':[40,50,60]}
df2 = pd.DataFrame(file)
print(df2)


x = df1.join(df2)
print(x)


data = {
    'A':[1,2,3],'B':[10,20,30]
}
a = pd.DataFrame(data,index = ['a','b','c'])
print(a)

file = {'c':[4,5,6],'D':[40,50,60]}
b = pd.DataFrame(file,index = ['a','b','c'])
print(b)


x = b.join(a)
print(x)
i = a.join(b,rsuffix = '_1')
print(i)

i = a.join(b,lsuffix = '_1')
print(i)

x = a.append(b)
print(x)
x = a.append(b,ignore_index = True,sort = False)
print(x)

data = {
    "name":["girish","omkar","sarvesh","pradip","yash"],
    "marks":[75,85,98,67,90],
    "citys":["ralegan","taleghar","gangapur","ambahatweej","borghar"]
}

df = pd.DataFrame(data)
print(df)

print(df.pivot_table(index = 'citys'))
print(df.pivot_table(index = 'citys',columns ='name'))
print(df.pivot_table(index = 'citys',columns ='name',aggfunc = 'count'))
print(df.pivot_table(index = 'citys',columns ='name',aggfunc = 'max'))
print(df.pivot_table(index = 'citys',columns ='name',aggfunc = 'sum'))
print(df.pivot_table(index = 'citys',columns ='name',fill_value = 0))

print(df.pivot_table(index = 'citys',columns ='name',fill_value = 0,margins = True))

df = pd.DataFrame(data)
print(df)
x = pd.melt(df)
print(x)
x = pd.melt(df,id_vars=['citys'])
print(x)
x = pd.melt(df,id_vars=['marks'])
print(x)
x = pd.melt(df,id_vars=['citys'],value_vars = ['marks'])
print(x)
x = pd.melt(df,id_vars=['citys'],var_name = 'girish',value_name = 'yash')
print(x)


data = {
    "name":["girish","omkar","sarvesh","pradip","yash"],
    "marks":[75,85,98,67,90],
    "citys":["ralegan","taleghar","gangapur","ambahatweej","borghar"],"date":[1-7-2021,2-7-2021,3-7-2021,4-7-2021,5-7-2021]
}

df = pd.DataFrame(data)
print(df)
print(df.dtypes)
print(type(df.date[3]))

data = {'birth':[23,45,67,78,45],'death':[23,67,56,53,98]}
df = pd.DataFrame(data)
df = pd.DataFrame(data,index=["a","b","c","d","e"])
print(df)
print(df.groupby("birth").mean())
print(df.groupby("birth")['death'].agg(['min',np.median,'max']))
print(df.groupby("birth").agg({'death':[np.median,np.mean]}))

x = (i**3 for i in range(100))
df = pd.DataFrame(x)
print(df)
print(df.sum())


