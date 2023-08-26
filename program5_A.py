# WAP to find a summation of a digit of a given number using iteration.

num=int(input("Enter Number:"))
sum=0
while num>0:
    temp=int(num%10)
    sum+=int(temp)
    num=num/10
print(sum)