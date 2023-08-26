# WAP to find a Factor of a given number using iteration.

num=int(input("Enter Number:"))
print("Factors:")
for i in range(1,num+1,1):
    if num % i==0:
        print(i)