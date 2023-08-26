# WAP to find a factorial of a given integer using iteration.

num=int(input("Enter number:"))
ans=1
for i in range(1,num+1,1):
    ans*=i
print(ans)