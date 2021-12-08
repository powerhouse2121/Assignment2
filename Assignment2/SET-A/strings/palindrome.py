#Assignment-2
#Set-A  Write a python program to check whether the string is symmetrical/palindrome

str=input("Enter the string::")
for i in range(int(len(str))):
    if(str[i]!=str[len(str)-i-1]):
        print("String is not palindrome")
        break
    else:
        print("String is palindrome")
        break

