#WAP to find a Fibonacci series up to n terms using iterative
num=int(input("Enter Number:"))
t1=0
t2=1
sum=0
for i in range(num):
    t1=int(t2)
    print(sum,end=',')
    t2=int(sum)
    sum=int(t1)+int(t2)