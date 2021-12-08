#Set-A Write a python program to reverse words in a given string

str=input("Enter string::")
s=str.split()
print("Split words:",s)
reverse_string=' '.join(reversed(s))
print(reverse_string)