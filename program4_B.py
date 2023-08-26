# WAP to find a factorial of a given integer using recursion.

num=int(input("Enter Number:"))
sum=1
temp=1
def factorial(temp,sum):
    if temp <=num:
        sum*=temp
        temp+=1
        
        return (factorial(temp,sum))
    else:
        return 0
factorial(temp,sum)
print(sum)