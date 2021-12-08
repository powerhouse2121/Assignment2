#SET-A Write a python program to reverse a string

def revers(str):
    l=len(str)
    x=str[::-1]
    print("Reverse string:", x)
str=input("Enter string::")
revers(str)