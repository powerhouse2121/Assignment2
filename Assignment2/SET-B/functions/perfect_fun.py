#Write a python function to check whether a number is perfect or not

def perfect(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum=sum+i
    if(sum==num):
        print("Number is perfect")
    else:
        print("Number is not perfect")

num=int(input("Enter the number:"))
perfect(num)
