# WAP to find a Fibonacci series up to n terms using recursion

num=int(input("Enter Number:"))

def Fibonacci(n):
    if n<=1:
        return n
    else:
        return(Fibonacci(n-1)+Fibonacci(n-2))
if(num <=0):
    print("Invalid Input")
else:
    for i in range(num):
        print(Fibonacci(i),end=',')