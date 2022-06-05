for city in ["junnar","pune","alephata"]:
    print(city)
print("")

for city in ["python","linux","hacker"]:
    print(city)
print("")

for char in "iteration is easy":
    print(char,end="  ")
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
city = ["junnar","pune","nashik","alephata","narayangaon"]
iter = iter(city)
print(iter)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    

def iterable(n):
    try:
        iter(n)
        return True
    except TypeError:
        return False
for i in [34,[4,5],(4,5),{"a":4},"girish",4.5]:
    print(i,">>>it's working::",iterable(i))