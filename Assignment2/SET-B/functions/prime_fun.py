#Write a python function that accept a number as a parameter and check the number prime or not

def prime(num):
    f=0
    for i in range(2,num):
        if(num%i==0):
            f=1
            break
    if(f==0):
        print("Number is prime")
    else:
        print("Number is not prime")

num=int(input("Enter the number:"))
prime(num)