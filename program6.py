#pattern
num=int(input("Enter number:"))

for i in range(1,num,1):
    for j in range(1,i+1,1):
        if i==1:
            continue
        else:
            print(j,end="")
    print("\n")