row = 6
for num in range(row):
  for i in range(num):
    print(num,end="")
  print("")

row = 6
for rows in range(1,row+1):
  for colomn in range(1,rows+1):
    print(colomn,end="")
  print("")

row = 5
b = 0
for i in range(row,0,-1):
  b += 1
  for j in range(1,i+1):
    print(b,end = '')
  print('\r')

n = 5
for i in range(0,n):
  for j in range(0,i+1):
    print("*. ",end = "")
  print("")

n = 5
k = 2*n - 2
for i in range(0, n): 
    for j in range(0, k): 
        print(end=" ")
    k = k - 1
    for j in range(0, i+1): 
          print("* ", end="") 
    print("\r")


def contnum(n):          
    for i in range(0, n):             
        for j in range(0, i+1):                               
          print(num, end=" ")            
          num = num + 1            
        print("\r") 

n = 5
def alphapat(n):         
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
          ch = chr(num)   
          print(ch, end=" ")     
        num = num + 1
        print("\r") 



n = 5
alphapat(n) 
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()


rows = 6
for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print(j, '', end='')
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows):
        print(k, '', end='')
    print('\n')


rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
    
    
size = 7
asciiNumber = 65
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")
    
    
n = 7
for i in range(0,n):
  for j in range(0,i+1):
    print((i,j),"",end="")
  print()
  a = 1
  k = 2
  if(k>n-k):
    k = n-k
  for i in range(0,k):
    a = a*(n-j)
    a = a//(j+1)
  print(a)


def printPascal(n) :     
  for line in range(0, n) :         
    for i in range(0, line + 1) : 
      print(binomialCoeff(line, i),"",end="") 
    print() 
def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1)     
    return res
n = 7
printPascal(n) 



def Diamond(rows): 
    n = 0
    for i in range(1, rows + 1): 
        # loop to print spaces 
        for j in range (1, (rows - i) + 1): 
            print(end = " ")                 
        while n != (2 * i - 1): 
            print("*", end = "") 
            n = n + 1
        n = 0                
        print() 
    k = 1
    n = 1
    for i in range(1, rows):         
        for j in range (1, k + 1): 
            print(end = " ") 
        k = k + 1                
        while n <= (2 * (rows - i) - 1): 
            print("*", end = "") 
            n = n + 1
        n = 1
        print()
rows = 5
Diamond(rows) 


word = "girishunde15@gmail.com"
x = ""
for i in word:
    x += i
    print(x)

word = "girish"
x = ""
for i in word:
  x += i
  print(x)

