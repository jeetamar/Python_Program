# WAP to print Fibonacci series

print("Fibonacci Series ")
n=int(input('Enter The Term : '))
if n<=0:
    print("Enter a Positive Number")
elif n==1:
    print('Fibonacci Series is ',0)
else:
    a,b=0,1
    print("Fibonacci Series is : ",a,b, end=' ')
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=' ')






# Fibonacci Series by Using Function
def fibonacci_series(nterm):
    if nterm <=0:
        return 'Plz Input a Positive Number'
    elif nterm==1:
        return 0
    else:
        a,b=0,1
        print('Fibonacci series is : ',a,b,end=' ')
        for i in range(2,nterm):
            c=a+b
            a,b=b,c
            print(c,end=' ')

nterm=int(input("\nEnter the Terms: "))
fibonacci_series(nterm)












# Python program to display the Fibonacci sequence  # Recursive Function

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 2

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("\n\t\t\t\t\t\t\t\t\tFibonacci sequence: ")
   for i in range(nterms):
       print(recur_fibo(i),end=' ')




def fibonacci(n):
    series = [ ]
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        # print(a)
        a, b = b, a + b
        # print(a)
    return series

fibonacci_series = fibonacci(int(input('Enter the Term: ')))
print()
print("Fibonacci series:", fibonacci_series)
