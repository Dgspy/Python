
# Function to accept array of roll numbers
def accept_array(A):
    N = int(input("Enter the total no. of students: "))
    print("Input roll numbers in sorted order")
    for i in range(N):
        x = int(input(f"Enter the roll no of student {i + 1}: "))
        A.append(x)
    print("Student Info accepted successfully\n\n")
    return N

# Function to display the array
def display_array(A, n):
    if n == 0:
        print("\nNo records in the database")
    else:
        print("Students Array: ", end=' ')
        for i in range(n):
            print(f"{A[i]} ", end=' ')
        print("\n")

# Recursive binary search function
def Recursive_Binary_Search(A, s, l, X):
    if s <= l:
        mid = (s + l) // 2
        if A[mid] == X:
            return mid  # Found
        elif X < A[mid]:
            return Recursive_Binary_Search(A, s, mid - 1, X)
        else:
            return Recursive_Binary_Search(A, mid + 1, l, X)
    return -1  # Not found

# Iterative binary search function
def Iterative_Binary_Search(A, n, X):
    s, l = 0, n - 1
    while s <= l:
        mid = (s + l) // 2
        if A[mid] == X:
            return mid  # Found
        elif X < A[mid]:
            l = mid - 1
        else:
            s = mid + 1
    return -1  # Not found

# Fibonacci search function
def Fibonacci_Search(A, n, X):
    f1, f2 = 0, 1
    f3 = f1 + f2
    offset = -1
    
    # Generate the smallest Fibonacci number greater than or equal to n
    while f3 < n:
        f1 = f2
        f2 = f3
        f3 = f1 + f2

    while f3 > 1:
        i = min(offset + f1, n - 1)
        if A[i] == X:
            return i  # Found
        elif X < A[i]:
            f3 = f1
            f2 = f2 - f1
            f1 = f3 - f2
        else:
            f3 = f2
            f2 = f1
            f1 = f3 - f2
            offset = i
    
    if f2 == 1 and (offset + 1) < n and A[offset + 1] == X:
        return offset + 1  # Found
    
    return -1  # Not found

# Main function
def main():
    A = []
    while True:
        print("\t1 : Accept & Display Students info")
        print("\t2 : Recursive Binary Search")
        print("\t3 : Iterative Binary Search")
        print("\t4 : Fibonacci Search")
        print("\t5 : Exit")
        
        ch = int(input("Enter your choice: "))
        
        if ch == 5:
            print("End of Program")
            break
        elif ch == 1:
            A = []
            n = accept_array(A)
            display_array(A, n)
        elif ch == 2:
            X = int(input("Enter the roll_no to be searched: "))
            flag = Recursive_Binary_Search(A, 0, n - 1, X)
            if flag == -1:
                print("\tRoll no to be Searched not Found\n")
            else:
                print(f"\tRoll no found at location {flag + 1}")
        elif ch == 3:
            X = int(input("Enter the roll_no to be searched: "))
            flag = Iterative_Binary_Search(A, n, X)
            if flag == -1:
                print("\tRoll no to be Searched not Found\n")
            else:
                print(f"\tRoll no found at location {flag + 1}")
        elif ch == 4:
            X = int(input("Enter the roll_no to be searched: "))
            flag = Fibonacci_Search(A, n, X)
            if flag == -1:
                print("\tRoll no to be Searched not Found\n")
            else:
                print(f"\tRoll no found at location {flag + 1}")
        else:
            print("Wrong choice entered!! Try again")

# Call main function
main()


2b

def accept_array(A): 
    n = int(input("Enter the total number of students: "))
    for i in range(n):
        x = int(input(f"Enter the roll number of student {i + 1}: "))
        A.append(x)
    print("Student Info accepted successfully\n\n")
    return n

def display_array(A, n): 
    if n == 0:
        print("\nNo records in the database")
    else:
        print("Students Array: ", end=' ')
        for i in range(n):
            print(f"{A[i]}  ", end=' ')
        print("\n")

def linear_search(A, n, X):
    for i in range(n):
        if A[i] == X:
            return i  # found, so returning the position (i.e., index)
    return -1  # not found

def sentinel_search(A, n, X):
    last = A[n - 1]
    i = 0
    A[n - 1] = X  # Here X is the roll number to be searched.
    while A[i] != X:
        i += 1
    A[n - 1] = last
    if i < n - 1 or X == A[n - 1]:
        return i  # roll number found at location i
    else:
        return -1  # roll number not found

def main():
    A = []
    n = 0  # initialize n to ensure it exists in the scope of main function
    while True:
        print("\t1 : Accept & Display Students info")
        print("\t2 : Linear Search")
        print("\t3 : Sentinel Search")
        print("\t4 : Exit")
        ch = int(input("Enter your choice: "))
        if ch == 4:
            print("End of Program")
            quit()
        elif ch == 1:
            A = []
            n = accept_array(A)
            display_array(A, n)
        elif ch == 2:
            X = int(input("Enter the roll number to be searched: "))
            flag = linear_search(A, n, X)
            if flag == -1:
                print("\tRoll number not found\n")
            else:
                print(f"\tRoll number found at location {flag + 1}")
        elif ch == 3:
            X = int(input("Enter the roll number to be searched: "))
            flag = sentinel_search(A, n, X)
            if flag == -1:
                print("\tRoll number not found\n")
            else:
                print(f"\tRoll number found at location {flag + 1}")
        else:
            print("Wrong choice entered! Try again.")

main()
