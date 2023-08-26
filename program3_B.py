# WAP to find a Factor of a given number using recursion.

num=int(input("Enter Number:"))
temp=1
def pallindrom(num,temp):
    if temp <=num:
        if num%temp==0:
            print(temp)
    else:
        return 0
    temp+=1
    return (pallindrom(num,temp))
pallindrom(num,temp)