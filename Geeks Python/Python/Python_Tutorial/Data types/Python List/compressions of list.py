#list compression in python 
#below list contain square of all odd number from range 1 to 10
odd_square = [x**2 for x in range(1,30) if x % 2==1]
print(odd_square)
even_square = [x**2 for x in range(1,30) if x % 2==0]
print(odd_square)
for i in odd_square:
    print(i)
even_square =[i**3 for i in range(1,30) if i % 2==0]
print(even_square)
odd_square =[i**3 for i in range(1,30) if i % 2==1]
print(even_square)