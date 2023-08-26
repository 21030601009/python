# WAP to find a summation of a digit of a given number using recursion.

num=int(input("Enter Number:"))
sum=0
def summation(num,sum):
    if num > 0:
        temp=int(num%10)
        sum+=temp
        num=int(num/10)
        print(sum)
        return summation(num,sum)
    else:
        return 0
summation(num,sum)
