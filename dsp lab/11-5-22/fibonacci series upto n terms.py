num=int(input("enter the number:"))
n1,n2=0,1
print("fibonacci series:",n1,n2,end=" ")
for i in range(2,num):
     n3=n1+n2
     n1=n2
     n2=n3
     print(n3,end=" ")
     print()