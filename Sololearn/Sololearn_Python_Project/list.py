
things = ["string",1,5,8,9]
print(things [0])
print(things [3])


devil = [
         [1,3,6],
         [5,9,8],
         [7,8,6]
         ]
print(devil[1][2])

m = [
     [1,2,3],
     [4,5,6]
     ]
print(m[1][2])

str = "hello world!"
print(str[6])

x = "Girish"
print(x[1]+x[4])

x = [2,4]
x += [6,8]
print(x[2]//x[0])

friend = ["girish","onkar","yash","sarvesh","yash"]
print("yash" in friend)
print("girish" in friend)
print("onkar" in friend) 
print("sarvesh" in friend)
print("omkar" in friend)

nums = [1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)


nums = [7,7,7,7,7]
nums[2] = 5
print(nums)

nums =[1,2,3,4,5]
nums[3] = nums[1]
print(nums[3])


nums = [1,2,3,4]
nums.append(5)
print(nums)
print(len(nums))

words = ["girish","yash"]
index = 1
words.insert(index,"is")
print(words)

letter = ['a','b','c','d','e','f']
print(letter.index('b'))
print(letter.index('e'))
print(letter.index('c'))

squares = [1,4,9,16,25,36,49,56,81,100]
print(squares[0:10])
print(squares[2:4])
print(squares[:7])
print(squares[7:])
print(squares[::4])
print(squares[2:8:4])
print(squares[2::])

list = [1,2,6,3,5,8]
print(len(list))

a = "{x},{y}".format(x = 5 , y = 12)
print(a)

cubes = [i**3 for i in range(5)]
print(cubes)

list = [i**2 for i in range(10)]
print('list')


m = [
    [1,2,3],
    [4,5,6]
    ]
print(m[0][1])

x = [2,3,5,6]
#reverse the list
x.reverse()
#sort a list
x.sort()
x.append(4)
x.remove(5)
x.insert(0,8)
print(x)
print(x.count(8))
print(min(x))

print(max(x))

list = [1,2,3,4,5,6,9,]
x = 5
c = 7
print(x,c in list)
