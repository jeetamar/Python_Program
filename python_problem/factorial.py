# WAP to print factorial

num=int(input("Enter The Number : "))
fact=1
for i in range(1,num+1):
    fact =fact*i
print(f"Factorial of this Number  {num}! is =>",fact)




# Factorial by using Recursive Function


def findFact(n):
    if n==0 or n==1:
        return n
    return n*findFact(n-1)

print(findFact(int(input("Enter The number: "))))