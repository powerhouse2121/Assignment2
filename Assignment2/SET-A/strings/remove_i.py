#Set-A Write a python program to remove i'th character from string

test_str=input("Enter the string:")
print("Original string:",test_str)
new_str=""
pos=int(input("Enter the position:"))
for i in range(len(test_str)):
    if(i!=pos):
        new_str=new_str+test_str[i]
print("The string after removal the character:",new_str)