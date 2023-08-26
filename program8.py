#WAP to find a total odd and total even digit of a given number.

num=int(input("Enter number:"))
odd=0
even=0
while num>=1:
    rem=num%10
    if(rem%2==0):
        even+=rem
    else:
        odd+=rem
    num=int(num/10)
print("Even sum=",even)
print("Odd sum=",odd)