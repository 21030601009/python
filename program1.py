# WAP to find a sum of even number into 1D array.

length=int(input("Enter array length:"))
array=[]
for i in range(length):
    array.append(int(input("Enter number:")))
sum=0
for j in array:
    if(j%2==0):
        sum = sum+j
print("Answer:",sum)