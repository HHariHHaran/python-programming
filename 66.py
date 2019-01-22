n=int(input("enter the number"))
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=flag+1
        if(flag==0):
 print("it is a prime")
else:
 print("not prime")
