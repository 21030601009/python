# WAP to find whether string is palindrome or not.

str=input("Enter String:")
if(str[0::]==str[::-1]):
    print("String is pallindrom")
else:
    print("String is not pallindrom")