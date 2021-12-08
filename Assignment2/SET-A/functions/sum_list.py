#SET-A Write a python function to sum of all the list elements

def sum_lst(list1):
    sumoflist=sum(list1)
    print("Sum of list:",sumoflist)

n=int(input("Enter the limit:"))
list1=[]
print("Enter the list elements:")
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
print("Original list:",list1)
sum_lst(list1)