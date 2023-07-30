# # Check number is prime or not
#
# # simple
#
# print("Here I'm Checkin The Number is Prime or Not")
# n=int(input("Enter The Number : "))
# flage=False
#
# for i in range(2,n):
#     if n%i==0:
#         flage=True
#         break
# if flage:
#     print(f"This Number {n} is not Prime")
# else:
#     print(f'This Number {n} is Prime Number')
#
#
#
#
# # Check Prime Number using Function
#
# def chkPrime(n):
#     flage=False
#     if n==0 or n==1:
#         return f'This Number {n} is not Prime Number'
#     elif n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 flage=True
#                 break
#         if flage:
#             return f'Thsi number {n} is not Prime'
#         else:
#             return f'This number {n} is Prime Number'
#
# # call the function
# n=int(input("Enter The Number: "))
# res=chkPrime(n)
# print(res)
#
# #Without using flage variable
#
#
#
# n = int(input("Enter The Number: "))
# # If given number is greater than 1
# if n > 1:
#     # Iterate from 2 to n
#     for i in range(2, n):
#
#         if (n % i) == 0:
#             print(n, "is not a prime number")
#             break
#     else:
#         print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")
#




# print Prime Number between lower and upper bound

lower=int(input("Enter the Lower number: "))
upper=int(input("Enter the Upper number: "))

print(f'All Prime Number Between {lower} and {upper}')

for num in range(lower,upper+1):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
    else:
        print('Wrong Input plz write number enter:')




# print Prime number using Function


print()
def printPrime(lower,upper):
    """
    prime: Which number is divide by one(1) and only itself known as a Prime Number
    lower - enter a number where to start print prime - e.g 2 (Because smallest prime number is 2)
    :param lower:
    :param upper:
    """
    l=lower
    u=upper
    for n in range(l,u+1):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                print(n)
l=int(input("enter the lower "))
u=int(input("enter the upper "))
printPrime(l,u)
